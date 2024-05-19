from apysc._material_design.icon.material_featured_play_list_icon import MaterialfeaturedPlayListIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfeaturedPlayListIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfeaturedPlayListIcon = MaterialfeaturedPlayListIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
