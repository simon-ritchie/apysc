"""Class implementation for the css interface.
"""

from typing import Dict
from typing import Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class CssInterface(VariableNameInterface, RevertInterface):

    _css: Dict[str, ap.String]

    def _initialize_css_if_not_initialized(self) -> None:
        """
        Initialize the _css attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_css'):
            return
        self._css = {}

    def get_css(self, name: Union[str, ap.String]) -> ap.String:
        """
        Get a CSS value string.

        Parameters
        ----------
        name : str or String
            CSS name (e.g., 'display').

        Returns
        -------
        css : ap.String
            CSS value.

        References
        ----------
        Display object get_css and set_css interfaces document
            https://bit.ly/3wNgIWI
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.get_css, locals_=locals(),
                module_name=__name__, class_=CssInterface):
            from apysc._converter import to_builtin_val_from_apysc
            self._initialize_css_if_not_initialized()
            name_: str = to_builtin_val_from_apysc.\
                get_builtin_str_from_apysc_val(string=name)
            if name_ in self._css:
                css: ap.String = self._css[name_]._copy()
            else:
                css = ap.String('')
            self._append_get_css_expresion(name=name, css=css)
            return css

    def _append_get_css_expresion(
            self, name: Union[str, ap.String], css: ap.String) -> None:
        """
        Append a css getter expression string.

        Parameters
        ----------
        name : str or String
            CSS name (e.g., 'display').
        css : String
            CSS value.
        """
        with ap.DebugInfo(
                callable_=self._append_get_css_expresion, locals_=locals(),
                module_name=__name__, class_=CssInterface):
            from apysc._type import value_util
            name_value_str: str = value_util.get_value_str_for_expression(
                value=name)
            css_value_str: str = value_util.get_value_str_for_expression(
                value=css)
            expression: str = (
                f'{css_value_str} = {self.variable_name}.'
                f'css({name_value_str});'
            )
            ap.append_js_expression(expression=expression)

    def set_css(
            self, name: Union[str, ap.String],
            value: Union[str, ap.String]) -> None:
        """
        Set a specified value string to the CSS.

        Parameters
        ----------
        name : str or String
            CSS name (e.g., 'display').
        value : str or String
            A CSS value string (e.g., 'none').

        References
        ----------
        Display object get_css and set_css interfaces document
            https://bit.ly/3wNgIWI
        """
        with ap.DebugInfo(
                callable_=self.set_css, locals_=locals(),
                module_name=__name__, class_=CssInterface):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._converter import to_builtin_val_from_apysc
            self._initialize_css_if_not_initialized()
            name_: str = to_builtin_val_from_apysc.\
                get_builtin_str_from_apysc_val(string=name)
            value_: ap.String = to_apysc_val_from_builtin.\
                get_copied_string_from_builtin_val(string=value)
            self._css[name_] = value_
            self._append_set_css_expression(name=name, value=value)

    def _append_set_css_expression(
            self, name: Union[str, ap.String],
            value: Union[str, ap.String]) -> None:
        """
        Append a css setter expression string.

        Parameters
        ----------
        name : str or String
            CSS name (e.g., 'display').
        value : str or String
            A CSS value string (e.g., 'none').
        """
        with ap.DebugInfo(
                callable_=self._append_set_css_expression, locals_=locals(),
                module_name=__name__, class_=CssInterface):
            from apysc._type import value_util
            name_value_str: str = value_util.get_value_str_for_expression(
                value=name)
            value_str: str = value_util.get_value_str_for_expression(
                value=value)
            expression: str = (
                f'{self.variable_name}.css({name_value_str}, {value_str});'
            )
            ap.append_js_expression(expression=expression)

    _css_snapshot: Dict[str, Dict[str, ap.String]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_css_if_not_initialized()
        if not hasattr(self, '_css_snapshot'):
            self._css_snapshot = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._css_snapshot[snapshot_name] = {**self._css}

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._css = self._css_snapshot[snapshot_name]
