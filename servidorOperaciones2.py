from concurrent import futures
import grpc
import calculo_servicio_pb2
import calculo_servicio_pb2_grpc

# Clase del servicio que implementa la funcionalidad de resta
class RestaService(calculo_servicio_pb2_grpc.CalculadoraServicer):
    def Resta(self, request, context):
        resultado = request.num1 - request.num2
        return calculo_servicio_pb2.OperacionResponse(resultado=resultado)

# Función para iniciar el servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Añadir la clase RestaService al servidor gRPC
    calculo_servicio_pb2_grpc.add_CalculadoraServicer_to_server(RestaService(), server)
    # Definir el puerto en el que escucha el servidor
    server.add_insecure_port('localhost:12347')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
