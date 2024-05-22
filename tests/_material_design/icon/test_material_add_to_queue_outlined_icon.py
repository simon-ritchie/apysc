from apysc._material_design.icon.material_add_to_queue_outlined_icon import (
    MaterialAddToQueueOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddToQueueOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddToQueueOutlinedIcon = MaterialAddToQueueOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
