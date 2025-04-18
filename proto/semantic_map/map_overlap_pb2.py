# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: semantic_map/map_overlap.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import geometry_pb2 as common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esemantic_map/map_overlap.proto\x12\x0f\x64\x65\x65proute.hdmap\x1a\x15\x63ommon/geometry.proto\"^\n\x0fLaneOverlapInfo\x12\x0f\n\x07start_s\x18\x01 \x01(\x01\x12\r\n\x05\x65nd_s\x18\x02 \x01(\x01\x12\x10\n\x08is_merge\x18\x03 \x01(\x08\x12\x19\n\x11region_overlap_id\x18\x04 \x01(\x05\"\x13\n\x11SignalOverlapInfo\"\x15\n\x13StopSignOverlapInfo\"s\n\x14\x43rosswalkOverlapInfo\x12\x19\n\x11region_overlap_id\x18\x01 \x01(\x05\x12@\n\x1dintersect_laneboundary_points\x18\x02 \x03(\x0b\x32\x19.deeproute.common.Point3D\"\x15\n\x13JunctionOverlapInfo\"\x12\n\x10YieldOverlapInfo\"\x16\n\x14\x43learAreaOverlapInfo\"\x16\n\x14SpeedBumpOverlapInfo\"\x19\n\x17ParkingSpaceOverlapInfo\"\x18\n\x16PNCJunctionOverlapInfo\"K\n\x11RegionOverlapInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12*\n\x07polygon\x18\x02 \x03(\x0b\x32\x19.deeproute.common.Polygon\"\x81\x06\n\x11ObjectOverlapInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12=\n\x11lane_overlap_info\x18\x03 \x01(\x0b\x32 .deeproute.hdmap.LaneOverlapInfoH\x00\x12\x41\n\x13signal_overlap_info\x18\x04 \x01(\x0b\x32\".deeproute.hdmap.SignalOverlapInfoH\x00\x12\x46\n\x16stop_sign_overlap_info\x18\x05 \x01(\x0b\x32$.deeproute.hdmap.StopSignOverlapInfoH\x00\x12G\n\x16\x63rosswalk_overlap_info\x18\x06 \x01(\x0b\x32%.deeproute.hdmap.CrosswalkOverlapInfoH\x00\x12\x45\n\x15junction_overlap_info\x18\x07 \x01(\x0b\x32$.deeproute.hdmap.JunctionOverlapInfoH\x00\x12\x44\n\x17yield_sign_overlap_info\x18\x08 \x01(\x0b\x32!.deeproute.hdmap.YieldOverlapInfoH\x00\x12H\n\x17\x63lear_area_overlap_info\x18\t \x01(\x0b\x32%.deeproute.hdmap.ClearAreaOverlapInfoH\x00\x12H\n\x17speed_bump_overlap_info\x18\n \x01(\x0b\x32%.deeproute.hdmap.SpeedBumpOverlapInfoH\x00\x12N\n\x1aparking_space_overlap_info\x18\x0b \x01(\x0b\x32(.deeproute.hdmap.ParkingSpaceOverlapInfoH\x00\x12L\n\x19pnc_junction_overlap_info\x18\x0c \x01(\x0b\x32\'.deeproute.hdmap.PNCJunctionOverlapInfoH\x00\x42\x0e\n\x0coverlap_info\"\xc6\x05\n\x07Overlap\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x32\n\x06object\x18\x02 \x03(\x0b\x32\".deeproute.hdmap.ObjectOverlapInfo\x12:\n\x0eregion_overlap\x18\x03 \x03(\x0b\x32\".deeproute.hdmap.RegionOverlapInfo\x12\x32\n\x04type\x18\x04 \x01(\x0e\x32$.deeproute.hdmap.Overlap.OverlapType\x12\x0f\n\x07s_begin\x18\x05 \x01(\x02\x12\r\n\x05s_end\x18\x06 \x01(\x02\"\xea\x03\n\x0bOverlapType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nCLEAR_ZONE\x10\x01\x12\x0e\n\nCROSS_WALK\x10\x02\x12\x0c\n\x08JUNCTION\x10\x03\x12\x08\n\x04LANE\x10\x04\x12\r\n\tSTOP_LINE\x10\x05\x12\x0c\n\x08\x45NTRANCE\x10\x06\x12\x0f\n\x0b\x42US_STATION\x10\x07\x12\x0b\n\x07PARKING\x10\x08\x12\x10\n\x0cPNC_JUNCTION\x10\t\x12\x15\n\x11JUNCTION_END_LINE\x10\n\x12\x0e\n\nSPEED_BUMP\x10\x0b\x12\r\n\tROAD_MASK\x10\x0c\x12\x12\n\x0eROAD_MASK_PLUS\x10\r\x12\x1f\n\x1b\x44\x45\x43\x45LERATION_AND_YIELD_LINE\x10\x0e\x12#\n\x1fTRANSVERSE_DECELERATION_MARKING\x10\x0f\x12!\n\x1dVEHICLE_GAP_CONFIRMATION_LINE\x10\x10\x12\r\n\tWIDE_LANE\x10\x11\x12\x10\n\x0cINVALID_AREA\x10\x12\x12\x12\n\x0e\x44IVERSION_AREA\x10\x13\x12\x10\n\x0cSTANDBY_AREA\x10\x14\x12\x10\n\x0cTOLL_STATION\x10\x15\x12\x0f\n\x0bLANE_MARKER\x10\x16\x12\x17\n\x13\x42ICYCLE_LANE_MARKER\x10\x17\x12\x13\n\x0f\x43ONNECTION_LINE\x10\x18')



