from apysc._material_design.icon.material_videocam_icon import MaterialvideocamIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvideocamIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvideocamIcon = MaterialvideocamIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
