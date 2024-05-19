from apysc._material_design.icon.material_dynamic_form_icon import MaterialdynamicFormIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdynamicFormIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdynamicFormIcon = MaterialdynamicFormIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
