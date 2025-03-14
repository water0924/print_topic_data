# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map/map_common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.map import common_type_pb2 as map_dot_common__type__pb2
from proto.map import sd_map_pb2 as map_dot_sd__map__pb2
from proto.lock_on_road import lock_on_road_pb2 as lock__on__road_dot_lock__on__road__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14map/map_common.proto\x12\rdeeproute.map\x1a\x15map/common_type.proto\x1a\x10map/sd_map.proto\x1a\x1flock_on_road/lock_on_road.proto\"\xb4\x01\n\x0c\x43rossingInfo\x12\x32\n\rcrossing_type\x18\x01 \x01(\x0e\x32\x1b.deeproute.map.CrossingType\x12.\n\rcrossing_turn\x18\x02 \x01(\x0e\x32\x17.deeproute.map.LaneTurn\x12\x1c\n\x14\x63rossing_remaining_s\x18\x03 \x01(\x01\x12\"\n\x1a\x66reeway_main_road_lane_ids\x18\x04 \x03(\x05\"\xf2\x02\n\nSdRoadInfo\x12,\n\nroad_class\x18\x01 \x01(\x0e\x32\x18.deeproute.map.RoadClass\x12\x32\n\rcrossing_info\x18\x02 \x01(\x0b\x32\x1b.deeproute.map.CrossingInfo\x12,\n\nlink_usage\x18\x03 \x01(\x0e\x32\x18.deeproute.map.LinkUsage\x12\x38\n\x0clink_formway\x18\x04 \x01(\x0e\x32\".deeproute.sd_map.LinkData.FormWay\x12\x33\n\x0e\x63rossing_infos\x18\x05 \x03(\x0b\x32\x1b.deeproute.map.CrossingInfo\x12\x17\n\x0fis_on_main_road\x18\x06 \x01(\x08\x12L\n\x13lock_on_road_status\x18\x07 \x01(\x0e\x32/.deeproute.localization.LockOnRoadResult.Status\"\xaf\x01\n\x08\x41reaInfo\x12\x33\n\tarea_type\x18\x01 \x01(\x0e\x32 .deeproute.map.AreaInfo.AreaType\x12\x1e\n\x16\x64istance_to_area_start\x18\x02 \x01(\x01\x12\x1c\n\x14\x64istance_to_area_end\x18\x03 \x01(\x01\"0\n\x08\x41reaType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tREST_AREA\x10\x01\x12\x08\n\x04TOLL\x10\x02')



_CROSSINGINFO = DESCRIPTOR.message_types_by_name['CrossingInfo']
_SDROADINFO = DESCRIPTOR.message_types_by_name['SdRoadInfo']
_AREAINFO = DESCRIPTOR.message_types_by_name['AreaInfo']
_AREAINFO_AREATYPE = _AREAINFO.enum_types_by_name['AreaType']
CrossingInfo = _reflection.GeneratedProtocolMessageType('CrossingInfo', (_message.Message,), {
  'DESCRIPTOR' : _CROSSINGINFO,
  '__module__' : 'map.map_common_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.map.CrossingInfo)
  })
_sym_db.RegisterMessage(CrossingInfo)

SdRoadInfo = _reflection.GeneratedProtocolMessageType('SdRoadInfo', (_message.Message,), {
  'DESCRIPTOR' : _SDROADINFO,
  '__module__' : 'map.map_common_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.map.SdRoadInfo)
  })
_sym_db.RegisterMessage(SdRoadInfo)

AreaInfo = _reflection.GeneratedProtocolMessageType('AreaInfo', (_message.Message,), {
  'DESCRIPTOR' : _AREAINFO,
  '__module__' : 'map.map_common_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.map.AreaInfo)
  })
_sym_db.RegisterMessage(AreaInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CROSSINGINFO._serialized_start=114
  _CROSSINGINFO._serialized_end=294
  _SDROADINFO._serialized_start=297
  _SDROADINFO._serialized_end=667
  _AREAINFO._serialized_start=670
  _AREAINFO._serialized_end=845
  _AREAINFO_AREATYPE._serialized_start=797
  _AREAINFO_AREATYPE._serialized_end=845
# @@protoc_insertion_point(module_scope)
