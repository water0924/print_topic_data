# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smart/driving/smart_driving_object.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.smart import smart_common_pb2 as smart_dot_smart__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(smart/driving/smart_driving_object.proto\x12\x05smart\x1a\x18smart/smart_common.proto\"\xb7\x01\n\x06\x45goVeh\x12\x12\n\ntime_stamp\x18\x01 \x01(\x04\x12\'\n\x0bvehicle_pos\x18\x02 \x01(\x0b\x32\x12.smart.Vehicle_Pos\x12%\n\nguide_line\x18\x03 \x01(\x0b\x32\x11.smart.Guide_Line\x12\x1d\n\x04objs\x18\x04 \x01(\x0b\x32\x0f.smart.Obj_Disp\x12*\n\x0f\x64\x65\x63\x65lerate_line\x18\x06 \x01(\x0b\x32\x11.smart.Guide_Line\"\x96\x01\n\x0bVehicle_Pos\x12\x11\n\tlongitude\x18\x05 \x01(\x02\x12\x10\n\x08latitude\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x02\x12\r\n\x05speed\x18\x08 \x01(\x02\x12\x19\n\x03pos\x18\t \x01(\x0b\x32\x0c.smart.Pnt3D\x12\x0b\n\x03yaw\x18\n \x01(\x01\x12\r\n\x05pitch\x18\x0b \x01(\x01\x12\x0c\n\x04roll\x18\x0c \x01(\x01\"\'\n\nGuide_Line\x12\x19\n\x03pnt\x18\x01 \x03(\x0b\x32\x0c.smart.Pnt3D\"A\n\x08Obj_Disp\x12\x12\n\ntime_stamp\x18\x01 \x01(\x04\x12!\n\x08obj_info\x18\x02 \x03(\x0b\x32\x0f.smart.Obj_Info\"\xd6\x08\n\x08Obj_Info\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x19\n\x03pos\x18\x02 \x01(\x0b\x32\x0c.smart.Pnt3D\x12\r\n\x05speed\x18\x03 \x01(\x02\x12\x0f\n\x07heading\x18\x04 \x01(\x02\x12&\n\x04type\x18\x05 \x01(\x0e\x32\x18.smart.Obj_Info.Obj_Type\x12\x0e\n\x06length\x18\x06 \x01(\x02\x12\r\n\x05width\x18\x07 \x01(\x02\x12\x0e\n\x06height\x18\x08 \x01(\x02\x12(\n\x0clight_status\x18\t \x03(\x0b\x32\x12.smart.LightStatus\x12\x35\n\x0e\x61ttribute_type\x18\n \x03(\x0e\x32\x1d.smart.Obj_Info.AttributeType\x12/\n\x0bobject_type\x18\x0b \x01(\x0e\x32\x1a.smart.Obj_Info.ObjectType\x12\x10\n\x08\x64istance\x18\x0c \x01(\x02\"\xcc\x04\n\x08Obj_Type\x12\x14\n\x10OBJ_TYPE_UNKNOWN\x10\x00\x12\x1a\n\x16OBJ_TYPE_PASSENGER_CAR\x10\x01\x12\x16\n\x12OBJ_TYPE_TRUCK_BOX\x10\x02\x12\x10\n\x0cOBJ_TYPE_BUS\x10\x03\x12\x14\n\x10OBJ_TYPE_BICYCLE\x10\x04\x12\x17\n\x13OBJ_TYPE_MOTORCYCLE\x10\x05\x12\x15\n\x11OBJ_TYPE_TRICYCLE\x10\x06\x12\x17\n\x13OBJ_TYPE_PEDESTRIAN\x10\x07\x12\x12\n\x0eOBJ_TYPE_CHILD\x10\x08\x12\x11\n\rOBJ_TYPE_CONE\x10\t\x12\x10\n\x0cOBJ_TYPE_SUV\x10\n\x12\x14\n\x10OBJ_TYPE_MINIBUS\x10\x0b\x12\x1c\n\x18OBJ_TYPE_ELETIRC_BICYCLE\x10\x0c\x12\x13\n\x0fOBJ_TYPE_POLICE\x10\r\x12\x13\n\x0fOBJ_TYPE_BUCKET\x10\x0e\x12\x13\n\x0fOBJ_TYPE_TRIPOD\x10\x0f\x12!\n\x1dOBJ_TYPE_WATER_FILLED_BARRIER\x10\x10\x12\x13\n\x0fOBJ_TYPE_PICKUP\x10\x11\x12\x17\n\x13OBJ_TYPE_TRUCK_FLAT\x10\x12\x12\x1d\n\x19OBJ_TYPE_SPECIAL_VEHICLES\x10\x13\x12\x15\n\x11OBJ_TYPE_SCAFFOLD\x10\x14\x12\x13\n\x0fOBJ_TYPE_PILLAR\x10\x15\x12\x16\n\x12OBJ_TYPE_SPEEDBUMP\x10\x16\x12\x12\n\x0eOBJ_TYPE_CHOCK\x10\x17\x12\x11\n\rOBJ_TYPE_LOCK\x10\x18\"Y\n\rAttributeType\x12\x0f\n\x0bNORMAL_TYPE\x10\x00\x12\x12\n\x0eLEFT_DOOR_OPEN\x10\x01\x12\x13\n\x0fRIGHT_DOOR_OPEN\x10\x02\x12\x0e\n\nTRUNK_OPEN\x10\x03\"^\n\nObjectType\x12\x15\n\x11\x44\x45\x46\x41ULT_ALARM_OBJ\x10\x00\x12\x12\n\x0eGRAY_ALARM_OBJ\x10\x01\x12\x12\n\x0e\x42LUE_ALARM_OBJ\x10\x02\x12\x11\n\rRED_ALARM_OBJ\x10\x03\"\xa2\x01\n\x0bLightStatus\x12\x17\n\x0f\x62rake_switch_on\x18\x01 \x01(\x08\x12\x1b\n\x13left_turn_switch_on\x18\x02 \x01(\x08\x12\x1c\n\x14right_turn_switch_on\x18\x03 \x01(\x08\x12!\n\x19left_right_turn_switch_on\x18\x04 \x01(\x08\x12\x1c\n\x14\x62rake_switch_unknown\x18\x05 \x01(\x08\"\xc5\x01\n\x0e\x43riticalObject\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x35\n\x0bobject_type\x18\x02 \x01(\x0e\x32 .smart.CriticalObject.ObjectType\x12\x10\n\x08\x64istance\x18\x03 \x01(\x02\"^\n\nObjectType\x12\x12\n\x0eGRAY_ALARM_OBJ\x10\x00\x12\x12\n\x0e\x42LUE_ALARM_OBJ\x10\x01\x12\x11\n\rRED_ALARM_OBJ\x10\x02\x12\x15\n\x11\x44\x45\x46\x41ULT_ALARM_OBJ\x10\x03\x62\x06proto3')



