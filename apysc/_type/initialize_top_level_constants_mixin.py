"""The mix-in class implementation for the top-level scope's `apysc`
values constants.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting


class InitializeTopLevelConstantsMixIn:

    @add_debug_info_setting(module_name=__name__)
    def _initialize_top_level_constants(self) -> None:
        """
        Initialize top-level scope's `apysc` values constants.
        """
        import apysc as ap
        from apysc._type.true import _True
        from apysc._type.false import _False

        ap.True_ = _True()
        ap.False_ = _False()
