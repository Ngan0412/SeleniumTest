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
    combo_input = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//input[@role='combobox' and @aria-label='Specify the search value for Is Deleted field']"
    )))
    combo_input.click()

    # 2. Chờ mục "False" hiển thị và click chọn
    false_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//*[normalize-space()='False']"
    )))
    false_option.click()
    time.sleep(5)  
    # chọn chọn sách đầu tiên
    checkbox = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")  # checkbox thứ 2
    checkbox.click()
    time.sleep(5)

    # click button order
    order_button = driver.find_element(By.XPATH, "//button[span[text()='Order']]")
    order_button.click()
    time.sleep(5)

     # tìm và lấy khuyến mãi mùa hè
    comboboxPromotion = driver.find_element(By.XPATH, "//input[@name='PromotionComboboxId']")
    comboboxPromotion.send_keys("Khuyến mãi mùa đông")
    # Nhấn Enter để chọn
    comboboxPromotion.send_keys(Keys.ENTER)
    time.sleep(5)

    #  lấy điều kiện
    condition = driver.find_element(By.XPATH, "//input[@name='condition']")
    #  lấy sô lượng khuyến mãi
    quantity = driver.find_element(By.XPATH, "//input[@name='quantity']")
    #  lấy phần trăm khuyến mãi
    discount = driver.find_element(By.XPATH, "//input[@name='discount']")
    #  lấy tổng tiền
    sum_element = driver.find_element(By.XPATH, "//input[@name='sum']")
     #  lấy số lượng sách
    quantityBookId = driver.find_element(By.XPATH, "//input[@name='quantityBookId']")
      #  lấy giá sách
    priceBook = driver.find_element(By.XPATH, "//input[@name='priceBook']")
    
    q_promotion = int(quantity.get_attribute("value"))
    q_book = int(quantityBookId.get_attribute("value"))
    condition_promtion = float(condition.get_attribute("value").replace(",", ""))
    price = float(priceBook.get_attribute("value").replace(",", ""))
    discount_str = discount.get_attribute("value")  # Ví dụ: "15%"
    discount_percent = float(discount_str.strip().replace("%", ""))
    total_expected = q_book * price

    # Lấy tổng tiền thực tế từ giao diện
    sum_actual = float(sum_element.get_attribute("value").replace(",", ""))

    #tổng bé hơn điều kiện
    if abs(total_expected < condition_promtion):
        # So sánh, cho phép sai số nhỏ do số thực
        #tiền không khuyến mãi phãi bằng sum
        if abs(total_expected - sum_actual) < 0.01:
            print(f"✅ Tổng tiền tính toán ĐÚNG: {total_expected}, Thực tế: {sum_actual}.")
        else:
            print("❌ Tổng tiền KHÔNG đúng!")
            print(f"👉 Kết quả mong đợi: {total_expected}, Thực tế: {sum_actual}")
    else:
         print("❌ Lỗi điều kiện khuyến mãi!")
    time.sleep(10)


except Exception as e:
    print(f"❌ Đã xảy ra lỗi: {e}")

finally:
    driver.quit()
