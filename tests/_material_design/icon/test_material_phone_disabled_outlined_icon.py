from apysc._material_design.icon.material_phone_disabled_outlined_icon import (
    MaterialphoneDisabledOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphoneDisabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphoneDisabledOutlinedIcon = MaterialphoneDisabledOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
