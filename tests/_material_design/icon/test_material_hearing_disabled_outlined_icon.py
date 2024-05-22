from apysc._material_design.icon.material_hearing_disabled_outlined_icon import (
    MaterialHearingDisabledOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHearingDisabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHearingDisabledOutlinedIcon = (
            MaterialHearingDisabledOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
