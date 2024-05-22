from apysc._material_design.icon.material_videocam_off_icon import (
    MaterialVideocamOffIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVideocamOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVideocamOffIcon = MaterialVideocamOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
