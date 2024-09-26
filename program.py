from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base64
import os

# Lista de diretórios de download
download_dirs = [
    os.path.join(os.getcwd(), 'images/M2'),
    os.path.join(os.getcwd(), 'images/M3'),
    os.path.join(os.getcwd(), 'images/M4'),
    os.path.join(os.getcwd(), 'images/M5'),
    os.path.join(os.getcwd(), 'images/M6'),
    os.path.join(os.getcwd(), 'images/W2'),
    os.path.join(os.getcwd(), 'images/W3'),
    os.path.join(os.getcwd(), 'images/W4'),
    os.path.join(os.getcwd(), 'images/W5'),
    os.path.join(os.getcwd(), 'images/W6')
]

# Criação dos diretórios caso não existam
for dir in download_dirs:
    if not os.path.exists(dir):
        os.makedirs(dir)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-fullscreen')

driver = webdriver.Chrome(options=options)

url = 'https://facestudio.app/'
driver.get(url)

def download_image_blob(download_dir):
    img_div = driver.find_element(By.XPATH, '//*[@id="generated_image_frame"]')
    
    style_attr = img_div.get_attribute('style')
    
    print(f"Style attribute: {style_attr}")
    
    if 'url(' in style_attr:
        blob_url = style_attr.split('url("')[1].split('")')[0]
        
        print(f"Blob URL: {blob_url}")
        
        script = """
            return new Promise((resolve, reject) => {
                fetch(arguments[0])
                    .then(response => response.blob())
                    .then(blob => {
                        const reader = new FileReader();
                        reader.onloadend = () => resolve(reader.result.split(',')[1]);
                        reader.onerror = reject;
                        reader.readAsDataURL(blob);
                    })
                    .catch(reject);
            });
        """
        base64_image = driver.execute_script(script, blob_url)

        image_data = base64.b64decode(base64_image)
        
        file_name = os.path.join(download_dir, f'image_{int(time.time())}.png')
        
        with open(file_name, 'wb') as file:
            file.write(image_data)
        print(f"Downloaded image: {file_name}")
    else:
        print("No URLs found")

def click_button():
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_generate_idle"]'))
    )

    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()
def m2():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[1]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def m3():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[1]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[3]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def m4():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[1]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[4]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def m5():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[1]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[5]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def m6():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[1]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[6]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def w2():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def w3():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[3]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def w4():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[4]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def w5():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[5]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def w6():
    button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="gender_component_group"]/label[2]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button1)
    button1.click()
    button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="age_component_group"]/label[6]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button2)
    button2.click()

def lat():
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ethnicity_component_group"]/label[7]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()

time.sleep(10)

lat()

# Loop para cada categoria de imagem
for category_index in range(len(download_dirs)):
    for i in range(10):
        # Chame a função apropriada dependendo da categoria
        if category_index < 5:  # M2 a M6
            m_functions = [m2, m3, m4, m5, m6]
            m_functions[category_index]()
        else:  # W2 a W6
            w_functions = [w2, w3, w4, w5, w6]
            w_functions[category_index - 5]()

        download_image_blob(download_dirs[category_index])
        
        time.sleep(10)
        click_button()
        time.sleep(5)

driver.quit()
