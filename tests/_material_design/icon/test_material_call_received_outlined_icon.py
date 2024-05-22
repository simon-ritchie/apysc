from apysc._material_design.icon.material_call_received_outlined_icon import (
    MaterialCallReceivedOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallReceivedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallReceivedOutlinedIcon = MaterialCallReceivedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
