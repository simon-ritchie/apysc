from apysc._material_design.icon.material_add_to_queue_outlined_icon import (
    MaterialaddToQueueOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddToQueueOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddToQueueOutlinedIcon = MaterialaddToQueueOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
