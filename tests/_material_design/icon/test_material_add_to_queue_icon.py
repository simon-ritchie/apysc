from apysc._material_design.icon.material_add_to_queue_icon import (
    MaterialAddToQueueIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddToQueueIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddToQueueIcon = MaterialAddToQueueIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
