# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculo_servicio_pb2 as calculo__servicio__pb2


class CalculadoraStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Suma = channel.unary_unary(
                '/calculo.Calculadora/Suma',
                request_serializer=calculo__servicio__pb2.SumaRequest.SerializeToString,
                response_deserializer=calculo__servicio__pb2.OperacionResponse.FromString,
                )
        self.Resta = channel.unary_unary(
                '/calculo.Calculadora/Resta',
                request_serializer=calculo__servicio__pb2.RestaRequest.SerializeToString,
                response_deserializer=calculo__servicio__pb2.OperacionResponse.FromString,
                )


class CalculadoraServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Suma(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Resta(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculadoraServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Suma': grpc.unary_unary_rpc_method_handler(
                    servicer.Suma,
                    request_deserializer=calculo__servicio__pb2.SumaRequest.FromString,
                    response_serializer=calculo__servicio__pb2.OperacionResponse.SerializeToString,
            ),
            'Resta': grpc.unary_unary_rpc_method_handler(
                    servicer.Resta,
                    request_deserializer=calculo__servicio__pb2.RestaRequest.FromString,
                    response_serializer=calculo__servicio__pb2.OperacionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calculo.Calculadora', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculadora(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Suma(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculo.Calculadora/Suma',
            calculo__servicio__pb2.SumaRequest.SerializeToString,
            calculo__servicio__pb2.OperacionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Resta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculo.Calculadora/Resta',
            calculo__servicio__pb2.RestaRequest.SerializeToString,
            calculo__servicio__pb2.OperacionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
