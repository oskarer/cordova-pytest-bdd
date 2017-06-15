# Minimal Pytest Appium setup

## Running the tests on local device
This is written for Windows

### 1. Virtual environment
This is to create a project specific environment and make sure we don't get
any unwanted global dependencies.

Create the virtual environment in the .virtualenv folder (only has to be done once);

`virtualenv .virtualenv`

Activate the virtual environment;

`./.virtualenv/bin/activate`

### 2. Install dependencies

`pip install -r requirements.txt`

`npm install -g appium`

### 3. Build Cordova app

`cordova build android`

### 4. Update script with device details

In tests/test_app.py theres a section which has to be updated with the details on the device you're using;

```
'platformName' : 'Android',
'platformVersion' : '6.0',
'deviceName' : 'Android',
'autoWebview': 'true',
'udid' : '0a30789d',
```

The udid can be found running `adb devices`.

### 5. Run tests

 * Start the appium server `appium`.
 * Run tests `py.test tests`.

## Run on AWS Device Farm

Comment out the device details in tests/test_app.py first, otherwise it won't work.

Then follow this guide;
https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-appium-python.html

*IMPORTANT:*

AWS Device Farm does not support any dependencies with native C extensions. MarkupSafe, which is included in pytest-bdd, has that so replace the MarkupSafe .whl-file in wheelhouse folder with the following;

https://www.dropbox.com/s/218uca7n0nzxvce/MarkupSafe-1.0-py2.py3-none-any.whl?dl=0
