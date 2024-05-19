from apysc._material_design.icon.material_videocam_off_icon import MaterialvideocamOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvideocamOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvideocamOffIcon = MaterialvideocamOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
