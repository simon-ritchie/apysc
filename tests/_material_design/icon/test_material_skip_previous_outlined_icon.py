from apysc._material_design.icon.material_skip_previous_outlined_icon import (
    MaterialskipPreviousOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialskipPreviousOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialskipPreviousOutlinedIcon = MaterialskipPreviousOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
