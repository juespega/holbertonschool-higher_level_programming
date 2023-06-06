#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_returns = []
    if not sentence:
        tuple_returns = len(sentence), None
        return tuple_returns
    else:
        tuple_returns = len(sentence), sentence[0]
        return tuple_returns
