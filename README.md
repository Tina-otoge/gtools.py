# gtools.py
> Collection of CLI tools for using Google Translate powered by [googletrans module by SuHun Han](https://pypi.python.org/pypi/googletrans)

# Requierements
* Python 3.4+
* googletrans module by SuHun Han
  * PyPI : https://pypi.python.org/pypi/googletrans
  * GitHub: https://github.com/ssut/py-googletrans
  
# Usage
## Translation
`translate.py [:lang] <text>`
### Examples:
* `$ python translate.py Bonjour, je suis français !`
* `$ python translate.py :fr Hello, I am English!`
## Pronunciation
`pronunciation.py <text>`
### Example:
* `$ python pronunciation.py 日本人`

# Screenshot
![demo screenshot](http://i.imgur.com/zQ1606r.png)

# Tutorial for easy use on Windows
## 1. Clone the repository somewhere
* Make sure your machine has [Git installed](https://git-for-windows.github.io)
* Open a terminal in the directory you want to download the script
* In this tutorial, the directory will be `C:\Users\foobar\utils`
* Issues `$ git clone https://github.com/skielred/gtools.py.git`
## 2. Create two batch scripts in [a directory included in your PATH](https://www.google.com/search?q=what+is+path+environment+variable), one for `translate.py` and one for `pronunciation.py`
* In this tutorial, we will create `trans.cmd` and `pronu.cmd` in `E:\bin`
## 3. Write a batch script in each file to call the correspondant Python script with Python
* Example `trans.cmd` :
```
@echo off
python C:\Users\foobar\utils\gtools.py\translate.py %*
```
## 4. Finished !
You can now call the command `trans` or `pronu` in any terminal and it will work!
![demo](http://i.imgur.com/87Jc6VV.png)

# Disclaimer
This project is not related with the googletrans project by SuHun Han.
If you want to contribute to googletrans, fork it on GitHub!
