from apysc._material_design.icon.material_tab_outlined_icon import (
    MaterialtabOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtabOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtabOutlinedIcon = MaterialtabOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
