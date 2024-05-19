from apysc._material_design.icon.material_preview_outlined_icon import (
    MaterialpreviewOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpreviewOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpreviewOutlinedIcon = MaterialpreviewOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
