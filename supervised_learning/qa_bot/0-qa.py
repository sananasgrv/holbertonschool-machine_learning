import tensorflow as tf
import tensorflow_hub as hub
from transformers import BertTokenizer


# BERT tokenizer
tokenizer = BertTokenizer.from_pretrained(
    "bert-large-uncased-whole-word-masking-finetuned-squad"
)

# BERT QA model
model = hub.load("https://tfhub.dev/see--/bert-uncased-tf2-qa/1")


def question_answer(question, reference):
    """
    Finds an answer to a question in the reference document.

    Args:
        question (str): The question to answer.
        reference (str): The reference document.

    Returns:
        str or None: The answer if one is found, otherwise None.
    """

    # Tokenize question and reference
    question_tokens = tokenizer.tokenize(question)
    reference_tokens = tokenizer.tokenize(reference)

    # Convert tokens to IDs
    question_ids = tokenizer.convert_tokens_to_ids(question_tokens)
    reference_ids = tokenizer.convert_tokens_to_ids(reference_tokens)

    # Add special tokens
    input_ids = (
        [tokenizer.cls_token_id]
        + question_ids
        + [tokenizer.sep_token_id]
        + reference_ids
        + [tokenizer.sep_token_id]
    )

    # Segment IDs:
    # 0 = question
    # 1 = reference
    segment_ids = (
        [0] * (len(question_ids) + 2)
        + [1] * (len(reference_ids) + 1)
    )

    # Attention mask
    input_mask = [1] * len(input_ids)

    # Convert to tensors
    input_ids = tf.constant([input_ids], dtype=tf.int32)
    input_mask = tf.constant([input_mask], dtype=tf.int32)
    segment_ids = tf.constant([segment_ids], dtype=tf.int32)

    # Run the model
    outputs = model(
        input_ids=input_ids,
        input_mask=input_mask,
        segment_ids=segment_ids
    )

    # Get start/end scores
    start_logits = outputs["start_logits"][0]
    end_logits = outputs["end_logits"][0]

    # Best start and end positions
    start = tf.argmax(start_logits).numpy()
    end = tf.argmax(end_logits).numpy()

    # Make sure the answer comes from the reference,
    # not from the question or special tokens.
    reference_start = len(question_ids) + 2

    if start < reference_start or end < start:
        return None

    # Convert IDs back to tokens
    answer_tokens = input_ids[0][start:end + 1].numpy().tolist()
    answer_tokens = tokenizer.convert_ids_to_tokens(answer_tokens)

    # Convert WordPiece tokens into readable text
    answer = tokenizer.convert_tokens_to_string(answer_tokens)

    answer = answer.strip()

    if not answer:
        return None

    return answer
