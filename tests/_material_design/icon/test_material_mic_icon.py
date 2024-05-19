from apysc._material_design.icon.material_mic_icon import MaterialmicIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmicIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmicIcon = MaterialmicIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
