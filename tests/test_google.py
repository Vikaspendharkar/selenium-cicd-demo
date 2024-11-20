from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS-level sandbox (required for CI/CD)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage (common issue in Docker and CI)
    
    # Initialize the Chrome WebDriver with the specified options
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
        
    

    # Run the test
    driver.get("https://www.google.com")
    abc = driver.title  # Get the page title
    print("\n=====My Test Results IS:======\n", abc)  # Print the title for debugging

    # Assert that "Google" is in the title
    assert "Google" in driver.title

    # Close the browser session
    driver.quit()

# If you want to directly run this test as a script:
if __name__ == "__main__":
    test_google()
