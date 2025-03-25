# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perception/deeproute_perception_ras_map.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.perception import deeproute_perception_obstacle_pb2 as perception_dot_deeproute__perception__obstacle__pb2
from proto.common import geometry_pb2 as common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-perception/deeproute_perception_ras_map.proto\x12\x14\x64\x65\x65proute.perception\x1a.perception/deeproute_perception_obstacle.proto\x1a\x15\x63ommon/geometry.proto\"\xb1\x06\n\x0cLaneBoundary\x12\x0f\n\x07virtual\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x45\n\x13lane_boundary_color\x18\x03 \x01(\x0e\x32(.deeproute.perception.LaneBoundary.Color\x12\x45\n\x13lane_boundary_shape\x18\x04 \x01(\x0e\x32(.deeproute.perception.LaneBoundary.Shape\x12,\n\x08\x62oundary\x18\x05 \x01(\x0b\x32\x1a.deeproute.common.Polyline\x12\x17\n\tis_stable\x18\x06 \x01(\x08:\x04true\x12\x12\n\nconfidence\x18\x07 \x01(\x02\x12G\n\x15point_boundary_colors\x18\x08 \x03(\x0e\x32(.deeproute.perception.LaneBoundary.Color\x12G\n\x15point_boundary_shapes\x18\t \x03(\x0e\x32(.deeproute.perception.LaneBoundary.Shape\x12\x16\n\x07is_left\x18\n \x01(\x08:\x05\x66\x61lse\x12\x17\n\x08is_right\x18\x0b \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x12\x63urve_coefficients\x18\x0c \x03(\x02\x12\r\n\x05width\x18\r \x01(\x02\x12\x16\n\x0etracking_count\x18\x0e \x01(\x05\x12\x19\n\x11point_uncertainty\x18\x0f \x03(\x02\x12\x1a\n\x0bis_leftturn\x18\x10 \x01(\x08:\x05\x66\x61lse\"3\n\x05\x43olor\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06YELLOW\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\t\n\x05GREEN\x10\x03\"\xa8\x01\n\x05Shape\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05SOLID\x10\x01\x12\x08\n\x04\x44\x41SH\x10\x02\x12\x10\n\x0c\x44OUBLE_SOLID\x10\x03\x12\x0f\n\x0b\x44OUBLE_DASH\x10\x04\x12\x17\n\x13\x44OUBLE_LDASH_RSOLID\x10\x05\x12\x17\n\x13\x44OUBLE_LSOLID_RDASH\x10\x06\x12\x16\n\x12SHORT_THICK_DOTTED\x10\x07\x12\x10\n\x0cPARKING_LINE\x10\x08\"{\n\x0cLaneInstance\x12\x0f\n\x07lane_id\x18\x01 \x01(\x05\x12\x16\n\x0einstance_score\x18\x02 \x01(\x02\x12\x16\n\x0epassable_score\x18\x03 \x01(\x02\x12*\n\x06points\x18\x04 \x01(\x0b\x32\x1a.deeproute.common.Polyline\"\x92\x01\n\x08TopoInfo\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.deeproute.perception.TopoInfo.Type\x12(\n\x05point\x18\x02 \x01(\x0b\x32\x19.deeproute.common.Point3D\")\n\x04Type\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05SPLIT\x10\x01\x12\t\n\x05MERGE\x10\x02\"\xe8\x0c\n\x04Lane\x12\x0f\n\x07virtual\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x18\n\x10left_boundary_id\x18\x03 \x01(\x05\x12\x19\n\x11right_boundary_id\x18\x04 \x01(\x05\x12.\n\ncenterline\x18\x05 \x01(\x0b\x32\x1a.deeproute.common.Polyline\x12\x16\n\x0epredecessor_id\x18\x06 \x03(\x05\x12\x14\n\x0csuccessor_id\x18\x07 \x03(\x05\x12\x18\n\x10left_neighbor_id\x18\x08 \x01(\x05\x12 \n\x18is_left_neighbor_reverse\x18\t \x01(\x08\x12\x19\n\x11right_neighbor_id\x18\n \x01(\x05\x12!\n\x19is_right_neighbor_reverse\x18\x0b \x01(\x08\x12\x1a\n\x0bis_ego_lane\x18\x0c \x01(\x08:\x05\x66\x61lse\x12\x12\n\nconfidence\x18\r \x01(\x02\x12\x37\n\tattribute\x18\x0e \x01(\x0e\x32$.deeproute.perception.Lane.Attribute\x12\x18\n\x10road_instance_id\x18\x0f \x01(\x05\x12\x14\n\x0clane_left_id\x18\x10 \x01(\x05\x12\x15\n\rlane_right_id\x18\x11 \x01(\x05\x12\x19\n\x11lane_left_id_list\x18\x12 \x03(\x05\x12\x1a\n\x12lane_right_id_list\x18\x13 \x03(\x05\x12\x10\n\x05layer\x18\x14 \x01(\x05:\x01\x30\x12<\n\x0fstart_topo_type\x18\x15 \x01(\x0e\x32#.deeproute.perception.Lane.Topology\x12:\n\rend_topo_type\x18\x16 \x01(\x0e\x32#.deeproute.perception.Lane.Topology\x12\x43\n\x12left_neighbor_type\x18\x17 \x01(\x0e\x32\'.deeproute.perception.Lane.NeighborType\x12\x44\n\x13right_neighbor_type\x18\x18 \x01(\x0e\x32\'.deeproute.perception.Lane.NeighborType\x12\x17\n\x0flane_width_list\x18\x19 \x03(\x02\x12\x1d\n\x15left_neighbor_id_list\x18\x1a \x03(\x05\x12\x1e\n\x16right_neighbor_id_list\x18\x1b \x03(\x05\x12\x1b\n\x13passable_confidence\x18\x1c \x01(\x02\x12\"\n\x1a\x61ssociate_stopline_id_list\x18\x1d \x03(\x05\x12\'\n\x1f\x61ssociate_stopline_s_begin_list\x18\x1e \x03(\x02\x12\x13\n\x0bis_instance\x18\x1f \x01(\x08\x12\x31\n\tleft_topo\x18  \x01(\x0b\x32\x1e.deeproute.perception.TopoInfo\x12\x32\n\nright_topo\x18! \x01(\x0b\x32\x1e.deeproute.perception.TopoInfo\x12\x17\n\x0fleft_width_list\x18\" \x03(\x02\x12\x18\n\x10right_width_list\x18# \x03(\x02\x12\x12\n\nsigma_list\x18$ \x03(\x02\x12\x1c\n\x14\x61ssociation_cnt_list\x18% \x03(\x05\"\xc8\x01\n\tAttribute\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\t\n\x05\x43LOSE\x10\x02\x12\x08\n\x04\x46ORK\x10\x03\x12\t\n\x05MERGE\x10\x04\x12\x0c\n\x08SHOULDER\x10\x05\x12\x0c\n\x08\x42IKELANE\x10\x06\x12\n\n\x06UPHILL\x10\x07\x12\x0c\n\x08\x44OWNHILL\x10\x08\x12\x0c\n\x08\x42US_LANE\x10\t\x12\x0e\n\nTIDAL_LANE\x10\n\x12\x1a\n\x16LEFT_TURN_WAITING_AREA\x10\x0b\x12\x15\n\x11\x44\x45\x43\x45LERATION_LANE\x10\x0c\"}\n\x08Topology\x12\x10\n\x0cLANE_UNKNOWN\x10\x00\x12\x0e\n\nLANE_START\x10\x01\x12\x11\n\rLANE_CONTINUE\x10\x02\x12\x0c\n\x08LANE_END\x10\x03\x12\x0e\n\nLANE_SPLIT\x10\x04\x12\x0e\n\nLANE_MERGE\x10\x05\x12\x0e\n\nLANE_CLOSE\x10\x06\"K\n\x0cNeighborType\x12\x13\n\x0fNORMAL_NEIGHBOR\x10\x00\x12\x12\n\x0eSPLIT_NEIGHBOR\x10\x01\x12\x12\n\x0eMERGE_NEIGHBOR\x10\x02\"D\n\x08RoadEdge\x12\n\n\x02id\x18\x01 \x01(\x05\x12,\n\x08polyline\x18\x02 \x01(\x0b\x32\x1a.deeproute.common.Polyline\"\xb3\x01\n\x04\x41rea\x12\n\n\x02id\x18\x01 \x01(\x05\x12*\n\x07polygon\x18\x02 \x01(\x0b\x32\x19.deeproute.common.Polygon\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.deeproute.perception.Area.Type\"D\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tCROSSWALK\x10\x01\x12\x10\n\x0cTOLL_STATION\x10\x02\x12\x0e\n\nCLEAR_ZONE\x10\x03\"\xd5\x01\n\x08StopLine\x12\n\n\x02id\x18\x01 \x01(\x05\x12,\n\x08polyline\x18\x02 \x01(\x0b\x32\x1a.deeproute.common.Polyline\x12\x12\n\noverlap_id\x18\x03 \x03(\x05\x12\x31\n\x04type\x18\x04 \x01(\x0e\x32#.deeproute.perception.StopLine.Type\"H\n\x04Type\x12\x06\n\x02TL\x10\x00\x12\x08\n\x04HOLD\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\t\n\x05YIELD\x10\x03\x12\x0b\n\x07UNKNOWN\x10\x04\x12\x0c\n\x08LEFTTURN\x10\x05\"U\n\x0ePerceptionInfo\x12\x13\n\x0bsensor_name\x18\x01 \x01(\t\x12.\n\x08img_bbox\x18\x02 \x01(\x0b\x32\x1c.deeproute.perception.BBox2D\"\xdd\x06\n\nMapElement\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x33\n\x04type\x18\x02 \x01(\x0e\x32%.deeproute.perception.MapElement.Type\x12+\n\x08position\x18\x03 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12=\n\x0fperception_info\x18\x04 \x01(\x0b\x32$.deeproute.perception.PerceptionInfo\x12\x13\n\x0btext_string\x18\x05 \x01(\t\x12\r\n\x05theta\x18\x06 \x01(\x02\x12\r\n\x05score\x18\x07 \x01(\x02\"\xee\x04\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rTRAFFIC_LIGHT\x10\x01\x12\x10\n\x0cTRAFFIC_SIGN\x10\x02\x12\x08\n\x04POLE\x10\x03\x12\x18\n\x14LANE_MARKER_STRAIGHT\x10\x04\x12\x19\n\x15LANE_MARKER_TURN_LEFT\x10\x05\x12\x1a\n\x16LANE_MARKER_TURN_RIGHT\x10\x06\x12\x1d\n\x19LANE_MARKER_STRAIGHT_LEFT\x10\x07\x12\x1e\n\x1aLANE_MARKER_STRAIGHT_RIGHT\x10\x08\x12\x15\n\x11LANE_MARKER_UTURN\x10\t\x12\x1a\n\x16LANE_MARKER_LEFT_UTURN\x10\n\x12\x1e\n\x1aLANE_MARKER_STRAIGHT_UTURN\x10\x0b\x12\x1a\n\x16LANE_MARKER_LEFT_RIGHT\x10\x0c\x12\r\n\tLANE_TEXT\x10\r\x12\x16\n\x12GROUND_SPEED_LIMIT\x10\x0e\x12\x1c\n\x18TRAFFIC_SIGN_SPEED_LIMIT\x10\x0f\x12#\n\x1fLANE_MARKER_STRAIGHT_LEFT_RIGHT\x10\x10\x12#\n\x1fLANE_MARKER_STRAIGHT_LEFT_UTURN\x10\x11\x12\x1b\n\x17LANE_MARKER_RIGHT_UTURN\x10\x12\x12 \n\x1cLANE_MARKER_LEFT_RIGHT_UTURN\x10\x13\x12$\n LANE_MARKER_STRAIGHT_RIGHT_UTURN\x10\x14\x12\x1a\n\x16LANE_MARKER_LEFT_MERGE\x10\x15\x12\x1b\n\x17LANE_MARKER_RIGHT_MERGE\x10\x16\"\x87\x0b\n\x0cParkingSpace\x12\n\n\x02id\x18\x01 \x01(\x05\x12/\n\x0c\x64irect_point\x18\x02 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x33\n\x10\x64irect_point_out\x18\x03 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x37\n\x14parking_space_vertex\x18\x04 \x03(\x0b\x32\x19.deeproute.common.Point3D\x12:\n\x17parking_space_center_pt\x18\x05 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x10\n\x08is_empty\x18\x06 \x01(\x08\x12@\n\nshape_type\x18\x07 \x01(\x0e\x32,.deeproute.perception.ParkingSpace.ShapeType\x12\x46\n\rboundary_type\x18\x0e \x01(\x0e\x32/.deeproute.perception.ParkingSpace.BoundaryType\x12\x42\n\x0bsource_type\x18\x08 \x01(\x0e\x32-.deeproute.perception.ParkingSpace.SourceType\x12@\n\nempty_type\x18\t \x03(\x0e\x32,.deeproute.perception.ParkingSpace.EmptyType\x12\x0f\n\x07heading\x18\n \x01(\x01\x12;\n\x18parking_space_vertex_vis\x18\x0b \x03(\x0b\x32\x19.deeproute.common.Point3D\x12>\n\x1bparking_space_center_pt_vis\x18\x0c \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x10\n\x05layer\x18\r \x01(\x05:\x01\x30\x12\x11\n\ttimestamp\x18\x0f \x01(\x04\x12%\n\x16head_parking_available\x18\x10 \x01(\x08:\x05\x66\x61lse\x12$\n\x16tail_parking_available\x18\x11 \x01(\x08:\x04true\"W\n\tShapeType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08VERTICAL\x10\x01\x12\x0c\n\x08PARALLEL\x10\x02\x12\x0b\n\x07SLANTED\x10\x03\x12\x14\n\x10VERTICAL_SLANTED\x10\x04\"6\n\x0c\x42oundaryType\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\r\n\tBILATERAL\x10\x02\"[\n\nSourceType\x12\n\n\x06VISION\x10\x00\x12\t\n\x05SPACE\x10\x01\x12\n\n\x06\x46USION\x10\x02\x12\x10\n\x0cUSER_DEFINED\x10\x03\x12\n\n\x06HD_MAP\x10\x04\x12\x0c\n\x08SLAM_MAP\x10\x05\"\xff\x02\n\tEmptyType\x12\x10\n\x0cOTHER_REASON\x10\x00\x12\x11\n\rOTHERS_STATIC\x10\x01\x12\x11\n\rOTHERS_MOTION\x10\x02\x12\x08\n\x04WALL\x10\x03\x12\t\n\x05\x43HOCK\x10\x04\x12\x0b\n\x07LOCK_ON\x10\x05\x12\t\n\x05\x46\x45NCE\x10\x06\x12\n\n\x06\x42IGCAR\x10\x07\x12\x07\n\x03\x43\x41R\x10\x08\x12\x08\n\x04\x43ONE\x10\t\x12\t\n\x05HUMAN\x10\n\x12\x0b\n\x07\x42ICYCLE\x10\x0b\x12\x0c\n\x08TRICYCLE\x10\x0c\x12\x08\n\x04\x43URB\x10\r\x12\x0e\n\nLESS_SPACE\x10\x0e\x12\x08\n\x04TURN\x10\x0f\x12\r\n\tJOINT_EGO\x10\x10\x12\x0c\n\x08LOCK_OFF\x10\x11\x12\n\n\x06PILLAR\x10\x12\x12\x08\n\x04\x42USH\x10\x13\x12\x08\n\x04TREE\x10\x14\x12\x0e\n\nDARK_SCENE\x10\x15\x12\x0c\n\x08\x46\x41R_AWAY\x10\x16\x12\x0f\n\x0bNARROW_ROAD\x10\x17\x12\x10\n\x0c\x46IRE_HYDRANT\x10\x18\x12\x14\n\x10\x43HARGING_STATION\x10\x19\x12\x10\n\x0c\x42\x41RRIER_GATE\x10\x1a\"\xce\x01\n\x04Road\x12\r\n\x05min_x\x18\x01 \x01(\x02\x12\r\n\x05max_x\x18\x02 \x01(\x02\x12\r\n\x05min_y\x18\x03 \x01(\x02\x12\r\n\x05max_y\x18\x04 \x01(\x02\x12\r\n\x05width\x18\x05 \x01(\x05\x12\x0e\n\x06height\x18\x06 \x01(\x05\x12\x0f\n\x07indices\x18\x07 \x03(\r\x12\x13\n\x0borientation\x18\x08 \x03(\x02\x12\x14\n\x0cinstance_ids\x18\t \x03(\x05\x12\x1b\n\x13lane_confidence_map\x18\n \x01(\x0c\x12\x12\n\nvisibility\x18\x0b \x03(\x02\"\xf3\x01\n\x0bRoadPolygon\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x34\n\x04type\x18\x02 \x01(\x0e\x32&.deeproute.perception.RoadPolygon.Type\x12*\n\x07polygon\x18\x03 \x01(\x0b\x32\x19.deeproute.common.Polygon\x12\x10\n\x08is_outer\x18\x04 \x01(\x08\"d\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04ROAD\x10\x01\x12\x0c\n\x08JUNCTION\x10\x02\x12\r\n\tDIVERSION\x10\x03\x12\x12\n\x0eNODIR_ROADMASK\x10\x04\x12\x14\n\x10\x42OTHDIR_ROADMASK\x10\x05\"H\n\nRoadCenter\x12\n\n\x02id\x18\x01 \x01(\x05\x12.\n\ncenterline\x18\x02 \x01(\x0b\x32\x1a.deeproute.common.Polyline\"\x8a\x01\n\x07MPPInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12+\n\x08position\x18\x03 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x31\n\x0eroll_pitch_yaw\x18\x04 \x01(\x0b\x32\x19.deeproute.common.Point3D\"\xa1\x08\n\x06RASMap\x12)\n\x05lanes\x18\x01 \x03(\x0b\x32\x1a.deeproute.perception.Lane\x12\x34\n\x08\x62oundary\x18\x02 \x03(\x0b\x32\".deeproute.perception.LaneBoundary\x12(\n\x04\x61rea\x18\x03 \x03(\x0b\x32\x1a.deeproute.perception.Area\x12,\n\x04\x65\x64ge\x18\x04 \x03(\x0b\x32\x1e.deeproute.perception.RoadEdge\x12\x31\n\tstop_line\x18\x05 \x03(\x0b\x32\x1e.deeproute.perception.StopLine\x12\x35\n\x0bmap_element\x18\x06 \x03(\x0b\x32 .deeproute.perception.MapElement\x12\x18\n\x10time_measurement\x18\x07 \x01(\x04\x12\x39\n\rparking_space\x18\x08 \x03(\x0b\x32\".deeproute.perception.ParkingSpace\x12(\n\x04road\x18\t \x01(\x0b\x32\x1a.deeproute.perception.Road\x12/\n\x0c\x61\x64\x63_position\x18\n \x01(\x0b\x32\x19.deeproute.common.Point3D\x12/\n\x0c\x61\x64\x63_rotation\x18\x0b \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x1d\n\x15has_road_link_binding\x18\x0c \x01(\x08\x12I\n\x10road_to_sd_links\x18\r \x03(\x0b\x32/.deeproute.perception.RASMap.RoadToSdLinksEntry\x12\x1a\n\x12\x65go_lane_curvature\x18\x0e \x01(\x02\x12\x38\n\rroad_polygons\x18\x0f \x03(\x0b\x32!.deeproute.perception.RoadPolygon\x12\x16\n\x0e\x65go_lane_width\x18\x10 \x01(\x02\x12\x36\n\x0croad_centers\x18\x11 \x03(\x0b\x32 .deeproute.perception.RoadCenter\x12\x11\n\tmpp_state\x18\x12 \x03(\x02\x12/\n\x08mpp_info\x18\x13 \x01(\x0b\x32\x1d.deeproute.perception.MPPInfo\x12 \n\x18has_stopline_association\x18\x14 \x01(\x08\x12:\n\x0elane_instances\x18\x15 \x03(\x0b\x32\".deeproute.perception.LaneInstance\x12\x15\n\rheading_angle\x18\x16 \x01(\x02\x12\x14\n\x0cis_uncertain\x18\x17 \x01(\x08\x1a\x34\n\x12RoadToSdLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"I\n\tExtrinsic\x12<\n\x11vehicle_to_rasmap\x18\x01 \x01(\x0b\x32!.deeproute.common.Transformation3')



_LANEBOUNDARY = DESCRIPTOR.message_types_by_name['LaneBoundary']
_LANEINSTANCE = DESCRIPTOR.message_types_by_name['LaneInstance']
_TOPOINFO = DESCRIPTOR.message_types_by_name['TopoInfo']
_LANE = DESCRIPTOR.message_types_by_name['Lane']
_ROADEDGE = DESCRIPTOR.message_types_by_name['RoadEdge']
_AREA = DESCRIPTOR.message_types_by_name['Area']
_STOPLINE = DESCRIPTOR.message_types_by_name['StopLine']
_PERCEPTIONINFO = DESCRIPTOR.message_types_by_name['PerceptionInfo']
_MAPELEMENT = DESCRIPTOR.message_types_by_name['MapElement']
_PARKINGSPACE = DESCRIPTOR.message_types_by_name['ParkingSpace']
_ROAD = DESCRIPTOR.message_types_by_name['Road']
_ROADPOLYGON = DESCRIPTOR.message_types_by_name['RoadPolygon']
_ROADCENTER = DESCRIPTOR.message_types_by_name['RoadCenter']
_MPPINFO = DESCRIPTOR.message_types_by_name['MPPInfo']
_RASMAP = DESCRIPTOR.message_types_by_name['RASMap']
_RASMAP_ROADTOSDLINKSENTRY = _RASMAP.nested_types_by_name['RoadToSdLinksEntry']
_EXTRINSIC = DESCRIPTOR.message_types_by_name['Extrinsic']
_LANEBOUNDARY_COLOR = _LANEBOUNDARY.enum_types_by_name['Color']
_LANEBOUNDARY_SHAPE = _LANEBOUNDARY.enum_types_by_name['Shape']
_TOPOINFO_TYPE = _TOPOINFO.enum_types_by_name['Type']
_LANE_ATTRIBUTE = _LANE.enum_types_by_name['Attribute']
_LANE_TOPOLOGY = _LANE.enum_types_by_name['Topology']
_LANE_NEIGHBORTYPE = _LANE.enum_types_by_name['NeighborType']
_AREA_TYPE = _AREA.enum_types_by_name['Type']
_STOPLINE_TYPE = _STOPLINE.enum_types_by_name['Type']
_MAPELEMENT_TYPE = _MAPELEMENT.enum_types_by_name['Type']
_PARKINGSPACE_SHAPETYPE = _PARKINGSPACE.enum_types_by_name['ShapeType']
_PARKINGSPACE_BOUNDARYTYPE = _PARKINGSPACE.enum_types_by_name['BoundaryType']
_PARKINGSPACE_SOURCETYPE = _PARKINGSPACE.enum_types_by_name['SourceType']
_PARKINGSPACE_EMPTYTYPE = _PARKINGSPACE.enum_types_by_name['EmptyType']
_ROADPOLYGON_TYPE = _ROADPOLYGON.enum_types_by_name['Type']
LaneBoundary = _reflection.GeneratedProtocolMessageType('LaneBoundary', (_message.Message,), {
  'DESCRIPTOR' : _LANEBOUNDARY,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.LaneBoundary)
  })
