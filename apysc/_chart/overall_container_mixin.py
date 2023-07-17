"""The mix-in class implementation for `overall_container`-related interfaces.
"""

from typing_extensions import final

from apysc._display.sprite import Sprite
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class OverallContainerMixIn:
    _overall_container: Sprite

    @final
    @arg_validation_decos.is_builtin_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _initialize_overall_container(self, *, variable_name_suffix: str) -> None:
        """
        Initialize an overall container.

        Parameters
        ----------
        variable_name_suffix : str
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._overall_container = Sprite(variable_name_suffix=variable_name_suffix)
