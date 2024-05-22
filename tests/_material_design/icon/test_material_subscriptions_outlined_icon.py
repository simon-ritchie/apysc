from apysc._material_design.icon.material_subscriptions_outlined_icon import (
    MaterialSubscriptionsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSubscriptionsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSubscriptionsOutlinedIcon = MaterialSubscriptionsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
