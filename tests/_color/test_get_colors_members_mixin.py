from typing import List
from typing import Tuple

import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestGetColorsMenmbersMixIn:
    @apply_test_settings()
    def test_get_colors_members(self) -> None:
        colors_members: List[Tuple[str, ap.Color]] = ap.Colors.get_colors_members()
        assert ("BLACK_000000", ap.Colors.BLACK_000000) in colors_members
        assert ("BLACK_111111", ap.Colors.BLACK_111111) in colors_members
        for name, color in colors_members:
            assert isinstance(name, str)
            assert isinstance(color, ap.Color)
