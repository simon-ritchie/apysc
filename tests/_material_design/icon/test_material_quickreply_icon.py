from apysc._material_design.icon.material_quickreply_icon import MaterialquickreplyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialquickreplyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialquickreplyIcon = MaterialquickreplyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
