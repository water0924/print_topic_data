# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: routing/cloud_task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18routing/cloud_task.proto\x12\x14\x64\x65\x65proute.cloud_task\"\x9a\x01\n\x11ImageCollectEvent\x12\x1b\n\x13min_move_dist_meter\x18\x03 \x01(\x01\x12\x1c\n\x14min_interval_time_us\x18\x04 \x01(\x03\x12\x16\n\x0emax_report_num\x18\x05 \x01(\x05\x12\x19\n\x11link_offset_start\x18\x06 \x01(\x01\x12\x17\n\x0flink_offset_end\x18\x07 \x01(\x01')



_IMAGECOLLECTEVENT = DESCRIPTOR.message_types_by_name['ImageCollectEvent']
ImageCollectEvent = _reflection.GeneratedProtocolMessageType('ImageCollectEvent', (_message.Message,), {
  'DESCRIPTOR' : _IMAGECOLLECTEVENT,
  '__module__' : 'routing.cloud_task_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.cloud_task.ImageCollectEvent)
  })
_sym_db.RegisterMessage(ImageCollectEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGECOLLECTEVENT._serialized_start=51
  _IMAGECOLLECTEVENT._serialized_end=205
# @@protoc_insertion_point(module_scope)
