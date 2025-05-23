# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/onboard_status.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63ommon/onboard_status.proto\x12\x10\x64\x65\x65proute.common\"r\n\x06Syslog\x12\x13\n\x0b\x64\x65\x62ug_level\x18\x01 \x01(\t\x12\x13\n\x0bmodule_name\x18\x02 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x03 \x01(\x05\x12\x12\n\nevent_name\x18\x04 \x01(\t\x12\x0b\n\x03msg\x18\x05 \x01(\t\x12\x0b\n\x03\x63md\x18\x06 \x01(\t\"W\n\x0cNotification\x12\x13\n\x0b\x64\x65\x62ug_level\x18\x01 \x01(\t\x12\x13\n\x0bmodule_name\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x04 \x01(\x05\"9\n\tCarStatus\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bmodule_name\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\"V\n\x0cOperationlog\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x13\n\x0bmodule_name\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\x12\n\nevent_name\x18\x04 \x01(\t')



_SYSLOG = DESCRIPTOR.message_types_by_name['Syslog']
_NOTIFICATION = DESCRIPTOR.message_types_by_name['Notification']
_CARSTATUS = DESCRIPTOR.message_types_by_name['CarStatus']
_OPERATIONLOG = DESCRIPTOR.message_types_by_name['Operationlog']
Syslog = _reflection.GeneratedProtocolMessageType('Syslog', (_message.Message,), {
  'DESCRIPTOR' : _SYSLOG,
  '__module__' : 'common.onboard_status_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.common.Syslog)
  })
_sym_db.RegisterMessage(Syslog)

Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATION,
  '__module__' : 'common.onboard_status_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.common.Notification)
  })
_sym_db.RegisterMessage(Notification)

CarStatus = _reflection.GeneratedProtocolMessageType('CarStatus', (_message.Message,), {
  'DESCRIPTOR' : _CARSTATUS,
  '__module__' : 'common.onboard_status_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.common.CarStatus)
  })
_sym_db.RegisterMessage(CarStatus)

Operationlog = _reflection.GeneratedProtocolMessageType('Operationlog', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONLOG,
  '__module__' : 'common.onboard_status_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.common.Operationlog)
  })
_sym_db.RegisterMessage(Operationlog)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYSLOG._serialized_start=49
  _SYSLOG._serialized_end=163
  _NOTIFICATION._serialized_start=165
  _NOTIFICATION._serialized_end=252
  _CARSTATUS._serialized_start=254
  _CARSTATUS._serialized_end=311
  _OPERATIONLOG._serialized_start=313
  _OPERATIONLOG._serialized_end=399
# @@protoc_insertion_point(module_scope)
