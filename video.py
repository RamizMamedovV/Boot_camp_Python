import cv2

# переменная face через библиотеку cv2 обращается к 'haar...xml' 
# их можно также найти в https://github.com/opencv/opencv/tree/4.x/data/haarcascades
# она поможет нам выделить лицо
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('pool.mp4')

while True:
    success, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('preview', frame) # для просмотра без обрамления для стопкадра:
    # в строке if cv2.waitKey(0) & 0xff == ord('q'): "поставим waitKey(0)"
    faces = face.detectMultiScale(img_gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 2), 2)

    cv2.imshow('Result', frame)

    if cv2.waitKey(24) & 0xff == ord('q'):
        break




#                       обромим лица в прямоугольники

# face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# img = cv2.imread('test.jpg')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face.detectMultiScale(img_gray)
# """
# print(faces)
# # [[394  53  59  59] вывод начала координат 394 53, длина и ширина прямоугольника: 59 59
# # [226 182  58  58]
# # [ 36 145  58  58]]
# """
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 2), 2) # BGR 0,255, 2, толшина 2

# cv2.imshow('Result', img)
# cv2.waitKey(0)





#                   фото окрасим в gray 

# # применим это к нашей фото и окрасим её в gray -> cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# img = cv2.imread('test.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Result', img)
# cv2.waitKey(1000)