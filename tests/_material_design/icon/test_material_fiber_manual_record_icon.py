from apysc._material_design.icon.material_fiber_manual_record_icon import (
    MaterialFiberManualRecordIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFiberManualRecordIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFiberManualRecordIcon = MaterialFiberManualRecordIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
