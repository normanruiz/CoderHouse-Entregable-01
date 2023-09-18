from Servicio.ServiciosConexionApi import ServiciosConexionApi


class ServiciosETL:
    def __init__(self):
        self._datos_crudos = {}

    @property
    def datos_crudos(self):
        return self._datos_crudos

    @datos_crudos.setter
    def datos_crudos(self, datos_crudos):
        self._datos_crudos = datos_crudos

    def extract(self, servicioslog, api):
        estado = True
        try:
            mensaje = f"Recuperando datos desde origen..."
            servicioslog.escribir(mensaje)

            serviciosconexionapi = ServiciosConexionApi(api)
            estado, self.datos_crudos = serviciosconexionapi.consultar(servicioslog)
            if estado is False:
                return

            mensaje = f"Registros recuperados: {str(self.datos_crudos['element_count'])}"
            servicioslog.escribir(mensaje)

            mensaje = f"Subproceso finalizado..."
            servicioslog.escribir(mensaje)
        except Exception as excepcion:
            estado = False
            mensaje = f"ERROR - Recuperando datos desde origen: {type(excepcion)} - {str(excepcion)}"
            servicioslog.escribir(mensaje)
            mensaje = f"WARNING!!! - Subproceso interrumpido..."
            servicioslog.escribir(mensaje)
        finally:
            mensaje = f" {'-' * 128}"
            servicioslog.escribir(mensaje, tiempo=False)
            return estado

    def transform(self):
        pass

    def load(self):
        pass