# PyScraper

**PyScraper** is a python class powered by known libraries to make
it easier to scrape websites!

# Installation

>-Clone/Download the script.
-Get into the folder after you download it, open your shell/terminal.
-Use the following code:

```sh
$ pip install setup.py
```
-- After you make sure that the installation is **DONE** follow the following Guide for using that `PyScraper Python class`

How to use ?
============
first of all you need to import the class
```python
from PyScraper import PyScraper
```

***done? tested? no `errors`?***

**Create A PyScraper Object!**
--------------------------------
**You can define the target URL while creating the object or doing that later, it won't be a big deal to care for ^^**
```py
# Syntax
# PyScraper([url=None, handleRobotsTXT=False])
# I guess the syntax is clear to be understandable for you.
```
---------------------------------------------------------------------------
```python
scraper = PyScraper()
```
---------------------------------------------------------------------------
**Now we created the object ... _Let's head to TRY:_**

**Normal Scraping:**
```python
# if you haven't set the URL while creating the object use any of these
# scraper.setURL('http://www.example.com')
# or
# scraper.url = 'http://www.example.com'
scraper.url = 'http://www.example.com'
scrapedText = scraper.scrape("div.myDiv p")
print(scrapedText)
# >>> [...] a list of <p> elements inside <div class="myDiv"></div>
# Selection is done using css selectors as you see above
```
-------------------------------------------------------------------------
**don't know how to use css selectors? No worries, [Check This](https://www.w3schools.com/cssref/css_selectors.asp)**

---------------------------------------------------------------------------
Does that website require you to login before accessing the info you need to scrape?
-------------------------------------------------------------------------------
**- Check this example below:**
The HTML of the login page of that website:
```html
<form id="loginForm" action="/passinfo" method="post">
    <input type="text" name="username" />
    <input type="password" name="pwd" />
</form>
```
```python
# let's define the URL while creating the class this time
scraper = PyScraper('http://www.example.com')
scraper.setLoginURL('http://www.example.com/login')
# you can use this below as well
# scraper.loginURL = 'http://www.example.com/login/'
########METHOD 1########
scraper.setFormSelectors({"id":"loginForm", "method":"post"})
# or select the first form using scraper.selectFormByOrder(0)
# select the right login form
scraper.UserNameFormName = 'username' # username input field name
scraper.PasswordFormName = 'pwd' # password input field name
scraper.login("MyUserName", "MyPassword")
# There are other ways to define stuff just check the bottom side of this
# README.md file later.

########METHOD 2########
scraper.setFormSelectors({"id":"loginForm", "method":"post"})
# or select the first form using scraper.selectFormByOrder(0)
scraper.otherLoginFormInfo = [("username", "MyUserName"), ("pwd", "MyPassword")]
# That's how you can add values while passing into the form
scraper.login()
# Now you should be logged in.
scrapedText = scraper.scrape("div.myDiv p")
print(scrapedText)
# >>> [...] a list of <p> elements inside <div class="myDiv"></div>
```
-------------------------------------------------------------------------------
All Methods
-------------

```py
scraper.addHeader(k, [v=None]) # v=None removes the header
scraper.getHeader(k, [d=None]) # gets the value of a header
# k -> key/name, v -> value, d -> default
scraper.getStrippedDomain() # gets the domain stripped
# if the URL is http://example.com/test/
# it returns example.com
scraper.setURL(url) 
scraper.url = url
# sets the target URL
scraper.setLoginURL(loginUrl)
scraper.loginURL = loginUrl
# sets login url
scraper.setFormNameForUsername(unameattr)
scraper.UserNameFormName = unameattr
# sets username input target name
scraper.setFormNameForPassword(pwdattr)
scraper.PasswordFormName = pwdattr
# sets password input target name
scraper.addOtherLoginFormNames(name, value)
# adds another name with its value while passing the form
scraper.otherLoginFormInfo = [("name1", "value1"), ("name2", "value2")]
# same thing, but different syntax, You can add several names and values
# at once using that syntax
scraper.selectFormByOrder(order)
scraper.formOrder = order
# selects the login form by its order, 0 is the first order index
scraper.setFormSelectors(selectors={})
# selects the login form by its attributes
# e.g: scraper.setFormSelectors(selectors={"id":"loginform", "name":"form"})
scraper.login([username=None, password=None]) # logs in depending on the  given Info above
scraper.addCookie(name, value[, domain='', path="/"])
scraper.getCookie(name, [directValue=False, domain='', path="/"])
# adding/getting cookies
# don't specify domain or set domain to '' to use the default scrapping
# URL which was set before
# directValue if was set to True it returns the cookie value directly
# as string, otherwise it returns a dictionary which has the value
# as returnedDict["value"]
scraper.scrape([selector=None])
# scraping function
# selector is a css selector as string
# if you do it once then u do it again it'll scrap from the current point
# eg u scrapped a <div class="mdiv"> that has a <span>test</span>
# using scraper.scrape(".mdiv"), you are scraping from the whole html document
# you'll get the what inside that div
# then if you scrap again with scraper.scrape("span")
# you'll get that 'test' inside the span
# you won't get any other <span> tags outside that div
# to avoid that you can use this below
scraper.scrape_once([selector=None])
# it scrapes from the doc directly no matter how much you use scraper.scrape([selector=None])
```
-------------------------------------------------------------------------
Thanks! That's all
------------------
-------------------------------------------------------------------------
