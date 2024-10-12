from flask import request
from flask_restx import Namespace, Resource,fields
from app.services.cliente_services import ClienteService

clienet_ns = Namespace ('cliente', description='Operaciones relacionadas con las categorias')

cliente_model = clienet_ns.model('Cliente',{
    'cli_nombre': fields.String(required = True, description= 'Nombre del cliente'),
    'cli_direccion': fields.String(required = True, description= 'Direccion del cliente'),
    'cli_telefono': fields.String(required = True, description= 'Telefono del cliente'),
    'cli_email': fields.String(required = True, description= 'Email del cliente')
})

@clienet_ns.route('/')
class ClienteResource(Resource):
    @clienet_ns.doc('create_cliente')
    @clienet_ns.expect(cliente_model,Validate=True)
    def post(self):
        data = request.get_json()
        cliente = ClienteService.create_cliente(data['cli_nombre'],data['cli_direccion'],data['cli_telefono'],data)