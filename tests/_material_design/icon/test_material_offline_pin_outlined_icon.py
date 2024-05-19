from apysc._material_design.icon.material_offline_pin_outlined_icon import (
    MaterialofflinePinOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialofflinePinOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialofflinePinOutlinedIcon = MaterialofflinePinOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
