from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'TTT' in browser.title, "Browser title was " + browser.title

browser.quit()
