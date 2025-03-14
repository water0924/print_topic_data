# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: semantic_map/map_lane.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.semantic_map import map_geometry_pb2 as semantic__map_dot_map__geometry__pb2
from proto.semantic_map import map_overlap_pb2 as semantic__map_dot_map__overlap__pb2
from proto.common import geometry_pb2 as common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bsemantic_map/map_lane.proto\x12\x0f\x64\x65\x65proute.hdmap\x1a\x1fsemantic_map/map_geometry.proto\x1a\x1esemantic_map/map_overlap.proto\x1a\x15\x63ommon/geometry.proto\"\x9f\x07\n\x10LaneBoundaryType\x12\t\n\x01s\x18\x01 \x01(\x01\x12\x35\n\x05types\x18\x02 \x03(\x0e\x32&.deeproute.hdmap.LaneBoundaryType.Type\"\xc8\x06\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rDOTTED_YELLOW\x10\x01\x12\x10\n\x0c\x44OTTED_WHITE\x10\x02\x12\x10\n\x0cSOLID_YELLOW\x10\x03\x12\x0f\n\x0bSOLID_WHITE\x10\x04\x12\x11\n\rDOUBLE_YELLOW\x10\x05\x12\x08\n\x04\x43URB\x10\x06\x12\x17\n\x13\x44OUBLE_SOLID_YELLOW\x10\x07\x12\x17\n\x13\x44OUBLE_DOTTED_WHITE\x10\x08\x12\x18\n\x14\x44OUBLE_DOTTED_YELLOW\x10\t\x12\x16\n\x12\x44OUBLE_SOLID_WHITE\x10\n\x12\x18\n\x14\x44OUBLE_LEFT_TO_RIGHT\x10\x0b\x12\x18\n\x14\x44OUBLE_RIGHT_TO_LEFT\x10\x0c\x12\x13\n\x0fPEDESTRIAN_POLE\x10\r\x12\x1b\n\x17OTHER_PHYSICAL_OBSTACLE\x10\x0e\x12\x1f\n\x1b\x44OUBLE_LEFT_TO_RIGHT_YELLOW\x10\x0f\x12\x1f\n\x1b\x44OUBLE_RIGHT_TO_LEFT_YELLOW\x10\x10\x12\x1c\n\x18SHORT_THICK_DOTTED_WHITE\x10\x11\x12%\n!DOUBLE_LEFT_WHITE_TO_RIGHT_YELLOW\x10\x12\x12%\n!DOUBLE_RIGHT_WHITE_TO_LEFT_YELLOW\x10\x13\x12%\n!DOUBLE_LEFT_YELLOW_TO_RIGHT_WHITE\x10\x14\x12%\n!DOUBLE_RIGHT_YELLOW_TO_LEFT_WHITE\x10\x15\x12\x10\n\x0cSOLID_ORANGE\x10\x16\x12\x11\n\rDOTTED_ORANGE\x10\x17\x12\x0e\n\nSOLID_BLUE\x10\x18\x12\x0f\n\x0b\x44OTTED_BLUE\x10\x19\x12\x08\n\x04\x45\x44GE\x10\x1a\x12,\n(DOUBLE_SOLID_LEFT_YELLOW_AND_RIGHT_WHITE\x10\x1b\x12-\n)DOUBLE_DOTTED_LEFT_YELLOW_AND_RIGHT_WHITE\x10\x1c\x12,\n(DOUBLE_SOLID_LEFT_WHITE_AND_RIGHT_YELLOW\x10\x1d\x12-\n)DOUBLE_DOTTED_LEFT_WHITE_AND_RIGHT_YELLOW\x10\x1e\"\xe6\x04\n\x0cLaneBoundary\x12%\n\x05\x63urve\x18\x01 \x01(\x0b\x32\x16.deeproute.hdmap.Curve\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\x0f\n\x07virtual\x18\x03 \x01(\x08\x12\x38\n\rboundary_type\x18\x04 \x03(\x0b\x32!.deeproute.hdmap.LaneBoundaryType\x12\n\n\x02id\x18\x05 \x01(\x05\x12,\n\x08\x62oundary\x18\x06 \x01(\x0b\x32\x1a.deeproute.common.Polyline\x12:\n\tcrossable\x18\x07 \x01(\x0e\x32\'.deeproute.hdmap.LaneBoundary.Crossable\x12\x0c\n\x04\x63ost\x18\x08 \x01(\x01\x12\x0e\n\x06layers\x18\t \x03(\x05\x12\x34\n\x04type\x18\n \x01(\x0e\x32&.deeproute.hdmap.LaneBoundaryType.Type\x12\x41\n\x14\x64otted_line_geometry\x18\x0b \x01(\x0b\x32#.deeproute.hdmap.DottedLineGeometry\x12%\n\x1dhas_left_deceleration_marking\x18\x0c \x01(\x08\x12&\n\x1ehas_right_deceleration_marking\x18\r \x01(\x08\"x\n\tCrossable\x12\x12\n\x0ePHYSICALLY_NOT\x10\x00\x12\x0f\n\x0bLEGALLY_NOT\x10\x01\x12\x11\n\rRIGHT_TO_LEFT\x10\x02\x12\x11\n\rLEFT_TO_RIGHT\x10\x03\x12\x08\n\x04\x42OTH\x10\x04\x12\x16\n\x12\x43\x41R_PHYSICALLY_NOT\x10\x05\"1\n\x15LaneSampleAssociation\x12\t\n\x01s\x18\x01 \x01(\x01\x12\r\n\x05width\x18\x02 \x01(\x01\"d\n\x08\x45ntrance\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07lane_id\x18\x02 \x01(\x05\x12+\n\x08location\x18\x03 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x0e\n\x06layers\x18\x04 \x03(\x05\"9\n\x04Rule\x12\x15\n\x0bspeed_limit\x18\x01 \x01(\x02H\x00\x12\x12\n\x08\x64isabled\x18\x02 \x01(\x08H\x00\x42\x06\n\x04rule\"&\n\x07Trigger\x12\x10\n\x06\x61lways\x18\x01 \x01(\x08H\x00\x42\t\n\x07trigger\"\xc4\x01\n\x08LaneRule\x12;\n\x0cvehicle_type\x18\x01 \x01(\x0e\x32%.deeproute.hdmap.LaneRule.VehicleType\x12)\n\x07trigger\x18\x02 \x01(\x0b\x32\x18.deeproute.hdmap.Trigger\x12#\n\x04rule\x18\x03 \x01(\x0b\x32\x15.deeproute.hdmap.Rule\"+\n\x0bVehicleType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0f\n\x0bLIGHT_TRUCK\x10\x01\"\xdb\x02\n\nMergeSplit\x12\x32\n\x05merge\x18\x01 \x01(\x0b\x32!.deeproute.hdmap.MergeSplit.MergeH\x00\x12\x32\n\x05split\x18\x02 \x01(\x0b\x32!.deeproute.hdmap.MergeSplit.SplitH\x00\x1aU\n\x05Merge\x12\x38\n\tdirection\x18\x01 \x01(\x0e\x32%.deeproute.hdmap.MergeSplit.Direction\x12\x12\n\nto_lane_id\x18\x02 \x01(\x05\x1aW\n\x05Split\x12\x38\n\tdirection\x18\x01 \x01(\x0e\x32%.deeproute.hdmap.MergeSplit.Direction\x12\x14\n\x0c\x66rom_lane_id\x18\x02 \x01(\x05\"-\n\tDirection\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\x42\x06\n\x04type\"\xa5\x01\n\rNeighborMerge\x12\x41\n\x13merge_from_lane_ids\x18\x01 \x01(\x0b\x32\".deeproute.hdmap.NeighborMerge.IdsH\x00\x12\x1a\n\x10merge_to_lane_id\x18\x02 \x01(\x05H\x00\x12\x19\n\x11successor_lane_id\x18\x03 \x01(\x05\x1a\x12\n\x03Ids\x12\x0b\n\x03ids\x18\x01 \x03(\x05\x42\x06\n\x04type\"\xff\x15\n\x04Lane\x12\n\n\x02id\x18\x01 \x01(\x05\x12-\n\rcentral_curve\x18\x02 \x01(\x0b\x32\x16.deeproute.hdmap.Curve\x12\x34\n\rleft_boundary\x18\x03 \x01(\x0b\x32\x1d.deeproute.hdmap.LaneBoundary\x12\x35\n\x0eright_boundary\x18\x04 \x01(\x0b\x32\x1d.deeproute.hdmap.LaneBoundary\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\x1f\n\x0bspeed_limit\x18\x06 \x01(\x02:\n11.1111107\x12\x12\n\noverlap_id\x18\x07 \x03(\x05\x12\x16\n\x0epredecessor_id\x18\x08 \x03(\x05\x12\x14\n\x0csuccessor_id\x18\t \x03(\x05\x12%\n\x1dleft_neighbor_forward_lane_id\x18\n \x01(\x05\x12&\n\x1eright_neighbor_forward_lane_id\x18\x0b \x01(\x05\x12,\n\x04type\x18\x0c \x01(\x0e\x32\x1e.deeproute.hdmap.Lane.LaneType\x12,\n\x04turn\x18\r \x01(\x0e\x32\x1e.deeproute.hdmap.Lane.LaneTurn\x12%\n\x1dleft_neighbor_reverse_lane_id\x18\x0e \x01(\x05\x12&\n\x1eright_neighbor_reverse_lane_id\x18\x0f \x01(\x05\x12\x13\n\x0bjunction_id\x18\x10 \x01(\x05\x12;\n\x0bleft_sample\x18\x11 \x03(\x0b\x32&.deeproute.hdmap.LaneSampleAssociation\x12<\n\x0cright_sample\x18\x12 \x03(\x0b\x32&.deeproute.hdmap.LaneSampleAssociation\x12\x36\n\tdirection\x18\x13 \x01(\x0e\x32#.deeproute.hdmap.Lane.LaneDirection\x12@\n\x10left_road_sample\x18\x14 \x03(\x0b\x32&.deeproute.hdmap.LaneSampleAssociation\x12\x41\n\x11right_road_sample\x18\x15 \x03(\x0b\x32&.deeproute.hdmap.LaneSampleAssociation\x12\x1c\n\x14self_reverse_lane_id\x18\x16 \x03(\x05\x12.\n\ncenterline\x18\x17 \x01(\x0b\x32\x1a.deeproute.common.Polyline\x12\x18\n\x0c\x63\x65nterline_s\x18\x18 \x03(\x02\x42\x02\x10\x01\x12\x18\n\x10left_boundary_id\x18\x19 \x01(\x05\x12\x19\n\x11right_boundary_id\x18\x1a \x01(\x05\x12\x43\n\x12\x62oundary_direction\x18\x1b \x01(\x0e\x32\'.deeproute.hdmap.Lane.BoundaryDirection\x12*\n\x08overlaps\x18\x1c \x03(\x0b\x32\x18.deeproute.hdmap.Overlap\x12\x0c\n\x04\x63ost\x18\x1d \x01(\x01\x12.\n\x05merge\x18\x1e \x01(\x0e\x32\x1f.deeproute.hdmap.Lane.MergeType\x12\x18\n\x10merge_to_lane_id\x18\x1f \x01(\x05\x12\x1a\n\x12merge_from_lane_id\x18  \x03(\x05\x12\x0e\n\x06layers\x18! \x03(\x05\x12\x19\n\x11\x62idi_copy_from_id\x18\" \x01(\x05\x12\x32\n*manually_set_left_neighbor_forward_lane_id\x18# \x01(\x05\x12\x33\n+manually_set_right_neighbor_forward_lane_id\x18$ \x01(\x05\x12\x11\n\troad_name\x18% \x03(\t\x12\x13\n\x0bis_disabled\x18& \x01(\x08\x12\x16\n\nis_virtual\x18\' \x01(\x08\x42\x02\x18\x01\x12\x19\n\x11truck_speed_limit\x18( \x01(\x02\x12\x11\n\tmin_width\x18) \x01(\x02\x12\x15\n\rmax_curvature\x18* \x01(\x02\x12\x14\n\x0cheading_diff\x18+ \x01(\x02\x12-\n\nlane_rules\x18, \x03(\x0b\x32\x19.deeproute.hdmap.LaneRule\x12\x1e\n\x16left_boundary_plus_ids\x18- \x03(\x05\x12\x1f\n\x17right_boundary_plus_ids\x18. \x03(\x05\x12\x31\n\x0cmerge_splits\x18/ \x03(\x0b\x32\x1b.deeproute.hdmap.MergeSplit\x12\x18\n\x10road_section_ids\x18\x30 \x03(\x05\x12\x37\n\x0fneighbor_merges\x18\x31 \x03(\x0b\x32\x1e.deeproute.hdmap.NeighborMerge\x12(\n\x1cmanually_set_predecessor_ids\x18\x32 \x03(\x05\x42\x02\x18\x01\x12&\n\x1amanually_set_successor_ids\x18\x33 \x03(\x05\x42\x02\x18\x01\x12\x15\n\rnext_lane_ids\x18\x34 \x03(\x05\x12\x15\n\rlast_lane_ids\x18\x35 \x03(\x05\x12\x33\n\nslope_type\x18\x36 \x01(\x0e\x32\x1f.deeproute.hdmap.Lane.SlopeType\x12-\n\x05types\x18\x37 \x03(\x0e\x32\x1e.deeproute.hdmap.Lane.LaneType\x12-\n\x05turns\x18\x38 \x03(\x0e\x32\x1e.deeproute.hdmap.Lane.LaneTurn\x12\x12\n\nlink_index\x18\x39 \x01(\x05\x12\x1b\n\x13turns_from_group_id\x18: \x01(\x05\"\xda\x02\n\x08LaneType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07HIGHWAY\x10\x01\x12\n\n\x06STREET\x10\x02\x12\x11\n\rBIDIRECTIONAL\x10\x03\x12\x0c\n\x08SHOULDER\x10\x04\x12\n\n\x06\x42IKING\x10\x05\x12\x0c\n\x08SIDEWALK\x10\x06\x12\x0e\n\nRESTRICTED\x10\x07\x12\x0b\n\x07PARKING\x10\x08\x12\x0c\n\x08ROADWORK\x10\t\x12\x0b\n\x07OFFRAMP\x10\n\x12\n\n\x06ONRAMP\x10\x0b\x12\x0b\n\x07\x42USLANE\x10\x0c\x12\x17\n\x13LEFTTURNWAITINGAREA\x10\r\x12\x08\n\x04PARK\x10\x0e\x12\x0e\n\nROUNDABOUT\x10\x0f\x12\x13\n\x0fRIGHT_TURN_ONLY\x10\x10\x12\x10\n\x0cPARK_ON_LANE\x10\x11\x12\x10\n\x0c\x44YNAMIC_LANE\x10\x12\x12\r\n\tWIDE_LANE\x10\x13\x12\x0e\n\nTIDAL_LANE\x10\x14\x12\x11\n\rTRANSFER_LANE\x10\x15\"]\n\x08LaneTurn\x12\x0b\n\x07INVALID\x10\x00\x12\x0c\n\x08STRAIGHT\x10\x01\x12\x08\n\x04LEFT\x10\x02\x12\t\n\x05RIGHT\x10\x04\x12\x0f\n\x0bU_TURN_LEFT\x10\x08\x12\x10\n\x0cU_TURN_RIGHT\x10\x10\";\n\rLaneDirection\x12\x0b\n\x07\x46ORWARD\x10\x01\x12\x0c\n\x08\x42\x41\x43KWARD\x10\x02\x12\x0f\n\x0b\x42IDIRECTION\x10\x03\"T\n\x11\x42oundaryDirection\x12\x08\n\x04SAME\x10\x00\x12\x10\n\x0cLEFT_REVERSE\x10\x01\x12\x11\n\rRIGHT_REVERSE\x10\x02\x12\x10\n\x0c\x42OTH_REVERSE\x10\x03\"4\n\tMergeType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tFROM_LEFT\x10\x01\x12\x0e\n\nFROM_RIGHT\x10\x02\"%\n\tSlopeType\x12\n\n\x06UPHILL\x10\x01\x12\x0c\n\x08\x44OWNHILL\x10\x02')



