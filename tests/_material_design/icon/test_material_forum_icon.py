from apysc._material_design.icon.material_forum_icon import MaterialforumIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforumIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialforumIcon = MaterialforumIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
