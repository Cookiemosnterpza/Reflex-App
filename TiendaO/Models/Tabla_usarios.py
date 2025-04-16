import refles as rx 

class UsuariosModel(rx.Model):
    id: int
    nombre: str
    apellido_p: str
    apellido_m: str
    correo: str
    contraseña: str


class UsuarioTipoModel(rx.Model):
    id: int   