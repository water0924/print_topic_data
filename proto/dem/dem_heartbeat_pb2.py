# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dem/dem_heartbeat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x64\x65m/dem_heartbeat.proto\x12\rdeeproute.dem\".\n\x0c\x44\x65mHeartBeat\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04')



_DEMHEARTBEAT = DESCRIPTOR.message_types_by_name['DemHeartBeat']
DemHeartBeat = _reflection.GeneratedProtocolMessageType('DemHeartBeat', (_message.Message,), {
  'DESCRIPTOR' : _DEMHEARTBEAT,
  '__module__' : 'dem.dem_heartbeat_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.dem.DemHeartBeat)
  })
_sym_db.RegisterMessage(DemHeartBeat)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEMHEARTBEAT._serialized_start=42
  _DEMHEARTBEAT._serialized_end=88
# @@protoc_insertion_point(module_scope)
