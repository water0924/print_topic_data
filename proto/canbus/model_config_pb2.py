# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: canbus/model_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63\x61nbus/model_config.proto\x12\x10\x64\x65\x65proute.canbus\"\x9e\x04\n\x0bModelConfig\x12\x30\n!flag_enable_steer_offset_observer\x18\x01 \x01(\x08:\x05\x66\x61lse\x12(\n\x19steer_offset_observer_max\x18\x02 \x01(\x01:\x05\x30.005\x12$\n\x18steer_offset_observer_b0\x18\x03 \x01(\x01:\x02\x31\x30\x12$\n\x18steer_offset_observer_b1\x18\x04 \x01(\x01:\x02\x31\x30\x12%\n\x18steer_offset_observer_b2\x18\x05 \x01(\x01:\x03\x30.5\x12\n\n\x02\x63\x66\x18\x06 \x01(\x01\x12\n\n\x02\x63r\x18\x07 \x01(\x01\x12\x0c\n\x04mass\x18\x08 \x01(\x01\x12\n\n\x02lf\x18\t \x01(\x01\x12\n\n\x02lr\x18\n \x01(\x01\x12\n\n\x02iz\x18\x0b \x01(\x01\x12\n\n\x02ts\x18\x0c \x01(\x01\x12 \n\x18minimum_speed_protection\x18\r \x01(\x01\x12$\n\x19\x65nable_observer_min_speed\x18\x0e \x01(\x01:\x01\x31\x12*\n\"cutoff_steer_wheel_rate_cmd_filter\x18\x0f \x01(\x01\x12\x1d\n\x15observer_lat_acc_thre\x18\x10 \x01(\x01\x12\x18\n\x10observer_vy_thre\x18\x11 \x01(\x01\x12\x1b\n\x13observer_steer_thre\x18\x12 \x01(\x01\x12 \n\x18observer_steer_rate_thre\x18\x13 \x01(\x01')



_MODELCONFIG = DESCRIPTOR.message_types_by_name['ModelConfig']
ModelConfig = _reflection.GeneratedProtocolMessageType('ModelConfig', (_message.Message,), {
  'DESCRIPTOR' : _MODELCONFIG,
  '__module__' : 'canbus.model_config_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.ModelConfig)
  })
_sym_db.RegisterMessage(ModelConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODELCONFIG._serialized_start=48
  _MODELCONFIG._serialized_end=590
# @@protoc_insertion_point(module_scope)
