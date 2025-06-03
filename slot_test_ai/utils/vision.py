import cv2

def detect_win(image_path):
    image = cv2.imread(image_path)
    template = cv2.imread("assets/win_banner.png")
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    return (res >= threshold).any()
