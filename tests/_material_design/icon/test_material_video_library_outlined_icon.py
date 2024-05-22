from apysc._material_design.icon.material_video_library_outlined_icon import (
    MaterialVideoLibraryOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVideoLibraryOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVideoLibraryOutlinedIcon = MaterialVideoLibraryOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
