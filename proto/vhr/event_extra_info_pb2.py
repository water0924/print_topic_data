# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vhr/event_extra_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1avhr/event_extra_info.proto\x12\x06\x64r.vhr\"v\n\x0e\x45ventExtraInfo\x12\x0f\n\x07\x61\x64_code\x18\x01 \x01(\x04\x12\x12\n\nroad_class\x18\x02 \x01(\x05\x12\x11\n\troad_type\x18\x03 \x01(\x05\x12\x15\n\rdsm_sub_state\x18\x04 \x01(\x05\x12\x15\n\rdr_road_class\x18\x05 \x01(\x05')



_EVENTEXTRAINFO = DESCRIPTOR.message_types_by_name['EventExtraInfo']
EventExtraInfo = _reflection.GeneratedProtocolMessageType('EventExtraInfo', (_message.Message,), {
  'DESCRIPTOR' : _EVENTEXTRAINFO,
  '__module__' : 'vhr.event_extra_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.vhr.EventExtraInfo)
  })
_sym_db.RegisterMessage(EventExtraInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENTEXTRAINFO._serialized_start=38
  _EVENTEXTRAINFO._serialized_end=156
# @@protoc_insertion_point(module_scope)
