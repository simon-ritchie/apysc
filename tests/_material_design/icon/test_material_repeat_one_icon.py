from apysc._material_design.icon.material_repeat_one_icon import MaterialrepeatOneIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrepeatOneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrepeatOneIcon = MaterialrepeatOneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