_sym_db.RegisterMessage(LaneBoundary)

LaneInstance = _reflection.GeneratedProtocolMessageType('LaneInstance', (_message.Message,), {
  'DESCRIPTOR' : _LANEINSTANCE,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.LaneInstance)
  })
_sym_db.RegisterMessage(LaneInstance)

TopoInfo = _reflection.GeneratedProtocolMessageType('TopoInfo', (_message.Message,), {
  'DESCRIPTOR' : _TOPOINFO,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.TopoInfo)
  })
_sym_db.RegisterMessage(TopoInfo)

Lane = _reflection.GeneratedProtocolMessageType('Lane', (_message.Message,), {
  'DESCRIPTOR' : _LANE,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.Lane)
  })
_sym_db.RegisterMessage(Lane)

RoadEdge = _reflection.GeneratedProtocolMessageType('RoadEdge', (_message.Message,), {
  'DESCRIPTOR' : _ROADEDGE,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.RoadEdge)
  })
_sym_db.RegisterMessage(RoadEdge)

Area = _reflection.GeneratedProtocolMessageType('Area', (_message.Message,), {
  'DESCRIPTOR' : _AREA,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.Area)
  })
_sym_db.RegisterMessage(Area)

StopLine = _reflection.GeneratedProtocolMessageType('StopLine', (_message.Message,), {
  'DESCRIPTOR' : _STOPLINE,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.StopLine)
  })
