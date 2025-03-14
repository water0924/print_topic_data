# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: semantic_map/map_parking_space.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import geometry_pb2 as common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$semantic_map/map_parking_space.proto\x12\x0f\x64\x65\x65proute.hdmap\x1a\x15\x63ommon/geometry.proto\"\xe7\x04\n\x0cParkingSpace\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x30\n\x04type\x18\x02 \x01(\x0e\x32\".deeproute.hdmap.ParkingSpace.Type\x12*\n\x07polygon\x18\x03 \x01(\x0b\x32\x19.deeproute.common.Polygon\x12\x0f\n\x07virtual\x18\x04 \x01(\x08\x12\x13\n\x07heading\x18\x05 \x01(\x01\x42\x02\x18\x01\x12\x34\n\x0c\x63\x65nter_point\x18\x06 \x01(\x0b\x32\x1a.deeproute.common.PointENUB\x02\x18\x01\x12\x34\n\x0cswitch_point\x18\x07 \x01(\x0b\x32\x1a.deeproute.common.PointENUB\x02\x18\x01\x12\x38\n\x10switch_point_out\x18\x08 \x01(\x0b\x32\x1a.deeproute.common.PointENUB\x02\x18\x01\x12\x32\n\x05shape\x18\t \x01(\x0e\x32#.deeproute.hdmap.ParkingSpace.Shape\x12\x1b\n\x13ground_obstacle_ids\x18\n \x03(\x05\"}\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x19\n\x15ON_LANE_PARKING_SPACE\x10\x01\x12\"\n\x1eOPEN_PARKING_LOT_PARKING_SPACE\x10\x02\x12)\n%UNDERGROUND_PARKING_LOT_PARKING_SPACE\x10\x03\"Q\n\x05Shape\x12\x18\n\x14VERTICAL_PARKING_LOT\x10\x01\x12\x14\n\x10SIDE_PARKING_LOT\x10\x02\x12\x18\n\x14INCLINED_PARKING_LOT\x10\x03')



_PARKINGSPACE = DESCRIPTOR.message_types_by_name['ParkingSpace']
_PARKINGSPACE_TYPE = _PARKINGSPACE.enum_types_by_name['Type']
_PARKINGSPACE_SHAPE = _PARKINGSPACE.enum_types_by_name['Shape']
ParkingSpace = _reflection.GeneratedProtocolMessageType('ParkingSpace', (_message.Message,), {
  'DESCRIPTOR' : _PARKINGSPACE,
  '__module__' : 'semantic_map.map_parking_space_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.ParkingSpace)
  })
_sym_db.RegisterMessage(ParkingSpace)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PARKINGSPACE.fields_by_name['heading']._options = None
  _PARKINGSPACE.fields_by_name['heading']._serialized_options = b'\030\001'
  _PARKINGSPACE.fields_by_name['center_point']._options = None
  _PARKINGSPACE.fields_by_name['center_point']._serialized_options = b'\030\001'
  _PARKINGSPACE.fields_by_name['switch_point']._options = None
  _PARKINGSPACE.fields_by_name['switch_point']._serialized_options = b'\030\001'
  _PARKINGSPACE.fields_by_name['switch_point_out']._options = None
  _PARKINGSPACE.fields_by_name['switch_point_out']._serialized_options = b'\030\001'
  _PARKINGSPACE._serialized_start=81
  _PARKINGSPACE._serialized_end=696
  _PARKINGSPACE_TYPE._serialized_start=488
  _PARKINGSPACE_TYPE._serialized_end=613
  _PARKINGSPACE_SHAPE._serialized_start=615
  _PARKINGSPACE_SHAPE._serialized_end=696
# @@protoc_insertion_point(module_scope)
