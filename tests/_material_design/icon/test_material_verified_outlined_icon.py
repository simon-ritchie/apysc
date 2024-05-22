from apysc._material_design.icon.material_verified_outlined_icon import (
    MaterialVerifiedOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVerifiedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVerifiedOutlinedIcon = MaterialVerifiedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
