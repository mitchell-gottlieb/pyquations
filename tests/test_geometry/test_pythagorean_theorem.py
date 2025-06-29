import pytest

from pyquations.geometry.pythagorean_theorem import pythagorean_theorem


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (1.5, 2, pytest.approx(2.5)),  # type: ignore
    ],
)
def test_pythagorean_theorem(a: float, b: float, expected: float):
    assert pythagorean_theorem(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        (-3, 4),
        (3, -4),
        (-3, -4),
        (0, 0),
    ],
)
def test_pythagorean_theorem_invalid(a: float, b: float):
    with pytest.raises(ValueError):
        pythagorean_theorem(a, b)
