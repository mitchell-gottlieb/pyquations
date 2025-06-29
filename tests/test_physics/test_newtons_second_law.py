import pytest

from pyquations.physics.newtons_second_law import newtons_second_law


@pytest.mark.parametrize(
    "mass, acceleration, force, expected",
    [
        # Solve for Mass
        (None, 9.8, 98, 10),
        (None, 3.2, 4.8, pytest.approx(1.5)),  # type: ignore
        (None, 1.5, 150, 100),
        # Solve for Acceleration
        (10, None, 98, pytest.approx(9.8)),  # type: ignore
        (1.5, None, 4.8, pytest.approx(3.2)),  # type: ignore
        (100, None, 150, pytest.approx(1.5)),  # type: ignore
        # Solve for Force
        (10, 9.8, None, 98),
        (1.5, 3.2, None, pytest.approx(4.8)),  # type: ignore
        (100, 1.5, None, 150),
    ],
)
def test_newtons_second_law(
    mass: float | None,
    acceleration: float | None,
    force: float | None,
    expected: float,
):
    assert (
        newtons_second_law(mass=mass, acceleration=acceleration, force=force)
        == expected
    )


@pytest.mark.parametrize(
    "mass, acceleration, force",
    [
        # Invalid Values
        (None, 0, 1),
        (1, None, -1),
        (0, 1, None),
        # Invalid Number of Parameters
        (1, 1, 1),
        (None, 1, None),
        (None, None, None),
    ],
)
def test_newtons_second_law_invalid(
    mass: float | None, acceleration: float | None, force: float | None
):
    with pytest.raises(ValueError):
        newtons_second_law(mass=mass, acceleration=acceleration, force=force)
