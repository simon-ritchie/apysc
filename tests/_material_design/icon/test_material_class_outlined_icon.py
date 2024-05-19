from apysc._material_design.icon.material_class_outlined_icon import MaterialclassOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialclassOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialclassOutlinedIcon = MaterialclassOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
