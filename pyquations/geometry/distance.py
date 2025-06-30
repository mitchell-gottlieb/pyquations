from math import sqrt


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculates the distance between two points in a Cartesian plane.

    The Euclidean distance formula is a direct application of the Pythagorean
    theorem, measuring the straight-line distance between two points in a
    Cartesian coordinate system. [1]_

    .. math::

        d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

    Args:
        x1 (float): x-coordinate of the first point.
        y1 (float): y-coordinate of the first point.
        x2 (float): x-coordinate of the second point.
        y2 (float): y-coordinate of the second point.

    Returns:
        float: The Euclidean distance between the two points.

    Examples:
        >>> distance(0, 0, 3, 4)
        5.0

        >>> distance(1, 2, 4, 6)
        5.0

        >>> distance(-2, -3, 2, 3)
        8.48528...

    References:
        .. [1] "Distance", Wikipedia.
            https://en.wikipedia.org/wiki/Distance#Geometry
    """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
