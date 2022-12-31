"""Class implementation for the `visible` mix-in.
"""

from typing import Dict

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.boolean import Boolean
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class VisibleMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _visible: Boolean

    @final
    def _initialize_visible_if_not_initialized(self) -> None:
        """
        Initialize _visible attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, "_visible"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="visible")
        self._visible = Boolean(
            True,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_visible_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_visible_attr_linking_setting(self) -> None:
        """
        Append a visible attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._visible, attr_name="visible"
        )
        self._append_attr_to_linking_stack(attr=self._visible, attr_name="visible")

    @property
    @add_debug_info_setting(module_name=__name__)
    def visible(self) -> Boolean:
        """
        Get a visibility value of this instance.

        Returns
        -------
        result : Boolean
            If this instance is visible, this interface returns True.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.visible = ap.Boolean(False)
        >>> rectangle.visible
        Boolean(False)
        """
        from apysc._type import value_util

        self._initialize_visible_if_not_initialized()
        return value_util.get_copy(value=self._visible)

    @visible.setter
    @arg_validation_decos.is_apysc_boolean(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def visible(self, value: Boolean) -> None:
        """
        Update a visibility value of this instance.

        Parameters
        ----------
        value : Boolean
            Boolean value to set.
        """
        self._visible = value
        self._append_visible_update_expression()

        self._append_visible_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_visible_update_expression(self) -> None:
        """
        Append visible property updating expression.
        """
        import apysc as ap

        expression: str = (
            f"if ({self._visible.variable_name}) {{"
            f"\n  {self.variable_name}.show();"
            "\n}else {"
            f"\n  {self.variable_name}.hide();"
            "\n}"
        )
        ap.append_js_expression(expression=expression)

    _visible_snapshots: Dict[str, bool]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_visible_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_visible_snapshots",
            value=self._visible._value,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value is snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._visible._value = self._visible_snapshots[snapshot_name]
