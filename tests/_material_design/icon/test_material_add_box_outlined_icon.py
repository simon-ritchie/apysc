from apysc._material_design.icon.material_add_box_outlined_icon import (
    MaterialAddBoxOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddBoxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddBoxOutlinedIcon = MaterialAddBoxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
