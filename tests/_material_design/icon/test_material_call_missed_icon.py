from apysc._material_design.icon.material_call_missed_icon import MaterialCallMissedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallMissedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallMissedIcon = MaterialCallMissedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
