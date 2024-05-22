from apysc._material_design.icon.material_cancel_schedule_send_icon import (
    MaterialCancelScheduleSendIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCancelScheduleSendIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCancelScheduleSendIcon = MaterialCancelScheduleSendIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