_sym_db.RegisterMessage(StopLine)

PerceptionInfo = _reflection.GeneratedProtocolMessageType('PerceptionInfo', (_message.Message,), {
  'DESCRIPTOR' : _PERCEPTIONINFO,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.PerceptionInfo)
  })
_sym_db.RegisterMessage(PerceptionInfo)

MapElement = _reflection.GeneratedProtocolMessageType('MapElement', (_message.Message,), {
  'DESCRIPTOR' : _MAPELEMENT,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.MapElement)
  })
_sym_db.RegisterMessage(MapElement)

ParkingSpace = _reflection.GeneratedProtocolMessageType('ParkingSpace', (_message.Message,), {
  'DESCRIPTOR' : _PARKINGSPACE,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.ParkingSpace)
  })
_sym_db.RegisterMessage(ParkingSpace)

Road = _reflection.GeneratedProtocolMessageType('Road', (_message.Message,), {
  'DESCRIPTOR' : _ROAD,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.Road)
  })
_sym_db.RegisterMessage(Road)

RoadPolygon = _reflection.GeneratedProtocolMessageType('RoadPolygon', (_message.Message,), {
  'DESCRIPTOR' : _ROADPOLYGON,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.RoadPolygon)
  })
_sym_db.RegisterMessage(RoadPolygon)

