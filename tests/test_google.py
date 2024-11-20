from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS sandbox
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Run the test
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
