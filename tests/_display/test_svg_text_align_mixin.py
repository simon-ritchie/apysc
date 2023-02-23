from typing import List
import apysc as ap
from apysc._display.svg_text_align_mixin import SVGTextAlign
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_SVGTextAlign() -> None:
    for enum_ in SVGTextAlign:
        assert isinstance(enum_.value, str)
    values: List[str] = [enum.value for enum in SVGTextAlign]
    assert len(values) == len(set(values))
