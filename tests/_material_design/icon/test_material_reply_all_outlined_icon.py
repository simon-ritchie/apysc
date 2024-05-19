from apysc._material_design.icon.material_reply_all_outlined_icon import (
    MaterialreplyAllOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreplyAllOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreplyAllOutlinedIcon = MaterialreplyAllOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
