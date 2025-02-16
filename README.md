<h1 align="center">Demo representation of autotest workflow 

## Table of Contents
- [The aim](#-the-aim)
- [Objects for tests](#-objects-for-tests)
- [Examples of tools in action](#%EF%B8%8F-examples-of-tools-in-action)
- [How to Build](#-how-to-build)

## 🎯 The aim
I'll take some simple positive tests, to show:
- how I bild structure of work directory
- how I solve problems for launch same tests for cloud and local
- prepared Jenkins build to simple launch wanted tests
- examples of tools in action  

## 🚩 Objects for tests
#### Mobile
For example used: [DNS-SHOP mobile](https://www.dns-shop.ru/)
- User authorization is successful
- Validation of search result
- Adding product to cart is successful
#### Web
For example used: [Demoshop](https://demowebshop.tricentis.com/)
- User authorization is successful
- Adding product to cart is successful
#### API
For example used: [Demoshop](https://demowebshop.tricentis.com/)
- User authorization is successful
- Adding product to cart is successful
- Clearing cart is successful

## ▶️ Examples of tools in action
### Allure report generated
<img src="https://github.com/andrejevdenis/demo_representation/blob/master/Icons/Allure_testops_report.png" width="630" height="320"/>

<img src="https://github.com/andrejevdenis/demo_representation/blob/master/Icons/Allure_report.png" width="630" height="320"/>

### Test statistics collected, bugs localized
<img src="https://github.com/andrejevdenis/demo_representation/blob/master/Icons/Allure_testops_results.png" width="630" height="320"/>

<img src="https://github.com/andrejevdenis/demo_representation/blob/master/Icons/Allure_result.png" width="630" height="320"/>

### Attached is a video of the test

<img src="https://github.com/andrejevdenis/demo_representation/blob/master/Icons/Mobile_test_example.webp" width="360" height="800"/>

### Notification received of Jenkins build results in Telegram bot
<img src="https://github.com/andrejevdenis/demo_representation/blob/master/Icons/Telegram.png" width="340" height="320"/>

### After all we have generated test cases
<img src="https://github.com/andrejevdenis/demo_representation/blob/master/Icons/Allure_testops_cases.png" width="630" height="320"/>

### Fast report creating with Jira integration
<img src="https://github.com/andrejevdenis/demo_representation/blob/master/Icons/Jira_integration.png" width="630" height="320"/>

<img src="https://github.com/andrejevdenis/demo_representation/blob/master/Icons/Jira_issue.png" width="630" height="320"/>

## 🧰 How to Build

To build autotests in Jenkins:
1. Open <div style="font-size: 16px; display: inline;">  <a href="https://jenkins.autotests.cloud/job/demo-representation/">  <b>Jenkins Project</b>  </a></div>
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
git clone https://github.com/andrejevdenis/demo_representation.git

# Download last version of Allure
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

# Download last version of Android Studio
https://developer.android.com/studio?hl

# Run project to build first allure report
pytest tests --context={choices}
choices=['app_cloud','app_local_real','all','mobile_app','local','cloud', 'web', 'web_cloud', 'web_local', 'api', 'api_local', 'api_cloud']

# Build allure report
allure/bin/allure.bat serve allure-results

# Troubleshooting 

1. Check installed python packages. Use pip install for frameworks from pyproject.toml
2. Check path environment variable windows
```

[Back to top](#top)