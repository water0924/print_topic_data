# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trip/trip_end.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13trip/trip_end.proto\x12\x0e\x64\x65\x65proute.trip\"q\n\x0cTripEndEvent\x12\x11\n\ttrip_name\x18\x01 \x01(\t\x12\x16\n\x0e\x64river_version\x18\x02 \x01(\t\x12\x18\n\x10\x65nd_timestamp_ns\x18\x03 \x01(\t\x12\x1c\n\x14\x64river_short_version\x18\x04 \x01(\t')



_TRIPENDEVENT = DESCRIPTOR.message_types_by_name['TripEndEvent']
TripEndEvent = _reflection.GeneratedProtocolMessageType('TripEndEvent', (_message.Message,), {
  'DESCRIPTOR' : _TRIPENDEVENT,
  '__module__' : 'trip.trip_end_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.trip.TripEndEvent)
  })
_sym_db.RegisterMessage(TripEndEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRIPENDEVENT._serialized_start=39
  _TRIPENDEVENT._serialized_end=152
# @@protoc_insertion_point(module_scope)
