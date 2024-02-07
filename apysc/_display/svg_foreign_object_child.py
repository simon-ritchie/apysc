"""The module for the `SvgForeignObjectChild` class.
"""

from typing import Union

from apysc._display.css_mixin import CssMixIn
from apysc._display.display_object import DisplayObject
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class SvgForeignObjectChild(
    CssMixIn,
    DisplayObject,
    VariableNameSuffixMixIn,
    InitializeWithBaseValueInterface,
    RevertMixIn,
):
    _html_str: String

    def __init__(
        self,
        *,
        html_str: Union[str, String],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Class implementation for the SVG's foreignObject child.

        Parameters
        ----------
        html_str : Union[str, String]
            A HTML string.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.SVG_FOREIGN_OBJECT_CHILD,
        )
        super(SvgForeignObjectChild, self).__init__(variable_name=variable_name)

        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="html_str"
        )
        self._html_str = to_apysc_val_from_builtin.get_copied_string_from_builtin_val(
            string=html_str,
            variable_name_suffix=suffix,
        )
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression of the SVG's foreignObject child.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"var {self.variable_name} = SVG({self._html_str.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @classmethod
    def _initialize_with_base_value(cls) -> "SvgForeignObjectChild":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        instance : SvgForeignObjectChild
            An initialized instance.
        """
        foreign_object_child: SvgForeignObjectChild = SvgForeignObjectChild(html_str="")
        return foreign_object_child

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, "_html_str"):
            return
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._html_str._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, "_html_str"):
            return
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._html_str._run_all_revert_methods(snapshot_name=snapshot_name)
