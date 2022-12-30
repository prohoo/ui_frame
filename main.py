import os

import pytest
if __name__ == '__main__':
    # os.environ['NO_COLOR'] = "1"  #要放第一行才生效？
    pytest.main()
    os.system("allure generate ./temp/.allure_results -o report --clean")
