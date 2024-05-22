from apysc._material_design.icon.material_eject_outlined_icon import (
    MaterialEjectOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialEjectOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialEjectOutlinedIcon = MaterialEjectOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
