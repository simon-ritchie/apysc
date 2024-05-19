from apysc._material_design.icon.material_label_off_icon import MateriallabelOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallabelOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallabelOffIcon = MateriallabelOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
