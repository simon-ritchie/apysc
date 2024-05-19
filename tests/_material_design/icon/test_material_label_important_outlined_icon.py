from apysc._material_design.icon.material_label_important_outlined_icon import (
    MateriallabelImportantOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallabelImportantOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallabelImportantOutlinedIcon = MateriallabelImportantOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
