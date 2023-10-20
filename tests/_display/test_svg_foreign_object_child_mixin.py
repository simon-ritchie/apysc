from apysc._display.svg_foreign_object_child_mixin import SVGForeignObjectChildMixIn


class TestSVGForeignObjectChildMixIn:
    def test__initialize_svg_foreign_object_child(self) -> None:
        mixin: SVGForeignObjectChildMixIn = SVGForeignObjectChildMixIn()
        mixin._initialize_svg_foreign_object_child(
            html_str='<p>test</p>',
            variable_name_suffix='test_suffix',
        )
        assert mixin._svg_foreign_object_child._html_str == '<p>test</p>'
        assert mixin._svg_foreign_object_child._variable_name_suffix == 'test_suffix'
