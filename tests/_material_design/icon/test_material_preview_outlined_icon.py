from apysc._material_design.icon.material_preview_outlined_icon import (
    MaterialPreviewOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPreviewOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPreviewOutlinedIcon = MaterialPreviewOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
