# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/drive_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63ommon/drive_state.proto\x12\x10\x64\x65\x65proute.common\"\xd0\x01\n\x0c\x45ngageAdvice\x12\x46\n\x06\x61\x64vice\x18\x01 \x01(\x0e\x32%.deeproute.common.EngageAdvice.Advice:\x0f\x44ISALLOW_ENGAGE\x12\x0e\n\x06reason\x18\x02 \x01(\t\"h\n\x06\x41\x64vice\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0f\x44ISALLOW_ENGAGE\x10\x01\x12\x13\n\x0fREADY_TO_ENGAGE\x10\x02\x12\x10\n\x0cKEEP_ENGAGED\x10\x03\x12\x15\n\x11PREPARE_DISENGAGE\x10\x04\"a\n\x0b\x44rivingMode\x12\x30\n\x04mode\x18\x01 \x01(\x0e\x32\".deeproute.common.DrivingMode.Mode\" \n\x04Mode\x12\x0b\n\x07\x44RIVING\x10\x00\x12\x0b\n\x07PARKING\x10\x01')



_ENGAGEADVICE = DESCRIPTOR.message_types_by_name['EngageAdvice']
_DRIVINGMODE = DESCRIPTOR.message_types_by_name['DrivingMode']
_ENGAGEADVICE_ADVICE = _ENGAGEADVICE.enum_types_by_name['Advice']
_DRIVINGMODE_MODE = _DRIVINGMODE.enum_types_by_name['Mode']
EngageAdvice = _reflection.GeneratedProtocolMessageType('EngageAdvice', (_message.Message,), {
  'DESCRIPTOR' : _ENGAGEADVICE,
  '__module__' : 'common.drive_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.common.EngageAdvice)
  })
_sym_db.RegisterMessage(EngageAdvice)

DrivingMode = _reflection.GeneratedProtocolMessageType('DrivingMode', (_message.Message,), {
  'DESCRIPTOR' : _DRIVINGMODE,
  '__module__' : 'common.drive_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.common.DrivingMode)
  })
_sym_db.RegisterMessage(DrivingMode)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENGAGEADVICE._serialized_start=47
  _ENGAGEADVICE._serialized_end=255
  _ENGAGEADVICE_ADVICE._serialized_start=151
  _ENGAGEADVICE_ADVICE._serialized_end=255
  _DRIVINGMODE._serialized_start=257
  _DRIVINGMODE._serialized_end=354
  _DRIVINGMODE_MODE._serialized_start=322
  _DRIVINGMODE_MODE._serialized_end=354
# @@protoc_insertion_point(module_scope)
