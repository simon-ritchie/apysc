from apysc._material_design.icon.material_mic_off_outlined_icon import MaterialmicOffOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmicOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmicOffOutlinedIcon = MaterialmicOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
