from apysc._material_design.icon.material_highlight_off_icon import (
    MaterialHighlightOffIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHighlightOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHighlightOffIcon = MaterialHighlightOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
