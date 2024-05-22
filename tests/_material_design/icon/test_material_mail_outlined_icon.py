from apysc._material_design.icon.material_mail_outlined_icon import (
    MaterialMailOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMailOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMailOutlinedIcon = MaterialMailOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
