import requests
from bs4 import BeautifulSoup
import lxml.html


url = 'http://erp.ncuindia.edu/'

start = requests.session()  # making a session object to handle cookies
token = '3BA8C6EB'  # hidden tokens
# list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")[0]))
token_1 = '/wEPDwUKLTI0NTk0MzIwMw8WAh4PQ2hhaXJtYW5NZXNzYWdlBRkxMDAxNV9DaGFpcm1hbk1lc3NhZ2UuanBnFgICAw9kFgoCAQ8PFgIeCEltYWdlVXJsBTV+XFVwbG9hZGVkRmlsZVxOb3RpZmljYXRpb25cMTAwMTVfQ2hhaXJtYW5NZXNzYWdlLmpwZ2RkAgMPDxYCHgRUZXh0BZwCVGhlIE5vcnRoQ2FwIFVuaXZlcnNpdHkgd2FzIGZvdW5kZWQgaW4gMTk5NiwgdG8gcHJvbW90ZSBleGNlbGxlbmNlIGluIFRlY2huaWNhbCBhbmQgTWFuYWdlbWVudCBlZHVjYXRpb24gYnkgRWR1Y2F0ZSBJbmRpYSBTb2NpZXR5LCByZWdpc3RlcmVkIHVuZGVyIHRoZSBSZWdpc3RyYXRpb24gb2YgU29jaWV0aWVzIEFjdCBvZiAxODYwLg0KVGhlIFVuaXZlcnNpdHkgd2FzIGNvbmNlaXZlZCBhcyBJbnN0aXR1dGUgb2YgVGVjaG5vbG9neSBhbmQgTWFuYWdlbWVudCBpbiByZXNwb25zZSB0byB0aC4uLi5kZAIHDw8WAh8BBTh+L0hhbmRsZXIvQ29sbGVnZUxvZ28uYXNoeD9Db2xsZWdlU3lzQ29kZT0xMDAxNSZVU2VySWQ9MGRkAgkPDxYCHwIFF1RIRSBOT1JUSENBUCBVTklWRVJTSVRZZGQCFQ8PFgIfAgUXVEhFIE5PUlRIQ0FQIFVOSVZFUlNJVFlkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUPQ2hrU3RheVNpZ25lZEluxX0otmSpE8Fty+bH2y3L6MS+l2A='
stuff = {

    'tbUserName': '16csu001',
    'tbPassword': 'Tangocharlie20!7',
    '__VIEWSTATEGENERATOR': token,
    'btnLogIn': 'Login',
    '__VIEWSTATE': token_1

}
update = {'__EVENTTARGET': '', '__EVENTARGUMENT': '',
          '__VIEWSTATE': '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',
          'tbUserName': '16CSU427', 'tbPassword': 'Vivek@2898', '__VIEWSTATEGENERATOR': '791C70D1', 'btnLogIn': 'Login',
          'ctl00_aAttandance': 'Attendance'}

opens = start.post(url=url, data=stuff)  # logging in


pars = lxml.html.fromstring(opens.text)
# getting some hidden CRSF stuff
hidden_inputs = pars.xpath(r'//form//input[@type="hidden"]')
hidden_stuff = {x.attrib['name']: x.attrib['value'] for x in hidden_inputs}
stuff.update(hidden_stuff)

stuff = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
}

soup = BeautifulSoup(opens.text, 'lxml')   # prettifying the dashboard

for I in soup.find_all('section', {'class': 'schedule'}):  # getting the table
    tr_tags = I.find_all('tr')

    for tr in tr_tags:
        td_tags = tr.find_all('td')

        for td in td_tags:
            list_text = td.text
            new = list_text.replace('Course Code', '').replace(' :-', ':')
            print(new + '\n')

print('thought of the day...\n')

for J in soup.find_all('article', {'class': 'lineH20'}):  # getting the thought
    print(J.text.replace('\u2019', ''))
