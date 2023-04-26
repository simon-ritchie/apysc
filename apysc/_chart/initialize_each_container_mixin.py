"""The mix-in class implementation for the `_initialize_each_container` method.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class InitializeEachContainerMixIn:
    @final
    @arg_validation_decos.is_builtin_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _initialize_each_container(self, *, variable_name_suffix: str) -> None:
        """
        Initialize each container instance.

        Parameters
        ----------
        variable_name_suffix : str
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Raises
        ------
        TypeError
            If this instance is not an instance of `OverallContainerMixIn`.
        """
        from apysc._chart.overall_container_mixin import OverallContainerMixIn
        from apysc._chart.background_container_mixin import BackgroundContainerMixIn
        from apysc._chart.chart_container_mixin import ChartContainerMixIn

        if not isinstance(self, OverallContainerMixIn):
            raise TypeError(
                "This interface only supports an `OverallContainerMixIn` "
                f"instance: {type(self).__name__}, {self}"
            )
        self._initialize_overall_container(variable_name_suffix=variable_name_suffix)

        if isinstance(self, BackgroundContainerMixIn):
            self._initialize_background_container(
                overall_container=self._overall_container,
                variable_name_suffix=variable_name_suffix
            )

        if isinstance(self, ChartContainerMixIn):
            self._initialize_chart_container(
                overall_container=self._overall_container,
                variable_name_suffix=variable_name_suffix,
            )
