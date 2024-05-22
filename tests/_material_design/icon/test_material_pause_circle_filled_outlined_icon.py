from apysc._material_design.icon.material_pause_circle_filled_outlined_icon import (
    MaterialPauseCircleFilledOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPauseCircleFilledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPauseCircleFilledOutlinedIcon = (
            MaterialPauseCircleFilledOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
