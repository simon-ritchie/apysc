from random import randint
from typing import List

from retrying import retry

import apysc as ap
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._expression import expression_data_util


class TestAttrLinkingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_attr_linking_stack(self) -> None:
        interface: AttrLinkingInterface = AttrLinkingInterface()
        interface._initialize_attr_linking_stack()
        assert interface._attr_linking_stack == []
        interface._attr_linking_stack.append(ap.Int(10))
        interface._initialize_attr_linking_stack()
        assert interface._attr_linking_stack == [ap.Int(10)]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_attr_to_linking_stack(self) -> None:
        interface: AttrLinkingInterface = AttrLinkingInterface()
        interface._append_attr_to_linking_stack(attr=ap.Int(10))
        assert interface._attr_linking_stack == [ap.Int(10)]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_applying_new_attr_val_exp(self) -> None:
        expression_data_util.empty_expression()
        interface: AttrLinkingInterface = AttrLinkingInterface()
        attr_1: ap.Int = ap.Int(10)
        attr_2: ap.Int = ap.Int(20)
        new_attr: ap.Int = ap.Int(30)
        interface._append_attr_to_linking_stack(attr=attr_1)
        interface._append_attr_to_linking_stack(attr=attr_2)
        interface._append_attr_to_linking_stack(attr=new_attr)
        interface._append_applying_new_attr_val_exp(
            new_attr=new_attr)
        expression: str = expression_data_util.get_current_expression()
        assert f'{attr_1.variable_name} = {new_attr.variable_name};' \
            in expression
        assert f'{attr_2.variable_name} = {new_attr.variable_name};' \
            in expression
        assert f'{new_attr.variable_name} = {new_attr.variable_name};' \
            not in expression
