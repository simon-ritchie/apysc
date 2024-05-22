from apysc._material_design.icon.material_clear_all_outlined_icon import (
    MaterialClearAllOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialClearAllOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialClearAllOutlinedIcon = MaterialClearAllOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
