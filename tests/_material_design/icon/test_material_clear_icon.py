from apysc._material_design.icon.material_clear_icon import MaterialclearIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialclearIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialclearIcon = MaterialclearIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
