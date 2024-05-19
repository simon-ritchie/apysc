from apysc._material_design.icon.material_label_outlined_icon import (
    MateriallabelOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallabelOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallabelOutlinedIcon = MateriallabelOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
