from apysc._material_design.icon.material_view_module_outlined_icon import (
    MaterialviewModuleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewModuleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewModuleOutlinedIcon = MaterialviewModuleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
