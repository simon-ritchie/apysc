from apysc._material_design.icon.material_mic_off_icon import MaterialmicOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmicOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmicOffIcon = MaterialmicOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
