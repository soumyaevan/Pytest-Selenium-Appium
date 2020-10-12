import pytest
import json
from selenium.webdriver import Chrome, Firefox

CONFIG_PATH = './lib/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSER = ['chrome','firefox']

@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSER:
        raise Exception(f"{config['browser']} is not supported in this framework")
    return config['browser']

@pytest.fixture(scope='session')
def config_implicit_wait(config):
    return config['implicit_wait'] if 'implicit_wait' in config else DEFAULT_WAIT_TIME

@pytest.fixture
def browser(config_browser,config_implicit_wait):
    if config_browser == 'chrome':
        driver = Chrome('./chromedriver')
    elif config_browser == 'firefox':
        driver = Firefox(executable_path='./geckodriver')
    else:
        raise Exception(f"{config['browser']} is not supported in this framework")
    driver.implicitly_wait(config_implicit_wait)
    yield driver
    driver.quit()