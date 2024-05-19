from apysc._material_design.icon.material_surround_sound_outlined_icon import MaterialsurroundSoundOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsurroundSoundOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsurroundSoundOutlinedIcon = MaterialsurroundSoundOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
