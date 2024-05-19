from apysc._material_design.icon.material_surround_sound_icon import MaterialsurroundSoundIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsurroundSoundIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsurroundSoundIcon = MaterialsurroundSoundIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
