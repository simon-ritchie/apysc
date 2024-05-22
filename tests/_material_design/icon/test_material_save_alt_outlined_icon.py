from apysc._material_design.icon.material_save_alt_outlined_icon import (
    MaterialSaveAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSaveAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSaveAltOutlinedIcon = MaterialSaveAltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
