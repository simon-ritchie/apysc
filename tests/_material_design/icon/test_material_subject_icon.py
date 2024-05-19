from apysc._material_design.icon.material_subject_icon import MaterialsubjectIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsubjectIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsubjectIcon = MaterialsubjectIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
