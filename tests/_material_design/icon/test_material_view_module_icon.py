from apysc._material_design.icon.material_view_module_icon import MaterialViewModuleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewModuleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewModuleIcon = MaterialViewModuleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
