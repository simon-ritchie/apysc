from apysc._material_design.icon.material_label_off_outlined_icon import (
    MateriallabelOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallabelOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallabelOffOutlinedIcon = MateriallabelOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
