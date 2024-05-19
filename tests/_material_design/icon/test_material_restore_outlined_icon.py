from apysc._material_design.icon.material_restore_outlined_icon import (
    MaterialrestoreOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrestoreOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrestoreOutlinedIcon = MaterialrestoreOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