RoadCenter = _reflection.GeneratedProtocolMessageType('RoadCenter', (_message.Message,), {
  'DESCRIPTOR' : _ROADCENTER,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.RoadCenter)
  })
_sym_db.RegisterMessage(RoadCenter)

MPPInfo = _reflection.GeneratedProtocolMessageType('MPPInfo', (_message.Message,), {
  'DESCRIPTOR' : _MPPINFO,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.MPPInfo)
  })
_sym_db.RegisterMessage(MPPInfo)

RASMap = _reflection.GeneratedProtocolMessageType('RASMap', (_message.Message,), {

  'RoadToSdLinksEntry' : _reflection.GeneratedProtocolMessageType('RoadToSdLinksEntry', (_message.Message,), {
    'DESCRIPTOR' : _RASMAP_ROADTOSDLINKSENTRY,
    '__module__' : 'perception.deeproute_perception_ras_map_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.perception.RASMap.RoadToSdLinksEntry)
    })
  ,
  'DESCRIPTOR' : _RASMAP,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.RASMap)
  })
_sym_db.RegisterMessage(RASMap)
_sym_db.RegisterMessage(RASMap.RoadToSdLinksEntry)

Extrinsic = _reflection.GeneratedProtocolMessageType('Extrinsic', (_message.Message,), {
  'DESCRIPTOR' : _EXTRINSIC,
  '__module__' : 'perception.deeproute_perception_ras_map_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.perception.Extrinsic)
  })
