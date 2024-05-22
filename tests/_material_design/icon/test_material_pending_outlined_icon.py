from apysc._material_design.icon.material_pending_outlined_icon import (
    MaterialPendingOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPendingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPendingOutlinedIcon = MaterialPendingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
