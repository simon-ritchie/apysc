from apysc._material_design.icon.material_cancel_schedule_send_outlined_icon import (
    MaterialcancelScheduleSendOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcancelScheduleSendOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcancelScheduleSendOutlinedIcon = (
            MaterialcancelScheduleSendOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
