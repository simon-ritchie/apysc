from apysc._material_design.icon.material_offline_pin_outlined_icon import (
    MaterialOfflinePinOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOfflinePinOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOfflinePinOutlinedIcon = MaterialOfflinePinOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
