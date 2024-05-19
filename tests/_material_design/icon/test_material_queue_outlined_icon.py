from apysc._material_design.icon.material_queue_outlined_icon import MaterialqueueOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialqueueOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialqueueOutlinedIcon = MaterialqueueOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
