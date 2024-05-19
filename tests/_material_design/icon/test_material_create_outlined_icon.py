from apysc._material_design.icon.material_create_outlined_icon import (
    MaterialcreateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcreateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcreateOutlinedIcon = MaterialcreateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
