
import grpc
import calculo_servicio_pb2
import calculo_servicio_pb2_grpc


class CalculatorClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = calculo_servicio_pb2_grpc.CalculadoraStub(self.channel)

    def suma(self, num1, num2):
        return self.stub.Suma(calculo_servicio_pb2.SumaRequest(num1=num1, num2=num2)).resultado

    def resta(self, num1, num2):
        return self.stub.Resta(calculo_servicio_pb2.RestaRequest(num1=num1, num2=num2)).resultado


# Ejemplo de uso del cliente
if __name__ == '__main__':
    client = CalculatorClient()

    # Solicitar la operación y los números desde la terminal
    operacion = input("Ingrese la operación (suma/resta): ").strip().lower()
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == 'suma':
        print(f"Resultado de la suma: {client.suma(num1, num2)}")
    elif operacion == 'resta':
        print(f"Resultado de la resta: {client.resta(num1, num2)}")
    else:
        print("Operación no reconocida.")
