from apysc._material_design.icon.material_print_outlined_icon import (
    MaterialprintOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialprintOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialprintOutlinedIcon = MaterialprintOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
