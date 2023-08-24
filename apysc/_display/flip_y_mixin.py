"""Class implementation for the flip_y mix-in.
"""

from typing import Dict
from typing import Optional

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


class FlipYMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):
    _flip_y: Boolean

    @final
    def _initialize_flip_y_if_not_initialized(self) -> None:
        """
        Initialize the _flip_y attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_flip_y"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="flip_y")
        self._flip_y = Boolean(
            False,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_flip_y_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_flip_y_attr_linking_setting(self) -> None:
        """
        Append a flip-y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._flip_y, attr_name="flip_y"
        )
        self._append_attr_to_linking_stack(attr=self._flip_y, attr_name="flip_y")

    @property
    @add_debug_info_setting(module_name=__name__)
    def flip_y(self) -> Boolean:
        """
        Get a boolean value whether the y-axis is flipping or not.

        Returns
        -------
        flip_y : Boolean
            A boolean value whether the y-axis is flipping or not.

        References
        ----------
        - GraphicsBase flip_x and flip_y interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_flip_interfaces.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=0, y=0),
        ...         ap.Point2D(x=50, y=0),
        ...         ap.Point2D(x=25, y=50),
        ...     ]
        ... )
        >>> polygon.flip_y = ap.Boolean(True)
        >>> polygon.flip_y
        Boolean(True)
        """
        from apysc._type import value_util

        self._initialize_flip_y_if_not_initialized()
        return value_util.get_copy(value=self._flip_y)

    @flip_y.setter
    @arg_validation_decos.is_apysc_boolean(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def flip_y(self, value: Boolean) -> None:
        """
        Update a y-axis flipping value.

        Parameters
        ----------
        value : Boolean
            Flipping value. If true, a y-axis will be flipped,
            otherwise it will be reset.

        References
        ----------
        - GraphicsBase flip_x and flip_y interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_flip_interfaces.html  # noqa
        """
        self._initialize_flip_y_if_not_initialized()
        before_value: Boolean = self._flip_y
        self._flip_y = value
        self._append_flip_y_update_expression(before_value=before_value)

        self._append_flip_y_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_flip_y_update_expression(self, *, before_value: Boolean) -> None:
        """
        Append a y-axis flipping value updating expression.

        Parameters
        ----------
        before_value : Boolean
            Before updating flipping value.
        """
        from apysc._display import flip_interface_helper
        from apysc._expression import expression_data_util

        self._initialize_flip_y_if_not_initialized()
        expression: str = flip_interface_helper.make_flip_update_expression(
            before_value=before_value,
            after_value=self._flip_y,
            axis=flip_interface_helper.Axis.Y,
            interface_variable_name=self.variable_name,
        )
        expression_data_util.append_js_expression(expression=expression)

    _flip_y_snapshots: Optional[Dict[str, bool]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_flip_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_flip_y_snapshots",
            value=self._flip_y._value,
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
        self._flip_y._value = self._get_snapshot_val_if_exists(
            current_value=self._flip_y._value,
            snapshot_dict=self._flip_y_snapshots,
            snapshot_name=snapshot_name,
        )
