# El principio de responsabilidad única establece que una clase debe tener una única responsabilidad,
# es decir, una única razón para cambiar. Esto significa que una clase debe encapsular solo una funcionalidad.

# En el ejemplo anterior, la clase Reporte se encarga de manejar los datos del reporte y generar el reporte.
# La clase ReporteGuardado se encarga de guardar el reporte en un archivo. De esta manera, cada clase tiene
# una única responsabilidad.

# Ejecución del ejemplo:
# 1. Guardar el código en un archivo llamado `1_responsabilidad_unica.py`.
# 2. Ejecutar el archivo desde la línea de comandos con el siguiente comando:
#    python 1_responsabilidad_unica.py

class Reporte:
    def __init__(self, datos):
        self.datos = datos

    def generar_reporte(self):
        return f"Reporte: {self.datos}"

class ReporteGuardado:
    def __init__(self, reporte):
        self.reporte = reporte

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(self.reporte.generar_reporte())


# Uso del ejemplo
datos = "Datos importantes del reporte"
reporte = Reporte(datos)
reporte_guardado = ReporteGuardado(reporte)
reporte_guardado.guardar_en_archivo("reporte.txt")
