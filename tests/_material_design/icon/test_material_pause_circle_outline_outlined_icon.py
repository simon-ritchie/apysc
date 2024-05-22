from apysc._material_design.icon.material_pause_circle_outline_outlined_icon import (
    MaterialPauseCircleOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPauseCircleOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPauseCircleOutlineOutlinedIcon = (
            MaterialPauseCircleOutlineOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
