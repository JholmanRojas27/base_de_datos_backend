from flask import request,jsonify
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
        return jsonify({'message': 'Cliente creado satisfactoriamente', 'cliente':cliente.cli_id})
    
    @clienet_ns.doc('get_clientes')
    def get(self):
        cliente = ClienteService.get_all_cliente()
        return jsonify({'clientes':[clientes.cli_id for clientes in cliente]})
    
    @clienet_ns.route('<cli_id>')
    @clienet_ns.param('cli_id', 'el ID del cliente')
    class ClienteDetailResource(Resource):
        @clienet_ns.doc('delete_cliente')
        def delet(self,cli_id):
            ClienteService.delete_cliente(cli_id)
            return jsonify({'mesage': 'El cliente se borró satisfactoriamente'})
    
    @clienet_ns.doc('update_cliente')
    @clienet_ns.expect(cliente_model, validate = True)
    def put(self,cli_id):
        new_data = request.get_json()
        ClienteService.update_cliente(cli_id,new_data)
        return jsonify({'message': 'El cliente fue actualizado satisfactoriamente'})