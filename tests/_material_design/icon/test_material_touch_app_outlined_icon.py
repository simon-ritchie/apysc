from apysc._material_design.icon.material_touch_app_outlined_icon import (
    MaterialTouchAppOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTouchAppOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTouchAppOutlinedIcon = MaterialTouchAppOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
