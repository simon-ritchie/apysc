from apysc._material_design.icon.material_get_app_outlined_icon import (
    MaterialgetAppOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgetAppOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgetAppOutlinedIcon = MaterialgetAppOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
