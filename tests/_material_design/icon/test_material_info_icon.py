from apysc._material_design.icon.material_info_icon import MaterialInfoIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialInfoIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialInfoIcon = MaterialInfoIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