_sym_db.RegisterMessage(Extrinsic)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RASMAP_ROADTOSDLINKSENTRY._options = None
  _RASMAP_ROADTOSDLINKSENTRY._serialized_options = b'8\001'
  _LANEBOUNDARY._serialized_start=143
  _LANEBOUNDARY._serialized_end=960
  _LANEBOUNDARY_COLOR._serialized_start=738
  _LANEBOUNDARY_COLOR._serialized_end=789
  _LANEBOUNDARY_SHAPE._serialized_start=792
  _LANEBOUNDARY_SHAPE._serialized_end=960
  _LANEINSTANCE._serialized_start=962
  _LANEINSTANCE._serialized_end=1085
  _TOPOINFO._serialized_start=1088
  _TOPOINFO._serialized_end=1234
  _TOPOINFO_TYPE._serialized_start=1193
  _TOPOINFO_TYPE._serialized_end=1234
  _LANE._serialized_start=1237
  _LANE._serialized_end=2877
  _LANE_ATTRIBUTE._serialized_start=2473
  _LANE_ATTRIBUTE._serialized_end=2673
  _LANE_TOPOLOGY._serialized_start=2675
  _LANE_TOPOLOGY._serialized_end=2800
  _LANE_NEIGHBORTYPE._serialized_start=2802
  _LANE_NEIGHBORTYPE._serialized_end=2877
  _ROADEDGE._serialized_start=2879
  _ROADEDGE._serialized_end=2947
  _AREA._serialized_start=2950
  _AREA._serialized_end=3129
  _AREA_TYPE._serialized_start=3061
  _AREA_TYPE._serialized_end=3129
  _STOPLINE._serialized_start=3132
  _STOPLINE._serialized_end=3345
  _STOPLINE_TYPE._serialized_start=3273
  _STOPLINE_TYPE._serialized_end=3345
  _PERCEPTIONINFO._serialized_start=3347
  _PERCEPTIONINFO._serialized_end=3432
  _MAPELEMENT._serialized_start=3435
  _MAPELEMENT._serialized_end=4296
  _MAPELEMENT_TYPE._serialized_start=3674
  _MAPELEMENT_TYPE._serialized_end=4296
  _PARKINGSPACE._serialized_start=4299
  _PARKINGSPACE._serialized_end=5714
  _PARKINGSPACE_SHAPETYPE._serialized_start=5092
  _PARKINGSPACE_SHAPETYPE._serialized_end=5179
  _PARKINGSPACE_BOUNDARYTYPE._serialized_start=5181
  _PARKINGSPACE_BOUNDARYTYPE._serialized_end=5235
  _PARKINGSPACE_SOURCETYPE._serialized_start=5237
  _PARKINGSPACE_SOURCETYPE._serialized_end=5328
  _PARKINGSPACE_EMPTYTYPE._serialized_start=5331
  _PARKINGSPACE_EMPTYTYPE._serialized_end=5714
  _ROAD._serialized_start=5717
  _ROAD._serialized_end=5923
  _ROADPOLYGON._serialized_start=5926
  _ROADPOLYGON._serialized_end=6169
  _ROADPOLYGON_TYPE._serialized_start=6069
  _ROADPOLYGON_TYPE._serialized_end=6169
  _ROADCENTER._serialized_start=6171
  _ROADCENTER._serialized_end=6243
  _MPPINFO._serialized_start=6246
  _MPPINFO._serialized_end=6384
  _RASMAP._serialized_start=6387
  _RASMAP._serialized_end=7444
  _RASMAP_ROADTOSDLINKSENTRY._serialized_start=7392
  _RASMAP_ROADTOSDLINKSENTRY._serialized_end=7444
  _EXTRINSIC._serialized_start=7446
  _EXTRINSIC._serialized_end=7519
# @@protoc_insertion_point(module_scope)
