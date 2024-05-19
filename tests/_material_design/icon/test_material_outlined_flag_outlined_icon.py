from apysc._material_design.icon.material_outlined_flag_outlined_icon import (
    MaterialoutlinedFlagOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialoutlinedFlagOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialoutlinedFlagOutlinedIcon = MaterialoutlinedFlagOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
