from apysc._material_design.icon.material_how_to_vote_outlined_icon import (
    MaterialHowToVoteOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHowToVoteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHowToVoteOutlinedIcon = MaterialHowToVoteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
