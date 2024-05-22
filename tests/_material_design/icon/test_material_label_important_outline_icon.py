from apysc._material_design.icon.material_label_important_outline_icon import (
    MaterialLabelImportantOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLabelImportantOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLabelImportantOutlineIcon = MaterialLabelImportantOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
