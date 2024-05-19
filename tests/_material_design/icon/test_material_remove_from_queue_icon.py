from apysc._material_design.icon.material_remove_from_queue_icon import (
    MaterialremoveFromQueueIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialremoveFromQueueIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialremoveFromQueueIcon = MaterialremoveFromQueueIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
