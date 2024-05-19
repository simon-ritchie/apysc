from apysc._material_design.icon.material_published_with_changes_icon import (
    MaterialpublishedWithChangesIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpublishedWithChangesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpublishedWithChangesIcon = MaterialpublishedWithChangesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
