from apysc._material_design.icon.material_label_off_outlined_icon import (
    MaterialLabelOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLabelOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLabelOffOutlinedIcon = MaterialLabelOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
