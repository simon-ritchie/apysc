from apysc._material_design.icon.material_store_outlined_icon import (
    MaterialStoreOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStoreOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStoreOutlinedIcon = MaterialStoreOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
