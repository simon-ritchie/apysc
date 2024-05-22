from apysc._material_design.icon.material_call_made_outlined_icon import (
    MaterialCallMadeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallMadeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallMadeOutlinedIcon = MaterialCallMadeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
