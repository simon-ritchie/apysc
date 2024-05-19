from apysc._material_design.icon.material_queue_icon import MaterialqueueIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialqueueIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialqueueIcon = MaterialqueueIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
