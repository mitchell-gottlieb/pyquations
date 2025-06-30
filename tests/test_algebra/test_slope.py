import pytest

from pyquations.algebra.slope import slope


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 1, 1, 1),
        (1, 2, 3, 6, 2),
        (2, 3, 5, 3, 0),
        (-2, -3, 4, 5, pytest.approx(1.3333333333333333)),
    ],
)
def test_slope(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    expected: float,
) -> None:
    result = slope(x1, y1, x2, y2)
    assert result == expected


@pytest.mark.parametrize(
    "x1, y1, x2, y2",
    [
        (5, 7, 5, 10),
    ],
)
def test_slope_invalid(x1: float, y1: float, x2: float, y2: float) -> None:
    with pytest.raises(ValueError):
        slope(x1, y1, x2, y2)
