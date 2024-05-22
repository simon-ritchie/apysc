from apysc._material_design.icon.material_contactless_outlined_icon import (
    MaterialContactlessOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContactlessOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContactlessOutlinedIcon = MaterialContactlessOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
