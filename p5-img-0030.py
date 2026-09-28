import cv2
# leer la imagen con cv2 = computer vision
img = cv2.imread('guauguau.jpg')
# determinar el tipo de imagen
print(type(img))
# Mostrart pixeles (280, 357, 3)
print(img.shape)
# mostrando imagen en ventana barra de titilo guauguau.jpg
cv2.imshow('guauguau.jpg', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()