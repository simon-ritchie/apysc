"""The constant definition for the `Colorless` class.
"""

from typing_extensions import Final

from apysc._color.color import Color


class Colorless(Color):
    """
    The constant class for the colorlessness.
    """

    def __init__(self) -> None:
        """
        The constant class for the colorlessness.
        """
        super(Colorless, self).__init__(value="", variable_name_suffix="colorless")


COLORLESS: Final[Colorless] = Colorless()
