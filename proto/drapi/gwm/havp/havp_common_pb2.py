# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drapi/gwm/havp/havp_common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n drapi/gwm/havp/havp_common.proto\x12\x04havp\"(\n\x05\x43oor3\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"7\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\r\n\x05\x66loor\x18\x07 \x01(\t\"d\n\x08Location\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\x0b\n\x03yaw\x18\x04 \x01(\x01\x12\r\n\x05pitch\x18\x05 \x01(\x01\x12\x0c\n\x04roll\x18\x06 \x01(\x01\x12\r\n\x05\x66loor\x18\x07 \x01(\t\"(\n\x05Pnt3D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"\xa5\x02\n\x0b\x42oundingBox\x12\x1f\n\nleft_front\x18\x01 \x01(\x0b\x32\x0b.havp.Coor3\x12\x1e\n\tleft_rear\x18\x02 \x01(\x0b\x32\x0b.havp.Coor3\x12\x1f\n\nright_rear\x18\x03 \x01(\x0b\x32\x0b.havp.Coor3\x12 \n\x0bright_front\x18\x04 \x01(\x0b\x32\x0b.havp.Coor3\x12#\n\x0eleft_front_top\x18\x05 \x01(\x0b\x32\x0b.havp.Coor3\x12\"\n\rleft_rear_top\x18\x06 \x01(\x0b\x32\x0b.havp.Coor3\x12#\n\x0eright_rear_top\x18\x07 \x01(\x0b\x32\x0b.havp.Coor3\x12$\n\x0fright_front_top\x18\x08 \x01(\x0b\x32\x0b.havp.Coor3\"=\n\x0cObstaclePose\x12\x1a\n\x05point\x18\x01 \x01(\x0b\x32\x0b.havp.Coor3\x12\x11\n\tdirection\x18\x02 \x01(\x02\"\xee\x11\n\x0cParkingSpace\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\r\x12=\n\x0c\x62ounding_box\x18\x03 \x03(\x0b\x32\'.havp.ParkingSpace.ParkSpaceBoundingBox\x12\x31\n\x04type\x18\x04 \x01(\x0e\x32#.havp.ParkingSpace.ParkingSpaceType\x12\x35\n\x06status\x18\x05 \x01(\x0e\x32%.havp.ParkingSpace.ParkingSpaceStatus\x12\x31\n\x03use\x18\x06 \x01(\x0e\x32$.havp.ParkingSpace.ParkingSpaceUsage\x12\x42\n\robstacle_type\x18\x07 \x01(\x0e\x32+.havp.ParkingSpace.ParkingSpaceObstacleType\x12\r\n\x05\x66loor\x18\x08 \x01(\t\x12\x10\n\x08\x66\x61vorite\x18\t \x01(\x08\x12\x15\n\rfavorite_time\x18\n \x01(\x05\x12\x0c\n\x04name\x18\x0b \x01(\t\x12/\n\x03tag\x18\x0c \x01(\x0e\x32\".havp.ParkingSpace.ParkingSpaceTag\x12\x12\n\nis_default\x18\r \x01(\x08\x12\x1b\n\x13is_last_destination\x18\x0e \x01(\x08\x12:\n\tsize_type\x18\x0f \x01(\x0e\x32\'.havp.ParkingSpace.ParkingSpaceSizeType\x12*\n\x03\x64ir\x18\x10 \x01(\x0e\x32\x1d.havp.ParkingSpace.ParkingDir\x1a\xb3\x02\n\x14ParkSpaceBoundingBox\x12\x1a\n\x05point\x18\x01 \x01(\x0b\x32\x0b.havp.Coor3\x12K\n\x08position\x18\x02 \x01(\x0e\x32\x39.havp.ParkingSpace.ParkSpaceBoundingBox.ParkSpacePosition\x12\x0f\n\x07quality\x18\x03 \x01(\x05\"\xa0\x01\n\x11ParkSpacePosition\x12\x11\n\rPOSITION_NONE\x10\x00\x12\x17\n\x13POSITION_LEFT_FRONT\x10\x01\x12\x16\n\x12POSITION_LEFT_REAR\x10\x02\x12\x17\n\x13POSITION_RIGHT_REAR\x10\x03\x12\x18\n\x14POSITION_RIGHT_FRONT\x10\x04\x12\x14\n\x10POSITION_INVALID\x10\x07\"\xa1\x01\n\x10ParkingSpaceType\x12\x18\n\x14PARK_SPACE_TYPE_NONE\x10\x00\x12\x1c\n\x18PARK_SPACE_TYPE_VERTICAL\x10\x01\x12\x1b\n\x17PARK_SPACE_TYPE_LATERAL\x10\x02\x12\x1b\n\x17PARK_SPACE_TYPE_OBLIQUE\x10\x03\x12\x1b\n\x17PARK_SPACE_TYPE_INVALID\x10\x04\"\x98\x02\n\x12ParkingSpaceStatus\x12\x1d\n\x19PARK_SPACE_STATUS_UNKNOWN\x10\x00\x12\x1a\n\x16PARK_SPACE_STATUS_FREE\x10\x01\x12\x1e\n\x1aPARK_SPACE_STATUS_OCCUPIED\x10\x02\x12!\n\x1dPARK_SPACE_STATUS_DESTINATION\x10\x03\x12 \n\x1cPARK_SPACE_STATUS_SELECTABLE\x10\x04\x12\x1e\n\x1aPARK_SPACE_STATUS_SELECTED\x10\x05\x12\x1d\n\x19PARK_SPACE_STATUS_INVALID\x10\x06\x12#\n\x1fPARK_SPACE_STATUS_UPDATE_IGNORE\x10\x07\"e\n\x11ParkingSpaceUsage\x12\x1a\n\x16PARK_SPACE_USE_INVALID\x10\x00\x12\x19\n\x15PARK_SPACE_USE_NORMAL\x10\x01\x12\x19\n\x15PARK_SPACE_USE_CHARGE\x10\x05\"\xe8\x02\n\x18ParkingSpaceObstacleType\x12#\n\x1fPARK_SPACE_OBSTACLE_TYPE_UNKNOW\x10\x00\x12 \n\x1cPARK_SPACE_OBSTACLE_TYPE_CAR\x10\x01\x12&\n\"PARK_SPACE_OBSTACLE_TYPE_NODISPLAY\x10\x02\x12\'\n#PARK_SPACE_OBSTACLE_TYPE_PEDESTRIAN\x10\x03\x12!\n\x1dPARK_SPACE_OBSTACLE_TYPE_CONE\x10\x04\x12!\n\x1dPARK_SPACE_OBSTACLE_TYPE_LOCK\x10\x05\x12(\n$PARK_SPACE_OBSTACLE_TYPE_PARKINGLOCK\x10\x06\x12 \n\x1cPARK_SPACE_OBSTACLE_TYPE_VAN\x10\x07\x12\"\n\x1ePARK_SPACE_OBSTACLE_TYPE_SMALL\x10\x08\"\x9f\x01\n\x0fParkingSpaceTag\x12\x17\n\x13PARK_SPACE_TAG_NONE\x10\x00\x12\x19\n\x15PARK_SPACE_TAG_CHARGE\x10\x01\x12\x1b\n\x17PARK_SPACE_TAG_ELEVATOR\x10\x02\x12\x1c\n\x18PARK_SPACE_TAG_STAIRCASE\x10\x03\x12\x1d\n\x19PARK_SPACE_TAG_PASSAGEWAY\x10\x04\"\x98\x01\n\x14ParkingSpaceSizeType\x12\x1d\n\x19PARK_SPACE_SIZE_TYPE_NONE\x10\x00\x12!\n\x1dPARK_SPACE_SIZE_TYPE_STANDARD\x10\x01\x12\x1f\n\x1bPARK_SPACE_SIZE_TYPE_NARROW\x10\x02\x12\x1d\n\x19PARK_SPACE_SIZE_TYPE_WIDE\x10\x03\"\x8d\x01\n\nParkingDir\x12\x11\n\rPARK_DIR_NONE\x10\x00\x12\x17\n\x13PARK_DIR_HEAD_FIXED\x10\x01\x12\x17\n\x13PARK_DIR_TAIL_FIXED\x10\x02\x12\x1c\n\x18PARK_DIR_HEAD_SWITCHABLE\x10\x03\x12\x1c\n\x18PARK_DIR_TAIL_SWITCHABLE\x10\x04\"\x8d\x02\n\x0bMapObstacle\x12\n\n\x02id\x18\x01 \x01(\x05\x12/\n\x04type\x18\x02 \x01(\x0e\x32!.havp.MapObstacle.MapObstacleType\x12(\n\rposition_info\x18\x03 \x01(\x0b\x32\x11.havp.BoundingBox\x12\r\n\x05\x66loor\x18\x04 \x01(\t\"\x87\x01\n\x0fMapObstacleType\x12\x19\n\x15OBSTACLE_TYPE_INVALID\x10\x00\x12\x1e\n\x1aOBSTACLE_TYPE_PILLAR_ROUND\x10\x01\x12\x1f\n\x1bOBSTACLE_TYPE_PILLAR_SQUARE\x10\x02\x12\x18\n\x14OBSTACLE_TYPE_BUMPER\x10\x03\"\xce\r\n\x17ObjectDetectionObstacle\x12\n\n\x02id\x18\x01 \x01(\x05\x12G\n\x04type\x18\x02 \x01(\x0e\x32\x39.havp.ObjectDetectionObstacle.ObjectDetectionObstacleType\x12(\n\rposition_info\x18\x03 \x01(\x0b\x32\x11.havp.BoundingBox\x12\x11\n\tis_moving\x18\x04 \x01(\x08\x12\x44\n\x0fobj_alarm_level\x18\x05 \x01(\x0e\x32+.havp.ObjectDetectionObstacle.ObjAlarmLevel\"\xdf\n\n\x1bObjectDetectionObstacleType\x12\x19\n\x15OBSTACLE_TYPE_INVALID\x10\x00\x12\x1e\n\x1aOBSTACLE_TYPE_PILLAR_ROUND\x10\x01\x12\x1f\n\x1bOBSTACLE_TYPE_PILLAR_SQUARE\x10\x02\x12\x18\n\x14OBSTACLE_TYPE_BUMPER\x10\x03\x12\x15\n\x11OBSTACLE_TYPE_CAR\x10\x04\x12\x1c\n\x18OBSTACLE_TYPE_PEDESTRIAN\x10\x05\x12\x16\n\x12OBSTACLE_TYPE_CONE\x10\x06\x12 \n\x1cOBSTACLE_TYPE_FLOOR_ENTRANCE\x10\x07\x12\x1c\n\x18OBSTACLE_TYPE_FLOOR_EXIT\x10\x08\x12\x17\n\x13OBSTACLE_TYPE_ARROW\x10\t\x12\x1d\n\x19OBSTACLE_TYPE_WARNINGSIGN\x10\n\x12\x1a\n\x16OBSTACLE_TYPE_TWOWHEEL\x10\x0b\x12\x1d\n\x19OBSTACLE_TYPE_PARKINGLOCK\x10\x0c\x12\x1e\n\x1aOBSTACLE_TYPE_MANHOLECOVER\x10\r\x12\x1d\n\x19OBSTACLE_TYPE_BARRIERGATE\x10\x0e\x12\x1d\n\x19OBSTACLE_TYPE_WARNINGPOST\x10\x0f\x12\x16\n\x12OBSTACLE_TYPE_LAMP\x10\x10\x12\x17\n\x13OBSTACLE_TYPE_RIDER\x10\x11\x12\x1f\n\x1bOBSTACLE_TYPE_STOPPER_SHORT\x10\x12\x12\x1e\n\x1aOBSTACLE_TYPE_STOPPER_LONG\x10\x13\x12\x16\n\x12OBSTACLE_TYPE_WALL\x10\x14\x12&\n\"OBSTACLE_TYPE_WATER_FILLED_BARRIER\x10\x15\x12\x1b\n\x17OBSTACLE_TYPE_TRASH_CAN\x10\x16\x12\"\n\x1eOBSTACLE_TYPE_GROUND_LOCK_OPEN\x10\x17\x12#\n\x1fOBSTACLE_TYPE_GROUND_LOCK_CLOSE\x10\x18\x12!\n\x1dOBSTACLE_TYPE_PARKING_LIMITER\x10\x19\x12*\n&OBSTACLE_TYPE_PARKING_LIMITER_SEPARATE\x10\x1a\x12\x15\n\x11OBSTACLE_TYPE_VAN\x10\x1b\x12\x17\n\x13OBSTACLE_TYPE_CHILD\x10\x1c\x12#\n\x1fOBSTACLE_TYPE_ARROW_TS_STRAIGHT\x10\x64\x12\x1f\n\x1bOBSTACLE_TYPE_ARROW_TS_LEFT\x10\x65\x12 \n\x1cOBSTACLE_TYPE_ARROW_TS_RIGHT\x10\x66\x12\x1f\n\x1bOBSTACLE_TYPE_ARROW_TS_BACK\x10g\x12(\n$OBSTACLE_TYPE_ARROW_TS_TOGETHER_LEFT\x10h\x12)\n%OBSTACLE_TYPE_ARROW_TS_TOGETHER_RIGHT\x10i\x12%\n!OBSTACLE_TYPE_ARROW_TS_LEFT_RIGHT\x10x\x12(\n$OBSTACLE_TYPE_ARROW_TS_STRAIGHT_LEFT\x10y\x12)\n%OBSTACLE_TYPE_ARROW_TS_STRAIGHT_RIGHT\x10z\x12$\n OBSTACLE_TYPE_ARROW_TS_LEFT_BACK\x10{\x12%\n!OBSTACLE_TYPE_ARROW_TS_RIGHT_BACK\x10|\x12.\n*OBSTACLE_TYPE_ARROW_TS_STRAIGHT_LEFT_RIGHT\x10}\"y\n\rObjAlarmLevel\x12\x18\n\x14OBJ_ALARM_LEVEL_NONE\x10\x00\x12\x19\n\x15OBJ_ALARM_LEVEL_GREEN\x10\x01\x12\x1a\n\x16OBJ_ALARM_LEVEL_YELLOW\x10\x02\x12\x17\n\x13OBJ_ALARM_LEVEL_RED\x10\x03\"N\n\x0bWallElement\x12\x1b\n\x04wall\x18\x01 \x03(\x0b\x32\r.havp.Polygon\x12\"\n\x0bwall_bottom\x18\x02 \x01(\x0b\x32\r.havp.Polygon\"#\n\x07Polygon\x12\x18\n\x03pnt\x18\x01 \x03(\x0b\x32\x0b.havp.Pnt3D\"$\n\x08Polyline\x12\x18\n\x03pnt\x18\x01 \x03(\x0b\x32\x0b.havp.Pnt3D\"\xf9\x07\n\x03PAS\x12.\n\x12\x46PAS_OBJFLCORNRAR1\x18\x01 \x01(\x0e\x32\x12.havp.PAS.Distance\x12.\n\x12\x46PAS_OBJFLCORNRAR2\x18\x02 \x01(\x0e\x32\x12.havp.PAS.Distance\x12.\n\x12\x46PAS_OBJFRCORNRAR1\x18\x03 \x01(\x0e\x32\x12.havp.PAS.Distance\x12.\n\x12\x46PAS_OBJFRCORNRAR2\x18\x04 \x01(\x0e\x32\x12.havp.PAS.Distance\x12-\n\x11\x46PAS_OBJFLMIDLAR1\x18\x05 \x01(\x0e\x32\x12.havp.PAS.Distance\x12-\n\x11\x46PAS_OBJFLMIDLAR2\x18\x06 \x01(\x0e\x32\x12.havp.PAS.Distance\x12-\n\x11\x46PAS_OBJFRMIDLAR1\x18\x07 \x01(\x0e\x32\x12.havp.PAS.Distance\x12-\n\x11\x46PAS_OBJFRMIDLAR2\x18\x08 \x01(\x0e\x32\x12.havp.PAS.Distance\x12.\n\x12RPAS_OBJRLCORNRAR1\x18\t \x01(\x0e\x32\x12.havp.PAS.Distance\x12.\n\x12RPAS_OBJRLCORNRAR2\x18\n \x01(\x0e\x32\x12.havp.PAS.Distance\x12.\n\x12RPAS_OBJRRCORNRAR1\x18\x0b \x01(\x0e\x32\x12.havp.PAS.Distance\x12.\n\x12RPAS_OBJRRCORNRAR2\x18\x0c \x01(\x0e\x32\x12.havp.PAS.Distance\x12-\n\x11RPAS_OBJRLMIDLAR1\x18\r \x01(\x0e\x32\x12.havp.PAS.Distance\x12-\n\x11RPAS_OBJRLMIDLAR2\x18\x0e \x01(\x0e\x32\x12.havp.PAS.Distance\x12-\n\x11RPAS_OBJRRMIDLAR1\x18\x0f \x01(\x0e\x32\x12.havp.PAS.Distance\x12-\n\x11RPAS_OBJRRMIDLAR2\x18\x10 \x01(\x0e\x32\x12.havp.PAS.Distance\"\xf9\x01\n\x08\x44istance\x12\x11\n\rDISTANCE_NONE\x10\x00\x12\x0b\n\x07\x46\x30T10CM\x10\x01\x12\x0c\n\x08\x46\x31\x31T20CM\x10\x02\x12\x0c\n\x08\x46\x32\x31T30CM\x10\x03\x12\x0c\n\x08\x46\x33\x31T40CM\x10\x04\x12\x0c\n\x08\x46\x34\x31T50CM\x10\x05\x12\x0c\n\x08\x46\x35\x31T60CM\x10\x06\x12\x0c\n\x08\x46\x36\x31T70CM\x10\x07\x12\x0c\n\x08\x46\x37\x31T80CM\x10\x08\x12\x0c\n\x08\x46\x38\x31T90CM\x10\t\x12\r\n\tF91T100CM\x10\n\x12\x0e\n\nF101T110CM\x10\x0b\x12\x0e\n\nF111T120CM\x10\x0c\x12\x0e\n\nF121T130CM\x10\r\x12\x0e\n\nF131T140CM\x10\x0e\x12\x0e\n\nF141T150CM\x10\x0f\"\xc7\x04\n\x10SignlineVertical\x12\n\n\x02id\x18\x01 \x01(\x05\x12-\n\x04type\x18\x02 \x01(\x0e\x32\x1f.havp.SignlineVertical.LineType\x12/\n\x05shape\x18\x03 \x01(\x0e\x32 .havp.SignlineVertical.LineShape\x12\x1a\n\x05\x63olor\x18\x04 \x01(\x0e\x32\x0b.havp.Color\x12\x35\n\x08material\x18\x05 \x01(\x0e\x32#.havp.SignlineVertical.LineMaterial\x12 \n\x08polyline\x18\x06 \x03(\x0b\x32\x0e.havp.Polyline\"6\n\x08LineType\x12\x16\n\x12LINE_TYPE_BOUNDARY\x10\x00\x12\x12\n\x0eLINE_TYPE_LANE\x10\x01\"\xa1\x01\n\tLineShape\x12\x13\n\x0fLINE_SHAPE_NONE\x10\x00\x12\x17\n\x13LINE_SHAPE_BOUNDARY\x10\x01\x12\x15\n\x11LINE_SHAPE_DOTTED\x10\x02\x12\x14\n\x10LINE_SHAPE_SOLID\x10\x03\x12\x1c\n\x18LINE_SHAPE_DOUBLE_DOTTED\x10\x04\x12\x1b\n\x17LINE_SHAPE_DOUBLE_SOLID\x10\x05\"v\n\x0cLineMaterial\x12\x16\n\x12LINE_MATERIAL_NONE\x10\x00\x12\x19\n\x15LINE_MATERIAL_MARKING\x10\x01\x12\x16\n\x12LINE_MATERIAL_CURB\x10\x02\x12\x1b\n\x17LINE_MATERIAL_GUARD_BAR\x10\x03\"\xfe\x01\n\x0bSignPolygon\x12\n\n\x02id\x18\x01 \x01(\x05\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.havp.SignPolygon.PolygonType\x12\x1a\n\x05\x63olor\x18\x03 \x01(\x0e\x32\x0b.havp.Color\x12\x1e\n\x07polygon\x18\x04 \x03(\x0b\x32\r.havp.Polygon\"z\n\x0bPolygonType\x12\x14\n\x10POLYON_TYPE_NONE\x10\x00\x12\x1b\n\x17POLYON_TYPE_DRIVINGAREA\x10\x01\x12\x19\n\x15POLYON_TYPE_CROSSWALK\x10\x02\x12\x1d\n\x19POLYON_TYPE_NOPARKINGAREA\x10\x03\"\xaf\x02\n\tAVPMapPin\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x05 \x01(\x01\x12\x0f\n\x07\x61\x64\x64ress\x18\x06 \x01(\t\x12)\n\x03tag\x18\x07 \x01(\x0e\x32\x1c.havp.AVPMapPin.AVPMapPinTag\"\x94\x01\n\x0c\x41VPMapPinTag\x12\x18\n\x14\x41VP_MAP_PIN_TAG_NONE\x10\x00\x12\x18\n\x14\x41VP_MAP_PIN_TAG_HOME\x10\x01\x12\x18\n\x14\x41VP_MAP_PIN_TAG_MALL\x10\x02\x12\x1c\n\x18\x41VP_MAP_PIN_TAG_HOSPITAL\x10\x03\x12\x18\n\x14\x41VP_MAP_PIN_TAG_PARK\x10\x04\",\n\x04Road\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x18\n\x03pts\x18\x02 \x03(\x0b\x32\x0b.havp.Point\"#\n\x06\x41VPMap\x12\x19\n\x05roads\x18\x01 \x03(\x0b\x32\n.havp.Road*j\n\x05\x43olor\x12\x0e\n\nCOLOR_NONE\x10\x00\x12\x0f\n\x0b\x43OLOR_WHITE\x10\x01\x12\x10\n\x0c\x43OLOR_YELLOW\x10\x02\x12\x0e\n\nCOLOR_BLUE\x10\x03\x12\x0f\n\x0b\x43OLOR_GREEN\x10\x04\x12\r\n\tCOLOR_RED\x10\x05*\xa5\x02\n\x0cHAVPNaviTips\x12\x11\n\rHAVP_TIP_NONE\x10\x00\x12\x18\n\x14HAVP_TIP_PARKING_OUT\x10\x01\x12\x18\n\x14HAVP_TIP_ARRIVE_DEST\x10\x02\x12\x16\n\x12HAVP_TIP_TURN_LEFT\x10\x03\x12\x17\n\x13HAVP_TIP_TURN_RIGHT\x10\x04\x12\x18\n\x14HAVP_TIP_TURN_AROUND\x10\x05\x12\x13\n\x0fHAVP_TIP_UPHILL\x10\x06\x12\x15\n\x11HAVP_TIP_DOWNHILL\x10\x07\x12\x1e\n\x1aHAVP_TIP_ENTER_PARKING_LOT\x10\x08\x12\x1d\n\x19HAVP_TIP_EXIT_PARKING_LOT\x10\t\x12\x18\n\x14HAVP_TIP_RETURN_ROAD\x10\nb\x06proto3')

