from apysc._material_design.icon.material_queue_play_next_icon import (
    MaterialQueuePlayNextIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQueuePlayNextIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQueuePlayNextIcon = MaterialQueuePlayNextIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
