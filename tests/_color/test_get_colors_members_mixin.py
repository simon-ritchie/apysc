from typing import List, Tuple
import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings, assert_raises


class TestGetColorsMenmbersMixIn:

    @apply_test_settings()
    def test___iter___and___next__(self) -> None:
        colors_members: List[Tuple[str, ap.Color]] = ap.Colors.get_colors_members()
        assert ("BLACK_000000", ap.Colors.BLACK_000000) in colors_members
        assert ("BLACK_111111", ap.Colors.BLACK_111111) in colors_members
        for name, color in colors_members:
            assert isinstance(name, str)
            assert isinstance(color, ap.Color)
