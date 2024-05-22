from apysc._material_design.icon.material_label_outline_icon import (
    MaterialLabelOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLabelOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLabelOutlineIcon = MaterialLabelOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
