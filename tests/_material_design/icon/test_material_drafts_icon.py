from apysc._material_design.icon.material_drafts_icon import MaterialDraftsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDraftsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDraftsIcon = MaterialDraftsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