_LANEBOUNDARYTYPE = DESCRIPTOR.message_types_by_name['LaneBoundaryType']
_LANEBOUNDARY = DESCRIPTOR.message_types_by_name['LaneBoundary']
_LANESAMPLEASSOCIATION = DESCRIPTOR.message_types_by_name['LaneSampleAssociation']
_ENTRANCE = DESCRIPTOR.message_types_by_name['Entrance']
_RULE = DESCRIPTOR.message_types_by_name['Rule']
_TRIGGER = DESCRIPTOR.message_types_by_name['Trigger']
_LANERULE = DESCRIPTOR.message_types_by_name['LaneRule']
_MERGESPLIT = DESCRIPTOR.message_types_by_name['MergeSplit']
_MERGESPLIT_MERGE = _MERGESPLIT.nested_types_by_name['Merge']
_MERGESPLIT_SPLIT = _MERGESPLIT.nested_types_by_name['Split']
_NEIGHBORMERGE = DESCRIPTOR.message_types_by_name['NeighborMerge']
_NEIGHBORMERGE_IDS = _NEIGHBORMERGE.nested_types_by_name['Ids']
_LANE = DESCRIPTOR.message_types_by_name['Lane']
_LANEBOUNDARYTYPE_TYPE = _LANEBOUNDARYTYPE.enum_types_by_name['Type']
_LANEBOUNDARY_CROSSABLE = _LANEBOUNDARY.enum_types_by_name['Crossable']
_LANERULE_VEHICLETYPE = _LANERULE.enum_types_by_name['VehicleType']
_MERGESPLIT_DIRECTION = _MERGESPLIT.enum_types_by_name['Direction']
_LANE_LANETYPE = _LANE.enum_types_by_name['LaneType']
_LANE_LANETURN = _LANE.enum_types_by_name['LaneTurn']
_LANE_LANEDIRECTION = _LANE.enum_types_by_name['LaneDirection']
_LANE_BOUNDARYDIRECTION = _LANE.enum_types_by_name['BoundaryDirection']
_LANE_MERGETYPE = _LANE.enum_types_by_name['MergeType']
_LANE_SLOPETYPE = _LANE.enum_types_by_name['SlopeType']
LaneBoundaryType = _reflection.GeneratedProtocolMessageType('LaneBoundaryType', (_message.Message,), {
  'DESCRIPTOR' : _LANEBOUNDARYTYPE,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.LaneBoundaryType)
  })
