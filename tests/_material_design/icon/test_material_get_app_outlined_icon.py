from apysc._material_design.icon.material_get_app_outlined_icon import (
    MaterialGetAppOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGetAppOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGetAppOutlinedIcon = MaterialGetAppOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
