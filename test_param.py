import pytest
from model import param


def test_param():
    val = param.faker()
    assert val == "It Works"
