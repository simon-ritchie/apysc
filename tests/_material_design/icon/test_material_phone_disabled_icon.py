from apysc._material_design.icon.material_phone_disabled_icon import (
    MaterialPhoneDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPhoneDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPhoneDisabledIcon = MaterialPhoneDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
