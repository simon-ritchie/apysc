from apysc._material_design.icon.material_done_outline_outlined_icon import (
    MaterialDoneOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDoneOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDoneOutlineOutlinedIcon = MaterialDoneOutlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
