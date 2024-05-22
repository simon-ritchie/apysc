from apysc._material_design.icon.material_unpublished_icon import (
    MaterialUnpublishedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialUnpublishedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialUnpublishedIcon = MaterialUnpublishedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
