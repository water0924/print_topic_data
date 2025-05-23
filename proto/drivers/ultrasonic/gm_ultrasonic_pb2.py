# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drivers/ultrasonic/gm_ultrasonic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&drivers/ultrasonic/gm_ultrasonic.proto\x12\x1b\x64\x65\x65proute.gm.c01.ultrasonic\"\xe0\x02\n\x10UltrasonicObject\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x10\n\x08\x64istance\x18\x02 \x01(\x02\x12\x12\n\necho_width\x18\x03 \x01(\x02\x12\x13\n\x0b\x65\x63ho_height\x18\x04 \x01(\x02\x12\x12\n\nconfidence\x18\x05 \x01(\x02\x12\x1b\n\x13\x63ross_distance_left\x18\x06 \x01(\x02\x12\x17\n\x0fleft_echo_width\x18\x07 \x01(\x02\x12\x18\n\x10left_echo_height\x18\x08 \x01(\x02\x12\x1c\n\x14left_echo_confidence\x18\t \x01(\x02\x12\x1c\n\x14\x63ross_distance_right\x18\n \x01(\x02\x12\x18\n\x10right_echo_width\x18\x0b \x01(\x02\x12\x19\n\x11right_echo_height\x18\x0c \x01(\x02\x12\x1d\n\x15right_echo_confidence\x18\r \x01(\x02\x12\n\n\x02id\x18\x0e \x01(\r\"\xac\x05\n\x12UltrasonicObstacle\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12S\n\x0fobstacle_height\x18\x02 \x01(\x0e\x32:.deeproute.gm.c01.ultrasonic.UltrasonicObstacle.HeightType\x12\x1c\n\x14obstacle_height_prob\x18\x03 \x01(\x02\x12\x10\n\x08point1_x\x18\x04 \x01(\x02\x12\x10\n\x08point1_y\x18\x05 \x01(\x02\x12\x10\n\x08point2_x\x18\x06 \x01(\x02\x12\x10\n\x08point2_y\x18\x07 \x01(\x02\x12S\n\robstacle_type\x18\x08 \x01(\x0e\x32<.deeproute.gm.c01.ultrasonic.UltrasonicObstacle.ObstacleType\x12\x12\n\nconfidence\x18\t \x01(\x02\x12\n\n\x02id\x18\n \x01(\r\"\x88\x01\n\nHeightType\x12\x13\n\x0fHEIGHT_TYPE_LOW\x10\x00\x12\x15\n\x11HEIGHT_TYPE_HIGHT\x10\x01\x12\x1b\n\x17HEIGHT_TYPE_TRAVERSIBLE\x10\x02\x12\x17\n\x13HEIGHT_TYPE_UNKNOWN\x10\x03\x12\x18\n\x14HEIGHT_TYPE_SPECIAL1\x10\x04\"\xc7\x01\n\x0cObstacleType\x12\x16\n\x12OBSTACLE_TYPE_NONE\x10\x00\x12\x17\n\x13OBSTACLE_TYPE_POINT\x10\x01\x12\"\n\x1eOBSTACLE_TYPE_STRAIGHT0_CORNER\x10\x02\x12\"\n\x1eOBSTACLE_TYPE_STRAIGHT1_CORNER\x10\x03\x12\"\n\x1eOBSTACLE_TYPE_STRAIGHT2_CORNER\x10\x04\x12\x1a\n\x16OBSTACLE_TYPE_RESERVED\x10\x05\"\xf1\r\n\x15UltrasonicParkingSlot\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\n\n\x02id\x18\x02 \x01(\r\x12Z\n\x0f\x64\x65pth_reference\x18\x03 \x01(\x0e\x32\x41.deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot.DepthReference\x12N\n\tslot_type\x18\x04 \x01(\x0e\x32;.deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot.SlotType\x12\r\n\x05\x64\x65pth\x18\x05 \x01(\x02\x12\x17\n\x0fobj1_start_pt_x\x18\x06 \x01(\x02\x12\x17\n\x0fobj1_start_pt_y\x18\x07 \x01(\x02\x12[\n\x14obj1_start_pt_status\x18\x08 \x01(\x0e\x32=.deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot.ObjectType\x12\x15\n\robj1_end_pt_x\x18\t \x01(\x02\x12\x15\n\robj1_end_pt_y\x18\n \x01(\x02\x12Y\n\x12obj1_end_pt_status\x18\x0b \x01(\x0e\x32=.deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot.ObjectType\x12\x17\n\x0fobj2_start_pt_x\x18\x0c \x01(\x02\x12\x17\n\x0fobj2_start_pt_y\x18\r \x01(\x02\x12[\n\x14obj2_start_pt_status\x18\x0e \x01(\x0e\x32=.deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot.ObjectType\x12\x15\n\robj2_end_pt_x\x18\x0f \x01(\x02\x12\x15\n\robj2_end_pt_y\x18\x10 \x01(\x02\x12Y\n\x12obj2_end_pt_status\x18\x11 \x01(\x0e\x32=.deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot.ObjectType\x12\x1b\n\x13slot_obj_start_pt_x\x18\x12 \x01(\x02\x12\x1b\n\x13slot_obj_start_pt_y\x18\x13 \x01(\x02\x12_\n\x18slot_obj_start_pt_status\x18\x14 \x01(\x0e\x32=.deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot.ObjectType\x12\x19\n\x11slot_obj_end_pt_x\x18\x15 \x01(\x02\x12\x19\n\x11slot_obj_end_pt_y\x18\x16 \x01(\x02\x12]\n\x16slot_obj_end_pt_status\x18\x17 \x01(\x0e\x32=.deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot.ObjectType\x12\x0e\n\x06length\x18\x18 \x01(\x02\"\xe9\x01\n\x0e\x44\x65pthReference\x12\x18\n\x14\x44\x45PTH_REFERENCE_NONE\x10\x00\x12\x18\n\x14\x44\x45PTH_REFERENCE_CURB\x10\x01\x12\x18\n\x14\x44\x45PTH_REFERENCE_WALL\x10\x02\x12\x1b\n\x17\x44\x45PTH_REFERENCE_VIRTUAL\x10\x03\x12\x17\n\x13\x44\x45PTH_REFERENCE_LOW\x10\x04\x12\x18\n\x14\x44\x45PTH_REFERENCE_HIGH\x10\x05\x12\x1b\n\x17\x44\x45PTH_REFERENCE_UNKNOWN\x10\x06\x12\x1c\n\x18\x44\x45PTH_REFERENCE_RESERVED\x10\x07\"\xdc\x01\n\x08SlotType\x12\x1b\n\x17SLOT_TYPE_LEFT_PARALLEL\x10\x00\x12\x1c\n\x18SLOT_TYPE_RIGHT_PARALLEL\x10\x01\x12\x18\n\x14SLOT_TYPE_LEFT_CROSS\x10\x02\x12\x19\n\x15SLOT_TYPE_RIGHT_CROSS\x10\x03\x12\x17\n\x13SLOT_TYPE_RESERVED1\x10\x04\x12\x17\n\x13SLOT_TYPE_RESERVED2\x10\x05\x12\x17\n\x13SLOT_TYPE_RESERVED3\x10\x06\x12\x15\n\x11SLOT_TYPE_INVALID\x10\x07\"V\n\nSlotStatus\x12\x17\n\x13SLOT_STATUS_PS_NONE\x10\x00\x12\x15\n\x11SLOT_STATUS_PS_OK\x10\x01\x12\x18\n\x14SLOT_STATUS_RESERVED\x10\x02\"k\n\nObjectType\x12\x14\n\x10OBJECT_TYPE_NONE\x10\x00\x12\x17\n\x13OBJECT_TYPE_VIRTUAL\x10\x01\x12\x14\n\x10OBJECT_TYPE_REAL\x10\x02\x12\x18\n\x14OBJECT_TYPE_RESERVED\x10\x03\"\xd7\x08\n\x0fUltrasonicState\x12N\n\x0c\x66pas_worksts\x18\x01 \x01(\x0e\x32\x38.deeproute.gm.c01.ultrasonic.UltrasonicState.FPASWorkSts\x12N\n\x0crpas_worksts\x18\x02 \x01(\x0e\x32\x38.deeproute.gm.c01.ultrasonic.UltrasonicState.RPASWorkSts\x12R\n\x0e\x61pasys_worksts\x18\x03 \x01(\x0e\x32:.deeproute.gm.c01.ultrasonic.UltrasonicState.APASysWorkSts\x12]\n\x14pdc_timestamp_status\x18\x04 \x01(\x0e\x32?.deeproute.gm.c01.ultrasonic.UltrasonicState.PDCTimeStampStatus\x12\x1f\n\x17object_detect_area_list\x18\x05 \x03(\r\x12\x14\n\x0c\x66pas_dispcmd\x18\x06 \x01(\x08\x12\x1f\n\x17\x46PAS_FLCornrSnsrFailSts\x18\x07 \x01(\x08\x12\x1f\n\x17\x46PAS_FLMiddlSnsrFailSts\x18\x08 \x01(\x08\x12\x1f\n\x17\x46PAS_FRMiddlSnsrFailSts\x18\t \x01(\x08\x12\x1f\n\x17\x46PAS_FRCornrSnsrFailSts\x18\n \x01(\x08\x12\x1f\n\x17RPAS_RLCornrSnsrFailSts\x18\x0b \x01(\x08\x12\x1f\n\x17RPAS_RLMiddlSnsrFailSts\x18\x0c \x01(\x08\x12\x1f\n\x17RPAS_RRMiddlSnsrFailSts\x18\r \x01(\x08\x12\x1f\n\x17RPAS_RRCornrSnsrFailSts\x18\x0e \x01(\x08\"R\n\x0b\x46PASWorkSts\x12\x10\n\x0c\x46PAS_DISABLE\x10\x00\x12\x0f\n\x0b\x46PAS_ENABLE\x10\x01\x12\x0f\n\x0b\x46PAS_ACTIVE\x10\x02\x12\x0f\n\x0b\x46PAS_FAILED\x10\x03\"R\n\x0bRPASWorkSts\x12\x10\n\x0cRPAS_DISABLE\x10\x00\x12\x0f\n\x0bRPAS_ENABLE\x10\x01\x12\x0f\n\x0bRPAS_ACTIVE\x10\x02\x12\x0f\n\x0bRPAS_FAILED\x10\x03\"\\\n\rAPASysWorkSts\x12\x12\n\x0e\x41PASys_DISABLE\x10\x00\x12\x11\n\rAPASys_ENABLE\x10\x01\x12\x11\n\rAPASys_ACTIVE\x10\x02\x12\x11\n\rAPASys_FAILED\x10\x03\"\xab\x01\n\x12PDCTimeStampStatus\x12\x0b\n\x07TIMEOUT\x10\x00\x12\x0e\n\nRESPONSE_A\x10\x01\x12\x13\n\x0fSYNC_TO_GATEWAY\x10\x02\x12\x14\n\x10GLOBAL_TIME_BASE\x10\x03\x12\x13\n\x0fTIMELEAP_FUTURE\x10\x04\x12\x11\n\rTIMELEAP_PAST\x10\x05\x12\x0e\n\nRESPONSE_B\x10\x06\x12\x15\n\x11\x45XT_GENERAL_ERROR\x10\x07\"f\n\x15UltrasonicObjectArray\x12\r\n\x05\x63\x61nid\x18\x01 \x01(\r\x12>\n\x07objects\x18\x02 \x03(\x0b\x32-.deeproute.gm.c01.ultrasonic.UltrasonicObject\"l\n\x17UltrasonicObstacleArray\x12\r\n\x05\x63\x61nid\x18\x01 \x01(\r\x12\x42\n\tobstacles\x18\x02 \x03(\x0b\x32/.deeproute.gm.c01.ultrasonic.UltrasonicObstacle\"v\n\x1aUltrasonicParkingSlotArray\x12\r\n\x05\x63\x61nid\x18\x01 \x01(\r\x12I\n\rparking_slots\x18\x02 \x03(\x0b\x32\x32.deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot\"f\n\x14UltrasonicStateArray\x12\r\n\x05\x63\x61nid\x18\x01 \x01(\r\x12?\n\tuss_state\x18\x02 \x01(\x0b\x32,.deeproute.gm.c01.ultrasonic.UltrasonicState\"\xda\x01\n\x10UltrasonicHeader\x12\x13\n\x0b\x63\x61nframenum\x18\x01 \x01(\r\x12\x0e\n\x06\x62itmap\x18\x02 \x01(\x04\x12\x12\n\ndatalength\x18\x03 \x01(\r\x12\x17\n\x0frolling_counter\x18\x04 \x01(\r\"t\n\x13UltrasonicArrayType\x12\x14\n\x10USS_OBJECT_ARRAY\x10\x00\x12\x16\n\x12USS_OBSTACLE_ARRAY\x10\x01\x12\x1a\n\x16USS_PARKING_SLOT_ARRAY\x10\x02\x12\x13\n\x0fUSS_STATE_ARRAY\x10\x03')



