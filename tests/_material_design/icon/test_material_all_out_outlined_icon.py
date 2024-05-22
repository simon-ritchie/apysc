from apysc._material_design.icon.material_all_out_outlined_icon import (
    MaterialAllOutOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAllOutOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAllOutOutlinedIcon = MaterialAllOutOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
