
Pytest Selenium
This sample project would allow you to understand basic pytest run along with Allure reporting

Please make sure you have Python, Java installed on your machine beforehand

How to install pytest
pip install pytest


How to install selenium
pip install selenium or python -m pip install selenium


How to install allure
Download allure commandline from: https://mvnrepository.com/artifact/io.qameta.allure/allure-commandline/2.8.1
Unzip the directory and put the path of bin to PATH in environment variables
pip install allure-pytest or pip install pytest-allure-adaptor

How to configure jenkins
Manage Jenkins -> Manage Plugins -> Python and Allure Also add Allure comma
ndline path in Global Tools Configuration

How to setup PyCharm
Install plugins in Pycharm explicitly for pytest, selenium and allure

How to run the code via cmd
pytest -v -s --alluredir=path to your report folder <test_filename.py>
