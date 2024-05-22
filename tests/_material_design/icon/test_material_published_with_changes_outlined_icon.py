from apysc._material_design.icon.material_published_with_changes_outlined_icon import (
    MaterialPublishedWithChangesOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPublishedWithChangesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPublishedWithChangesOutlinedIcon = (
            MaterialPublishedWithChangesOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
