from apysc._material_design.icon.material_flag_outlined_icon import (
    MaterialflagOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialflagOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialflagOutlinedIcon = MaterialflagOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
