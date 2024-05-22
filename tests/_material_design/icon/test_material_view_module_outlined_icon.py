from apysc._material_design.icon.material_view_module_outlined_icon import (
    MaterialViewModuleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewModuleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewModuleOutlinedIcon = MaterialViewModuleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
