from typing import Callable


def point_slope_form(
    x1: float,
    y1: float,
    m: float,
) -> Callable[[float], float]:
    """Creates a function representing a line in point-slope form.

    The point-slope form is a way to express the equation of a line using a
    point on the line and the slope of the line. It is particularly useful
    when a point on the line and the slope are known. [1]_

    .. math::

        y - y_1 = m(x - x_1)

    Where:

    - :math:`(x_1, y_1)` is a known point on the line.
    - :math:`m` is the slope of the line.

    Args:
        x1 (float): x-coordinate of the known point on the line.
        y1 (float): y-coordinate of the known point on the line.
        m (float): The slope of the line.

    Returns:
        Callable[[float], float]: A function that takes an x-coordinate and
        returns the corresponding y-coordinate on the line.

    Examples:
        >>> line = point_slope_form(2, 3, 4)
        >>> line(3)
        7.0
        >>> line(0)
        -5.0

    Resources:
        - `Math is Fun: Point Slope Form <https://www.mathsisfun.com/algebra/
          line-equation-point-slope.html>`_

    References:
        .. [1] "Point-slope form", Wikipedia.
            https://en.wikipedia.org/wiki/Linear_equation#Point-slope_form
    """

    def line_function(x: float) -> float:
        """Calculate the y-coordinate for a given x using point-slope form.

        Args:
            x (float): The x-coordinate to calculate the corresponding
                y-coordinate for.

        Returns:
            float: The y-coordinate on the line.
        """
        return y1 + m * (x - x1)

    return line_function
