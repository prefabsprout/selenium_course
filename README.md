# Selenium Course Homeworks
This is a repository for Selenium course homeworks

## Before you start
First you need to install required packages with next command:  
```
python -m pip install -r requirements.txt
```  

After that be sure you have `chromedriver.exe` in your PATH directory.

## Recommended system requirements
- Windows 8.1 (64-bit)
- Chrome 90.0.4430.212 (64 bit)
- Python 3.8.8

## Test execution
To execute test scripts type in terminal:  
```
pytest --alluredir=reports test
```
To see Allure reports type:
```
allure serve reports
```

## Execution with Jenkins
You need to download `jenkins.war` file in order to launch Jenkins as a process.
To launch Jenkins type:
```
java -jar jenkins.war
```
To export Jenkins job download `jenkins-cli` tool and type:
```
java -jar jenkins-cli.jar -s http://localhost:8080/ create-job JENKINS_AUTOMATION < JENKINS_AUTOMATION.xml
```
Don't forget to change `customWorkspace` in `JENKINS_AUTOMATION.xml` with repository to your local path.
