from apysc._material_design.icon.material_reorder_outlined_icon import (
    MaterialReorderOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReorderOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReorderOutlinedIcon = MaterialReorderOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
