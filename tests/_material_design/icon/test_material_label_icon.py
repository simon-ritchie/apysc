from apysc._material_design.icon.material_label_icon import MaterialLabelIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLabelIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLabelIcon = MaterialLabelIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
