from apysc._material_design.icon.material_fiber_smart_record_icon import (
    MaterialFiberSmartRecordIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFiberSmartRecordIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFiberSmartRecordIcon = MaterialFiberSmartRecordIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
