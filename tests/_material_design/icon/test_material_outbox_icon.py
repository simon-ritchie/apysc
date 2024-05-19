from apysc._material_design.icon.material_outbox_icon import MaterialoutboxIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialoutboxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialoutboxIcon = MaterialoutboxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
