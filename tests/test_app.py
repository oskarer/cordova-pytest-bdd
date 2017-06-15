import time
import os
import pytest
from pytest_bdd import scenarios, when, then

scenarios('features')

@pytest.fixture(scope='session', autouse=True)
def driver():
    from appium import webdriver
    ios = os.path.abspath(
                os.path.join(os.path.dirname(__file__),
                '../platforms/ios/build/emulator/HelloCordova.app'))
    android = os.path.abspath(
                os.path.join(os.path.dirname(__file__),
                '../platforms/android/build/outputs/apk/android-debug.apk'))
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            # IOS
            # 'app': ios,
            # 'platformName' : 'iOS',
            # 'platformVersion' : '10.2',
            # 'deviceName' : 'iPhone SE',
            # ANDROID
            # 'app': android,
            # 'platformName' : 'Android',
            # 'platformVersion' : '6.0',
            # 'deviceName' : 'Android',
            # 'autoWebview': 'true',
            # 'udid' : '0a30789d',
        }
    )
    time.sleep(1)
    print driver.contexts
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
