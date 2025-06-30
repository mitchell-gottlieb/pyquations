import pytest

from pyquations.geometry.distance import distance


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 3, 4, 5.0),
        (1, 2, 4, 6, 5.0),
        (5, 5, 5, 8, 3.0),
        (2, 3, 7, 3, 5.0),
        (-2, -3, 2, 3, pytest.approx(7.211102550927978)),
        (1, -5, -2, -1, 5.0),
        (0.5, 1.5, 3.5, 5.5, pytest.approx(5.0)),
        (1.1, 2.2, 4.1, 6.2, pytest.approx(5.0)),
        (3, 7, 3, 7, 0.0),
        (1, 1, 4, 5, pytest.approx(5.0)),
        (2, 3, 6, 9, pytest.approx(7.211102550927978)),
    ],
)
def test_distance(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    expected: float,
) -> None:
    result = distance(x1, y1, x2, y2)
    assert result == expected
