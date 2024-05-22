from apysc._material_design.icon.material_dynamic_form_icon import (
    MaterialDynamicFormIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDynamicFormIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDynamicFormIcon = MaterialDynamicFormIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
