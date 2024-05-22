from apysc._material_design.icon.material_label_important_outlined_icon import (
    MaterialLabelImportantOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLabelImportantOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLabelImportantOutlinedIcon = MaterialLabelImportantOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
