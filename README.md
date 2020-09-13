<h1 align=center>Initial Committer</h1>

Automates Github Initial Commit by using Selenium Webdriver-Python
## Requirements
- [python3](https://www.python.org/downloads/)
- [Selenium](https://www.selenium.dev/selenium/docs/api/py/)
- Clone of this repository

## SetUp

1. Add your Default Projects folder path in [.commands.sh](https://github.com/sooryaprakash31/InitialCommitter/blob/master/.commands.sh#L8) 
2. Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases) and place it in the folder
3. Copy the files to the standard directory <br />
  ```
  sudo cp -a InitialCommitter/. /usr/bin/
  ```
4. Navigate to `/usr/bin/`
  ```
  source .commands.sh
  ```
## Execution <br />
Use this command from any folder
```
createrepo <ProjectName>
```
Enter your Github credentials <br />

