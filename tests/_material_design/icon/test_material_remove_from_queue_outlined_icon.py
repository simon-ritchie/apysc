from apysc._material_design.icon.material_remove_from_queue_outlined_icon import (
    MaterialRemoveFromQueueOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRemoveFromQueueOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRemoveFromQueueOutlinedIcon = (
            MaterialRemoveFromQueueOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
