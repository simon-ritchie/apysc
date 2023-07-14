"""The mix-in class implementation for the `_validate_stage_is_created`
method.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting


class ValidateStateIsCreatedMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _validate_stage_is_created(self) -> None:
        """
        Validate whether a created stage exists or not.

        Raises
        ------
        StageNotCreatedError
            If there is no instantiated stage yet.
        """
        from apysc._display.stage import is_stage_created, StageNotCreatedError

        if is_stage_created():
            return
        raise StageNotCreatedError(
            "A stage instance has not been created yet."
            "\nPlease instantiate the `Stage` class before calling this interface."
        )
