from apysc._material_design.icon.material_add_to_queue_icon import MaterialaddToQueueIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddToQueueIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddToQueueIcon = MaterialaddToQueueIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
