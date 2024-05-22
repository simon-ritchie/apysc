from apysc._material_design.icon.material_clear_icon import MaterialClearIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialClearIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialClearIcon = MaterialClearIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
