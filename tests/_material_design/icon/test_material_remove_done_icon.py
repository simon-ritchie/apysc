from apysc._material_design.icon.material_remove_done_icon import MaterialRemoveDoneIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRemoveDoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRemoveDoneIcon = MaterialRemoveDoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
