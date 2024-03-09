from concurrent import futures
import grpc
import calculo_servicio_pb2
import calculo_servicio_pb2_grpc

# Definir los clientes gRPC para los servidores de operaciones
class OperationClient:
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        # Asegúrate de tener el stub adecuado para los servidores de operaciones
        self.stub = calculo_servicio_pb2_grpc.CalculadoraStub(self.channel)

    def suma(self, num1, num2):
        return self.stub.Suma(calculo_servicio_pb2.SumaRequest(num1=num1, num2=num2))

    def resta(self, num1, num2):
        return self.stub.Resta(calculo_servicio_pb2.RestaRequest(num1=num1, num2=num2))

# Servicio que reenvía las peticiones a los servidores de operaciones
class CalculadoraService(calculo_servicio_pb2_grpc.CalculadoraServicer):
    def __init__(self):
        self.suma_client = OperationClient('localhost', 12346)  # Asumiendo que este es el puerto para suma
        self.resta_client = OperationClient('localhost', 12347)  # Asumiendo que este es el puerto para resta

    def Suma(self, request, context):
        response = self.suma_client.suma(request.num1, request.num2)
        return calculo_servicio_pb2.OperacionResponse(resultado=response.resultado)

    def Resta(self, request, context):
        response = self.resta_client.resta(request.num1, request.num2)
        return calculo_servicio_pb2.OperacionResponse(resultado=response.resultado)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculo_servicio_pb2_grpc.add_CalculadoraServicer_to_server(CalculadoraService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
