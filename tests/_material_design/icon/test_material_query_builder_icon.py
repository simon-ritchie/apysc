from apysc._material_design.icon.material_query_builder_icon import (
    MaterialqueryBuilderIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialqueryBuilderIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialqueryBuilderIcon = MaterialqueryBuilderIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
