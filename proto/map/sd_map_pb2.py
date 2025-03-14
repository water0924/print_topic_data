# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map/sd_map.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import geometry_pb2 as common_dot_geometry__pb2
from proto.map import common_type_pb2 as map_dot_common__type__pb2
from proto.map import sd_map_type_pb2 as map_dot_sd__map__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10map/sd_map.proto\x12\x10\x64\x65\x65proute.sd_map\x1a\x15\x63ommon/geometry.proto\x1a\x15map/common_type.proto\x1a\x15map/sd_map_type.proto\"\x9a\x01\n\x08LaneCond\x12\x15\n\rlaneinfo_cond\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12/\n\x08vehicles\x18\x04 \x03(\x0e\x32\x1d.deeproute.sd_map.VehicleType\x12\x38\n\rspecial_times\x18\x05 \x03(\x0e\x32!.deeproute.sd_map.SpecialTimeType\"\xc0\x01\n\x08LaneData\x12\r\n\x05\x61rrow\x18\x01 \x01(\r\x12\x0e\n\x06\x62itmap\x18\x02 \x01(\r\x12\x12\n\nbus_bitmap\x18\x03 \x01(\r\x12\x10\n\x08left_add\x18\x04 \x01(\x03\x12\x11\n\tright_add\x18\x05 \x01(\x03\x12\x13\n\x0blane_number\x18\x06 \x01(\x04\x12\x17\n\x0fout_dr_link_ids\x18\x07 \x03(\x04\x12.\n\nlane_conds\x18\x08 \x03(\x0b\x32\x1a.deeproute.sd_map.LaneCond\"/\n\x0cLaneTimeSpan\x12\r\n\x05index\x18\x01 \x01(\r\x12\x10\n\x08timespan\x18\x02 \x01(\t\"e\n\x10\x43onnectivityData\x12\x11\n\tforbidden\x18\x01 \x01(\x08\x12\x1b\n\x13\x64irected_dr_link_id\x18\x02 \x01(\x04\x12!\n\x19pass_directed_dr_link_ids\x18\x03 \x03(\x04\"\x83\x02\n\x08LaneAttr\x12J\n\x14lane_extension_types\x18\x01 \x03(\x0e\x32,.deeproute.sd_map.LaneAttr.LaneExtensionType\x12\'\n\x06\x61rrows\x18\x02 \x03(\x0e\x32\x17.deeproute.sd_map.Arrow\"\x81\x01\n\x11LaneExtensionType\x12\x19\n\x15LANE_EXTENSION_NORMAL\x10\x00\x12\x16\n\x12LANE_EXTENSION_BUS\x10\x01\x12\x17\n\x13LANE_EXTENSION_TIDE\x10\x02\x12 \n\x1cLANE_EXTENSION_TURNALTERABLE\x10\x03\"\x8c\x02\n\x11SpecLaneAttribute\x12\r\n\x05index\x18\x01 \x01(\x05\x12V\n\x13lane_extension_type\x18\x02 \x01(\x0e\x32\x39.deeproute.sd_map.SpecLaneAttribute.SpecLaneExtensionType\"\x8f\x01\n\x15SpecLaneExtensionType\x12\x1e\n\x1aSPEC_LANE_EXTENSION_NORMAL\x10\x00\x12)\n%SPEC_LANE_EXTENSION_BICYCLE_LANE_ROAD\x10\x01\x12+\n\'SPEC_LANE_EXTENSION_EMERGENCY_LANE_ROAD\x10\x02\"\x89\x01\n\x0cLaneInfoData\x12\x1c\n\x14lane_left_change_num\x18\x02 \x01(\x05\x12\x1d\n\x15lane_right_change_num\x18\x03 \x01(\x05\x12<\n\x0flane_attributes\x18\x04 \x03(\x0b\x32#.deeproute.sd_map.SpecLaneAttribute\"v\n\x06\x43\x61mera\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.deeproute.map.CameraType\x12.\n\ncoordinate\x18\x02 \x01(\x0b\x32\x1a.deeproute.common.PointLLH\x12\x13\n\x0bspeed_limit\x18\x03 \x01(\x05\"\xf4\x15\n\x08LinkData\x12\x14\n\x0cshape_points\x18\x03 \x01(\t\x12\x12\n\ndr_link_id\x18\x01 \x01(\x04\x12\x12\n\nnavinfo_id\x18\x13 \x01(\x04\x12\x0e\n\x06raw_id\x18\x1d \x01(\x04\x12\x0f\n\x07\x66orward\x18\x14 \x01(\x08\x12\x0e\n\x06length\x18\x02 \x01(\r\x12\x15\n\rtraffic_light\x18\x04 \x01(\x08\x12\x13\n\x0bspeed_limit\x18\x05 \x01(\r\x12\x18\n\x10\x66orward_lane_num\x18\x06 \x01(\r\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x10\n\x08priority\x18\x08 \x01(\r\x12)\n\x05lanes\x18\t \x03(\x0b\x32\x1a.deeproute.sd_map.LaneData\x12\x1e\n\x16reversible_lane_bitmap\x18\n \x01(\r\x12!\n\x19variable_turn_lane_bitmap\x18\x0b \x01(\r\x12#\n\x1b\x63onditional_bus_lane_bitmap\x18\x0c \x01(\r\x12\x46\n\x1e\x63onditional_bus_lane_timespans\x18\r \x03(\x0b\x32\x1e.deeproute.sd_map.LaneTimeSpan\x12\x41\n\x19reversible_lane_timespans\x18\x0e \x03(\x0b\x32\x1e.deeproute.sd_map.LaneTimeSpan\x12\r\n\x05usage\x18\x0f \x01(\r\x12\x34\n\x08\x66ormways\x18\x17 \x03(\x0e\x32\".deeproute.sd_map.LinkData.FormWay\x12\x0e\n\x06tunnel\x18\x10 \x01(\x08\x12\x39\n\rin_links_data\x18\x11 \x03(\x0b\x32\".deeproute.sd_map.ConnectivityData\x12:\n\x0eout_links_data\x18\x12 \x03(\x0b\x32\".deeproute.sd_map.ConnectivityData\x12\x10\n\x08\x65levated\x18\x15 \x01(\x08\x12\"\n\x1atoll_station_at_link_start\x18\x16 \x01(\x08\x12.\n\nlane_attrs\x18\x18 \x03(\x0b\x32\x1a.deeproute.sd_map.LaneAttr\x12\x15\n\rstart_node_id\x18\x19 \x01(\x04\x12\x13\n\x0b\x65nd_node_id\x18\x1a \x01(\x04\x12\x14\n\x0cmain_node_id\x18\x1b \x01(\x04\x12\x0f\n\x07tile_id\x18\x1c \x01(\r\x12\x1e\n\x16\x65xperience_speed_limit\x18\x1e \x01(\r\x12\x12\n\nadmin_code\x18\x1f \x01(\x05\x12\x36\n\x0elane_info_data\x18  \x01(\x0b\x32\x1e.deeproute.sd_map.LaneInfoData\x12\x19\n\x11\x65xact_speed_limit\x18! \x01(\r\x12(\n\x06\x63\x61mera\x18\" \x03(\x0b\x32\x18.deeproute.sd_map.Camera\x12*\n\x06points\x18\x65 \x03(\x0b\x32\x1a.deeproute.common.PointLLH\x12+\n\x08points2d\x18\x66 \x03(\x0b\x32\x19.deeproute.common.Point2D\"\xe5\x0c\n\x07\x46ormWay\x12\x12\n\x0eROAD_KIND_NONE\x10\x00\x12\x18\n\x14ROAD_KIND_ROUNDABOUT\x10\x01\x12\x1c\n\x18ROAD_KIND_DIRECTION_SPIT\x10\x02\x12\x11\n\rROAD_KIND_JCT\x10\x03\x12\x19\n\x15ROAD_KIND_CROSS_INNER\x10\x04\x12\x10\n\x0cROAD_KIND_IC\x10\x05\x12\x10\n\x0cROAD_KIND_PA\x10\x06\x12\x10\n\x0cROAD_KIND_SA\x10\x07\x12\x19\n\x15ROAD_KIND_WALK_STREET\x10\x08\x12\x17\n\x13ROAD_KIND_SECONDARY\x10\t\x12\x12\n\x0eROAD_KIND_RAMP\x10\n\x12\x19\n\x15ROAD_KIND_POI_CONNECT\x10\x0b\x12\x14\n\x10ROAD_KIND_TUNNEL\x10\x0c\x12\x18\n\x14ROAD_KIND_RIGHT_TURN\x10\r\x12\x1a\n\x16ROAD_KIND_INNER_REGION\x10\x0e\x12\x17\n\x13ROAD_KIND_LEFT_TURN\x10\x0f\x12\x14\n\x10ROAD_KIND_U_TURN\x10\x10\x12%\n!ROAD_KIND_MAIN_SECONDARY_ENTRANCE\x10\x11\x12\x1b\n\x17ROAD_KIND_REVERSAL_LEFT\x10\x12\x12\x17\n\x13ROAD_KIND_MAIN_ROAD\x10\x13\x12\x16\n\x12ROAD_KIND_ELEVATED\x10\x14\x12\x12\n\x0eROAD_KIND_TOLL\x10\x15\x12\x1a\n\x16ROAD_KIND_HIGHWAY_PORT\x10\x16\x12\x1e\n\x1aROAD_KIND_AHEAD_TURN_RIGHT\x10\x17\x12\x17\n\x13ROAD_KIND_WIDE_LANE\x10\x18\x12\x17\n\x13ROAD_KIND_BIKE_LANE\x10\x19\x12\x16\n\x12ROAD_KIND_SHOULDER\x10\x1a\x12!\n\x1dROAD_KIND_CROSS_LINE_OVERPASS\x10\x1d\x12\x19\n\x15ROAD_KIND_SUNKEN_ROAD\x10\x1e\x12\x14\n\x10ROAD_KIND_BRIDGE\x10\x1f\x12\x17\n\x13ROAD_KIND_ENCLOSURE\x10 \x12\x17\n\x13ROAD_KIND_UNDEFINED\x10!\x12\x11\n\rROAD_KIND_BUS\x10\"\x12\x12\n\x0eROAD_KIND_VIEW\x10#\x12\x1b\n\x17ROAD_KIND_PARK_ENTRANCE\x10$\x12\x1c\n\x18ROAD_KIND_MOVABLE_BRIDGE\x10%\x12\x18\n\x14ROAD_KIND_FRONT_DOOR\x10&\x12\x18\n\x14ROAD_KIND_TRUCK_LANE\x10\'\x12\x14\n\x10ROAD_KIND_NORMAL\x10(\x12\x1a\n\x16ROAD_KIND_CONSTRUCTION\x10)\x12\x1a\n\x16ROAD_KIND_INTERSECTION\x10*\x12 \n\x1cROAD_KIND_HIGHWAY_CONNECTION\x10+\x12$\n ROAD_KIND_NONSTANDARD_ROUNDABOUT\x10,\x12 \n\x1cROAD_KIND_SPECIAL_CONNECTION\x10-\x12!\n\x1dROAD_KIND_PARKING_OCCUPY_ROAD\x10.\x12\x17\n\x13ROAD_KIND_OWNERSHIP\x10/\x12#\n\x1fROAD_KIND_INNER_VIRTUAL_CONNECT\x10\x30\x12\x12\n\x0eROAD_KIND_TAXI\x10\x31\x12\x12\n\x0eROAD_KIND_TIDE\x10\x32\x12\x17\n\x13ROAD_KIND_STEP_ROAD\x10\x33\x12\x1e\n\x1aROAD_KIND_INNER_CROSS_ROAD\x10\x34\x12\'\n#ROAD_KIND_ENTRANCE_AND_EXIT_CONNECT\x10\x35\x12\x1c\n\x18ROAD_KIND_RAMP_BOTH_PASS\x10\x36\x12\x1b\n\x17ROAD_KIND_MOUNTAIN_ROAD\x10\x37\x12\x1e\n\x1aROAD_KIND_SUNKEN_ROAD_PORT\x10\x38\x12\x13\n\x0fROAD_KIND_OTHER\x10\x39\x12&\n\"ROAD_KIND_VIRTUAL_SOLID_CONNECTION\x10:\x12#\n\x1fROAD_KIND_PARKING_INTERNAL_ROAD\x10;\x12 \n\x1cROAD_KIND_ENTER_SINGLE_CROSS\x10\x1b\x12\x1f\n\x1bROAD_KIND_ENTER_MULTI_CROSS\x10\x1c\"\xab\x01\n\x07SdLinks\x12\x33\n\nlink_frame\x18\x01 \x01(\x0e\x32\x1f.deeproute.sd_map.SdLinks.Frame\x12)\n\x05links\x18\x02 \x03(\x0b\x32\x1a.deeproute.sd_map.LinkData\"@\n\x05\x46rame\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05WGS84\x10\x01\x12\t\n\x05GCJ02\x10\x02\x12\x07\n\x03UTM\x10\x03\x12\x0b\n\x07VEHICLE\x10\x04\"\xb6\x01\n\x05SDMap\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.deeproute.sd_map.SDMap.Header\x12)\n\x05links\x18\x02 \x03(\x0b\x32\x1a.deeproute.sd_map.LinkData\x12\x1d\n\x15not_found_dr_link_ids\x18\x03 \x03(\x04\x1a\x33\n\x06Header\x12\x13\n\x0bmap_version\x18\x01 \x01(\t\x12\x14\n\x0crelease_date\x18\x02 \x01(\t\"C\n\x0cSDMapOnboard\x12\n\n\x02id\x18\x01 \x01(\x05\x12\'\n\x06sd_map\x18\x02 \x01(\x0b\x32\x17.deeproute.sd_map.SDMap\"\x9f\t\n\x13SDMapVersionOnboard\x12\x1b\n\x13sd_map_plus_version\x18\x01 \x01(\t\x12R\n\x12tencent_sd_version\x18\x02 \x01(\x0b\x32\x36.deeproute.sd_map.SDMapVersionOnboard.TencentSDVersion\x12Q\n\x11transfer_protocol\x18\x03 \x01(\x0e\x32\x36.deeproute.sd_map.SDMapVersionOnboard.TransferProtocol\x12K\n\x0e\x63onnect_config\x18\x04 \x03(\x0b\x32\x33.deeproute.sd_map.SDMapVersionOnboard.ConnectConfig\x12\x61\n\x1agraph_match_routing_config\x18\x05 \x01(\x0b\x32=.deeproute.sd_map.SDMapVersionOnboard.GraphMatchRoutingConfig\x12T\n\x13image_report_config\x18\x06 \x01(\x0b\x32\x37.deeproute.sd_map.SDMapVersionOnboard.ImageReportConfig\x1a\xc0\x01\n\x10TencentSDVersion\x12\\\n\x0e\x66ormat_version\x18\x01 \x01(\x0b\x32\x44.deeproute.sd_map.SDMapVersionOnboard.TencentSDVersion.FormatVersion\x12\x12\n\nversoin_id\x18\x02 \x01(\r\x1a:\n\rFormatVersion\x12\x14\n\x0cmain_version\x18\x01 \x01(\r\x12\x13\n\x0bsub_version\x18\x02 \x01(\r\x1a\x7f\n\rConnectConfig\x12\x1b\n\x13request_timeout_sec\x18\x01 \x01(\x05\x12\x1e\n\x16\x63onnection_timeout_sec\x18\x02 \x01(\x05\x12\x1b\n\x13use_long_connection\x18\x03 \x01(\x08\x12\x14\n\x0cservice_name\x18\x04 \x01(\t\x1a\x9b\x01\n\x17GraphMatchRoutingConfig\x12\x1e\n\x16\x61\x62le_segmented_routing\x18\x01 \x01(\x08\x12\x14\n\x0cpre_link_num\x18\x02 \x01(\x05\x12\x19\n\x11max_segm_distance\x18\x03 \x01(\x04\x12\x19\n\x11send_pre_polyline\x18\x04 \x01(\x08\x12\x14\n\x0cmax_segm_num\x18\x05 \x01(\x05\x1a\xb3\x01\n\x11ImageReportConfig\x12\x1b\n\x13\x65nable_for_lane_num\x18\x01 \x01(\x08\x12\x1c\n\x14\x65nable_for_lane_topo\x18\x02 \x01(\x08\x12\x1e\n\x16\x65nable_for_lane_marker\x18\x03 \x01(\x08\x12 \n\x18\x65nable_for_traffic_light\x18\x04 \x01(\x08\x12!\n\x19\x65nable_for_lane_attribute\x18\x05 \x01(\x08\"&\n\x10TransferProtocol\x12\x08\n\x04HTTP\x10\x00\x12\x08\n\x04GRPC\x10\x01*o\n\x05\x41rrow\x12\x0e\n\nARROW_NONE\x10\x00\x12\x12\n\x0e\x41RROW_STRAIGHT\x10\x01\x12\x0f\n\x0b\x41RROW_RIGHT\x10\x04\x12\x10\n\x0c\x41RROW_U_TURN\x10\x07\x12\x0e\n\nARROW_LEFT\x10\n\x12\x0f\n\x0b\x41RROW_EMPTY\x10\r')

