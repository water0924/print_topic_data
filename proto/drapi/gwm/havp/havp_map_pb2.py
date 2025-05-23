# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drapi/gwm/havp/havp_map.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.drapi.gwm.havp import havp_common_pb2 as drapi_dot_gwm_dot_havp_dot_havp__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x64rapi/gwm/havp/havp_map.proto\x12\x04havp\x1a drapi/gwm/havp/havp_common.proto\"\xb4\x03\n\nAVPMapData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x1a\n\x05route\x18\x05 \x03(\x0b\x32\x0b.havp.Point\x12#\n\x0e\x66loor_entrance\x18\x06 \x03(\x0b\x32\x0b.havp.Point\x12\x1f\n\nfloor_exit\x18\x07 \x03(\x0b\x32\x0b.havp.Point\x12*\n\x0eparking_spaces\x18\x08 \x03(\x0b\x32\x12.havp.ParkingSpace\x12(\n\rmap_obstacles\x18\t \x03(\x0b\x32\x11.havp.MapObstacle\x12&\n\x0cparking_pois\x18\n \x03(\x0b\x32\x10.havp.ParkingPoi\x12\x0e\n\x06length\x18\x0b \x01(\x05\x12\x15\n\rcreation_time\x18\x0c \x01(\x05\x12\x14\n\x0crenewal_time\x18\r \x01(\x05\x12/\n\x1aglobal_planning_trajectory\x18\x0e \x03(\x0b\x32\x0b.havp.Point\x12\x19\n\x03map\x18\x0f \x01(\x0b\x32\x0c.havp.AVPMap\"\x94\x03\n\x0c\x41VPMapManage\x12\x32\n\x08opt_type\x18\x01 \x01(\x0e\x32 .havp.AVPMapManage.OperationType\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08map_name\x18\x03 \x01(\t\x12)\n\rparking_space\x18\x04 \x01(\x0b\x32\x12.havp.ParkingSpace\x12%\n\x0bparking_poi\x18\x05 \x01(\x0b\x32\x10.havp.ParkingPoi\"\xdf\x01\n\rOperationType\x12\x17\n\x13OPERATION_TYPE_NONE\x10\x00\x12\x1a\n\x16OPERATION_TYPE_EDITMAP\x10\x01\x12\x1c\n\x18OPERATION_TYPE_DELETEMAP\x10\x02\x12#\n\x1fOPERATION_TYPE_EDITPARKINGSPACE\x10\x03\x12\x19\n\x15OPERATION_TYPE_REQMAP\x10\x05\x12\x1e\n\x1aOPERATION_TYPE_SELECTP_POI\x10\x06\x12\x1b\n\x17OPERATION_TYPE_EDIT_POI\x10\x07\"\xc6\x01\n\x0e\x41VPNaviMapData\x12\x1d\n\x04pins\x18\x01 \x03(\x0b\x32\x0f.havp.AVPMapPin\x12\x34\n\x08opt_type\x18\x02 \x01(\x0e\x32\".havp.AVPNaviMapData.OperationType\"_\n\rOperationType\x12\x17\n\x13OPERATION_TYPE_NONE\x10\x00\x12\x19\n\x15OPERATION_TYPE_MAPPIN\x10\x01\x12\x1a\n\x16OPERATION_TYPE_GETNAME\x10\x02\x62\x06proto3')



_AVPMAPDATA = DESCRIPTOR.message_types_by_name['AVPMapData']
_AVPMAPMANAGE = DESCRIPTOR.message_types_by_name['AVPMapManage']
_AVPNAVIMAPDATA = DESCRIPTOR.message_types_by_name['AVPNaviMapData']
_AVPMAPMANAGE_OPERATIONTYPE = _AVPMAPMANAGE.enum_types_by_name['OperationType']
_AVPNAVIMAPDATA_OPERATIONTYPE = _AVPNAVIMAPDATA.enum_types_by_name['OperationType']
AVPMapData = _reflection.GeneratedProtocolMessageType('AVPMapData', (_message.Message,), {
  'DESCRIPTOR' : _AVPMAPDATA,
  '__module__' : 'drapi.gwm.havp.havp_map_pb2'
  # @@protoc_insertion_point(class_scope:havp.AVPMapData)
  })
_sym_db.RegisterMessage(AVPMapData)

AVPMapManage = _reflection.GeneratedProtocolMessageType('AVPMapManage', (_message.Message,), {
  'DESCRIPTOR' : _AVPMAPMANAGE,
  '__module__' : 'drapi.gwm.havp.havp_map_pb2'
  # @@protoc_insertion_point(class_scope:havp.AVPMapManage)
  })
_sym_db.RegisterMessage(AVPMapManage)

AVPNaviMapData = _reflection.GeneratedProtocolMessageType('AVPNaviMapData', (_message.Message,), {
  'DESCRIPTOR' : _AVPNAVIMAPDATA,
  '__module__' : 'drapi.gwm.havp.havp_map_pb2'
  # @@protoc_insertion_point(class_scope:havp.AVPNaviMapData)
  })
_sym_db.RegisterMessage(AVPNaviMapData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AVPMAPDATA._serialized_start=74
  _AVPMAPDATA._serialized_end=510
  _AVPMAPMANAGE._serialized_start=513
  _AVPMAPMANAGE._serialized_end=917
  _AVPMAPMANAGE_OPERATIONTYPE._serialized_start=694
  _AVPMAPMANAGE_OPERATIONTYPE._serialized_end=917
  _AVPNAVIMAPDATA._serialized_start=920
  _AVPNAVIMAPDATA._serialized_end=1118
  _AVPNAVIMAPDATA_OPERATIONTYPE._serialized_start=1023
  _AVPNAVIMAPDATA_OPERATIONTYPE._serialized_end=1118
# @@protoc_insertion_point(module_scope)
