from apysc._material_design.icon.material_eject_outlined_icon import (
    MaterialejectOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialejectOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialejectOutlinedIcon = MaterialejectOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