_ARROW = DESCRIPTOR.enum_types_by_name['Arrow']
Arrow = enum_type_wrapper.EnumTypeWrapper(_ARROW)
ARROW_NONE = 0
ARROW_STRAIGHT = 1
ARROW_RIGHT = 4
ARROW_U_TURN = 7
ARROW_LEFT = 10
ARROW_EMPTY = 13


_LANECOND = DESCRIPTOR.message_types_by_name['LaneCond']
_LANEDATA = DESCRIPTOR.message_types_by_name['LaneData']
_LANETIMESPAN = DESCRIPTOR.message_types_by_name['LaneTimeSpan']
_CONNECTIVITYDATA = DESCRIPTOR.message_types_by_name['ConnectivityData']
_LANEATTR = DESCRIPTOR.message_types_by_name['LaneAttr']
_SPECLANEATTRIBUTE = DESCRIPTOR.message_types_by_name['SpecLaneAttribute']
_LANEINFODATA = DESCRIPTOR.message_types_by_name['LaneInfoData']
_CAMERA = DESCRIPTOR.message_types_by_name['Camera']
_LINKDATA = DESCRIPTOR.message_types_by_name['LinkData']
_SDLINKS = DESCRIPTOR.message_types_by_name['SdLinks']
_SDMAP = DESCRIPTOR.message_types_by_name['SDMap']
_SDMAP_HEADER = _SDMAP.nested_types_by_name['Header']
_SDMAPONBOARD = DESCRIPTOR.message_types_by_name['SDMapOnboard']
_SDMAPVERSIONONBOARD = DESCRIPTOR.message_types_by_name['SDMapVersionOnboard']
_SDMAPVERSIONONBOARD_TENCENTSDVERSION = _SDMAPVERSIONONBOARD.nested_types_by_name['TencentSDVersion']
_SDMAPVERSIONONBOARD_TENCENTSDVERSION_FORMATVERSION = _SDMAPVERSIONONBOARD_TENCENTSDVERSION.nested_types_by_name['FormatVersion']
_SDMAPVERSIONONBOARD_CONNECTCONFIG = _SDMAPVERSIONONBOARD.nested_types_by_name['ConnectConfig']
_SDMAPVERSIONONBOARD_GRAPHMATCHROUTINGCONFIG = _SDMAPVERSIONONBOARD.nested_types_by_name['GraphMatchRoutingConfig']
_SDMAPVERSIONONBOARD_IMAGEREPORTCONFIG = _SDMAPVERSIONONBOARD.nested_types_by_name['ImageReportConfig']
_LANEATTR_LANEEXTENSIONTYPE = _LANEATTR.enum_types_by_name['LaneExtensionType']
_SPECLANEATTRIBUTE_SPECLANEEXTENSIONTYPE = _SPECLANEATTRIBUTE.enum_types_by_name['SpecLaneExtensionType']
_LINKDATA_FORMWAY = _LINKDATA.enum_types_by_name['FormWay']
_SDLINKS_FRAME = _SDLINKS.enum_types_by_name['Frame']
_SDMAPVERSIONONBOARD_TRANSFERPROTOCOL = _SDMAPVERSIONONBOARD.enum_types_by_name['TransferProtocol']
LaneCond = _reflection.GeneratedProtocolMessageType('LaneCond', (_message.Message,), {
  'DESCRIPTOR' : _LANECOND,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.LaneCond)
  })