_COLOR = DESCRIPTOR.enum_types_by_name['Color']
Color = enum_type_wrapper.EnumTypeWrapper(_COLOR)
_HAVPNAVITIPS = DESCRIPTOR.enum_types_by_name['HAVPNaviTips']
HAVPNaviTips = enum_type_wrapper.EnumTypeWrapper(_HAVPNAVITIPS)
COLOR_NONE = 0
COLOR_WHITE = 1
COLOR_YELLOW = 2
COLOR_BLUE = 3
COLOR_GREEN = 4
COLOR_RED = 5
HAVP_TIP_NONE = 0
HAVP_TIP_PARKING_OUT = 1
HAVP_TIP_ARRIVE_DEST = 2
HAVP_TIP_TURN_LEFT = 3
HAVP_TIP_TURN_RIGHT = 4
HAVP_TIP_TURN_AROUND = 5
HAVP_TIP_UPHILL = 6
HAVP_TIP_DOWNHILL = 7
HAVP_TIP_ENTER_PARKING_LOT = 8
HAVP_TIP_EXIT_PARKING_LOT = 9
HAVP_TIP_RETURN_ROAD = 10


_COOR3 = DESCRIPTOR.message_types_by_name['Coor3']
_POINT = DESCRIPTOR.message_types_by_name['Point']
_LOCATION = DESCRIPTOR.message_types_by_name['Location']
_PNT3D = DESCRIPTOR.message_types_by_name['Pnt3D']
_BOUNDINGBOX = DESCRIPTOR.message_types_by_name['BoundingBox']
_OBSTACLEPOSE = DESCRIPTOR.message_types_by_name['ObstaclePose']
_PARKINGSPACE = DESCRIPTOR.message_types_by_name['ParkingSpace']
_PARKINGSPACE_PARKSPACEBOUNDINGBOX = _PARKINGSPACE.nested_types_by_name['ParkSpaceBoundingBox']
_MAPOBSTACLE = DESCRIPTOR.message_types_by_name['MapObstacle']
_OBJECTDETECTIONOBSTACLE = DESCRIPTOR.message_types_by_name['ObjectDetectionObstacle']
_WALLELEMENT = DESCRIPTOR.message_types_by_name['WallElement']
_POLYGON = DESCRIPTOR.message_types_by_name['Polygon']
_POLYLINE = DESCRIPTOR.message_types_by_name['Polyline']
_PAS = DESCRIPTOR.message_types_by_name['PAS']
_SIGNLINEVERTICAL = DESCRIPTOR.message_types_by_name['SignlineVertical']
_SIGNPOLYGON = DESCRIPTOR.message_types_by_name['SignPolygon']
_AVPMAPPIN = DESCRIPTOR.message_types_by_name['AVPMapPin']
_ROAD = DESCRIPTOR.message_types_by_name['Road']
_AVPMAP = DESCRIPTOR.message_types_by_name['AVPMap']
_PARKINGSPACE_PARKSPACEBOUNDINGBOX_PARKSPACEPOSITION = _PARKINGSPACE_PARKSPACEBOUNDINGBOX.enum_types_by_name['ParkSpacePosition']
_PARKINGSPACE_PARKINGSPACETYPE = _PARKINGSPACE.enum_types_by_name['ParkingSpaceType']
_PARKINGSPACE_PARKINGSPACESTATUS = _PARKINGSPACE.enum_types_by_name['ParkingSpaceStatus']
_PARKINGSPACE_PARKINGSPACEUSAGE = _PARKINGSPACE.enum_types_by_name['ParkingSpaceUsage']
_PARKINGSPACE_PARKINGSPACEOBSTACLETYPE = _PARKINGSPACE.enum_types_by_name['ParkingSpaceObstacleType']
_PARKINGSPACE_PARKINGSPACETAG = _PARKINGSPACE.enum_types_by_name['ParkingSpaceTag']
_PARKINGSPACE_PARKINGSPACESIZETYPE = _PARKINGSPACE.enum_types_by_name['ParkingSpaceSizeType']
_PARKINGSPACE_PARKINGDIR = _PARKINGSPACE.enum_types_by_name['ParkingDir']
_MAPOBSTACLE_MAPOBSTACLETYPE = _MAPOBSTACLE.enum_types_by_name['MapObstacleType']
_OBJECTDETECTIONOBSTACLE_OBJECTDETECTIONOBSTACLETYPE = _OBJECTDETECTIONOBSTACLE.enum_types_by_name['ObjectDetectionObstacleType']
_OBJECTDETECTIONOBSTACLE_OBJALARMLEVEL = _OBJECTDETECTIONOBSTACLE.enum_types_by_name['ObjAlarmLevel']
_PAS_DISTANCE = _PAS.enum_types_by_name['Distance']
_SIGNLINEVERTICAL_LINETYPE = _SIGNLINEVERTICAL.enum_types_by_name['LineType']
_SIGNLINEVERTICAL_LINESHAPE = _SIGNLINEVERTICAL.enum_types_by_name['LineShape']
_SIGNLINEVERTICAL_LINEMATERIAL = _SIGNLINEVERTICAL.enum_types_by_name['LineMaterial']
_SIGNPOLYGON_POLYGONTYPE = _SIGNPOLYGON.enum_types_by_name['PolygonType']
_AVPMAPPIN_AVPMAPPINTAG = _AVPMAPPIN.enum_types_by_name['AVPMapPinTag']
Coor3 = _reflection.GeneratedProtocolMessageType('Coor3', (_message.Message,), {
  'DESCRIPTOR' : _COOR3,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.Coor3)
  })