_ULTRASONICOBJECT = DESCRIPTOR.message_types_by_name['UltrasonicObject']
_ULTRASONICOBSTACLE = DESCRIPTOR.message_types_by_name['UltrasonicObstacle']
_ULTRASONICPARKINGSLOT = DESCRIPTOR.message_types_by_name['UltrasonicParkingSlot']
_ULTRASONICSTATE = DESCRIPTOR.message_types_by_name['UltrasonicState']
_ULTRASONICOBJECTARRAY = DESCRIPTOR.message_types_by_name['UltrasonicObjectArray']
_ULTRASONICOBSTACLEARRAY = DESCRIPTOR.message_types_by_name['UltrasonicObstacleArray']
_ULTRASONICPARKINGSLOTARRAY = DESCRIPTOR.message_types_by_name['UltrasonicParkingSlotArray']
_ULTRASONICSTATEARRAY = DESCRIPTOR.message_types_by_name['UltrasonicStateArray']
_ULTRASONICHEADER = DESCRIPTOR.message_types_by_name['UltrasonicHeader']
_ULTRASONICOBSTACLE_HEIGHTTYPE = _ULTRASONICOBSTACLE.enum_types_by_name['HeightType']
_ULTRASONICOBSTACLE_OBSTACLETYPE = _ULTRASONICOBSTACLE.enum_types_by_name['ObstacleType']
_ULTRASONICPARKINGSLOT_DEPTHREFERENCE = _ULTRASONICPARKINGSLOT.enum_types_by_name['DepthReference']
_ULTRASONICPARKINGSLOT_SLOTTYPE = _ULTRASONICPARKINGSLOT.enum_types_by_name['SlotType']
_ULTRASONICPARKINGSLOT_SLOTSTATUS = _ULTRASONICPARKINGSLOT.enum_types_by_name['SlotStatus']
_ULTRASONICPARKINGSLOT_OBJECTTYPE = _ULTRASONICPARKINGSLOT.enum_types_by_name['ObjectType']
_ULTRASONICSTATE_FPASWORKSTS = _ULTRASONICSTATE.enum_types_by_name['FPASWorkSts']
_ULTRASONICSTATE_RPASWORKSTS = _ULTRASONICSTATE.enum_types_by_name['RPASWorkSts']
_ULTRASONICSTATE_APASYSWORKSTS = _ULTRASONICSTATE.enum_types_by_name['APASysWorkSts']
_ULTRASONICSTATE_PDCTIMESTAMPSTATUS = _ULTRASONICSTATE.enum_types_by_name['PDCTimeStampStatus']
_ULTRASONICHEADER_ULTRASONICARRAYTYPE = _ULTRASONICHEADER.enum_types_by_name['UltrasonicArrayType']
UltrasonicObject = _reflection.GeneratedProtocolMessageType('UltrasonicObject', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICOBJECT,
  '__module__' : 'drivers.ultrasonic.gm_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.gm.c01.ultrasonic.UltrasonicObject)
  })
