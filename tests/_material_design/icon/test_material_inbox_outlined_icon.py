from apysc._material_design.icon.material_inbox_outlined_icon import (
    MaterialInboxOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialInboxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialInboxOutlinedIcon = MaterialInboxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
