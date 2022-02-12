"""Class implementation for the CSS interface.
"""

from typing import Dict
from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_interface import RevertInterface
from apysc._type.string import String
from apysc._type.variable_name_interface import VariableNameInterface


class CssInterface(VariableNameInterface, RevertInterface):

    _css: Dict[str, String]

    def _initialize_css_if_not_initialized(self) -> None:
        """
        Initialize the _css attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, '_css'):
            return
        self._css = {}

    @add_debug_info_setting(  # type: ignore
        module_name=__name__, class_name='CssInterface')
    def get_css(self, name: Union[str, String]) -> String:
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
        - Display object get_css and set_css interfaces document
            - https://simon-ritchie.github.io/apysc/display_object_get_and_set_css.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
        >>> sprite.set_css(name='display', value='none')
        >>> sprite.get_css(name='display')
        String('none')
        """
        import apysc as ap
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

    @add_debug_info_setting(  # type: ignore
        module_name=__name__, class_name='CssInterface')
    def _append_get_css_expresion(
            self, *, name: Union[str, String], css: String) -> None:
        """
        Append a CSS getter expression string.

        Parameters
        ----------
        name : str or String
            CSS name (e.g., 'display').
        css : String
            CSS value.
        """
        import apysc as ap
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

    @add_debug_info_setting(  # type: ignore
        module_name=__name__, class_name='CssInterface')
    def set_css(
            self, name: Union[str, String],
            value: Union[str, String]) -> None:
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
        - Display object get_css and set_css interfaces document
            - https://simon-ritchie.github.io/apysc/display_object_get_and_set_css.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
        >>> sprite.set_css(name='display', value='none')
        >>> sprite.get_css(name='display')
        String('none')
        """
        import apysc as ap
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._converter import to_builtin_val_from_apysc
        self._initialize_css_if_not_initialized()
        name_: str = to_builtin_val_from_apysc.\
            get_builtin_str_from_apysc_val(string=name)
        value_: ap.String = to_apysc_val_from_builtin.\
            get_copied_string_from_builtin_val(string=value)
        self._css[name_] = value_
        self._append_set_css_expression(name=name, value=value)

    @add_debug_info_setting(  # type: ignore
        module_name=__name__, class_name='CssInterface')
    def _append_set_css_expression(
            self, *, name: Union[str, String],
            value: Union[str, String]) -> None:
        """
        Append a CSS setter expression string.

        Parameters
        ----------
        name : str or String
            CSS name (e.g., 'display').
        value : str or String
            A CSS value string (e.g., 'none').
        """
        import apysc as ap
        from apysc._type import value_util
        name_value_str: str = value_util.get_value_str_for_expression(
            value=name)
        value_str: str = value_util.get_value_str_for_expression(
            value=value)
        expression: str = (
            f'{self.variable_name}.css({name_value_str}, {value_str});'
        )
        ap.append_js_expression(expression=expression)

    _css_snapshot: Dict[str, Dict[str, String]]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_css_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_css_snapshot',
            value={**self._css}, snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
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
