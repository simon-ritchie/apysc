from apysc._material_design.icon.material_input_outlined_icon import (
    MaterialInputOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialInputOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialInputOutlinedIcon = MaterialInputOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
