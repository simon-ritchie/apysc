"""The class implementation for the `MultiLineText` class.
"""

from typing import Optional
from typing import Union

from apysc._display.add_foreign_object_child_mixin import AddForeignObjectChildMixIn
from apysc._display.add_to_parent_mixin import AddToParentMixIn
from apysc._display.append_foreign_object_constructor_expression_mixin import (
    AppendForeignObjectConstructorExpressionMixIn,
)
from apysc._display.child_mixin import ChildMixIn
from apysc._display.css_mixin import CssMixIn
from apysc._display.display_object import DisplayObject
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.svg_foreign_object_child_mixin import SVGForeignObjectChildMixIn
from apysc._display.svg_foreign_object_initialize_width_mixin import (
    SVGForeignObjectInitializeWidthMixIn,
)
from apysc._display.svg_foreign_object_text_mixin import SVGForeignObjectTextMixIn
from apysc._display.width_mixin import WidthMixIn
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.int import Int
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class MultiLineText(
    DisplayObject,
    WidthMixIn,
    VariableNameSuffixMixIn,
    CssMixIn,
    SetOverflowVisibleSettingMixIn,
    InitializeWithBaseValueInterface,
    AddForeignObjectChildMixIn,
    AppendForeignObjectConstructorExpressionMixIn,
    SVGForeignObjectInitializeWidthMixIn,
    SVGForeignObjectTextMixIn,
    SVGForeignObjectChildMixIn,
    AddToParentMixIn,
):
    # parent
    @arg_validation_decos.is_display_object_container(
        arg_position_index=3, optional=True
    )
    def __init__(
        self,
        text: Union[str, String],
        width: Union[int, Int],
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class implementation for a multiline text element.

        Parameters
        ----------
        text : Union[str, String]
            Text to display. An HTML tag is available.
        width : Union[int, Int]
            Width of the text to wrap.
        parent : ChildMixIn or None, default None
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._variable_name_suffix = variable_name_suffix
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.MULTILINE_TEXT,
        )
        super(MultiLineText, self).__init__(variable_name=variable_name)
        self._initialize_width(width=width)
        self._append_foreign_object_constructor_expression()
        self._add_to_parent(parent=parent)
        self._set_overflow_visible_setting()
        self._initialize_text(text=text)
        self._initialize_svg_foreign_object_child(
            html_str=self._text, variable_name_suffix=variable_name_suffix
        )

    @classmethod
    def _initialize_with_base_value(cls) -> "MultiLineText":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        text : MultiLineText
            An initialized instance.
        """
        text: MultiLineText = cls(text="", width=0)
        return text
