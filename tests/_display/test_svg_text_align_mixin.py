from typing import List
import apysc as ap
from apysc._display.svg_text_align_mixin import SVGTextAlign
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._display.svg_text_align_mixin import SVGTextAlignMixIn


@apply_test_settings()
def test_SVGTextAlign() -> None:
    for enum_ in SVGTextAlign:
        assert isinstance(enum_.value, str)
    values: List[str] = [enum.value for enum in SVGTextAlign]
    assert len(values) == len(set(values))


class TestSVGTextAlignMixIn:
    @apply_test_settings()
    def test_align(self) -> None:
        expression_data_util.empty_expression()
        mixin: SVGTextAlignMixIn = SVGTextAlignMixIn()
        mixin.variable_name = "test_mixin"
        assert mixin.align == SVGTextAlign.LEFT

        mixin.align = SVGTextAlign.CENTER
        assert mixin.align == SVGTextAlign.CENTER
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{mixin.variable_name}.font("anchor", "middle")'
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot__revert(self) -> None:
        mixin: SVGTextAlignMixIn = SVGTextAlignMixIn()
        mixin.align = SVGTextAlign.CENTER
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.align = SVGTextAlign.LEFT
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.align == SVGTextAlign.CENTER

        mixin.align = SVGTextAlign.LEFT
        mixin._run_all_revert_methods(snapshot_name="not_existing_snapshot")
        assert mixin.align == SVGTextAlign.LEFT
