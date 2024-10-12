from app import db

class Cliente(db.Model):
    __tablename__ ='cliente'

    cli_id = db.Column(db.Integer, primary_key = True)
    cli_nombre = db.Column(db.String(100), nullable = False)
    cli_direccion= db.Column(db.String(80), nullable = False)
    cli_telefono = db.Column(db.String(10), nullable = False)
    cli_email = db.Column(db.String(20), nullable = False)


    def __init__ (self, cli_nombre,cli_direccion,cli_telefono,cli_email):
        self.cli_nombre = cli_nombre
        self.cli_direccion = cli_direccion
        self.cli_telefono = cli_telefono
        self.cli_email = cli_email

