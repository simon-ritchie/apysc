from apysc._material_design.icon.material_volume_mute_icon import MaterialVolumeMuteIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVolumeMuteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVolumeMuteIcon = MaterialVolumeMuteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
