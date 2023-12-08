from selenium import webdriver
from selenium.webdriver.common.by import By


class LastfmScrapper:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=self.options)

    def login(self) -> None:
        email_prompt = self.driver.find_element(By.NAME, "username_or_email")
        password_prompt = self.driver.find_element(By.NAME, "password")
        email_prompt.send_keys(self.username)
        password_prompt.send_keys(self.password)
        self.driver.find_element(By.NAME, "submit").click()

    def cookies_rejecter(self) -> None:
        self.driver.find_element(By.ID, "onetrust-reject-all-handler").click()
        self.driver.implicitly_wait(1)

    def get_recommended_artists(self) -> list[str]:
        self.driver.get("https://www.last.fm/music/+recommended/artists")
        artists = self.driver.find_elements(By.CLASS_NAME, "music-recommended-artists-artist-name")
        return [artist.text for artist in artists]


if __name__ == '__main__':
    scrapper = LastfmScrapper(username="Pradzix", password="73v*57EDP5!^mP")
    driver = scrapper.driver
    driver.get("https://www.last.fm/login")
    driver.implicitly_wait(1)
    scrapper.cookies_rejecter()
    scrapper.login()
    driver.implicitly_wait(1)
    print(scrapper.get_recommended_artists())
