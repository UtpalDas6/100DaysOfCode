import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from find_binary import binary

@pytest.mark.parametrize(
    "num, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (5, "101"),
        (10, "1010"),
    ],
)
def test_binary(num, expected):
    assert binary(num) == expected
