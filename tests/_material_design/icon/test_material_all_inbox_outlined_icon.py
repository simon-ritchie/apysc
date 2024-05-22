from apysc._material_design.icon.material_all_inbox_outlined_icon import (
    MaterialAllInboxOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAllInboxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAllInboxOutlinedIcon = MaterialAllInboxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
