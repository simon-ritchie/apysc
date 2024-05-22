from apysc._material_design.icon.material_system_update_alt_outlined_icon import (
    MaterialSystemUpdateAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSystemUpdateAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSystemUpdateAltOutlinedIcon = (
            MaterialSystemUpdateAltOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
