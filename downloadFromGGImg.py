from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import requests
import uuid
import os

browser = r'C:\Users\hnm08\PycharmProjects\crawlImageFromGGImg\chrome-win64\chrome.exe'
browser_download_location = r"C:\Users\hnm08\PycharmProjects\crawlImageFromGGImg"
link = r'https://www.google.com/search?q=c%C4%83n+c%C6%B0%E1%BB%9Bc+c%C3%B4ng+d%C3%A2n&sca_esv=85af15397c77c0f6&udm=2&biw=1366&bih=607&ei=UDLeZai4OLX11e8PwLKAsAY&ved=0ahUKEwiooI2am8yEAxW1evUHHUAZAGYQ4dUDCBA&uact=5&oq=c%C4%83n+c%C6%B0%E1%BB%9Bc+c%C3%B4ng+d%C3%A2n&gs_lp=Egxnd3Mtd2l6LXNlcnAiF2PEg24gY8aw4bubYyBjw7RuZyBkw6JuMggQABiABBixAzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjdB1AmWKQDcAF4AJABAJgBTKABlgGqAQEyuAEDyAEA-AEBmAIDoAKsAcICBhAAGAcYHsICBBAAGB7CAgYQABgIGB6YAwCIBgGSBwEz&sclient=gws-wiz-serp'
save_directory = r'C:\Users\hnm08\PycharmProjects\crawlImageFromGGImg\rawImg'

# Khởi tạo ChromeOptions
chrome_options = Options()

# Thêm đường dẫn tới trình duyệt vào ChromeOptions
chrome_options.binary_location = browser

# Điều chỉnh download location
prefs = {'download.default_directory': browser_download_location}
chrome_options.add_experimental_option('prefs', prefs)

# Khởi tạo trình duyệt Chrome với ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Truy cập vào trang web
driver.get(link)

# Tạo đối tượng ActionChains
actions = ActionChains(driver)

with open('downloadShortcut.js', 'r', encoding='utf-8') as file:
    js_code = file.read()

driver.execute_script(js_code)

input("Nhấn Enter để kết thúc")

# Tạo thư mục nếu nó chưa tồn tại
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

with open(os.path.join(browser_download_location, 'image_links.txt'), 'r') as file:
    image_links = file.readlines()


for link in image_links:
    link = link.strip()

    try:
        # Tải ảnh từ liên kết
        response = requests.get(link)

        # Kiểm tra xem yêu cầu có thành công không (status code 200)
        if response.status_code == 200:
            # Xác định định dạng của ảnh
            image_format = os.path.splitext(link)[1]

            # Nếu không có phần mở rộng hoặc phần mở rộng không hợp lệ, sử dụng '.jpg' mặc định
            if not image_format or image_format.lower() not in ('jpg', 'jpeg', 'png'):
                image_format = 'jpg'

            if image_format:
                # Sinh ra một tên không trùng lặp cho tệp ảnh
                filename = os.path.join(save_directory, str(uuid.uuid4()) + '.' + image_format)

                # Lưu ảnh xuống tệp
                with open(filename, 'wb') as img_file:
                    img_file.write(response.content)
                    print("Đã tải xuống ảnh từ:", link, "và lưu thành:", filename)
            else:
                print("Không thể xác định định dạng của ảnh từ:", link)
        else:
            print("Không thể tải xuống ảnh từ:", link)
    except Exception:
        pass

os.remove(os.path.join(browser_download_location , 'image_links.txt'))