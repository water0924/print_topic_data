# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: semantic_map/map.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.semantic_map import map_clear_area_pb2 as semantic__map_dot_map__clear__area__pb2
from proto.semantic_map import map_crosswalk_pb2 as semantic__map_dot_map__crosswalk__pb2
from proto.semantic_map import map_diversion_area_pb2 as semantic__map_dot_map__diversion__area__pb2
from proto.semantic_map import map_junction_pb2 as semantic__map_dot_map__junction__pb2
from proto.semantic_map import map_lane_pb2 as semantic__map_dot_map__lane__pb2
from proto.semantic_map import map_overlap_pb2 as semantic__map_dot_map__overlap__pb2
from proto.semantic_map import map_signal_pb2 as semantic__map_dot_map__signal__pb2
from proto.semantic_map import map_speed_bump_pb2 as semantic__map_dot_map__speed__bump__pb2
from proto.semantic_map import map_stop_sign_pb2 as semantic__map_dot_map__stop__sign__pb2
from proto.semantic_map import map_yield_sign_pb2 as semantic__map_dot_map__yield__sign__pb2
from proto.semantic_map import map_road_pb2 as semantic__map_dot_map__road__pb2
from proto.semantic_map import map_parking_space_pb2 as semantic__map_dot_map__parking__space__pb2
from proto.semantic_map import map_pnc_junction_pb2 as semantic__map_dot_map__pnc__junction__pb2
from proto.semantic_map import map_trafficlight_pb2 as semantic__map_dot_map__trafficlight__pb2
from proto.semantic_map import map_bus_station_pb2 as semantic__map_dot_map__bus__station__pb2
from proto.semantic_map import map_toll_station_pb2 as semantic__map_dot_map__toll__station__pb2
from proto.semantic_map import map_standby_area_pb2 as semantic__map_dot_map__standby__area__pb2
from proto.semantic_map import map_object_model_pb2 as semantic__map_dot_map__object__model__pb2
from proto.semantic_map import map_invalid_area_pb2 as semantic__map_dot_map__invalid__area__pb2
from proto.semantic_map import map_road_mask_pb2 as semantic__map_dot_map__road__mask__pb2
from proto.semantic_map import map_road_mask_plus_pb2 as semantic__map_dot_map__road__mask__plus__pb2
from proto.semantic_map import map_line_sign_pb2 as semantic__map_dot_map__line__sign__pb2
from proto.semantic_map import map_connection_line_pb2 as semantic__map_dot_map__connection__line__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16semantic_map/map.proto\x12\x0f\x64\x65\x65proute.hdmap\x1a!semantic_map/map_clear_area.proto\x1a semantic_map/map_crosswalk.proto\x1a%semantic_map/map_diversion_area.proto\x1a\x1fsemantic_map/map_junction.proto\x1a\x1bsemantic_map/map_lane.proto\x1a\x1esemantic_map/map_overlap.proto\x1a\x1dsemantic_map/map_signal.proto\x1a!semantic_map/map_speed_bump.proto\x1a semantic_map/map_stop_sign.proto\x1a!semantic_map/map_yield_sign.proto\x1a\x1bsemantic_map/map_road.proto\x1a$semantic_map/map_parking_space.proto\x1a#semantic_map/map_pnc_junction.proto\x1a#semantic_map/map_trafficlight.proto\x1a\"semantic_map/map_bus_station.proto\x1a#semantic_map/map_toll_station.proto\x1a#semantic_map/map_standby_area.proto\x1a#semantic_map/map_object_model.proto\x1a#semantic_map/map_invalid_area.proto\x1a semantic_map/map_road_mask.proto\x1a%semantic_map/map_road_mask_plus.proto\x1a semantic_map/map_line_sign.proto\x1a&semantic_map/map_connection_line.proto\"c\n\rMapProjection\x12\x0c\n\x04proj\x18\x01 \x01(\t\x12\x15\n\rlongitude_deg\x18\x02 \x01(\x01\x12\x14\n\x0clatitude_deg\x18\x03 \x01(\x01\x12\x17\n\x0cscale_factor\x18\x04 \x01(\x01:\x01\x31\"\x9e\x02\n\x06Header\x12\x0f\n\x07version\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\x0c\x12\x32\n\nprojection\x18\x03 \x01(\x0b\x32\x1e.deeproute.hdmap.MapProjection\x12\x10\n\x08\x64istrict\x18\x04 \x01(\x0c\x12\x12\n\ngeneration\x18\x05 \x01(\x0c\x12\x11\n\trev_major\x18\x06 \x01(\x0c\x12\x11\n\trev_minor\x18\x07 \x01(\x0c\x12\x0c\n\x04left\x18\x08 \x01(\x01\x12\x0b\n\x03top\x18\t \x01(\x01\x12\r\n\x05right\x18\n \x01(\x01\x12\x0e\n\x06\x62ottom\x18\x0b \x01(\x01\x12\x0e\n\x06vendor\x18\x0c \x01(\x0c\x12\x17\n\x0fndt_map_version\x18\r \x01(\t\x12\x12\n\ntile_level\x18\x0e \x01(\x05\"\xfa\x0e\n\x03Map\x12\'\n\x06header\x18\x01 \x01(\x0b\x32\x17.deeproute.hdmap.Header\x12-\n\tcrosswalk\x18\x02 \x03(\x0b\x32\x1a.deeproute.hdmap.Crosswalk\x12+\n\x08junction\x18\x03 \x03(\x0b\x32\x19.deeproute.hdmap.Junction\x12#\n\x04lane\x18\x04 \x03(\x0b\x32\x15.deeproute.hdmap.Lane\x12,\n\tstop_sign\x18\x05 \x03(\x0b\x32\x19.deeproute.hdmap.StopSign\x12\'\n\x06signal\x18\x06 \x03(\x0b\x32\x17.deeproute.hdmap.Signal\x12)\n\x05yield\x18\x07 \x03(\x0b\x32\x1a.deeproute.hdmap.YieldSign\x12)\n\x07overlap\x18\x08 \x03(\x0b\x32\x18.deeproute.hdmap.Overlap\x12.\n\nclear_area\x18\t \x03(\x0b\x32\x1a.deeproute.hdmap.ClearArea\x12.\n\nspeed_bump\x18\n \x03(\x0b\x32\x1a.deeproute.hdmap.SpeedBump\x12#\n\x04road\x18\x0b \x03(\x0b\x32\x15.deeproute.hdmap.Road\x12\x34\n\rparking_space\x18\x0c \x03(\x0b\x32\x1d.deeproute.hdmap.ParkingSpace\x12\x32\n\x0cpnc_junction\x18\r \x03(\x0b\x32\x1c.deeproute.hdmap.PNCJunction\x12\x36\n\x0flane_boundaries\x18\x0e \x03(\x0b\x32\x1d.deeproute.hdmap.LaneBoundary\x12-\n\nstop_lines\x18\x0f \x03(\x0b\x32\x19.deeproute.hdmap.StopLine\x12\x35\n\x0etraffic_lights\x18\x10 \x03(\x0b\x32\x1d.deeproute.hdmap.TrafficLight\x12,\n\tentrances\x18\x11 \x03(\x0b\x32\x19.deeproute.hdmap.Entrance\x12\x31\n\x0c\x62us_stations\x18\x12 \x03(\x0b\x32\x1b.deeproute.hdmap.BusStation\x12\x33\n\rtoll_stations\x18\x13 \x03(\x0b\x32\x1c.deeproute.hdmap.TollStation\x12\x33\n\rstandby_areas\x18\x14 \x03(\x0b\x32\x1c.deeproute.hdmap.StandbyArea\x12<\n\x12junction_end_lines\x18\x15 \x03(\x0b\x32 .deeproute.hdmap.JunctionEndLine\x12\x33\n\rtraffic_signs\x18\x16 \x03(\x0b\x32\x1c.deeproute.hdmap.TrafficSign\x12\x35\n\x0eground_symbols\x18\x17 \x03(\x0b\x32\x1d.deeproute.hdmap.GroundSymbol\x12$\n\x05poles\x18\x18 \x03(\x0b\x32\x15.deeproute.hdmap.Pole\x12\x33\n\rroad_sections\x18\x19 \x03(\x0b\x32\x1c.deeproute.hdmap.RoadSection\x12\x39\n\x10ground_obstacles\x18\x1a \x03(\x0b\x32\x1f.deeproute.hdmap.GroundObstacle\x12\x33\n\rinvalid_areas\x18\x1b \x03(\x0b\x32\x1c.deeproute.hdmap.InvalidArea\x12-\n\nroad_masks\x18\x1c \x03(\x0b\x32\x19.deeproute.hdmap.RoadMask\x12\x37\n\x0f\x64iversion_areas\x18\x1d \x03(\x0b\x32\x1e.deeproute.hdmap.DiversionArea\x12\x37\n\x10road_mask_pluses\x18\x1e \x03(\x0b\x32\x1d.deeproute.hdmap.RoadMaskPlus\x12O\n\x1c\x64\x65\x63\x65leration_and_yield_lines\x18\x1f \x03(\x0b\x32).deeproute.hdmap.DecelerationAndYieldLine\x12X\n transverse_deceleration_markings\x18  \x03(\x0b\x32..deeproute.hdmap.TransverseDecelerationMarking\x12S\n\x1evehicle_gap_confirmation_lines\x18! \x03(\x0b\x32+.deeproute.hdmap.VehicleGapConfirmationLine\x12\x31\n\x0clane_markers\x18\" \x03(\x0b\x32\x1b.deeproute.hdmap.LaneMarker\x12@\n\x14\x62icycle_lane_markers\x18# \x03(\x0b\x32\".deeproute.hdmap.BicycleLaneMarker\x12\x39\n\x10\x63onnection_lines\x18$ \x03(\x0b\x32\x1f.deeproute.hdmap.ConnectionLine')



_MAPPROJECTION = DESCRIPTOR.message_types_by_name['MapProjection']
_HEADER = DESCRIPTOR.message_types_by_name['Header']
_MAP = DESCRIPTOR.message_types_by_name['Map']
MapProjection = _reflection.GeneratedProtocolMessageType('MapProjection', (_message.Message,), {
  'DESCRIPTOR' : _MAPPROJECTION,
  '__module__' : 'semantic_map.map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.MapProjection)
  })
_sym_db.RegisterMessage(MapProjection)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'semantic_map.map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.Header)
  })
_sym_db.RegisterMessage(Header)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {
  'DESCRIPTOR' : _MAP,
  '__module__' : 'semantic_map.map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.hdmap.Map)
  })
_sym_db.RegisterMessage(Map)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAPPROJECTION._serialized_start=852
  _MAPPROJECTION._serialized_end=951
  _HEADER._serialized_start=954
  _HEADER._serialized_end=1240
  _MAP._serialized_start=1243
  _MAP._serialized_end=3157
# @@protoc_insertion_point(module_scope)
