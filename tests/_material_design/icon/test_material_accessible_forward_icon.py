from apysc._material_design.icon.material_accessible_forward_icon import (
    MaterialAccessibleForwardIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccessibleForwardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccessibleForwardIcon = MaterialAccessibleForwardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
