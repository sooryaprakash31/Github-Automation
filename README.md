# Github-Automation
Automating Github Initial Commit using Python
<h1 align=center>Github-Automation</h1>

Automates Github Initial Commit by using Selenium Webdriver-Python

## Set Up

1. Clone this repository <br />
2. Add the Default Projects folder in [.commands.sh](https://github.com/sooryaprakash31/Github-Automation/blob/master/.commands.sh#L9) 
3. Get the paths from your browser and add them to [github_automate.py](github_automate.py)
  - [Chrome Profile path](https://github.com/sooryaprakash31/Github-Automation/blob/master/github_automate.py#L16)
  - [Executable ChromeDriver path](https://github.com/sooryaprakash31/Github-Automation/blob/master/github_automate.py#L17)
3. Copy the files to the standard directory <br />
  ```
  sudo cp -a /Github-Automation/. /usr/bin/
  ```
## Execute <br />

```
createrepo ProjectName
```
Enter the Github Username and Password <br />

>Account Credentials are not stored anywhere