_sym_db.RegisterMessage(LaneCond)

LaneData = _reflection.GeneratedProtocolMessageType('LaneData', (_message.Message,), {
  'DESCRIPTOR' : _LANEDATA,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.LaneData)
  })
_sym_db.RegisterMessage(LaneData)

LaneTimeSpan = _reflection.GeneratedProtocolMessageType('LaneTimeSpan', (_message.Message,), {
  'DESCRIPTOR' : _LANETIMESPAN,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.LaneTimeSpan)
  })
_sym_db.RegisterMessage(LaneTimeSpan)

ConnectivityData = _reflection.GeneratedProtocolMessageType('ConnectivityData', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIVITYDATA,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.ConnectivityData)
  })
_sym_db.RegisterMessage(ConnectivityData)

LaneAttr = _reflection.GeneratedProtocolMessageType('LaneAttr', (_message.Message,), {
  'DESCRIPTOR' : _LANEATTR,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.LaneAttr)
  })
_sym_db.RegisterMessage(LaneAttr)

SpecLaneAttribute = _reflection.GeneratedProtocolMessageType('SpecLaneAttribute', (_message.Message,), {
  'DESCRIPTOR' : _SPECLANEATTRIBUTE,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.SpecLaneAttribute)
  })
_sym_db.RegisterMessage(SpecLaneAttribute)

