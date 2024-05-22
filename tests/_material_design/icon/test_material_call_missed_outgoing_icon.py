from apysc._material_design.icon.material_call_missed_outgoing_icon import (
    MaterialCallMissedOutgoingIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallMissedOutgoingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallMissedOutgoingIcon = MaterialCallMissedOutgoingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
