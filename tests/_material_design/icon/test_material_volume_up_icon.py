from apysc._material_design.icon.material_volume_up_icon import MaterialvolumeUpIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvolumeUpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvolumeUpIcon = MaterialvolumeUpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
