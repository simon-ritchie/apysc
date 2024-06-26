from apysc._material_design.icon.material_stay_primary_portrait_outlined_icon import (
    MaterialStayPrimaryPortraitOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStayPrimaryPortraitOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStayPrimaryPortraitOutlinedIcon = (
            MaterialStayPrimaryPortraitOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