_sym_db.RegisterMessage(UltrasonicObject)

UltrasonicObstacle = _reflection.GeneratedProtocolMessageType('UltrasonicObstacle', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICOBSTACLE,
  '__module__' : 'drivers.ultrasonic.gm_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.gm.c01.ultrasonic.UltrasonicObstacle)
  })
_sym_db.RegisterMessage(UltrasonicObstacle)

UltrasonicParkingSlot = _reflection.GeneratedProtocolMessageType('UltrasonicParkingSlot', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICPARKINGSLOT,
  '__module__' : 'drivers.ultrasonic.gm_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.gm.c01.ultrasonic.UltrasonicParkingSlot)
  })
_sym_db.RegisterMessage(UltrasonicParkingSlot)

UltrasonicState = _reflection.GeneratedProtocolMessageType('UltrasonicState', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICSTATE,
  '__module__' : 'drivers.ultrasonic.gm_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.gm.c01.ultrasonic.UltrasonicState)
  })
_sym_db.RegisterMessage(UltrasonicState)

UltrasonicObjectArray = _reflection.GeneratedProtocolMessageType('UltrasonicObjectArray', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICOBJECTARRAY,
  '__module__' : 'drivers.ultrasonic.gm_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.gm.c01.ultrasonic.UltrasonicObjectArray)
  })
