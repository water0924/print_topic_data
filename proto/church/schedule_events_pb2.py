# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: church/schedule_events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.church import schedule_event_pb2 as church_dot_schedule__event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63hurch/schedule_events.proto\x12\x10\x64\x65\x65proute.church\x1a\x1b\x63hurch/schedule_event.proto\"J\n\x0eScheduleEvents\x12\x38\n\x0fschedule_events\x18\x01 \x03(\x0b\x32\x1f.deeproute.church.ScheduleEvent')



_SCHEDULEEVENTS = DESCRIPTOR.message_types_by_name['ScheduleEvents']
ScheduleEvents = _reflection.GeneratedProtocolMessageType('ScheduleEvents', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULEEVENTS,
  '__module__' : 'church.schedule_events_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.church.ScheduleEvents)
  })
_sym_db.RegisterMessage(ScheduleEvents)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCHEDULEEVENTS._serialized_start=79
  _SCHEDULEEVENTS._serialized_end=153
# @@protoc_insertion_point(module_scope)
