from apysc._material_design.icon.material_mic_outlined_icon import (
    MaterialMicOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMicOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMicOutlinedIcon = MaterialMicOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