_sym_db.RegisterMessage(LaneBoundaryType)

LaneBoundary = _reflection.GeneratedProtocolMessageType('LaneBoundary', (_message.Message,), {
  'DESCRIPTOR' : _LANEBOUNDARY,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.LaneBoundary)
  })
_sym_db.RegisterMessage(LaneBoundary)

LaneSampleAssociation = _reflection.GeneratedProtocolMessageType('LaneSampleAssociation', (_message.Message,), {
  'DESCRIPTOR' : _LANESAMPLEASSOCIATION,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.LaneSampleAssociation)
  })
_sym_db.RegisterMessage(LaneSampleAssociation)

Entrance = _reflection.GeneratedProtocolMessageType('Entrance', (_message.Message,), {
  'DESCRIPTOR' : _ENTRANCE,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.Entrance)
  })
_sym_db.RegisterMessage(Entrance)

Rule = _reflection.GeneratedProtocolMessageType('Rule', (_message.Message,), {
  'DESCRIPTOR' : _RULE,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.Rule)
  })
_sym_db.RegisterMessage(Rule)

Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGER,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.Trigger)
  })
_sym_db.RegisterMessage(Trigger)

LaneRule = _reflection.GeneratedProtocolMessageType('LaneRule', (_message.Message,), {
  'DESCRIPTOR' : _LANERULE,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.LaneRule)
  })
