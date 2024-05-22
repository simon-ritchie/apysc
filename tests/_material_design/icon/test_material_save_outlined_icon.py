from apysc._material_design.icon.material_save_outlined_icon import (
    MaterialSaveOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSaveOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSaveOutlinedIcon = MaterialSaveOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
