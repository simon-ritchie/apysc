from apysc._material_design.icon.material_check_circle_icon import (
    MaterialCheckCircleIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCheckCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCheckCircleIcon = MaterialCheckCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
