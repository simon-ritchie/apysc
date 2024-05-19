from apysc._material_design.icon.material_snooze_outlined_icon import MaterialsnoozeOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsnoozeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsnoozeOutlinedIcon = MaterialsnoozeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