_sym_db.RegisterMessage(Coor3)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.Point)
  })
_sym_db.RegisterMessage(Point)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.Location)
  })
_sym_db.RegisterMessage(Location)

Pnt3D = _reflection.GeneratedProtocolMessageType('Pnt3D', (_message.Message,), {
  'DESCRIPTOR' : _PNT3D,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.Pnt3D)
  })
_sym_db.RegisterMessage(Pnt3D)

BoundingBox = _reflection.GeneratedProtocolMessageType('BoundingBox', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDINGBOX,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.BoundingBox)
  })
_sym_db.RegisterMessage(BoundingBox)

ObstaclePose = _reflection.GeneratedProtocolMessageType('ObstaclePose', (_message.Message,), {
  'DESCRIPTOR' : _OBSTACLEPOSE,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.ObstaclePose)
  })
_sym_db.RegisterMessage(ObstaclePose)

ParkingSpace = _reflection.GeneratedProtocolMessageType('ParkingSpace', (_message.Message,), {

  'ParkSpaceBoundingBox' : _reflection.GeneratedProtocolMessageType('ParkSpaceBoundingBox', (_message.Message,), {
    'DESCRIPTOR' : _PARKINGSPACE_PARKSPACEBOUNDINGBOX,
    '__module__' : 'drapi.gwm.havp.havp_common_pb2'
    # @@protoc_insertion_point(class_scope:havp.ParkingSpace.ParkSpaceBoundingBox)
    })
  ,
  'DESCRIPTOR' : _PARKINGSPACE,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.ParkingSpace)
  })
