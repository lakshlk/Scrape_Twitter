from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import time
import pymongo
import datetime
import uuid

def fetch_trending_topics():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    # Specify the path to chromedriver
    driver_path = "C:/Users/LAKSH/Downloads/chrome-win64/chromedriver.exe"  # Change this to the actual path
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    driver.get('https://twitter.com/login')
    
    # Add your login code here
    time.sleep(5)  # Wait for the login page to load

    username = driver.find_element(By.NAME, 'session[username_or_email]')
    password = driver.find_element(By.NAME, 'session[password]')

    username.send_keys('your_twitter_username')
    password.send_keys('your_twitter_password')
    password.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for the login process to complete

    driver.get('https://twitter.com/home')
    time.sleep(5)  # Wait for the home page to load

    trends = driver.find_elements(By.XPATH, '//div[@aria-label="Timeline: Trending now"]//span')
    top_5_trends = [trend.text for trend in trends[:5]]

    driver.quit()

    # Get the current IP address
    ip_address = requests.get('http://icanhazip.com').text.strip()

    # Store results in MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["twitter_trends"]
    collection = db["trends"]

    unique_id = str(uuid.uuid4())
    result = {
        "_id": unique_id,
        "trend1": top_5_trends[0] if len(top_5_trends) > 0 else None,
        "trend2": top_5_trends[1] if len(top_5_trends) > 1 else None,
        "trend3": top_5_trends[2] if len(top_5_trends) > 2 else None,
        "trend4": top_5_trends[3] if len(top_5_trends) > 3 else None,
        "trend5": top_5_trends[4] if len(top_5_trends) > 4 else None,
        "timestamp": datetime.datetime.now(),
        "ip_address": ip_address
    }

    collection.insert_one(result)

    return result
