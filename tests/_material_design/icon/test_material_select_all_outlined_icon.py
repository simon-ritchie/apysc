from apysc._material_design.icon.material_select_all_outlined_icon import (
    MaterialselectAllOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialselectAllOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialselectAllOutlinedIcon = MaterialselectAllOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
