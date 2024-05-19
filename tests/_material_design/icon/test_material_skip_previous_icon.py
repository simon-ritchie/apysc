from apysc._material_design.icon.material_skip_previous_icon import (
    MaterialskipPreviousIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialskipPreviousIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialskipPreviousIcon = MaterialskipPreviousIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
