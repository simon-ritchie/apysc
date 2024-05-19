from apysc._material_design.icon.material_volume_off_icon import MaterialvolumeOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvolumeOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvolumeOffIcon = MaterialvolumeOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
