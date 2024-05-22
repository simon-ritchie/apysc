from apysc._material_design.icon.material_call_outlined_icon import (
    MaterialCallOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallOutlinedIcon = MaterialCallOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