_LANEOVERLAPINFO = DESCRIPTOR.message_types_by_name['LaneOverlapInfo']
_SIGNALOVERLAPINFO = DESCRIPTOR.message_types_by_name['SignalOverlapInfo']
_STOPSIGNOVERLAPINFO = DESCRIPTOR.message_types_by_name['StopSignOverlapInfo']
_CROSSWALKOVERLAPINFO = DESCRIPTOR.message_types_by_name['CrosswalkOverlapInfo']
_JUNCTIONOVERLAPINFO = DESCRIPTOR.message_types_by_name['JunctionOverlapInfo']
_YIELDOVERLAPINFO = DESCRIPTOR.message_types_by_name['YieldOverlapInfo']
_CLEARAREAOVERLAPINFO = DESCRIPTOR.message_types_by_name['ClearAreaOverlapInfo']
_SPEEDBUMPOVERLAPINFO = DESCRIPTOR.message_types_by_name['SpeedBumpOverlapInfo']
_PARKINGSPACEOVERLAPINFO = DESCRIPTOR.message_types_by_name['ParkingSpaceOverlapInfo']
_PNCJUNCTIONOVERLAPINFO = DESCRIPTOR.message_types_by_name['PNCJunctionOverlapInfo']
_REGIONOVERLAPINFO = DESCRIPTOR.message_types_by_name['RegionOverlapInfo']
_OBJECTOVERLAPINFO = DESCRIPTOR.message_types_by_name['ObjectOverlapInfo']
_OVERLAP = DESCRIPTOR.message_types_by_name['Overlap']
_OVERLAP_OVERLAPTYPE = _OVERLAP.enum_types_by_name['OverlapType']
LaneOverlapInfo = _reflection.GeneratedProtocolMessageType('LaneOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _LANEOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.LaneOverlapInfo)
  })
_sym_db.RegisterMessage(LaneOverlapInfo)

SignalOverlapInfo = _reflection.GeneratedProtocolMessageType('SignalOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _SIGNALOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.SignalOverlapInfo)
  })
_sym_db.RegisterMessage(SignalOverlapInfo)

StopSignOverlapInfo = _reflection.GeneratedProtocolMessageType('StopSignOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _STOPSIGNOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.StopSignOverlapInfo)
  })
_sym_db.RegisterMessage(StopSignOverlapInfo)

CrosswalkOverlapInfo = _reflection.GeneratedProtocolMessageType('CrosswalkOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _CROSSWALKOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.CrosswalkOverlapInfo)
  })
_sym_db.RegisterMessage(CrosswalkOverlapInfo)

