from apysc._material_design.icon.material_accessible_forward_outlined_icon import (
    MaterialAccessibleForwardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccessibleForwardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccessibleForwardOutlinedIcon = (
            MaterialAccessibleForwardOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
