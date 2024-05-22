from apysc._material_design.icon.material_flag_outlined_icon import (
    MaterialFlagOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFlagOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFlagOutlinedIcon = MaterialFlagOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
