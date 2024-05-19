from apysc._material_design.icon.material_block_icon import MaterialblockIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialblockIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialblockIcon = MaterialblockIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
