import qrcode
from PIL import Image

cadena = input("Introduzca el texto para el codigo QR: ")
imagen = qrcode.make(cadena)

nombre_imagen  = input("Introducir el nombre de la imagen: ") + '.png'
archivo_imagen = open('GENERADOR/generadorQREstaticos/simple/codigosQR/'+nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = 'GENERADOR/generadorQREstaticos/simple/codigosQR/'+nombre_imagen
Image.open(ruta_imagen).show()