LaneInfoData = _reflection.GeneratedProtocolMessageType('LaneInfoData', (_message.Message,), {
  'DESCRIPTOR' : _LANEINFODATA,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.LaneInfoData)
  })
_sym_db.RegisterMessage(LaneInfoData)

Camera = _reflection.GeneratedProtocolMessageType('Camera', (_message.Message,), {
  'DESCRIPTOR' : _CAMERA,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.Camera)
  })
_sym_db.RegisterMessage(Camera)

LinkData = _reflection.GeneratedProtocolMessageType('LinkData', (_message.Message,), {
  'DESCRIPTOR' : _LINKDATA,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.LinkData)
  })
_sym_db.RegisterMessage(LinkData)

SdLinks = _reflection.GeneratedProtocolMessageType('SdLinks', (_message.Message,), {
  'DESCRIPTOR' : _SDLINKS,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.SdLinks)
  })
_sym_db.RegisterMessage(SdLinks)

SDMap = _reflection.GeneratedProtocolMessageType('SDMap', (_message.Message,), {

  'Header' : _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR' : _SDMAP_HEADER,
    '__module__' : 'map.sd_map_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.sd_map.SDMap.Header)
    })
  ,
  'DESCRIPTOR' : _SDMAP,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.SDMap)
  })
_sym_db.RegisterMessage(SDMap)
_sym_db.RegisterMessage(SDMap.Header)

