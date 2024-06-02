import cv2
import matplotlib.pyplot as plt


def rotate_image(image, theta_degrees):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, theta_degrees, 1.0)
    rotated = cv2.warpAffine(image, matrix, (w, h))
    return rotated


def resize_image(image, fx, fy):
    resized = cv2.resize(image, None, fx=fx, fy=fy)
    return resized


def mirror_image(image, axis):
    if axis == 'x':
        mirrored = cv2.flip(image, 0)
    elif axis == 'y':
        mirrored = cv2.flip(image, 1)
    else:
        raise ValueError("Axis must be 'x' or 'y'")
    return mirrored


def show_image(title, image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()


image = cv2.imread('image.jpeg')

if image is None:
    print("Error: Зображення не знайдено або не вдалося зчитати")
else:
    show_image('Оригінальне', image)

    rotated_image = rotate_image(image, 90)
    show_image('Повернуте на 90 градусів', rotated_image)

    resized_image = resize_image(image, 2, 2)
    show_image('Змінене у 2x, 2y', resized_image)

    mirrored_image = mirror_image(image, 'y')
    show_image('Відзеркалене по вісі Y', mirrored_image)

    images = [image, rotated_image, resized_image, mirrored_image]
    titles = ['Оригінальне', 'Повернуте на 90 градусів', 'Змінене у 2x, 2y',
              'Відзеркалене по вісі Y']

    for img, title in zip(images, titles):
            cv2.imshow(title, img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()