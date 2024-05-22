from apysc._material_design.icon.material_volume_off_icon import MaterialVolumeOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVolumeOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVolumeOffIcon = MaterialVolumeOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
