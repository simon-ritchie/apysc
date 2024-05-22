from apysc._material_design.icon.material_check_circle_outline_outlined_icon import (
    MaterialCheckCircleOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCheckCircleOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCheckCircleOutlineOutlinedIcon = (
            MaterialCheckCircleOutlineOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
