from apysc._material_design.icon.material_source_outlined_icon import (
    MaterialsourceOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsourceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsourceOutlinedIcon = MaterialsourceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
