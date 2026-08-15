#!/usr/bin/env python3

semantic_search = __import__('3-semantic_search').semantic_search
question_answer_from_text = __import__('0-qa').question_answer


def question_answer(coprus_path):
    while True:
        question = input("Q: ")

        if question.lower() in ["exit", "quit", "goodbye", "bye"]:
            print("A: Goodbye")
            break

        reference = semantic_search(coprus_path, question)

        if reference is None:
            print("A: Sorry, I do not understand your question.")
            continue

        answer = question_answer_from_text(question, reference)

        if answer is None:
            print("A: Sorry, I do not understand your question.")
        else:
            print("A:", answer)
