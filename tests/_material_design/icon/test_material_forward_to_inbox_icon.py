from apysc._material_design.icon.material_forward_to_inbox_icon import (
    MaterialForwardToInboxIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForwardToInboxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForwardToInboxIcon = MaterialForwardToInboxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
