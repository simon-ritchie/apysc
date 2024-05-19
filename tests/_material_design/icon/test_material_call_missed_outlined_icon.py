from apysc._material_design.icon.material_call_missed_outlined_icon import (
    MaterialcallMissedOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcallMissedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcallMissedOutlinedIcon = MaterialcallMissedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