_sym_db.RegisterMessage(UltrasonicObjectArray)

UltrasonicObstacleArray = _reflection.GeneratedProtocolMessageType('UltrasonicObstacleArray', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICOBSTACLEARRAY,
  '__module__' : 'drivers.ultrasonic.gm_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.gm.c01.ultrasonic.UltrasonicObstacleArray)
  })
_sym_db.RegisterMessage(UltrasonicObstacleArray)

UltrasonicParkingSlotArray = _reflection.GeneratedProtocolMessageType('UltrasonicParkingSlotArray', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICPARKINGSLOTARRAY,
  '__module__' : 'drivers.ultrasonic.gm_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.gm.c01.ultrasonic.UltrasonicParkingSlotArray)
  })
_sym_db.RegisterMessage(UltrasonicParkingSlotArray)

UltrasonicStateArray = _reflection.GeneratedProtocolMessageType('UltrasonicStateArray', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICSTATEARRAY,
  '__module__' : 'drivers.ultrasonic.gm_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.gm.c01.ultrasonic.UltrasonicStateArray)
  })
_sym_db.RegisterMessage(UltrasonicStateArray)

UltrasonicHeader = _reflection.GeneratedProtocolMessageType('UltrasonicHeader', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICHEADER,
  '__module__' : 'drivers.ultrasonic.gm_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.gm.c01.ultrasonic.UltrasonicHeader)
  })