SDMapOnboard = _reflection.GeneratedProtocolMessageType('SDMapOnboard', (_message.Message,), {
  'DESCRIPTOR' : _SDMAPONBOARD,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.SDMapOnboard)
  })
_sym_db.RegisterMessage(SDMapOnboard)

SDMapVersionOnboard = _reflection.GeneratedProtocolMessageType('SDMapVersionOnboard', (_message.Message,), {

  'TencentSDVersion' : _reflection.GeneratedProtocolMessageType('TencentSDVersion', (_message.Message,), {

    'FormatVersion' : _reflection.GeneratedProtocolMessageType('FormatVersion', (_message.Message,), {
      'DESCRIPTOR' : _SDMAPVERSIONONBOARD_TENCENTSDVERSION_FORMATVERSION,
      '__module__' : 'map.sd_map_pb2'
      # @@protoc_insertion_point(class_scope:deeproute.sd_map.SDMapVersionOnboard.TencentSDVersion.FormatVersion)
      })
    ,
    'DESCRIPTOR' : _SDMAPVERSIONONBOARD_TENCENTSDVERSION,
    '__module__' : 'map.sd_map_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.sd_map.SDMapVersionOnboard.TencentSDVersion)
    })
  ,

  'ConnectConfig' : _reflection.GeneratedProtocolMessageType('ConnectConfig', (_message.Message,), {
    'DESCRIPTOR' : _SDMAPVERSIONONBOARD_CONNECTCONFIG,
    '__module__' : 'map.sd_map_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.sd_map.SDMapVersionOnboard.ConnectConfig)
    })
  ,

  'GraphMatchRoutingConfig' : _reflection.GeneratedProtocolMessageType('GraphMatchRoutingConfig', (_message.Message,), {
    'DESCRIPTOR' : _SDMAPVERSIONONBOARD_GRAPHMATCHROUTINGCONFIG,
    '__module__' : 'map.sd_map_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.sd_map.SDMapVersionOnboard.GraphMatchRoutingConfig)
    })
  ,

  'ImageReportConfig' : _reflection.GeneratedProtocolMessageType('ImageReportConfig', (_message.Message,), {
    'DESCRIPTOR' : _SDMAPVERSIONONBOARD_IMAGEREPORTCONFIG,
    '__module__' : 'map.sd_map_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.sd_map.SDMapVersionOnboard.ImageReportConfig)
    })
  ,
  'DESCRIPTOR' : _SDMAPVERSIONONBOARD,
  '__module__' : 'map.sd_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.sd_map.SDMapVersionOnboard)
  })
