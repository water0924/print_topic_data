# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: church/serialized_module_event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$church/serialized_module_event.proto\x12\tdr.common\"4\n\x13SerializedEventInfo\x12\x1d\n\x15serialized_event_info\x18\x01 \x01(\x0c\"X\n\x16SerializedModuleEvents\x12>\n\x16serialized_event_infos\x18\x01 \x03(\x0b\x32\x1e.dr.common.SerializedEventInfo')



_SERIALIZEDEVENTINFO = DESCRIPTOR.message_types_by_name['SerializedEventInfo']
_SERIALIZEDMODULEEVENTS = DESCRIPTOR.message_types_by_name['SerializedModuleEvents']
SerializedEventInfo = _reflection.GeneratedProtocolMessageType('SerializedEventInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERIALIZEDEVENTINFO,
  '__module__' : 'church.serialized_module_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.common.SerializedEventInfo)
  })
_sym_db.RegisterMessage(SerializedEventInfo)

SerializedModuleEvents = _reflection.GeneratedProtocolMessageType('SerializedModuleEvents', (_message.Message,), {
  'DESCRIPTOR' : _SERIALIZEDMODULEEVENTS,
  '__module__' : 'church.serialized_module_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.common.SerializedModuleEvents)
  })
_sym_db.RegisterMessage(SerializedModuleEvents)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERIALIZEDEVENTINFO._serialized_start=51
  _SERIALIZEDEVENTINFO._serialized_end=103
  _SERIALIZEDMODULEEVENTS._serialized_start=105
  _SERIALIZEDMODULEEVENTS._serialized_end=193
# @@protoc_insertion_point(module_scope)
