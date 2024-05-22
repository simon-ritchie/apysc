from apysc._material_design.icon.material_hearing_disabled_icon import (
    MaterialHearingDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHearingDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHearingDisabledIcon = MaterialHearingDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
