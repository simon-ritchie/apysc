from apysc._material_design.icon.material_send_icon import MaterialsendIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsendIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsendIcon = MaterialsendIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
