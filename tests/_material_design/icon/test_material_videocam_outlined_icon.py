from apysc._material_design.icon.material_videocam_outlined_icon import (
    MaterialvideocamOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvideocamOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvideocamOutlinedIcon = MaterialvideocamOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
