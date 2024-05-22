from apysc._material_design.icon.material_call_missed_outgoing_outlined_icon import (
    MaterialCallMissedOutgoingOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallMissedOutgoingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallMissedOutgoingOutlinedIcon = (
            MaterialCallMissedOutgoingOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
