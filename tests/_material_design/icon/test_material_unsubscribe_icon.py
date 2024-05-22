from apysc._material_design.icon.material_unsubscribe_icon import (
    MaterialUnsubscribeIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialUnsubscribeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialUnsubscribeIcon = MaterialUnsubscribeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
