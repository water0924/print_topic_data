# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: devices/devices.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x64\x65vices/devices.proto\x12\x10\x64\x65\x65proute.common\"\xa7\x01\n\rDevicesConfig\x12$\n\x15has_remote_controller\x18\x01 \x01(\x08:\x05\x66\x61lse\x12!\n\x12has_remote_cockpit\x18\x02 \x01(\x08:\x05\x66\x61lse\x12,\n\x1dhas_video_transmission_device\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10has_backup_brake\x18\x04 \x01(\x08:\x05\x66\x61lse')



_DEVICESCONFIG = DESCRIPTOR.message_types_by_name['DevicesConfig']
DevicesConfig = _reflection.GeneratedProtocolMessageType('DevicesConfig', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESCONFIG,
  '__module__' : 'devices.devices_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.common.DevicesConfig)
  })
_sym_db.RegisterMessage(DevicesConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEVICESCONFIG._serialized_start=44
  _DEVICESCONFIG._serialized_end=211
# @@protoc_insertion_point(module_scope)
