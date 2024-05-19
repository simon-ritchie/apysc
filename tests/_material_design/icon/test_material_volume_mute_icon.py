from apysc._material_design.icon.material_volume_mute_icon import MaterialvolumeMuteIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvolumeMuteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvolumeMuteIcon = MaterialvolumeMuteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
