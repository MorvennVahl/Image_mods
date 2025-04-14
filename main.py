import matplotlib.pyplot as plt
import numpy as np
import cv2
import math


arr = np.array([1, 5, 10, 15, 20])
lower, upper = 5, 15

clipped_count = np.sum((arr < lower) | (arr > upper))

clipped_arr = np.clip(arr, lower, upper)

print(clipped_count)


def blend_image(img1, img2):
    alpha = 0.5
    new_img = np.clip(img1.astype(np.uint8) * alpha + img2.astype(np.uint8) * alpha, 0, 255).astype(np.uint8)
    return new_img


def blend_images(img1, img2):
    height, width, channels = img1.shape
    new_img = np.zeros([height, width, channels], dtype=np.uint8)
    for i in range(height):
        alpha = i/height
        new_img[i, :] = img1[i, :] * alpha + img2[i, :] * (1- alpha)

    return new_img


def transform(phi: float, r: float, W: int) -> tuple[int, int]:
    x = int(((phi + np.pi) / (2 * np.pi)) * (W - 1))
    y = int(r)
    return np.abs(x), np.abs(y)


def transform_image(image: np.ndarray) -> np.ndarray:
    H, W, C = image.shape
    center = (W // 2, H // 2)
    transformed = np.zeros_like(image)

    for y in range(H):
        for x in range(W):
            dx, dy = x - center[0], y - center[1]
            r = math.sqrt(dx**2 + dy**2)
            if r > center[1]:
                continue
            phi = np.arctan2(dy, dx)
            src_x, src_y = transform(phi, r, H, W)
            transformed[y, x] = image[src_y, src_x]

    return transformed


a = cv2.imread("C:/Users/Alexa/OneDrive/Desktop/a.png").astype(dtype=np.uint8)
b = cv2.imread("C:/Users/Alexa/OneDrive/Desktop/b.png").astype(dtype=np.uint8)
c = cv2.imread("C:/Users/Alexa/OneDrive/Desktop/bloody.png").astype(dtype=np.uint8)

cv2.imwrite("C:/Users/Alexa/OneDrive/Desktop/bloody_dangerous.png", transform_image(c))
cv2.imwrite("C:/Users/Alexa/OneDrive/Desktop/bloody.png", blend_image(a, b))
cv2.imwrite("C:/Users/Alexa/OneDrive/Desktop/bloody_hell.png", blend_images(a, b))


def graustufen(img):
    return np.round(img[:, :, 0] * 0.2 + img[:, :, 1] * 0.7 + img[:, :, 2] * 0.1).astype(dtype=np.uint8)



d = cv2.imread("C:/Users/Alexa/OneDrive/Desktop/bloody_dangerous.png").astype(dtype=np.uint8)
cv2.imshow("d", d)
cv2.imshow("d graustufen", graustufen(d))
cv2.waitKey(0)


def grau_rahmen(img, radius):
    H, W, C = img.shape
    m_x, m_y = W//2, H//2

    radius_x, radius_y = int(0), int(0)
    img_new = np.zeros([H, W, C], dtype=np.uint8)
    for i in range(0, W - 1):
        for n in range(0, H - 1):
            if i < m_x and n < m_y:
                radius_x = m_x - i
                radius_y = m_y - n
            elif i > m_x and n < m_y:
                radius_x = i - m_x
                radius_y = m_y - n
            elif i < m_x and n > m_y:
                radius_x = m_x - i
                radius_y = n - m_y
            elif i > m_x and n > m_y:
                radius_x = i- m_x
                radius_y = n - m_y
            elif i == m_x and n == m_y:
                radius_x = i
                radius_y = n

            distance = math.sqrt(radius_x ** 2 + radius_y ** 2)
            for c in range(C):
                if distance > radius:
                    gray_value = np.clip(np.round(img[n, i, 0] * 0.2 + img[n, i, 1] * 0.7 + img[n, i, 2] * 0.1).astype(dtype=np.uint8), 0, 255)
                    img_new[n, i, c] = gray_value
                else:
                    img_new[n, i, c] = img[n, i, c]
    return img_new


cv2.imshow("grau_rahmen", grau_rahmen(a, 200))
cv2.waitKey(0)


def histogramm(img, num_bins):
    hist = np.zeros(num_bins, dtype=np.uint8)
    if len(img.shape) >= 3:
        return
    threshold = num_bins // 256
    for i in range(0, img.shape[0]):
        for n in range(0, img.shape[1]):
            box = int(img[i, n] * threshold)
            hist[box] += 1
    return






