_sym_db.RegisterMessage(SDMapVersionOnboard)
_sym_db.RegisterMessage(SDMapVersionOnboard.TencentSDVersion)
_sym_db.RegisterMessage(SDMapVersionOnboard.TencentSDVersion.FormatVersion)
_sym_db.RegisterMessage(SDMapVersionOnboard.ConnectConfig)
_sym_db.RegisterMessage(SDMapVersionOnboard.GraphMatchRoutingConfig)
_sym_db.RegisterMessage(SDMapVersionOnboard.ImageReportConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ARROW._serialized_start=5825
  _ARROW._serialized_end=5936
  _LANECOND._serialized_start=108
  _LANECOND._serialized_end=262
  _LANEDATA._serialized_start=265
  _LANEDATA._serialized_end=457
  _LANETIMESPAN._serialized_start=459
  _LANETIMESPAN._serialized_end=506
  _CONNECTIVITYDATA._serialized_start=508
  _CONNECTIVITYDATA._serialized_end=609
  _LANEATTR._serialized_start=612
  _LANEATTR._serialized_end=871
  _LANEATTR_LANEEXTENSIONTYPE._serialized_start=742
  _LANEATTR_LANEEXTENSIONTYPE._serialized_end=871
  _SPECLANEATTRIBUTE._serialized_start=874
  _SPECLANEATTRIBUTE._serialized_end=1142
  _SPECLANEATTRIBUTE_SPECLANEEXTENSIONTYPE._serialized_start=999
  _SPECLANEATTRIBUTE_SPECLANEEXTENSIONTYPE._serialized_end=1142
  _LANEINFODATA._serialized_start=1145
  _LANEINFODATA._serialized_end=1282
  _CAMERA._serialized_start=1284
  _CAMERA._serialized_end=1402
  _LINKDATA._serialized_start=1405
  _LINKDATA._serialized_end=4209
  _LINKDATA_FORMWAY._serialized_start=2572
  _LINKDATA_FORMWAY._serialized_end=4209
  _SDLINKS._serialized_start=4212
  _SDLINKS._serialized_end=4383
  _SDLINKS_FRAME._serialized_start=4319
  _SDLINKS_FRAME._serialized_end=4383
  _SDMAP._serialized_start=4386
  _SDMAP._serialized_end=4568
  _SDMAP_HEADER._serialized_start=4517
  _SDMAP_HEADER._serialized_end=4568
  _SDMAPONBOARD._serialized_start=4570
  _SDMAPONBOARD._serialized_end=4637
  _SDMAPVERSIONONBOARD._serialized_start=4640
  _SDMAPVERSIONONBOARD._serialized_end=5823
  _SDMAPVERSIONONBOARD_TENCENTSDVERSION._serialized_start=5122
  _SDMAPVERSIONONBOARD_TENCENTSDVERSION._serialized_end=5314
  _SDMAPVERSIONONBOARD_TENCENTSDVERSION_FORMATVERSION._serialized_start=5256
  _SDMAPVERSIONONBOARD_TENCENTSDVERSION_FORMATVERSION._serialized_end=5314
  _SDMAPVERSIONONBOARD_CONNECTCONFIG._serialized_start=5316
  _SDMAPVERSIONONBOARD_CONNECTCONFIG._serialized_end=5443
  _SDMAPVERSIONONBOARD_GRAPHMATCHROUTINGCONFIG._serialized_start=5446
  _SDMAPVERSIONONBOARD_GRAPHMATCHROUTINGCONFIG._serialized_end=5601
  _SDMAPVERSIONONBOARD_IMAGEREPORTCONFIG._serialized_start=5604
  _SDMAPVERSIONONBOARD_IMAGEREPORTCONFIG._serialized_end=5783
  _SDMAPVERSIONONBOARD_TRANSFERPROTOCOL._serialized_start=5785
  _SDMAPVERSIONONBOARD_TRANSFERPROTOCOL._serialized_end=5823
# @@protoc_insertion_point(module_scope)
