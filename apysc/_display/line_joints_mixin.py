"""Class implementation for line joints mix-in.
"""

from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._display.line_joints import LineJoints
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class LineJointsMixIn(VariableNameSuffixAttrMixIn, VariableNameMixIn, RevertMixIn):

    _line_joints: String

    @final
    def _initialize_line_joints_if_not_initialized(self) -> None:
        """
        Initialize _line_joints attribute if this interface does
        not initialize it yet.
        """
        if hasattr(self, "_line_joints"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="line_joints")
        self._line_joints = String(
            LineJoints.MITER.value,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_joints(self) -> Union[String, LineJoints]:
        """
        Get this instance's line joints style setting.

        Returns
        -------
        line_joints : String
            Line joints style setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=10)
        >>> _ = sprite.graphics.move_to(x=50, y=100)
        >>> _ = sprite.graphics.line_to(x=100, y=50)
        >>> line: ap.Polyline = sprite.graphics.line_to(x=150, y=100)
        >>> line.line_joints = ap.LineJoints.ROUND
        >>> line.line_joints
        String('round')
        """
        self._initialize_line_joints_if_not_initialized()
        return self._line_joints._copy()

    @line_joints.setter
    @arg_validation_decos.is_line_joints(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def line_joints(self, value: Union[String, LineJoints]) -> None:
        """
        Set line joints style setting.

        Parameters
        ----------
        value : String or LineJoints
            Line joints style setting to set.
        """
        self._update_line_joints_and_skip_appending_exp(value=value)
        self._append_line_joints_update_expression()

    @final
    def _update_line_joints_and_skip_appending_exp(
        self, *, value: Union[String, LineJoints]
    ) -> None:
        """
        Update line joints and skip appending expression.

        Parameters
        ----------
        value : STring or LineJoints
            Line joints style setting to set.
        """
        if not isinstance(value, (String, LineJoints)):
            raise TypeError(
                "Not supported line_joints type specified: "
                f"{type(value)}"
                "\nAcceptable ones are: String or LineJoints."
            )
        if isinstance(value, String):
            self._line_joints = value._copy()
        else:
            self._line_joints = String(value.value)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_joints_update_expression(self) -> None:
        """
        Append line cap updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        joints_name: str = value_util.get_value_str_for_expression(
            value=self._line_joints
        )
        expression: str = (
            f"{self.variable_name}.attr" f'({{"stroke-linejoin": {joints_name}}});'
        )
        ap.append_js_expression(expression=expression)

    _line_joints_snapshots: Dict[str, str]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_joints_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_joints_snapshots",
            value=self._line_joints._value,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._line_joints._value = self._line_joints_snapshots[snapshot_name]