_sym_db.RegisterMessage(ParkingSpace)
_sym_db.RegisterMessage(ParkingSpace.ParkSpaceBoundingBox)

MapObstacle = _reflection.GeneratedProtocolMessageType('MapObstacle', (_message.Message,), {
  'DESCRIPTOR' : _MAPOBSTACLE,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.MapObstacle)
  })
_sym_db.RegisterMessage(MapObstacle)

ObjectDetectionObstacle = _reflection.GeneratedProtocolMessageType('ObjectDetectionObstacle', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDETECTIONOBSTACLE,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.ObjectDetectionObstacle)
  })
_sym_db.RegisterMessage(ObjectDetectionObstacle)

WallElement = _reflection.GeneratedProtocolMessageType('WallElement', (_message.Message,), {
  'DESCRIPTOR' : _WALLELEMENT,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.WallElement)
  })
_sym_db.RegisterMessage(WallElement)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), {
  'DESCRIPTOR' : _POLYGON,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.Polygon)
  })
_sym_db.RegisterMessage(Polygon)

Polyline = _reflection.GeneratedProtocolMessageType('Polyline', (_message.Message,), {
  'DESCRIPTOR' : _POLYLINE,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.Polyline)
  })
_sym_db.RegisterMessage(Polyline)

PAS = _reflection.GeneratedProtocolMessageType('PAS', (_message.Message,), {
  'DESCRIPTOR' : _PAS,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.PAS)
  })
