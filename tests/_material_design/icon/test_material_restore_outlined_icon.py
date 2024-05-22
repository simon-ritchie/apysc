from apysc._material_design.icon.material_restore_outlined_icon import (
    MaterialRestoreOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRestoreOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRestoreOutlinedIcon = MaterialRestoreOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
