# This is study project for Dvmn.org

This script can shorten links to bitlinks and prints clicks number for bitlink

## How to install

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Also you will need to register on https://app.bitly.com/ and get own access token from bitly.
For more information, please go to [bitly help page](https://dev.bitly.com/docs/getting-started/introduction)

### Create .env file with bitly acces token
Please keep your bitly token in project directory in ".env" file. 
**DO NOT PUSH!** this file to GitHub. 
The name of the variable for token in your own ".env" file should be "BITLY_DEVMAN_TOKEN".
For example, your .env file should contain string:
```
"BITLY_DEVMAN_TOKEN" = "[your bitly acces token here]"
```





## How to use the script

Please enter the link after the main.py file (link should start from the name of protocol)
If it's not shorten link the script will give you the short bitly link 
```
python main.py https://www.google.com/
```
If you would like to know the numbers of clicks on yout bitly-link, you can use 
```
python main.py [http://your_bitlink]
```
And the script returns to you the number of clicks to the bitly link for one month
## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
