from apysc._material_design.icon.material_pause_outlined_icon import (
    MaterialpauseOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpauseOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpauseOutlinedIcon = MaterialpauseOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
