# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dem/store_trip_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x64\x65m/store_trip_data.proto\x12\rdeeproute.dem\"3\n\x14StoreTripDataRequest\x12\x1b\n\x13\x63\x61n_store_trip_data\x18\x01 \x01(\x08\"5\n\x15StoreTripDataResponse\x12\x1c\n\x14skip_store_trip_data\x18\x02 \x01(\x08')



_STORETRIPDATAREQUEST = DESCRIPTOR.message_types_by_name['StoreTripDataRequest']
_STORETRIPDATARESPONSE = DESCRIPTOR.message_types_by_name['StoreTripDataResponse']
StoreTripDataRequest = _reflection.GeneratedProtocolMessageType('StoreTripDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORETRIPDATAREQUEST,
  '__module__' : 'dem.store_trip_data_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.dem.StoreTripDataRequest)
  })
_sym_db.RegisterMessage(StoreTripDataRequest)

StoreTripDataResponse = _reflection.GeneratedProtocolMessageType('StoreTripDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORETRIPDATARESPONSE,
  '__module__' : 'dem.store_trip_data_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.dem.StoreTripDataResponse)
  })
_sym_db.RegisterMessage(StoreTripDataResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STORETRIPDATAREQUEST._serialized_start=44
  _STORETRIPDATAREQUEST._serialized_end=95
  _STORETRIPDATARESPONSE._serialized_start=97
  _STORETRIPDATARESPONSE._serialized_end=150
# @@protoc_insertion_point(module_scope)
