def slope(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculates the slope of a line between two points.

    The slope formula is a fundamental concept in analytic geometry that
    describes the steepness and direction of a line. It represents the ratio
    of the vertical change to the horizontal change between two points on the
    line. [1]_

    .. math::

        m = \\frac{y_2 - y_1}{x_2 - x_1}

    Args:
        x1 (float): x-coordinate of the first point.
        y1 (float): y-coordinate of the first point.
        x2 (float): x-coordinate of the second point.
        y2 (float): y-coordinate of the second point.

    Returns:
        float: The slope of the line connecting the two points.

    Raises:
        ValueError: If 'x1' equals 'x2', as this would represent a vertical
            line with an undefined slope.

    Examples:
        >>> slope(1, 2, 3, 6)
        2.0

        >>> slope(0, 0, 5, 5)
        1.0

    Resources:
        - `Math is Fun: Slope <https://www.mathsisfun.com/gradient.html>`_

    References:
        .. [1] "Slope", Wikipedia.
            https://en.wikipedia.org/wiki/Slope
    """
    if x1 == x2:
        raise ValueError(
            "The x-coordinates must be different to calculate slope (vertical "
            "line has undefined slope).",
        )

    slope: float = (y2 - y1) / (x2 - x1)

    return slope
