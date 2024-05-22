from apysc._material_design.icon.material_cancel_schedule_send_outlined_icon import (
    MaterialCancelScheduleSendOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCancelScheduleSendOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCancelScheduleSendOutlinedIcon = (
            MaterialCancelScheduleSendOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
