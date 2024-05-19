from apysc._material_design.icon.material_perm_phone_msg_outlined_icon import (
    MaterialpermPhoneMsgOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpermPhoneMsgOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpermPhoneMsgOutlinedIcon = MaterialpermPhoneMsgOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
