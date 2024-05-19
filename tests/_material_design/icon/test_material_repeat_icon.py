from apysc._material_design.icon.material_repeat_icon import MaterialrepeatIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrepeatIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrepeatIcon = MaterialrepeatIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
