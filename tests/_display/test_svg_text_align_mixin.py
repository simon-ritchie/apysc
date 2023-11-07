from typing import List

from apysc._display.svg_text_align_mixin import SvgTextAlign
from apysc._display.svg_text_align_mixin import SvgTextAlignMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_SVGTextAlign() -> None:
    for enum_ in SvgTextAlign:
        assert isinstance(enum_.value, str)
    values: List[str] = [enum.value for enum in SvgTextAlign]
    assert len(values) == len(set(values))


class TestSVGTextAlignMixIn:
    @apply_test_settings()
    def test_align(self) -> None:
        mixin: SvgTextAlignMixIn = SvgTextAlignMixIn()
        mixin.variable_name = "test_mixin"
        assert mixin.align == SvgTextAlign.LEFT

        mixin.align = SvgTextAlign.CENTER
        assert mixin.align == SvgTextAlign.CENTER
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{mixin.variable_name}.font("anchor", "middle")'
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot__revert(self) -> None:
        mixin: SvgTextAlignMixIn = SvgTextAlignMixIn()
        mixin.align = SvgTextAlign.CENTER
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.align = SvgTextAlign.LEFT
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.align == SvgTextAlign.CENTER

        mixin.align = SvgTextAlign.LEFT
        mixin._run_all_revert_methods(snapshot_name="not_existing_snapshot")
        assert mixin.align == SvgTextAlign.LEFT
