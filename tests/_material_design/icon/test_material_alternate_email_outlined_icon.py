from apysc._material_design.icon.material_alternate_email_outlined_icon import (
    MaterialAlternateEmailOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlternateEmailOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlternateEmailOutlinedIcon = MaterialAlternateEmailOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
