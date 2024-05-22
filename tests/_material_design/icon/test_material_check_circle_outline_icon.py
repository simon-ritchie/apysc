from apysc._material_design.icon.material_check_circle_outline_icon import (
    MaterialCheckCircleOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCheckCircleOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCheckCircleOutlineIcon = MaterialCheckCircleOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
