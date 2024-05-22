from apysc._material_design.icon.material_list_outlined_icon import (
    MaterialListOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialListOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialListOutlinedIcon = MaterialListOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
