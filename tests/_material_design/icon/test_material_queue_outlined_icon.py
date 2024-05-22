from apysc._material_design.icon.material_queue_outlined_icon import (
    MaterialQueueOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQueueOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQueueOutlinedIcon = MaterialQueueOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
