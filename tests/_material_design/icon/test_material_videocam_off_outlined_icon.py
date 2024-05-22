from apysc._material_design.icon.material_videocam_off_outlined_icon import (
    MaterialVideocamOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVideocamOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVideocamOffOutlinedIcon = MaterialVideocamOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
