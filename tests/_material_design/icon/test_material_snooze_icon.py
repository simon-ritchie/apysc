from apysc._material_design.icon.material_snooze_icon import MaterialSnoozeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSnoozeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSnoozeIcon = MaterialSnoozeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
