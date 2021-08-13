# import pytest
# @pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
# def test_eval(test_input,expected):
#     assert eval(test_input) == expected
import pytest
import yaml


class TestDemo:

    @pytest.mark.parametrize("a,b",yaml.safe_load(open("./a.yaml")))
    def test_dmeo(self,a,b):
        print(a+b)