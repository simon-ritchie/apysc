from apysc._material_design.icon.material_reply_outlined_icon import (
    MaterialReplyOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReplyOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReplyOutlinedIcon = MaterialReplyOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
