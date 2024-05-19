from apysc._material_design.icon.material_all_inbox_outlined_icon import (
    MaterialallInboxOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialallInboxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialallInboxOutlinedIcon = MaterialallInboxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
