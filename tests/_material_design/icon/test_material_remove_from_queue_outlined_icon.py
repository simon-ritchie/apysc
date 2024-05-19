from apysc._material_design.icon.material_remove_from_queue_outlined_icon import (
    MaterialremoveFromQueueOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialremoveFromQueueOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialremoveFromQueueOutlinedIcon = (
            MaterialremoveFromQueueOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
