from apysc._material_design.icon.material_print_icon import MaterialprintIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialprintIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialprintIcon = MaterialprintIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
