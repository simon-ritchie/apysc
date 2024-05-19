from apysc._material_design.icon.material_touch_app_outlined_icon import (
    MaterialtouchAppOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtouchAppOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtouchAppOutlinedIcon = MaterialtouchAppOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
