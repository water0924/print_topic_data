# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drapi/request.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.drapi import local_config_pb2 as drapi_dot_local__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x64rapi/request.proto\x12\ndr.request\x1a\x18\x64rapi/local_config.proto\"W\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\t\x12\x34\n\x0bload_config\x18\x02 \x01(\x0b\x32\x1d.dr.request.LoadConfigRequestH\x00\x42\n\n\x08requests\"Y\n\x08Response\x12\n\n\x02id\x18\x01 \x01(\t\x12\x35\n\x0bload_config\x18\x02 \x01(\x0b\x32\x1e.dr.request.LoadConfigResponseH\x00\x42\n\n\x08response\"\x13\n\x11LoadConfigRequest\"E\n\x12LoadConfigResponse\x12/\n\x0buser_config\x18\x01 \x01(\x0b\x32\x1a.dr.localconfig.UserConfigb\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_LOADCONFIGREQUEST = DESCRIPTOR.message_types_by_name['LoadConfigRequest']
_LOADCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['LoadConfigResponse']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'drapi.request_pb2'
  # @@protoc_insertion_point(class_scope:dr.request.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'drapi.request_pb2'
  # @@protoc_insertion_point(class_scope:dr.request.Response)
  })
_sym_db.RegisterMessage(Response)

LoadConfigRequest = _reflection.GeneratedProtocolMessageType('LoadConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOADCONFIGREQUEST,
  '__module__' : 'drapi.request_pb2'
  # @@protoc_insertion_point(class_scope:dr.request.LoadConfigRequest)
  })
_sym_db.RegisterMessage(LoadConfigRequest)

LoadConfigResponse = _reflection.GeneratedProtocolMessageType('LoadConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOADCONFIGRESPONSE,
  '__module__' : 'drapi.request_pb2'
  # @@protoc_insertion_point(class_scope:dr.request.LoadConfigResponse)
  })
_sym_db.RegisterMessage(LoadConfigResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=61
  _REQUEST._serialized_end=148
  _RESPONSE._serialized_start=150
  _RESPONSE._serialized_end=239
  _LOADCONFIGREQUEST._serialized_start=241
  _LOADCONFIGREQUEST._serialized_end=260
  _LOADCONFIGRESPONSE._serialized_start=262
  _LOADCONFIGRESPONSE._serialized_end=331
# @@protoc_insertion_point(module_scope)
