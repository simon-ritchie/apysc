from apysc._material_design.icon.material_schedule_send_icon import (
    MaterialScheduleSendIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialScheduleSendIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialScheduleSendIcon = MaterialScheduleSendIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
