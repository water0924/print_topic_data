# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto.idl import lock_on_road_service_pb2 as idl_dot_lock__on__road__service__pb2


class LockOnRoadServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/deeproute.idl.lock_on_road_service.LockOnRoadService/Init',
                request_serializer=idl_dot_lock__on__road__service__pb2.LockOnRoadInitRequest.SerializeToString,
                response_deserializer=idl_dot_lock__on__road__service__pb2.LockOnRoadInitResponse.FromString,
                )
        self.Proc = channel.unary_unary(
                '/deeproute.idl.lock_on_road_service.LockOnRoadService/Proc',
                request_serializer=idl_dot_lock__on__road__service__pb2.LockOnRoadProcRequest.SerializeToString,
                response_deserializer=idl_dot_lock__on__road__service__pb2.LockOnRoadProcResponse.FromString,
                )


class LockOnRoadServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Proc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LockOnRoadServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=idl_dot_lock__on__road__service__pb2.LockOnRoadInitRequest.FromString,
                    response_serializer=idl_dot_lock__on__road__service__pb2.LockOnRoadInitResponse.SerializeToString,
            ),
            'Proc': grpc.unary_unary_rpc_method_handler(
                    servicer.Proc,
                    request_deserializer=idl_dot_lock__on__road__service__pb2.LockOnRoadProcRequest.FromString,
                    response_serializer=idl_dot_lock__on__road__service__pb2.LockOnRoadProcResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'deeproute.idl.lock_on_road_service.LockOnRoadService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LockOnRoadService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/deeproute.idl.lock_on_road_service.LockOnRoadService/Init',
            idl_dot_lock__on__road__service__pb2.LockOnRoadInitRequest.SerializeToString,
            idl_dot_lock__on__road__service__pb2.LockOnRoadInitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Proc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/deeproute.idl.lock_on_road_service.LockOnRoadService/Proc',
            idl_dot_lock__on__road__service__pb2.LockOnRoadProcRequest.SerializeToString,
            idl_dot_lock__on__road__service__pb2.LockOnRoadProcResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
