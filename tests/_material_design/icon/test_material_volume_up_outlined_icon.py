from apysc._material_design.icon.material_volume_up_outlined_icon import MaterialvolumeUpOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvolumeUpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvolumeUpOutlinedIcon = MaterialvolumeUpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
