from apysc._material_design.icon.material_list_icon import MateriallistIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallistIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallistIcon = MateriallistIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
