from apysc._material_design.icon.material_event_icon import MaterialeventIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialeventIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialeventIcon = MaterialeventIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
