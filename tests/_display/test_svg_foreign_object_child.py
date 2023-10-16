from apysc._display.svg_foreign_object_child import SVGForeignObjectChild
import apysc as ap
from apysc._expression import expression_data_util, var_names
from apysc._testing.testing_helper import apply_test_settings
import re
from typing import Optional, Match


class TestSVGForeignObjectChild:
    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        foreign_object_child: SVGForeignObjectChild = SVGForeignObjectChild(
            html_str='<div></div>',
        )
        expression: str = expression_data_util.get_current_expression()
        match_: Optional[Match] = re.search(
            pattern=rf"var {foreign_object_child.variable_name} = "
            rf"SVG\({var_names.STRING}_\d+?\);",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match_ is not None

    @apply_test_settings()
    def test__initialize_with_base_value(self) -> None:
        foreign_object_child: SVGForeignObjectChild = (
            SVGForeignObjectChild._initialize_with_base_value()
        )
        assert foreign_object_child._html_str == ""

    @apply_test_settings()
    def test__make_snapshot__revert(self) -> None:
        foreign_object_child = SVGForeignObjectChild(html_str="<div></div>")
        snapshot_name: str = foreign_object_child._get_next_snapshot_name()
        foreign_object_child._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        foreign_object_child._html_str._value = "<span></span>"
        foreign_object_child._run_all_revert_methods(snapshot_name=snapshot_name)
        assert foreign_object_child._html_str == "<div></div>"

        foreign_object_child._html_str._value = "<span></span>"
        foreign_object_child._run_all_revert_methods(snapshot_name=snapshot_name)
        assert foreign_object_child._html_str == "<span></span>"
