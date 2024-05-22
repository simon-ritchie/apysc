from apysc._material_design.icon.material_play_arrow_outlined_icon import (
    MaterialPlayArrowOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlayArrowOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlayArrowOutlinedIcon = MaterialPlayArrowOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
