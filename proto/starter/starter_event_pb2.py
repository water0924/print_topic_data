# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: starter/starter_event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bstarter/starter_event.proto\x12\x11\x64\x65\x65proute.starter\"6\n\x12StarterReportEvent\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t')



_STARTERREPORTEVENT = DESCRIPTOR.message_types_by_name['StarterReportEvent']
StarterReportEvent = _reflection.GeneratedProtocolMessageType('StarterReportEvent', (_message.Message,), {
  'DESCRIPTOR' : _STARTERREPORTEVENT,
  '__module__' : 'starter.starter_event_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.starter.StarterReportEvent)
  })
_sym_db.RegisterMessage(StarterReportEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STARTERREPORTEVENT._serialized_start=50
  _STARTERREPORTEVENT._serialized_end=104
# @@protoc_insertion_point(module_scope)
