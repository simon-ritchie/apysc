from apysc._material_design.icon.material_radio_outlined_icon import (
    MaterialRadioOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRadioOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRadioOutlinedIcon = MaterialRadioOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
