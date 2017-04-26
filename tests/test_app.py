import time
import os
import pytest
from pytest_bdd import scenarios, when, then

scenarios('features')

@pytest.fixture(scope='session', autouse=True)
def driver():
    from appium import webdriver
    app = os.path.abspath(
                os.path.join(os.path.dirname(__file__),
                '../platforms/ios/build/emulator/HelloCordova.app'))
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            # 'app': app,
            # 'platformName' : 'iOS',
            # 'platformVersion' : '10.2',
            # 'deviceName' : 'iPhone SE',
        }
    )
    webview = driver.contexts[-1]
    driver.switch_to.context(webview)
    yield driver
    driver.quit()


@when('I open the app')
def open_the_app(driver):
    time.sleep(1)

@then('I should see Cordova start screen')
def see_cordova_start(driver):
    time.sleep(1)
    title = driver.find_element_by_class_name("title")
    assert title.text == 'APACHE CORDOVA'