_sym_db.RegisterMessage(UltrasonicHeader)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ULTRASONICOBJECT._serialized_start=72
  _ULTRASONICOBJECT._serialized_end=424
  _ULTRASONICOBSTACLE._serialized_start=427
  _ULTRASONICOBSTACLE._serialized_end=1111
  _ULTRASONICOBSTACLE_HEIGHTTYPE._serialized_start=773
  _ULTRASONICOBSTACLE_HEIGHTTYPE._serialized_end=909
  _ULTRASONICOBSTACLE_OBSTACLETYPE._serialized_start=912
  _ULTRASONICOBSTACLE_OBSTACLETYPE._serialized_end=1111
  _ULTRASONICPARKINGSLOT._serialized_start=1114
  _ULTRASONICPARKINGSLOT._serialized_end=2891
  _ULTRASONICPARKINGSLOT_DEPTHREFERENCE._serialized_start=2238
  _ULTRASONICPARKINGSLOT_DEPTHREFERENCE._serialized_end=2471
  _ULTRASONICPARKINGSLOT_SLOTTYPE._serialized_start=2474
  _ULTRASONICPARKINGSLOT_SLOTTYPE._serialized_end=2694
  _ULTRASONICPARKINGSLOT_SLOTSTATUS._serialized_start=2696
  _ULTRASONICPARKINGSLOT_SLOTSTATUS._serialized_end=2782
  _ULTRASONICPARKINGSLOT_OBJECTTYPE._serialized_start=2784
  _ULTRASONICPARKINGSLOT_OBJECTTYPE._serialized_end=2891
  _ULTRASONICSTATE._serialized_start=2894
  _ULTRASONICSTATE._serialized_end=4005
  _ULTRASONICSTATE_FPASWORKSTS._serialized_start=3571
  _ULTRASONICSTATE_FPASWORKSTS._serialized_end=3653
  _ULTRASONICSTATE_RPASWORKSTS._serialized_start=3655
  _ULTRASONICSTATE_RPASWORKSTS._serialized_end=3737
  _ULTRASONICSTATE_APASYSWORKSTS._serialized_start=3739
  _ULTRASONICSTATE_APASYSWORKSTS._serialized_end=3831
  _ULTRASONICSTATE_PDCTIMESTAMPSTATUS._serialized_start=3834
  _ULTRASONICSTATE_PDCTIMESTAMPSTATUS._serialized_end=4005
  _ULTRASONICOBJECTARRAY._serialized_start=4007
  _ULTRASONICOBJECTARRAY._serialized_end=4109
  _ULTRASONICOBSTACLEARRAY._serialized_start=4111
  _ULTRASONICOBSTACLEARRAY._serialized_end=4219
  _ULTRASONICPARKINGSLOTARRAY._serialized_start=4221
  _ULTRASONICPARKINGSLOTARRAY._serialized_end=4339
  _ULTRASONICSTATEARRAY._serialized_start=4341
  _ULTRASONICSTATEARRAY._serialized_end=4443
  _ULTRASONICHEADER._serialized_start=4446
  _ULTRASONICHEADER._serialized_end=4664
  _ULTRASONICHEADER_ULTRASONICARRAYTYPE._serialized_start=4548
  _ULTRASONICHEADER_ULTRASONICARRAYTYPE._serialized_end=4664
# @@protoc_insertion_point(module_scope)
