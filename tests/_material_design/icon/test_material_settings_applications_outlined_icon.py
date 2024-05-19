from apysc._material_design.icon.material_settings_applications_outlined_icon import (
    MaterialsettingsApplicationsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsApplicationsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsApplicationsOutlinedIcon = (
            MaterialsettingsApplicationsOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
