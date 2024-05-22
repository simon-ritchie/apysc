from apysc._material_design.icon.material_event_outlined_icon import (
    MaterialEventOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialEventOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialEventOutlinedIcon = MaterialEventOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
