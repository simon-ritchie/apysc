from apysc._material_design.icon.material_extension_outlined_icon import (
    MaterialExtensionOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialExtensionOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialExtensionOutlinedIcon = MaterialExtensionOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
