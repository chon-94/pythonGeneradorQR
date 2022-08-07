import qrcode
from PIL import Image

cadena = input("Introduzca el texto para el codigo QR: ")
imagen = qrcode.make(cadena)

nombre_imagen  = input("Introducir el nombre de la imagen: ") + '.png'
archivo_imagen = open('GENERADOR/generadorqr0/codigosQR/'+nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = 'GENERADOR/generadorqr0/codigosQR/'+nombre_imagen
Image.open(ruta_imagen).show()