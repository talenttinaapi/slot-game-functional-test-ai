def change_bet(page):
    original_bet = page.text_content("#bet-amount")
    page.click("#bet-increase")
    page.wait_for_timeout(1000)
    new_bet = page.text_content("#bet-amount")
    if new_bet != original_bet:
        print("✅ Bet changed successfully")
    else:
        print("❌ Bet change failed")
