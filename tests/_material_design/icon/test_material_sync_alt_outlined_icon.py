from apysc._material_design.icon.material_sync_alt_outlined_icon import (
    MaterialsyncAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsyncAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsyncAltOutlinedIcon = MaterialsyncAltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
