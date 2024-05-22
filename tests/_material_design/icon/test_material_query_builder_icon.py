from apysc._material_design.icon.material_query_builder_icon import (
    MaterialQueryBuilderIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQueryBuilderIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQueryBuilderIcon = MaterialQueryBuilderIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
