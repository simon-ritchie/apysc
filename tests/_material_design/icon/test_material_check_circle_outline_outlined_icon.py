from apysc._material_design.icon.material_check_circle_outline_outlined_icon import (
    MaterialcheckCircleOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcheckCircleOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcheckCircleOutlineOutlinedIcon = (
            MaterialcheckCircleOutlineOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
