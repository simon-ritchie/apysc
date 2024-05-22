from apysc._material_design.icon.material_call_end_icon import MaterialCallEndIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallEndIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallEndIcon = MaterialCallEndIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
