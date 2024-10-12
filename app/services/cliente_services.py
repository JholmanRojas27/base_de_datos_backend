from app import db, bcrypt
from app.models.cliente_models import Cliente

class ClienteService:
    @staticmethod
    def create_cliente(cli_nombre,cli_direccion,cli_telefono,cli_email):
        cliente = Cliente(cli_nombre,cli_direccion,cli_telefono,cli_email)
        db.session.add(cliente)
        db.session.commit()

        return cliente
    
    @staticmethod
    def update_cliente(cli_id,cli_nombre,cli_direccion,cli_telefono,cli_email):
        cliente = Cliente.query.get(cli_id)

        if not cliente:
            raise ValueError('El cliente no está registrado')
        
        if cli_nombre:
            cliente.cli_nombre = cli_nombre

        if cli_direccion:
            cliente.cli_direccion = cli_direccion

        if cli_telefono:
            cliente.cli_telefono = cli_telefono
            
        if cli_email:
            cliente.cli_email = cli_email
        
        db.session.commit()
        return cliente
    
    @staticmethod
    def delete_cliente(cli_id):
        cliente = Cliente.query.get(cli_id)
        if not cliente:
            raise ValueError('Cliente no encontrado')
        db.session.delete(cliente)
        db.session.commit()

    @staticmethod
    def get_all_cliente(cli_id):
        cliente = Cliente.query.get(cli_id)

        if not cliente:
            raise ValueError('Cliente no encontrado')
        cliente.completed = True
        db.session.commit()
        return cliente
    
    def mark_cliente_incomplete(cli_id):
        cliente = Cliente.query.get(cli_id)
        if not cliente:
            raise ValueError('Cliente no encontrado')
        cliente.completed = False
        db.session.commit()
        return cliente