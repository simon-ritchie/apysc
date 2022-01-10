"""Class implementation for line joints interface.
"""

from typing import Dict
from typing import Union

from apysc._display.line_joints import LineJoints
from apysc._type.revert_interface import RevertInterface
from apysc._type.string import String
from apysc._type.variable_name_interface import VariableNameInterface


class LineJointsInterface(VariableNameInterface, RevertInterface):

    _line_joints: String

    def _initialize_line_joints_if_not_initialized(self) -> None:
        """
        Initialize _line_joints attribute if that it is not
        initialized yet.
        """
        if hasattr(self, '_line_joints'):
            return
        self._line_joints = String(LineJoints.MITER.value)

    @property
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
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> _ = sprite.graphics.move_to(x=50, y=100)
        >>> _ = sprite.graphics.line_to(x=100, y=50)
        >>> line: ap.Polyline = sprite.graphics.line_to(x=150, y=100)
        >>> line.line_joints = ap.LineJoints.ROUND
        >>> line.line_joints
        String('round')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_joints', locals_=locals(),
                module_name=__name__, class_=LineJointsInterface):
            self._initialize_line_joints_if_not_initialized()
            return self._line_joints._copy()

    @line_joints.setter
    def line_joints(self, value: Union[String, LineJoints]) -> None:
        """
        Set line joints style setting.

        Parameters
        ----------
        value : String or LineJoints
            Line joints style setting to set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_joints', locals_=locals(),
                module_name=__name__, class_=LineJointsInterface):
            self._update_line_joints_and_skip_appending_exp(value=value)
            self._append_line_joints_update_expression()

    def _update_line_joints_and_skip_appending_exp(
            self, *, value: Union[String, LineJoints]) -> None:
        """
        Update line joints and skip appending expression.

        Parameters
        ----------
        value : STring or LineJoints
            Line joints style setting to set.
        """
        from apysc._validation.display_validation import validate_line_joints
        if not isinstance(value, (String, LineJoints)):
            raise TypeError(
                'Not supported line_joints type specified: '
                f'{type(value)}'
                '\nAcceptable ones are: String or LineJoints.')
        validate_line_joints(joints=value)
        if isinstance(value, String):
            self._line_joints = value._copy()
        else:
            self._line_joints = String(value.value)

    def _append_line_joints_update_expression(self) -> None:
        """
        Append line cap updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_line_joints_update_expression,
                locals_=locals(),
                module_name=__name__, class_=LineJointsInterface):
            from apysc._type import value_util
            joints_name: str = value_util.get_value_str_for_expression(
                value=self._line_joints)
            expression: str = (
                f'{self.variable_name}.attr'
                f'({{"stroke-linejoin": {joints_name}}});'
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
            dict_name='_line_joints_snapshots',
            value=self._line_joints._value, snapshot_name=snapshot_name)

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