_EGOVEH = DESCRIPTOR.message_types_by_name['EgoVeh']
_VEHICLE_POS = DESCRIPTOR.message_types_by_name['Vehicle_Pos']
_GUIDE_LINE = DESCRIPTOR.message_types_by_name['Guide_Line']
_OBJ_DISP = DESCRIPTOR.message_types_by_name['Obj_Disp']
_OBJ_INFO = DESCRIPTOR.message_types_by_name['Obj_Info']
_LIGHTSTATUS = DESCRIPTOR.message_types_by_name['LightStatus']
_CRITICALOBJECT = DESCRIPTOR.message_types_by_name['CriticalObject']
_OBJ_INFO_OBJ_TYPE = _OBJ_INFO.enum_types_by_name['Obj_Type']
_OBJ_INFO_ATTRIBUTETYPE = _OBJ_INFO.enum_types_by_name['AttributeType']
_OBJ_INFO_OBJECTTYPE = _OBJ_INFO.enum_types_by_name['ObjectType']
_CRITICALOBJECT_OBJECTTYPE = _CRITICALOBJECT.enum_types_by_name['ObjectType']
EgoVeh = _reflection.GeneratedProtocolMessageType('EgoVeh', (_message.Message,), {
  'DESCRIPTOR' : _EGOVEH,
  '__module__' : 'smart.driving.smart_driving_object_pb2'
  # @@protoc_insertion_point(class_scope:smart.EgoVeh)
  })
