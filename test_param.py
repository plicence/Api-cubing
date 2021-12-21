import pytest
from model import param


def test_param():
    val = param.faker()
    print("GNEEUUE")
    assert val == "It Works"
