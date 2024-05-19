from apysc._material_design.icon.material_play_circle_outline_outlined_icon import (
    MaterialplayCircleOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialplayCircleOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialplayCircleOutlineOutlinedIcon = (
            MaterialplayCircleOutlineOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