_sym_db.RegisterMessage(EgoVeh)

Vehicle_Pos = _reflection.GeneratedProtocolMessageType('Vehicle_Pos', (_message.Message,), {
  'DESCRIPTOR' : _VEHICLE_POS,
  '__module__' : 'smart.driving.smart_driving_object_pb2'
  # @@protoc_insertion_point(class_scope:smart.Vehicle_Pos)
  })
_sym_db.RegisterMessage(Vehicle_Pos)

Guide_Line = _reflection.GeneratedProtocolMessageType('Guide_Line', (_message.Message,), {
  'DESCRIPTOR' : _GUIDE_LINE,
  '__module__' : 'smart.driving.smart_driving_object_pb2'
  # @@protoc_insertion_point(class_scope:smart.Guide_Line)
  })
_sym_db.RegisterMessage(Guide_Line)

Obj_Disp = _reflection.GeneratedProtocolMessageType('Obj_Disp', (_message.Message,), {
  'DESCRIPTOR' : _OBJ_DISP,
  '__module__' : 'smart.driving.smart_driving_object_pb2'
  # @@protoc_insertion_point(class_scope:smart.Obj_Disp)
  })
_sym_db.RegisterMessage(Obj_Disp)

Obj_Info = _reflection.GeneratedProtocolMessageType('Obj_Info', (_message.Message,), {
  'DESCRIPTOR' : _OBJ_INFO,
  '__module__' : 'smart.driving.smart_driving_object_pb2'
  # @@protoc_insertion_point(class_scope:smart.Obj_Info)
  })
_sym_db.RegisterMessage(Obj_Info)

LightStatus = _reflection.GeneratedProtocolMessageType('LightStatus', (_message.Message,), {
  'DESCRIPTOR' : _LIGHTSTATUS,
  '__module__' : 'smart.driving.smart_driving_object_pb2'
  # @@protoc_insertion_point(class_scope:smart.LightStatus)
  })
_sym_db.RegisterMessage(LightStatus)

CriticalObject = _reflection.GeneratedProtocolMessageType('CriticalObject', (_message.Message,), {
  'DESCRIPTOR' : _CRITICALOBJECT,
  '__module__' : 'smart.driving.smart_driving_object_pb2'
  # @@protoc_insertion_point(class_scope:smart.CriticalObject)
  })
_sym_db.RegisterMessage(CriticalObject)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EGOVEH._serialized_start=78
  _EGOVEH._serialized_end=261
  _VEHICLE_POS._serialized_start=264
  _VEHICLE_POS._serialized_end=414
  _GUIDE_LINE._serialized_start=416
  _GUIDE_LINE._serialized_end=455
  _OBJ_DISP._serialized_start=457
  _OBJ_DISP._serialized_end=522
  _OBJ_INFO._serialized_start=525
  _OBJ_INFO._serialized_end=1635
  _OBJ_INFO_OBJ_TYPE._serialized_start=860
  _OBJ_INFO_OBJ_TYPE._serialized_end=1448
  _OBJ_INFO_ATTRIBUTETYPE._serialized_start=1450
  _OBJ_INFO_ATTRIBUTETYPE._serialized_end=1539
  _OBJ_INFO_OBJECTTYPE._serialized_start=1541
  _OBJ_INFO_OBJECTTYPE._serialized_end=1635
  _LIGHTSTATUS._serialized_start=1638
  _LIGHTSTATUS._serialized_end=1800
  _CRITICALOBJECT._serialized_start=1803
  _CRITICALOBJECT._serialized_end=2000
  _CRITICALOBJECT_OBJECTTYPE._serialized_start=1906
  _CRITICALOBJECT_OBJECTTYPE._serialized_end=2000
# @@protoc_insertion_point(module_scope)
