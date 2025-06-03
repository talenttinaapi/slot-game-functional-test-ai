from actions import game_launcher, spinner, bet_manager, feature_checker, audio_control, help_navigator

def run_tests():
    page, browser = game_launcher.launch_game()

    spinner.test_spin_win(page)
    spinner.test_spin_lose(page)
    feature_checker.check_features(page)
    help_navigator.open_paytable(page)
    bet_manager.change_bet(page)
    spinner.test_autoplay(page)
    audio_control.toggle_mute_unmute(page)
    help_navigator.access_help(page)

    browser.close()

if __name__ == "__main__":
    run_tests()
print("All tests completed successfully.")