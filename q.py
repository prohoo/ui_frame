# import pytest
#
#
# @pytest.mark.parametrize("data",["中文","乱码"])
# def test_q(data):
#     pass
#

import json
data = {"name":"qwe","sex":"male"}
# with open("json.json", "r") as f:
#     data = json.load(f)
# print(data)
with open("json2.json", "w") as f:
    json.dump(data, f)