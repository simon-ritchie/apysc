from apysc._material_design.icon.material_videocam_outlined_icon import (
    MaterialVideocamOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVideocamOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVideocamOutlinedIcon = MaterialVideocamOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
