from apysc._material_design.icon.material_https_outlined_icon import (
    MaterialHttpsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHttpsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHttpsOutlinedIcon = MaterialHttpsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
