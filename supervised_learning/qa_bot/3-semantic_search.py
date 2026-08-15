#!/usr/bin/env python3

import os
from sentence_transformers import SentenceTransformer, util


def semantic_search(corpus_path, sentence):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    documents = []

    for filename in os.listdir(corpus_path):
        filepath = os.path.join(corpus_path, filename)

        if os.path.isfile(filepath):
            with open(filepath, encoding='utf-8') as f:
                documents.append(f.read())

    if not documents:
        return None

    sentence_embedding = model.encode(sentence, convert_to_tensor=True)
    document_embeddings = model.encode(documents, convert_to_tensor=True)

    similarities = util.cos_sim(
        sentence_embedding,
        document_embeddings
    )[0]

    best_index = similarities.argmax().item()

    return documents[best_index]
