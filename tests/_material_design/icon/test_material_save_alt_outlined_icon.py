from apysc._material_design.icon.material_save_alt_outlined_icon import (
    MaterialsaveAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsaveAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsaveAltOutlinedIcon = MaterialsaveAltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
