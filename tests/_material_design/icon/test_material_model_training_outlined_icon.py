from apysc._material_design.icon.material_model_training_outlined_icon import (
    MaterialmodelTrainingOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmodelTrainingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmodelTrainingOutlinedIcon = MaterialmodelTrainingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
