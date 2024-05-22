from apysc._material_design.icon.material_online_prediction_icon import (
    MaterialOnlinePredictionIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOnlinePredictionIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOnlinePredictionIcon = MaterialOnlinePredictionIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
