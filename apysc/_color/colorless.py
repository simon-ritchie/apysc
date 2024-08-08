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

        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="colorless"
        )
        super(Colorless, self).__init__(value="", variable_name_suffix=suffix)


COLORLESS: Final[Colorless] = Colorless()