_sym_db.RegisterMessage(PAS)

SignlineVertical = _reflection.GeneratedProtocolMessageType('SignlineVertical', (_message.Message,), {
  'DESCRIPTOR' : _SIGNLINEVERTICAL,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.SignlineVertical)
  })
_sym_db.RegisterMessage(SignlineVertical)

SignPolygon = _reflection.GeneratedProtocolMessageType('SignPolygon', (_message.Message,), {
  'DESCRIPTOR' : _SIGNPOLYGON,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.SignPolygon)
  })
_sym_db.RegisterMessage(SignPolygon)

AVPMapPin = _reflection.GeneratedProtocolMessageType('AVPMapPin', (_message.Message,), {
  'DESCRIPTOR' : _AVPMAPPIN,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.AVPMapPin)
  })
_sym_db.RegisterMessage(AVPMapPin)

Road = _reflection.GeneratedProtocolMessageType('Road', (_message.Message,), {
  'DESCRIPTOR' : _ROAD,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.Road)
  })
_sym_db.RegisterMessage(Road)

AVPMap = _reflection.GeneratedProtocolMessageType('AVPMap', (_message.Message,), {
  'DESCRIPTOR' : _AVPMAP,
  '__module__' : 'drapi.gwm.havp.havp_common_pb2'
  # @@protoc_insertion_point(class_scope:havp.AVPMap)
  })
