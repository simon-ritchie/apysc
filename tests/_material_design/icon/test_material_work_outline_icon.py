from apysc._material_design.icon.material_work_outline_icon import (
    MaterialWorkOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWorkOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWorkOutlineIcon = MaterialWorkOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
