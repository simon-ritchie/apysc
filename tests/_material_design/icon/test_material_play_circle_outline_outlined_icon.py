from apysc._material_design.icon.material_play_circle_outline_outlined_icon import (
    MaterialPlayCircleOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlayCircleOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlayCircleOutlineOutlinedIcon = (
            MaterialPlayCircleOutlineOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
