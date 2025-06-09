from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Đường dẫn Edge WebDriver
EDGE_DRIVER_PATH = "C:\\DaiCa\\Project\\BookStore\\Test\\SeleniumTest\\msedgedriver.exe"

# Khởi động WebDriver
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service)
try:
    # vào trang đăng nhập
    driver.get("https://localhost:7226/")
    time.sleep(1)

    # Điền thông tin đăng nhập
    driver.find_element(By.ID, "email").send_keys("phucnaoto@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    time.sleep(1)

    # click btn login
    driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
    time.sleep(5)

    # chờ 5s
    wait = WebDriverWait(driver, 5)
    # Tìm input combobox bằng thuộc tính aria-label
    comboTrue_input = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//input[@role='combobox' and @aria-label='Specify the search value for Is Deleted field']"
    )))
    comboTrue_input.click()

    # 2. Chờ mục "True" hiển thị và click chọn
    true_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//*[normalize-space()='True']"
    )))
    true_option.click()
    time.sleep(5)
    # chọn sách  vi tri thu 1
    checkbox = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")  # checkbox thứ 2
    checkbox.click()
    time.sleep(5)

    # Tìm input combobox bằng thuộc tính aria-label
    comboFalse_input = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//input[@role='combobox' and @aria-label='Specify the search value for Is Deleted field']"
    )))
    comboFalse_input.click()
    # 2. Chờ mục "False" hiển thị và click chọn
    false_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//*[normalize-space()='False']"
    )))
    false_option.click()
    time.sleep(5)
    # chọn sách  vi tri thu 1
    checkboxFalse = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")  # checkbox thứ 2
    checkboxFalse.click()
    time.sleep(5)

    # click button order
    order_button = driver.find_element(By.XPATH, "//button[span[text()='Order']]")
    order_button.click()
    time.sleep(5)
     # tìm và lấy nhân viên thùy ngân
    comboboxCustomer = driver.find_element(By.XPATH, "//input[@name='CustomerComboboxId']")
    comboboxCustomer.send_keys("Thùy Ngân")
    # Nhấn Enter để chọn
    comboboxCustomer.send_keys(Keys.ENTER)
    time.sleep(5)

     # tìm và lấy khuyến mãi mùa hè
    comboboxPromotion = driver.find_element(By.XPATH, "//input[@name='PromotionComboboxId']")
    comboboxPromotion.send_keys("Khuyến Mãi Mùa Hè")
    # Nhấn Enter để chọn
    comboboxPromotion.send_keys(Keys.ENTER)
    time.sleep(5)



    # click button save
    order_button = driver.find_element(By.XPATH, "//button[span[text()='Save']]")
    order_button.click()

    # Đợi toast chứa text xuất hiện trong vòng 5 giây
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "custom-toast-background"),
            "Order created successfully."
        )
    )
    print("✅ Tạo thành công đơn hàng.")
    time.sleep(10)

except Exception as e:
    print(f"❌ Đã xảy ra lỗi: {e}")

finally:
    driver.quit()
