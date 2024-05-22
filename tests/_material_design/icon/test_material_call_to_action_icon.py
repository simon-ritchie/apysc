from apysc._material_design.icon.material_call_to_action_icon import (
    MaterialCallToActionIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallToActionIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallToActionIcon = MaterialCallToActionIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