_sym_db.RegisterMessage(AVPMap)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COLOR._serialized_start=7357
  _COLOR._serialized_end=7463
  _HAVPNAVITIPS._serialized_start=7466
  _HAVPNAVITIPS._serialized_end=7759
  _COOR3._serialized_start=42
  _COOR3._serialized_end=82
  _POINT._serialized_start=84
  _POINT._serialized_end=139
  _LOCATION._serialized_start=141
  _LOCATION._serialized_end=241
  _PNT3D._serialized_start=243
  _PNT3D._serialized_end=283
  _BOUNDINGBOX._serialized_start=286
  _BOUNDINGBOX._serialized_end=579
  _OBSTACLEPOSE._serialized_start=581
  _OBSTACLEPOSE._serialized_end=642
  _PARKINGSPACE._serialized_start=645
  _PARKINGSPACE._serialized_end=2931
  _PARKINGSPACE_PARKSPACEBOUNDINGBOX._serialized_start=1250
  _PARKINGSPACE_PARKSPACEBOUNDINGBOX._serialized_end=1557
  _PARKINGSPACE_PARKSPACEBOUNDINGBOX_PARKSPACEPOSITION._serialized_start=1397
  _PARKINGSPACE_PARKSPACEBOUNDINGBOX_PARKSPACEPOSITION._serialized_end=1557
  _PARKINGSPACE_PARKINGSPACETYPE._serialized_start=1560
  _PARKINGSPACE_PARKINGSPACETYPE._serialized_end=1721
  _PARKINGSPACE_PARKINGSPACESTATUS._serialized_start=1724
  _PARKINGSPACE_PARKINGSPACESTATUS._serialized_end=2004
  _PARKINGSPACE_PARKINGSPACEUSAGE._serialized_start=2006
  _PARKINGSPACE_PARKINGSPACEUSAGE._serialized_end=2107
  _PARKINGSPACE_PARKINGSPACEOBSTACLETYPE._serialized_start=2110
  _PARKINGSPACE_PARKINGSPACEOBSTACLETYPE._serialized_end=2470
  _PARKINGSPACE_PARKINGSPACETAG._serialized_start=2473
  _PARKINGSPACE_PARKINGSPACETAG._serialized_end=2632
  _PARKINGSPACE_PARKINGSPACESIZETYPE._serialized_start=2635
  _PARKINGSPACE_PARKINGSPACESIZETYPE._serialized_end=2787
  _PARKINGSPACE_PARKINGDIR._serialized_start=2790
  _PARKINGSPACE_PARKINGDIR._serialized_end=2931
  _MAPOBSTACLE._serialized_start=2934
  _MAPOBSTACLE._serialized_end=3203
  _MAPOBSTACLE_MAPOBSTACLETYPE._serialized_start=3068
  _MAPOBSTACLE_MAPOBSTACLETYPE._serialized_end=3203
  _OBJECTDETECTIONOBSTACLE._serialized_start=3206
  _OBJECTDETECTIONOBSTACLE._serialized_end=4948
  _OBJECTDETECTIONOBSTACLE_OBJECTDETECTIONOBSTACLETYPE._serialized_start=3450
  _OBJECTDETECTIONOBSTACLE_OBJECTDETECTIONOBSTACLETYPE._serialized_end=4825
  _OBJECTDETECTIONOBSTACLE_OBJALARMLEVEL._serialized_start=4827
  _OBJECTDETECTIONOBSTACLE_OBJALARMLEVEL._serialized_end=4948
  _WALLELEMENT._serialized_start=4950
  _WALLELEMENT._serialized_end=5028
  _POLYGON._serialized_start=5030
  _POLYGON._serialized_end=5065
  _POLYLINE._serialized_start=5067
  _POLYLINE._serialized_end=5103
  _PAS._serialized_start=5106
  _PAS._serialized_end=6123
  _PAS_DISTANCE._serialized_start=5874
  _PAS_DISTANCE._serialized_end=6123
  _SIGNLINEVERTICAL._serialized_start=6126
  _SIGNLINEVERTICAL._serialized_end=6709
  _SIGNLINEVERTICAL_LINETYPE._serialized_start=6371
  _SIGNLINEVERTICAL_LINETYPE._serialized_end=6425
  _SIGNLINEVERTICAL_LINESHAPE._serialized_start=6428
  _SIGNLINEVERTICAL_LINESHAPE._serialized_end=6589
  _SIGNLINEVERTICAL_LINEMATERIAL._serialized_start=6591
  _SIGNLINEVERTICAL_LINEMATERIAL._serialized_end=6709
  _SIGNPOLYGON._serialized_start=6712
  _SIGNPOLYGON._serialized_end=6966
  _SIGNPOLYGON_POLYGONTYPE._serialized_start=6844
  _SIGNPOLYGON_POLYGONTYPE._serialized_end=6966
  _AVPMAPPIN._serialized_start=6969
  _AVPMAPPIN._serialized_end=7272
  _AVPMAPPIN_AVPMAPPINTAG._serialized_start=7124
  _AVPMAPPIN_AVPMAPPINTAG._serialized_end=7272
  _ROAD._serialized_start=7274
  _ROAD._serialized_end=7318
  _AVPMAP._serialized_start=7320
  _AVPMAP._serialized_end=7355
# @@protoc_insertion_point(module_scope)
