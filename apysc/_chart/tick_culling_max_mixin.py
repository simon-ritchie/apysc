"""The mix-in class implementation for the `tick_culling_max_mixin` value.
"""

from typing import Dict, Optional, Union
from apysc._type.revert_mixin import RevertMixIn
from typing_extensions import final
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos
from apysc._type.int import Int


class TickCullingMaxMixIn(
    RevertMixIn,
):

    _tick_culling_max: Optional[Int]

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_tick_culling_max(
        self,
        *,
        tick_culling_max: Optional[Union[int, Int]],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial tick max display number

        Parameters
        ----------
        tick_culling_max : Optional[Union[int, Int]]
            A tick max display number.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if tick_culling_max is not None and not isinstance(tick_culling_max, Int):
            tick_culling_max_: Optional[Int] = Int(
                tick_culling_max, variable_name_suffix=variable_name_suffix
            )
        else:
            tick_culling_max_ = tick_culling_max
        self._tick_culling_max = tick_culling_max_

    _tick_culling_max_snapshots: Optional[Dict[str, int]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if self._tick_culling_max is None:
            return
        self._set_single_snapshot_val_to_dict(
            dict_name="_tick_culling_max_snapshots",
            value=self._tick_culling_max._value,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if self._tick_culling_max is None:
            return
        self._tick_culling_max._value = self._get_snapshot_val_if_exists(
            current_value=self._tick_culling_max._value,
            snapshot_dict=self._tick_culling_max_snapshots,
            snapshot_name=snapshot_name,
        )
