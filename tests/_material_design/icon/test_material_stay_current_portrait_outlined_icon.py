from apysc._material_design.icon.material_stay_current_portrait_outlined_icon import (
    MaterialstayCurrentPortraitOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstayCurrentPortraitOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstayCurrentPortraitOutlinedIcon = (
            MaterialstayCurrentPortraitOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
