from apysc._material_design.icon.material_fiber_smart_record_outlined_icon import (
    MaterialfiberSmartRecordOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfiberSmartRecordOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfiberSmartRecordOutlinedIcon = (
            MaterialfiberSmartRecordOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
