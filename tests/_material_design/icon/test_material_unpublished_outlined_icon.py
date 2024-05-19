from apysc._material_design.icon.material_unpublished_outlined_icon import MaterialunpublishedOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialunpublishedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialunpublishedOutlinedIcon = MaterialunpublishedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
