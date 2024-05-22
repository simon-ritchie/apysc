from apysc._material_design.icon.material_work_outline_outlined_icon import (
    MaterialWorkOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWorkOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWorkOutlineOutlinedIcon = MaterialWorkOutlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
