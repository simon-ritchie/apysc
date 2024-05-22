from apysc._material_design.icon.material_fiber_manual_record_outlined_icon import (
    MaterialFiberManualRecordOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFiberManualRecordOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFiberManualRecordOutlinedIcon = (
            MaterialFiberManualRecordOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