_sym_db.RegisterMessage(LaneRule)

MergeSplit = _reflection.GeneratedProtocolMessageType('MergeSplit', (_message.Message,), {

  'Merge' : _reflection.GeneratedProtocolMessageType('Merge', (_message.Message,), {
    'DESCRIPTOR' : _MERGESPLIT_MERGE,
    '__module__' : 'semantic_map.map_lane_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.MergeSplit.Merge)
    })
  ,

  'Split' : _reflection.GeneratedProtocolMessageType('Split', (_message.Message,), {
    'DESCRIPTOR' : _MERGESPLIT_SPLIT,
    '__module__' : 'semantic_map.map_lane_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.MergeSplit.Split)
    })
  ,
  'DESCRIPTOR' : _MERGESPLIT,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.MergeSplit)
  })
_sym_db.RegisterMessage(MergeSplit)
_sym_db.RegisterMessage(MergeSplit.Merge)
_sym_db.RegisterMessage(MergeSplit.Split)

NeighborMerge = _reflection.GeneratedProtocolMessageType('NeighborMerge', (_message.Message,), {

  'Ids' : _reflection.GeneratedProtocolMessageType('Ids', (_message.Message,), {
    'DESCRIPTOR' : _NEIGHBORMERGE_IDS,
    '__module__' : 'semantic_map.map_lane_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.NeighborMerge.Ids)
    })
  ,
  'DESCRIPTOR' : _NEIGHBORMERGE,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.NeighborMerge)
  })
