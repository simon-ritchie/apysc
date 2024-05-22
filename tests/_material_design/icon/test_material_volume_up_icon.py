from apysc._material_design.icon.material_volume_up_icon import MaterialVolumeUpIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVolumeUpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVolumeUpIcon = MaterialVolumeUpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
