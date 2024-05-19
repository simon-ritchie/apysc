from apysc._material_design.icon.material_repeat_on_icon import MaterialrepeatOnIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrepeatOnIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrepeatOnIcon = MaterialrepeatOnIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
