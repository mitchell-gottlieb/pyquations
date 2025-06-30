import pytest

from pyquations.algebra.point_slope_form import point_slope_form


@pytest.mark.parametrize(
    "x1, y1, m, x_test, expected",
    [
        (2, 3, 4, 3, 7),
        (0, 0, 1, 5, 5),
        (-1, 2, -2, 3, -6),
        (3, 5, 0, 10, 5),
        (4, -2, 2.5, 6, 3),
    ],
)
def test_point_slope_form(
    x1: float, y1: float, m: float, x_test: float, expected: float
) -> None:
    line_function = point_slope_form(x1, y1, m)
    assert callable(line_function)
    assert line_function(x_test) == pytest.approx(expected)


@pytest.mark.parametrize(
    "x1, y1, m, x_values, expected_values",
    [
        (1, 2, 3, [0, 1, 2, 3], [-1, 2, 5, 8]),
        (0, 0, -1, [-2, -1, 0, 1, 2], [2, 1, 0, -1, -2]),
    ],
)
def test_point_slope_form_multiple_points(
    x1: float,
    y1: float,
    m: float,
    x_values: list[float],
    expected_values: list[float],
) -> None:
    line_function = point_slope_form(x1, y1, m)
    for x, expected in zip(x_values, expected_values):
        assert line_function(x) == pytest.approx(expected)
