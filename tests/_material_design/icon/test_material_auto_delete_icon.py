from apysc._material_design.icon.material_auto_delete_icon import MaterialAutoDeleteIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAutoDeleteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAutoDeleteIcon = MaterialAutoDeleteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
