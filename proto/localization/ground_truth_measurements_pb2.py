# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: localization/ground_truth_measurements.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.drivers.gnss import ins_pb2 as drivers_dot_gnss_dot_ins__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,localization/ground_truth_measurements.proto\x12 deeproute.benchmark.v2.proto_ads\x1a\x16\x64rivers/gnss/ins.proto\"L\n\x17GroundTruthMeasurements\x12\x31\n\x0cmeasurements\x18\x01 \x03(\x0b\x32\x1b.deeproute.drivers.gnss.Ins')



_GROUNDTRUTHMEASUREMENTS = DESCRIPTOR.message_types_by_name['GroundTruthMeasurements']
GroundTruthMeasurements = _reflection.GeneratedProtocolMessageType('GroundTruthMeasurements', (_message.Message,), {
  'DESCRIPTOR' : _GROUNDTRUTHMEASUREMENTS,
  '__module__' : 'localization.ground_truth_measurements_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.benchmark.v2.proto_ads.GroundTruthMeasurements)
  })
_sym_db.RegisterMessage(GroundTruthMeasurements)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GROUNDTRUTHMEASUREMENTS._serialized_start=106
  _GROUNDTRUTHMEASUREMENTS._serialized_end=182
# @@protoc_insertion_point(module_scope)
