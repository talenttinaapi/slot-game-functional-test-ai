def open_paytable(page):
    page.click("#menu-button")
    page.click("#paytable-button")
    print("✅ Paytable opened")

def access_help(page):
    page.click("#menu-button")
    page.click("#help-button")
    print("✅ Helpfile accessed")
