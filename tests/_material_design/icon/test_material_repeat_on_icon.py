from apysc._material_design.icon.material_repeat_on_icon import MaterialRepeatOnIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRepeatOnIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRepeatOnIcon = MaterialRepeatOnIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
