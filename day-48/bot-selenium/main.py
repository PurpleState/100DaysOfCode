from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/Users/aishwaryashilpi/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#URL = "https://www.amazon.com/Fitbit-Fitness-Activity-Tracking-Included/dp/B084CQ41M2/ref=lp_16225014011_1_4"
#URL = "https://www.python.org/"
#URL = "https://en.wikipedia.org/wiki/Main_Page"

#driver.get(URL)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[2]')
# print(bug_link.text)

# widget_link = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]')
# links = widget_link.find_elements("a")
# print(links)

# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
#
# print(events)

#<a href="/wiki/Special:Statistics" title="Special:Statistics">6,289,495</a>
#article_count = driver.find_element_by_css_selector("#articlecount a")
#article_count.click()
#all_portals = driver.find_element_by_link_text("All portals")

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("alpha")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("alpha")
email = driver.find_element_by_name("email")
email.send_keys("alpha@gamma.com")
submit = driver.find_element_by_css_selector("form button")
submit.click()

driver.quit()
