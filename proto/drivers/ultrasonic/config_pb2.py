# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drivers/ultrasonic/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import geometry_pb2 as common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x64rivers/ultrasonic/config.proto\x12\x1c\x64\x65\x65proute.drivers.ultrasonic\x1a\x15\x63ommon/geometry.proto\"t\n\x06\x43onfig\x12\x10\n\x08\x66rame_id\x18\x01 \x01(\t\x12\x0b\n\x03\x66ov\x18\x02 \x01(\r\x12?\n\x14sensor_to_ultrasonic\x18\x03 \x01(\x0b\x32!.deeproute.common.Transformation3\x12\n\n\x02id\x18\x04 \x01(\r\"H\n\x10UltrasonicConfig\x12\x34\n\x06\x63onfig\x18\x01 \x03(\x0b\x32$.deeproute.drivers.ultrasonic.Config')



_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_ULTRASONICCONFIG = DESCRIPTOR.message_types_by_name['UltrasonicConfig']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'drivers.ultrasonic.config_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.ultrasonic.Config)
  })
_sym_db.RegisterMessage(Config)

UltrasonicConfig = _reflection.GeneratedProtocolMessageType('UltrasonicConfig', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICCONFIG,
  '__module__' : 'drivers.ultrasonic.config_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.ultrasonic.UltrasonicConfig)
  })
_sym_db.RegisterMessage(UltrasonicConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIG._serialized_start=88
  _CONFIG._serialized_end=204
  _ULTRASONICCONFIG._serialized_start=206
  _ULTRASONICCONFIG._serialized_end=278
# @@protoc_insertion_point(module_scope)
