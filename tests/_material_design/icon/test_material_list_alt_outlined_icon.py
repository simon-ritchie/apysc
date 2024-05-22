from apysc._material_design.icon.material_list_alt_outlined_icon import (
    MaterialListAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialListAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialListAltOutlinedIcon = MaterialListAltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
