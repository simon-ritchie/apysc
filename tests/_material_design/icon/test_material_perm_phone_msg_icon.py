from apysc._material_design.icon.material_perm_phone_msg_icon import (
    MaterialPermPhoneMsgIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPermPhoneMsgIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPermPhoneMsgIcon = MaterialPermPhoneMsgIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
