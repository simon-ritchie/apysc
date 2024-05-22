from apysc._material_design.icon.material_email_outlined_icon import (
    MaterialEmailOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialEmailOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialEmailOutlinedIcon = MaterialEmailOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
