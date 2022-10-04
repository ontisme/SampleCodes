# //*[contains(text(),'ABC')] # 找所有節點包含 ABC
# //span[contains(text(),'ABC')] # 找span節點包含 ABC
# //a[(text()='ABC')] #找a節點文字為ABC

node = WebDriverwait(driver, 20).until(
EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(),'ABC')]"))
node.click()
