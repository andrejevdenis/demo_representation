<h1 align="center">Demo testing of mobile app <a href="https://www.dns-shop.ru/" target="_blank">DNS-SHOP</a> 



## Table of Contents
- [Objects for test](#-objects-for-test)
- [How to Build](#-how-to-build)
- [Example of a report](#%EF%B8%8F-example-of-a-report)
- [Summary](#-summary)

## 🎯 Aim
I'l take some simple positive tests, to show:
- how i bild structure of work directory
- how i solve problems for launch same tests for cloud and local
- prepared Jankins build to simple launch wanted tests
- examples of tools in action 

## 🎯 Objects for test
#### Mobile
- User authorization
- Validation of search result
- Adding product to cart
#### Web
- User authorization
- Adding product to cart

#### API

## 📝 How to Build

To build autotests in Jenkins:
1. Open [project](https://jenkins.autotests.cloud/job/DNS_mobile/)
2. Choose Build with parameters
3. If necessary, change the parameters by selecting values from lists
4. Push Build
5. The result of starting the assembly can be viewed in the Allure report

To build the test local follow these steps:
```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed

# Clone the repository
git clone https://github.com/andrejevdenis/DNS_mobile_demo

# Download last version of Allure
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

# Download last version of Android Studio
https://developer.android.com/studio?hl

# Run project to build first allure report
pytest tests --context={choises}
choices=['app_cloud','app_local_real','all','mobile','local','cloud', 'web', 'web_cloud', 'web_local', 'api', 'api_local', 'api_cloud']

# Build allure report
allure/bin/allure.bat serve allure-results

# Troubleshooting 

1. Check installed python packages. Use pip install for frameworks from pyproject.toml
2. Check path environment variable windows
```
## ▶️ Example of a report
### Allure report generated
<img src="https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Allure1.png" width="630" height="320"/>

### Test statistics collected, bugs localized
<img src="https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Allure2.png" width="630" height="320"/>

### Attached is a video of the test
<img src="https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Allure3.gif" width="630" height="320"/>

### Notification received of Jenkins build results in Telegram bot
<img src="https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Telegram.png" width="350" height="320"/>

## 📈 Summary
First test is just an example of valid test. I fill an incorrect email in order not to clog the production. But it passed! And here we go to interesting part of my test...  
Second and third shows bugs on https://www.takamul.net.sa
If i truly worked on it, for failed autotests i go there and manually locate this bug, check what can be wrong else? And then i can create a bug report for developers/

