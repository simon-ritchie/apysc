from apysc._material_design.icon.material_videocam_off_outlined_icon import MaterialvideocamOffOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvideocamOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvideocamOffOutlinedIcon = MaterialvideocamOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
