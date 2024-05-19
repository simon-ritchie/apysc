from apysc._material_design.icon.material_store_outlined_icon import (
    MaterialstoreOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstoreOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstoreOutlinedIcon = MaterialstoreOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
