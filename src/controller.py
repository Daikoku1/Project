from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebController:
    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\user\Documents\Python\Project\src\driver\chromedriver.exe")

    def init_chrome(self):
        SCREEN_WIDTH: int = 1920
        SCREEN_HEIGHT: int = 1080

        self.driver.set_window_position(SCREEN_WIDTH / 2 - 170, 0)
        self.driver.set_window_size(SCREEN_WIDTH / 2 + 170, SCREEN_HEIGHT)
        self.driver.get("https://www.hometax.go.kr/")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "로그인")))
        self.action_button_click_by_text("로그인")

    def action_button_click(self, button_id: str):
        try:
            self._button_click(self.driver.find_element(By.ID, button_id))
        except Exception as error:
            print(error)

    def action_button_click_by_text(self, text: str):
        try:
            self._button_click(self.driver.find_element(By.PARTIAL_LINK_TEXT, text))
        except Exception as error:
            print(error)

    def alert_handler(self):
        if self._has_alert():
            alert = self.driver.switch_to.alert
            text = alert.text

            print()
            print(text)
            alert.accept()

    def logout_and_login_strategy(self):
        if self._has_hometax_login():
            self.action_button_click_by_text("로그아웃")
            self.alert_handler()
            # wait
            wait = WebDriverWait(self.driver, 1000)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "로그인")))

        self.action_button_click_by_text("로그인")

    def _button_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def _has_hometax_login(self):
        try:
            self.driver.find_element(By.LINK_TEXT, "로그아웃")
            return True
        except:
            return False

    def _has_alert(self):
        try:
            check_alert = self.driver.switch_to.alert  # check Alert
            return True
        except Exception as e:
            return False


if __name__ == '__main__':
    pass
