# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recorder/record_stats.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1brecorder/record_stats.proto\x12\x12\x64\x65\x65proute.recorder\"=\n\x07\x42\x61gInfo\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\x04\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x04\"\xd4\x01\n\x0bRecordStats\x12\x14\n\x0coutput_paths\x18\x01 \x03(\t\x12\x14\n\x0cmin_msg_time\x18\x02 \x01(\x04\x12\x14\n\x0cmax_msg_time\x18\x03 \x01(\x04\x12\x11\n\tmsg_count\x18\x04 \x01(\x04\x12\x13\n\x0b\x63hunk_count\x18\x05 \x01(\x04\x12\x15\n\rdropped_count\x18\x06 \x01(\x04\x12.\n\tbags_info\x18\x07 \x03(\x0b\x32\x1b.deeproute.recorder.BagInfo\x12\x14\n\x0cqueued_count\x18\x08 \x01(\x04')



_BAGINFO = DESCRIPTOR.message_types_by_name['BagInfo']
_RECORDSTATS = DESCRIPTOR.message_types_by_name['RecordStats']
BagInfo = _reflection.GeneratedProtocolMessageType('BagInfo', (_message.Message,), {
  'DESCRIPTOR' : _BAGINFO,
  '__module__' : 'recorder.record_stats_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.recorder.BagInfo)
  })
_sym_db.RegisterMessage(BagInfo)

RecordStats = _reflection.GeneratedProtocolMessageType('RecordStats', (_message.Message,), {
  'DESCRIPTOR' : _RECORDSTATS,
  '__module__' : 'recorder.record_stats_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.recorder.RecordStats)
  })
_sym_db.RegisterMessage(RecordStats)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BAGINFO._serialized_start=51
  _BAGINFO._serialized_end=112
  _RECORDSTATS._serialized_start=115
  _RECORDSTATS._serialized_end=327
# @@protoc_insertion_point(module_scope)
