# Slot Game Functional Test AI

An AI-driven automation framework using **Python**, **Playwright**, and **OpenCV** for functional testing of slot games via web interface.2025

## 🚀 Features Tested

- 🎰 Launch Game
- 🔄 Spin and Win / Lose Detection
- 💰 Feature Trigger Checks (Bonus Rounds etc.)
- 📜 Paytable and Help Navigation
- 🎚️ Bet Amount Adjustment
- 🔁 Autoplay Support
- 🔇 Mute/Unmute Toggle

## 🧱 Tech Stack

- Python 3.9+
- Playwright (Browser automation)
- OpenCV (Image recognition)
- Tesseract (Optional: OCR for text reading)

## 📦 Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run Tests
python main.py
```

## 🧪 Directory Structure

slot_test_ai/
├── actions/           # Test logic: spins, features, autoplay
├── utils/             # Helpers: vision, screenshot, logger
├── config.py          # Game config (selectors, URL)
├── main.py            # Test runner
├── requirements.txt
└── .github/workflows/python-ci.yml
```
slot_test_ai/
├── actions/           # Test logic: spins, features, autoplay
├── utils/             # Helpers: vision, screenshot, logger
├── config.py          # Game config (selectors, URL)
├── main.py            # Test runner
├── requirements.txt
└── .github/workflows/python-ci.yml
```

## 🛠️ CI/CD

GitHub Actions integration available in `.github/workflows/python-ci.yml`
