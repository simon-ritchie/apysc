from apysc._material_design.icon.material_mail_outline_outlined_icon import (
    MaterialMailOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMailOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMailOutlineOutlinedIcon = MaterialMailOutlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
