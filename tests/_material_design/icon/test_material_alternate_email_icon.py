from apysc._material_design.icon.material_alternate_email_icon import (
    MaterialAlternateEmailIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlternateEmailIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlternateEmailIcon = MaterialAlternateEmailIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
