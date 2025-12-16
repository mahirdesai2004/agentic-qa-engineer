from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def run_test(steps, url):
    driver = webdriver.Chrome()
    driver.get(url)

    result = "PASS"
    reason = ""

    try:
        for step in steps:
            action = step["action"]

            if action == "navigate":
                continue

            elif action == "input":
                driver.find_element(By.ID, step["selector"]).send_keys(step["value"])

            elif action == "click":
                driver.find_element(By.TAG_NAME, step["selector"]).click()

            elif action == "check":
                time.sleep(1)
                text = driver.find_element(By.ID, step["selector"]).text
                if step["value"] not in text:
                    result = "FAIL"
                    reason = f"Expected '{step['value']}', got '{text}'"

    except Exception as e:
        result = "FAIL"
        reason = str(e)

    time.sleep(2)
    driver.quit()
    return result, reason