from apysc._material_design.icon.material_mic_off_icon import MaterialMicOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMicOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMicOffIcon = MaterialMicOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
