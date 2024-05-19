from apysc._material_design.icon.material_volume_down_icon import MaterialvolumeDownIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvolumeDownIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvolumeDownIcon = MaterialvolumeDownIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
