# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prediction/offline_feature.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n prediction/offline_feature.proto\x12\x14\x64\x65\x65proute.prediction\"\xab\x01\n\x0fLaneFeatureInfo\x12\x0f\n\x07lane_id\x18\x01 \x01(\x03\x12\x0e\n\x06lane_s\x18\x02 \x01(\x01\x12\x0e\n\x06lane_l\x18\x03 \x01(\x01\x12\x12\n\nangle_diff\x18\x04 \x01(\x01\x12\x1d\n\x15\x64ist_to_left_boundary\x18\x05 \x01(\x01\x12\x1e\n\x16\x64ist_to_right_boundary\x18\x06 \x01(\x01\x12\x14\n\x0clane_heading\x18\x07 \x01(\x01\"i\n\x16ObstacleOffLineFeature\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x43\n\x14\x63urrent_lane_feature\x18\x02 \x01(\x0b\x32%.deeproute.prediction.LaneFeatureInfo\"`\n\x0eOfflineFeature\x12N\n\x18obstacle_offline_feature\x18\x01 \x03(\x0b\x32,.deeproute.prediction.ObstacleOffLineFeature')



_LANEFEATUREINFO = DESCRIPTOR.message_types_by_name['LaneFeatureInfo']
_OBSTACLEOFFLINEFEATURE = DESCRIPTOR.message_types_by_name['ObstacleOffLineFeature']
_OFFLINEFEATURE = DESCRIPTOR.message_types_by_name['OfflineFeature']
LaneFeatureInfo = _reflection.GeneratedProtocolMessageType('LaneFeatureInfo', (_message.Message,), {
  'DESCRIPTOR' : _LANEFEATUREINFO,
  '__module__' : 'prediction.offline_feature_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.prediction.LaneFeatureInfo)
  })
_sym_db.RegisterMessage(LaneFeatureInfo)

ObstacleOffLineFeature = _reflection.GeneratedProtocolMessageType('ObstacleOffLineFeature', (_message.Message,), {
  'DESCRIPTOR' : _OBSTACLEOFFLINEFEATURE,
  '__module__' : 'prediction.offline_feature_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.prediction.ObstacleOffLineFeature)
  })
_sym_db.RegisterMessage(ObstacleOffLineFeature)

OfflineFeature = _reflection.GeneratedProtocolMessageType('OfflineFeature', (_message.Message,), {
  'DESCRIPTOR' : _OFFLINEFEATURE,
  '__module__' : 'prediction.offline_feature_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.prediction.OfflineFeature)
  })
_sym_db.RegisterMessage(OfflineFeature)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LANEFEATUREINFO._serialized_start=59
  _LANEFEATUREINFO._serialized_end=230
  _OBSTACLEOFFLINEFEATURE._serialized_start=232
  _OBSTACLEOFFLINEFEATURE._serialized_end=337
  _OFFLINEFEATURE._serialized_start=339
  _OFFLINEFEATURE._serialized_end=435
# @@protoc_insertion_point(module_scope)
