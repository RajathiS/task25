from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearchAutomation:
    def __init__(self):
        # Initialize the WebDriver (Chrome in this case)
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        try:
            self.driver.get(url)
            print("Page opened successfully.")
        except Exception as e:
            print(f"Failed to open page: {str(e)}")

    def fill_form(self, first_name=None, last_name=None, birth_year=None, gender=None):
        try:
            if first_name or last_name:
                name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "name")))
                name_field.clear()
                name_field.send_keys(f"{first_name} {last_name}".strip())

            if birth_year:
                birth_year_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "birth_date")))
                birth_year_field.clear()
                birth_year_field.send_keys(birth_year)

            if gender:
                gender_dropdown = self.wait.until(EC.visibility_of_element_located((By.NAME, "gender")))
                gender_dropdown.send_keys(gender.capitalize())  # IMDb might use "Female" or "Male"

            print("Form filled successfully.")
        except Exception as e:
            print(f"Error while filling the form: {str(e)}")

    def perform_search(self):
        try:
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']")))
            search_button.click()

            # Wait for the search results page to load
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))
            print("Search completed successfully!")
        except Exception as e:
            print(f"Error during search: {str(e)}")

    def close_browser(self):
        try:
            self.driver.quit()
            print("Browser closed successfully.")
        except Exception as e:
            print(f"Error closing the browser: {str(e)}")

# Example usage
if __name__ == "__main__":
    imdb_bot = IMDbSearchAutomation()
    imdb_bot.open_page("https://www.imdb.com/search/name/")
    imdb_bot.fill_form(
        first_name="guvi",
        last_name="network",
        birth_year="1974",
        gender="Female",  # Capitalized to match typical dropdown options
    )
    imdb_bot.perform_search()
    imdb_bot.close_browser()
