from apysc._material_design.icon.material_call_received_icon import (
    MaterialCallReceivedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallReceivedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallReceivedIcon = MaterialCallReceivedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
