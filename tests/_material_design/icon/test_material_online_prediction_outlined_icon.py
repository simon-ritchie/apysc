from apysc._material_design.icon.material_online_prediction_outlined_icon import (
    MaterialOnlinePredictionOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOnlinePredictionOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOnlinePredictionOutlinedIcon = (
            MaterialOnlinePredictionOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
