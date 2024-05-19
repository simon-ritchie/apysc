from apysc._material_design.icon.material_drafts_outlined_icon import MaterialdraftsOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdraftsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdraftsOutlinedIcon = MaterialdraftsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
