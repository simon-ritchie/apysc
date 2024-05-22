from apysc._material_design.icon.material_pause_outlined_icon import (
    MaterialPauseOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPauseOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPauseOutlinedIcon = MaterialPauseOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
