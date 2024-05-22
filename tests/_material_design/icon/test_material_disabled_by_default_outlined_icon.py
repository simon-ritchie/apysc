from apysc._material_design.icon.material_disabled_by_default_outlined_icon import (
    MaterialDisabledByDefaultOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDisabledByDefaultOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDisabledByDefaultOutlinedIcon = (
            MaterialDisabledByDefaultOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
