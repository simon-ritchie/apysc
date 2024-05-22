from apysc._material_design.icon.material_call_to_action_outlined_icon import (
    MaterialCallToActionOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallToActionOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallToActionOutlinedIcon = MaterialCallToActionOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
