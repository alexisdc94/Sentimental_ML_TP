import pytest
from .main import sentiment_analysis


def toArray(string):
    sentence = []
    sentence.append(string)
    return sentence


def test_sentiment_positive():
    assert "positive" == sentiment_analysis(toArray("I love coconuts"))


def test_sentiment_neutral():
    assert "neutral" == sentiment_analysis(toArray("These flannel wipes are OK, but in my opinion not worth keeping."))


def test_sentiment_negative():
    assert "negative" == sentiment_analysis(toArray("I hate coconuts"))
