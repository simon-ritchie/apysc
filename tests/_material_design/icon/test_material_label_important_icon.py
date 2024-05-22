from apysc._material_design.icon.material_label_important_icon import (
    MaterialLabelImportantIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLabelImportantIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLabelImportantIcon = MaterialLabelImportantIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
