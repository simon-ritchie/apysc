from apysc._material_design.icon.material_mic_off_outlined_icon import (
    MaterialMicOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMicOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMicOffOutlinedIcon = MaterialMicOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
