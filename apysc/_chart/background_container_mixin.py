"""The mix-in class implementation for `background_container`-related interfaces.
"""

from typing_extensions import final

from apysc._display.sprite import Sprite
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class BackgroundContainerMixIn:
    _background_container: Sprite

    @final
    @arg_validation_decos.is_display_object_container(
        arg_position_index=1, optional=False
    )
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _initialize_background_container(
        self,
        *,
        overall_container: Sprite,
        variable_name_suffix: str,
    ) -> None:
        """
        Initialize a background container.

        Parameters
        ----------
        overall_container : Sprite
            An overall container instance.
        variable_name_suffix : str
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._background_container = Sprite(variable_name_suffix=variable_name_suffix)
        overall_container.add_child(self._background_container)
