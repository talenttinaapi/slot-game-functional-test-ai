from playwright.sync_api import sync_playwright
from config import GAME_URL

def launch_game():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(GAME_URL)
    page.wait_for_timeout(5000)
    return page, browser
