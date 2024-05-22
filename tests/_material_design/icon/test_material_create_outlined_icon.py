from apysc._material_design.icon.material_create_outlined_icon import (
    MaterialCreateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCreateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCreateOutlinedIcon = MaterialCreateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
