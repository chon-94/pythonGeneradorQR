import qrcode
from PIL import Image

ape = input("Ingrese los apellidos: "+"\n") 
nom = input("Ingrese los nombres: "+"\n")
nac = input("Ingrese fechade nacimiento: "+"\n")
gsa = input("ingrese grupo sanguineo: "+"\n")

imagen = qrcode.make(
"apellidos: "+ape+"\n" 
"nombres: "+nom+"\n" 
"nacimiento: "+nac+"\n" 
"tipo de sangre: "+gsa+"\n")

nombre_imagen  = input("Introducir el nombre de la imagen: ")+'.png'
archivo_imagen = open('GENERADOR/generadorQREstaticos/datos/codigosQR/'+nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = 'GENERADOR/generadorQREstaticos/datos/codigosQR/'+nombre_imagen
Image.open(ruta_imagen).show()