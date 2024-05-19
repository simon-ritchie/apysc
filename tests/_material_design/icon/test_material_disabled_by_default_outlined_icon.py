from apysc._material_design.icon.material_disabled_by_default_outlined_icon import (
    MaterialdisabledByDefaultOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdisabledByDefaultOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdisabledByDefaultOutlinedIcon = (
            MaterialdisabledByDefaultOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
