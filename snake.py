from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 设置指纹浏览器的选项
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # 最大化窗口
options.add_argument("--ignore-certificate-errors")  # 忽略证书错误
options.add_argument("--disable-popup-blocking")  # 禁用弹出窗口阻止功能

# 启动指纹浏览器
browser = webdriver.Chrome(options=options)

# 打开搜索引擎进行搜索
search_query = "Python automation with Selenium"  # 要搜索的关键词
search_engine_url = "https://www.google.com"  # 替换为你想使用的搜索引擎
browser.get(search_engine_url)
search_box = browser.find_element_by_name("q")  # 根据搜索引擎的网页结构找到搜索框元素
search_box.send_keys(search_query + Keys.RETURN)  # 输入搜索关键词并按下回车键

time.sleep(5)  # 等待页面加载

# 登录Twitter
twitter_url = "https://twitter.com/login"  # Twitter登录页面
browser.get(twitter_url)
username = "your_username"  # 替换为你的Twitter用户名
password = "your_password"  # 替换为你的Twitter密码
username_field = browser.find_element_by_name("session[username_or_email]")
password_field = browser.find_element_by_name("session[password]")
login_button = browser.find_element_by_xpath('//span[text()="Log in"]')

username_field.send_keys(username)
password_field.send_keys(password)
login_button.click()

time.sleep(5)  # 等待登录完成

# 在这里可以进行后续操作，例如发推、查看时间线等
# 例如：
# tweet_box = browser.find_element_by_xpath('//div[@aria-label="Tweet text"]')
# tweet_box.send_keys('Hello, this is a tweet from automated script!')

# 关闭指纹浏览器
browser.quit()
