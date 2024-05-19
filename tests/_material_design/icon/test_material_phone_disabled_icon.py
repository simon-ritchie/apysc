from apysc._material_design.icon.material_phone_disabled_icon import (
    MaterialphoneDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphoneDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphoneDisabledIcon = MaterialphoneDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
