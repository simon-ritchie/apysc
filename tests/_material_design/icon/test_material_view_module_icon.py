from apysc._material_design.icon.material_view_module_icon import MaterialviewModuleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewModuleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewModuleIcon = MaterialviewModuleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