_sym_db.RegisterMessage(NeighborMerge)
_sym_db.RegisterMessage(NeighborMerge.Ids)

Lane = _reflection.GeneratedProtocolMessageType('Lane', (_message.Message,), {
  'DESCRIPTOR' : _LANE,
  '__module__' : 'semantic_map.map_lane_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.Lane)
  })
_sym_db.RegisterMessage(Lane)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LANE.fields_by_name['centerline_s']._options = None
  _LANE.fields_by_name['centerline_s']._serialized_options = b'\020\001'
  _LANE.fields_by_name['is_virtual']._options = None
  _LANE.fields_by_name['is_virtual']._serialized_options = b'\030\001'
  _LANE.fields_by_name['manually_set_predecessor_ids']._options = None
  _LANE.fields_by_name['manually_set_predecessor_ids']._serialized_options = b'\030\001'
  _LANE.fields_by_name['manually_set_successor_ids']._options = None
  _LANE.fields_by_name['manually_set_successor_ids']._serialized_options = b'\030\001'
  _LANEBOUNDARYTYPE._serialized_start=137
  _LANEBOUNDARYTYPE._serialized_end=1064
  _LANEBOUNDARYTYPE_TYPE._serialized_start=224
  _LANEBOUNDARYTYPE_TYPE._serialized_end=1064
  _LANEBOUNDARY._serialized_start=1067
  _LANEBOUNDARY._serialized_end=1681
  _LANEBOUNDARY_CROSSABLE._serialized_start=1561
  _LANEBOUNDARY_CROSSABLE._serialized_end=1681
  _LANESAMPLEASSOCIATION._serialized_start=1683
  _LANESAMPLEASSOCIATION._serialized_end=1732
  _ENTRANCE._serialized_start=1734
  _ENTRANCE._serialized_end=1834
  _RULE._serialized_start=1836
  _RULE._serialized_end=1893
  _TRIGGER._serialized_start=1895
  _TRIGGER._serialized_end=1933
  _LANERULE._serialized_start=1936
  _LANERULE._serialized_end=2132
  _LANERULE_VEHICLETYPE._serialized_start=2089
  _LANERULE_VEHICLETYPE._serialized_end=2132
  _MERGESPLIT._serialized_start=2135
  _MERGESPLIT._serialized_end=2482
  _MERGESPLIT_MERGE._serialized_start=2253
  _MERGESPLIT_MERGE._serialized_end=2338
  _MERGESPLIT_SPLIT._serialized_start=2340
  _MERGESPLIT_SPLIT._serialized_end=2427
  _MERGESPLIT_DIRECTION._serialized_start=2429
  _MERGESPLIT_DIRECTION._serialized_end=2474
  _NEIGHBORMERGE._serialized_start=2485
  _NEIGHBORMERGE._serialized_end=2650
  _NEIGHBORMERGE_IDS._serialized_start=2624
  _NEIGHBORMERGE_IDS._serialized_end=2642
  _LANE._serialized_start=2653
  _LANE._serialized_end=5468
  _LANE_LANETYPE._serialized_start=4787
  _LANE_LANETYPE._serialized_end=5133
  _LANE_LANETURN._serialized_start=5135
  _LANE_LANETURN._serialized_end=5228
  _LANE_LANEDIRECTION._serialized_start=5230
  _LANE_LANEDIRECTION._serialized_end=5289
  _LANE_BOUNDARYDIRECTION._serialized_start=5291
  _LANE_BOUNDARYDIRECTION._serialized_end=5375
  _LANE_MERGETYPE._serialized_start=5377
  _LANE_MERGETYPE._serialized_end=5429
  _LANE_SLOPETYPE._serialized_start=5431
  _LANE_SLOPETYPE._serialized_end=5468
# @@protoc_insertion_point(module_scope)
