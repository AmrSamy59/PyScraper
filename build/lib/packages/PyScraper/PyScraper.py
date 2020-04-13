import mechanize
import http.cookiejar
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class PyScraper:
    def __init__(self, url=None, handleRobotsTXT=False):
        self.__info = {}
        self.__otherLoginInfo = {}
        self.__formOrder = -1
        self.url = url
        self.soup = None
        self.website = None
        # create a browser with its options
        self.browser = mechanize.Browser()
        self.cookies = http.cookiejar.LWPCookieJar()
        self.browser.set_cookiejar(self.cookies)
        self.browser.set_handle_equiv(True)
        self.browser.set_handle_gzip(True)
        self.browser.set_handle_redirect(True)
        self.browser.set_handle_referer(True)
        self.browser.set_handle_robots(handleRobotsTXT)
        self.browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        self.browser.addheaders = [('User-agent', 'Chrome')]
    # handling important misc
    def addHeader(self, k, v=None): # if value is None then the header gets removed
        return self.browser.add_header(k, val=v)
    def getHeader(self, k,d=None):
        return self.browser.get_header(k, default=d)
    def getStrippedDomain(self):
        if isinstance(self.url, str):
            domain = urlparse(self.url).netloc
            return domain
    def __setOptions(self, options, value=""):
        if isinstance(options, str):
            self.__info[options] = value
        elif isinstance(options, dict):
            for i, v in options.items():
                self.__info[i] = v
        elif isinstance(options, tuple):
            self.__info[options[0]] = options[1]
    def setURL(self, newURL):
        if isinstance(newURL, str):
            self.url = newURL
    def login(self, username=None, password=None):
        if not "login_url" in self.__info.keys():
            print("Login Page URL wasn't set\nUse the method Object.setLoginURL(url)")
            return
        self.browser.open(self.__info["login_url"])

        if "form_selectors" in self.__info.keys() and isinstance(self.__info["form_selectors"], dict):
            selectorsA = self.__info["form_selectors"]
            self.browser.select_form(**selectorsA)
        else:
            self.browser.form = self.browser.forms()[self.__formOrder if self.__formOrder >= 0 else 0]

        # Login Info
        if "username_attr" in self.__info.keys():
            self.browser.form[self.__info["username_attr"]] = username
        if "password_attr" in self.__info.keys():
            self.browser.form[self.__info["password_attr"]] = password
        for index, val in self.__otherLoginInfo.items():
            self.browser.form[index] = val
        # log in
        self.browser.submit()
    # In case you need to set some cookies
    def addCookie(self, name, value, domain='', path="/"):
        if domain == '':
            domain = self.getStrippedDomain()
        self.browser.set_simple_cookie(name, value, domain, path=path)
    def getCookie(self, name, directValue=False, domain='', path="/"):
        try:
            if domain == '':
                domain = self.getStrippedDomain()
            cookiedict = self.browser.cookiejar.__dict__["_cookies"][domain][path][name].__dict__
            if directValue == True:
                return cookiedict["value"]
            else:
                return cookiedict
        except Exception:
            pass
    # In case you need to login before accessing the website
    def setLoginURL(self, loginUrl):
        self.__info["login_url"] = loginUrl
    @property
    def loginURL(self):
        return self.__info["login_url"]
    @loginURL.setter
    def loginURL(self, loginURL):
        self.__info["login_url"] = loginURL
    # The name of the input of each of password and username
    def setFormNameForUsername(self, unameattr):
        self.__info["username_attr"] = unameattr
    @property
    def UserNameFormName(self):
        return self.__info["username_attr"]
    @UserNameFormName.setter
    def UserNameFormName(self, unameattr):
        self.__info["username_attr"] = unameattr
    def setFormNameForPassword(self, pwdattr):
        self.__info["password_attr"] = pwdattr
    @property
    def PasswordFormName(self):
        return self.__info["password_attr"]
    @PasswordFormName.setter
    def PasswordFormName(self, pwdattr):
        self.__info["password_attr"] = pwdattr
    def setFormSelectors(self, selectors={}):
        self.__info["form_selectors"] = selectors
    def selectFormByOrder(self, order):
        if order >= 0:
            self.__formOrder = order
    @property
    def formOrder(self):
        return self.__formOrder
    @formOrder.setter
    def formOrder(self, order):
        if order >= 0:
            self.__formOrder = order
    def addOtherLoginFormNames(self, name, value):
        self.__otherLoginInfo[name] = value
    @property
    def otherLoginFormInfo(self):
        return self.__otherLoginInfo
    @otherLoginFormInfo.setter
    def otherLoginFormInfo(self, value):
        for items in value:
            self.__otherLoginInfo[items[0]] = items[1]
    # scraping methods
    def scrape(self, selector=None):
        if isinstance(self.url, str):
            if self.soup == None or self.soup == False:
                self.website = self.browser.open(self.url).read()
                self.soup = BeautifulSoup(self.website, 'html.parser')
            self.selected = self.soup.select(selector)
            return self.selected
    def scrape_once(self, selector=None):
        if isinstance(self.url, str):
            if self.website == None or self.website == False:
                tempwebsite = self.browser.open(self.url).read()
            else:
                tempwebsite = self.website
            tempsoup = BeautifulSoup(tempwebsite, 'html.parser')
            tselected = tempsoup.select(selector)
            return tselected
    def getSoup(self):
        return self.soup
    def getBrowser(self):
        return self.browser