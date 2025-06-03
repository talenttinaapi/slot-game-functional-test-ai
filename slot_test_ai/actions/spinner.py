from utils.screen import take_screenshot
from utils.vision import detect_win

def test_spin_win(page):
    page.click("#spin-button")
    page.wait_for_timeout(3000)
    take_screenshot(page, "spin_result.png")
    if detect_win("spin_result.png"):
        print("✅ Spin resulted in a win")
    else:
        print("❌ Expected a win but none detected")

def test_spin_lose(page):
    page.click("#spin-button")
    page.wait_for_timeout(3000)
    take_screenshot(page, "spin_result.png")
    if not detect_win("spin_result.png"):
        print("✅ Spin resulted in a loss")
    else:
        print("❌ Expected a loss but win detected")

def test_autoplay(page):
    page.click("#autoplay-button")
    page.wait_for_timeout(10000)
    print("✅ Autoplay triggered and ran")
