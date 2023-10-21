"""The mix-in class for the `_add_to_stage` method.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting


class AddToStageMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _add_to_stage(self) -> None:
        """
        Add this instance to a stage instance.
        """
        from apysc._display.display_object import DisplayObject
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage

        if not isinstance(self, DisplayObject):
            raise TypeError(
                "This method is only available for `DisplayObject` subclasses."
            )

        stage: Stage = get_stage()
        stage.add_child(child=self)
