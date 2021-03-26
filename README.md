### Django  
- Step One :  
Install and download python3 source : 
<a href="https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tar.xz">Python Source</a>  

Installing sofware :  
```bash
apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev  
```  

- Step Two :  
After compress python3.9 source, access directory in your terminal :  

```bash
# cd Python-3.9.2/
# ./configure && make && make install
```  
Check the version : 
```bash
# which python3.9
# which pip3.9
```  
check pip list :  

```bash
# pip3.9 list
```  

- Step Three :  

**Setup virtual Env**  

```bash
# mkdir -p project-dir
```  
***Create Environmen***  

```bash
# python3.9 -m venv Env
```  
***Access Virtual Environment***  

```bash
# source Env/bin/activate
```  
```bash
# pip list
```  

***Upgrade Pip***  

```bash
# pip list --upgrade pip
```  

- Step Four :  

***Installing Django***  
Check the version
```bash
# python -V
```  
```bash
# pip install Django==1.11.*
```  
**Create new project**  

```bash
# django-admin startproject mywebsite
```  

**Activate django server**  
```bash
# cd mywebsite
# python manage.py runserver
```  

And access your web browser http://localhost:8000  

***Deactivate environment***  

```bash
# deactivate
```


