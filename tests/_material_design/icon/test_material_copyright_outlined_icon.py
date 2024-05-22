from apysc._material_design.icon.material_copyright_outlined_icon import (
    MaterialCopyrightOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCopyrightOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCopyrightOutlinedIcon = MaterialCopyrightOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
