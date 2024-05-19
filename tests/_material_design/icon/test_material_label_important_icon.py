from apysc._material_design.icon.material_label_important_icon import (
    MateriallabelImportantIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallabelImportantIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallabelImportantIcon = MateriallabelImportantIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