JunctionOverlapInfo = _reflection.GeneratedProtocolMessageType('JunctionOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _JUNCTIONOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.JunctionOverlapInfo)
  })
_sym_db.RegisterMessage(JunctionOverlapInfo)

YieldOverlapInfo = _reflection.GeneratedProtocolMessageType('YieldOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _YIELDOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.YieldOverlapInfo)
  })
_sym_db.RegisterMessage(YieldOverlapInfo)

ClearAreaOverlapInfo = _reflection.GeneratedProtocolMessageType('ClearAreaOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _CLEARAREAOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.ClearAreaOverlapInfo)
  })
_sym_db.RegisterMessage(ClearAreaOverlapInfo)

SpeedBumpOverlapInfo = _reflection.GeneratedProtocolMessageType('SpeedBumpOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDBUMPOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.SpeedBumpOverlapInfo)
  })
_sym_db.RegisterMessage(SpeedBumpOverlapInfo)

ParkingSpaceOverlapInfo = _reflection.GeneratedProtocolMessageType('ParkingSpaceOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _PARKINGSPACEOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.ParkingSpaceOverlapInfo)
  })
_sym_db.RegisterMessage(ParkingSpaceOverlapInfo)

PNCJunctionOverlapInfo = _reflection.GeneratedProtocolMessageType('PNCJunctionOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _PNCJUNCTIONOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.PNCJunctionOverlapInfo)
  })
_sym_db.RegisterMessage(PNCJunctionOverlapInfo)

RegionOverlapInfo = _reflection.GeneratedProtocolMessageType('RegionOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _REGIONOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.RegionOverlapInfo)
  })
_sym_db.RegisterMessage(RegionOverlapInfo)

ObjectOverlapInfo = _reflection.GeneratedProtocolMessageType('ObjectOverlapInfo', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTOVERLAPINFO,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.ObjectOverlapInfo)
  })
_sym_db.RegisterMessage(ObjectOverlapInfo)

Overlap = _reflection.GeneratedProtocolMessageType('Overlap', (_message.Message,), {
  'DESCRIPTOR' : _OVERLAP,
  '__module__' : 'semantic_map.map_overlap_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.Overlap)
  })
_sym_db.RegisterMessage(Overlap)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LANEOVERLAPINFO._serialized_start=74
  _LANEOVERLAPINFO._serialized_end=168
  _SIGNALOVERLAPINFO._serialized_start=170
  _SIGNALOVERLAPINFO._serialized_end=189
  _STOPSIGNOVERLAPINFO._serialized_start=191
  _STOPSIGNOVERLAPINFO._serialized_end=212
  _CROSSWALKOVERLAPINFO._serialized_start=214
  _CROSSWALKOVERLAPINFO._serialized_end=329
  _JUNCTIONOVERLAPINFO._serialized_start=331
  _JUNCTIONOVERLAPINFO._serialized_end=352
  _YIELDOVERLAPINFO._serialized_start=354
  _YIELDOVERLAPINFO._serialized_end=372
  _CLEARAREAOVERLAPINFO._serialized_start=374
  _CLEARAREAOVERLAPINFO._serialized_end=396
  _SPEEDBUMPOVERLAPINFO._serialized_start=398
  _SPEEDBUMPOVERLAPINFO._serialized_end=420
  _PARKINGSPACEOVERLAPINFO._serialized_start=422
  _PARKINGSPACEOVERLAPINFO._serialized_end=447
  _PNCJUNCTIONOVERLAPINFO._serialized_start=449
  _PNCJUNCTIONOVERLAPINFO._serialized_end=473
  _REGIONOVERLAPINFO._serialized_start=475
  _REGIONOVERLAPINFO._serialized_end=550
  _OBJECTOVERLAPINFO._serialized_start=553
  _OBJECTOVERLAPINFO._serialized_end=1322
  _OVERLAP._serialized_start=1325
  _OVERLAP._serialized_end=2035
  _OVERLAP_OVERLAPTYPE._serialized_start=1545
  _OVERLAP_OVERLAPTYPE._serialized_end=2035
# @@protoc_insertion_point(module_scope)
