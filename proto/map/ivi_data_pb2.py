# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map/ivi_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import geometry_pb2 as common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12map/ivi_data.proto\x12\rdeeproute.map\x1a\x15\x63ommon/geometry.proto\"\x8b\x01\n\x0bIVIAmapLink\x12\x0f\n\x07\x66ormway\x18\x01 \x01(\x05\x12\x0b\n\x03len\x18\x02 \x01(\x05\x12\x11\n\tlink_type\x18\x03 \x01(\x05\x12\x13\n\x0bpnt_beg_idx\x18\x04 \x01(\x05\x12\x0f\n\x07pnt_cnt\x18\x05 \x01(\x05\x12\x11\n\troad_name\x18\x06 \x01(\t\x12\x12\n\nroad_class\x18\x07 \x01(\x05\"f\n\x0eIVIAmapSegment\x12\x14\n\x0clink_beg_idx\x18\x01 \x01(\x05\x12\x10\n\x08link_cnt\x18\x02 \x01(\x05\x12\x13\n\x0bmain_action\x18\x03 \x01(\x05\x12\x17\n\x0froad_board_name\x18\x04 \x01(\t\"\xe0\x01\n\x10IVIAmapRouteData\x12\x0f\n\x07path_id\x18\x01 \x01(\x05\x12\x10\n\x08link_cnt\x18\x02 \x01(\x05\x12)\n\x05links\x18\x03 \x03(\x0b\x32\x1a.deeproute.map.IVIAmapLink\x12\x0f\n\x07pnt_cnt\x18\x04 \x01(\x05\x12\'\n\x04pnts\x18\x05 \x03(\x0b\x32\x19.deeproute.common.Point3D\x12\x13\n\x0bsegment_cnt\x18\x06 \x01(\x05\x12/\n\x08segments\x18\x07 \x03(\x0b\x32\x1d.deeproute.map.IVIAmapSegment\"t\n\x13IVIAmapRequestRoute\x12\x14\n\x0cnavi_path_id\x18\x01 \x01(\x05\x12\x33\n\nroute_data\x18\x02 \x01(\x0b\x32\x1f.deeproute.map.IVIAmapRouteData\x12\x12\n\nroute_name\x18\x03 \x01(\t\"9\n\x17IVIAmapSelectedNaviPath\x12\x0f\n\x07path_id\x18\x01 \x01(\x05\x12\r\n\x05valid\x18\x02 \x01(\x08\"\xb8\x01\n\x14IVIAmapRequestResult\x12\x0c\n\x04mode\x18\x01 \x01(\x05\x12\x39\n\rrequest_route\x18\x02 \x03(\x0b\x32\".deeproute.map.IVIAmapRequestRoute\x12\x13\n\x0brequest_seq\x18\x03 \x01(\x05\x12\x42\n\x12selected_navi_path\x18\x04 \x01(\x0b\x32&.deeproute.map.IVIAmapSelectedNaviPath')



_IVIAMAPLINK = DESCRIPTOR.message_types_by_name['IVIAmapLink']
_IVIAMAPSEGMENT = DESCRIPTOR.message_types_by_name['IVIAmapSegment']
_IVIAMAPROUTEDATA = DESCRIPTOR.message_types_by_name['IVIAmapRouteData']
_IVIAMAPREQUESTROUTE = DESCRIPTOR.message_types_by_name['IVIAmapRequestRoute']
_IVIAMAPSELECTEDNAVIPATH = DESCRIPTOR.message_types_by_name['IVIAmapSelectedNaviPath']
_IVIAMAPREQUESTRESULT = DESCRIPTOR.message_types_by_name['IVIAmapRequestResult']
IVIAmapLink = _reflection.GeneratedProtocolMessageType('IVIAmapLink', (_message.Message,), {
  'DESCRIPTOR' : _IVIAMAPLINK,
  '__module__' : 'map.ivi_data_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.map.IVIAmapLink)
  })
_sym_db.RegisterMessage(IVIAmapLink)

IVIAmapSegment = _reflection.GeneratedProtocolMessageType('IVIAmapSegment', (_message.Message,), {
  'DESCRIPTOR' : _IVIAMAPSEGMENT,
  '__module__' : 'map.ivi_data_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.map.IVIAmapSegment)
  })
_sym_db.RegisterMessage(IVIAmapSegment)

IVIAmapRouteData = _reflection.GeneratedProtocolMessageType('IVIAmapRouteData', (_message.Message,), {
  'DESCRIPTOR' : _IVIAMAPROUTEDATA,
  '__module__' : 'map.ivi_data_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.map.IVIAmapRouteData)
  })
_sym_db.RegisterMessage(IVIAmapRouteData)

IVIAmapRequestRoute = _reflection.GeneratedProtocolMessageType('IVIAmapRequestRoute', (_message.Message,), {
  'DESCRIPTOR' : _IVIAMAPREQUESTROUTE,
  '__module__' : 'map.ivi_data_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.map.IVIAmapRequestRoute)
  })
_sym_db.RegisterMessage(IVIAmapRequestRoute)

IVIAmapSelectedNaviPath = _reflection.GeneratedProtocolMessageType('IVIAmapSelectedNaviPath', (_message.Message,), {
  'DESCRIPTOR' : _IVIAMAPSELECTEDNAVIPATH,
  '__module__' : 'map.ivi_data_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.map.IVIAmapSelectedNaviPath)
  })
_sym_db.RegisterMessage(IVIAmapSelectedNaviPath)

IVIAmapRequestResult = _reflection.GeneratedProtocolMessageType('IVIAmapRequestResult', (_message.Message,), {
  'DESCRIPTOR' : _IVIAMAPREQUESTRESULT,
  '__module__' : 'map.ivi_data_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.map.IVIAmapRequestResult)
  })
_sym_db.RegisterMessage(IVIAmapRequestResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IVIAMAPLINK._serialized_start=61
  _IVIAMAPLINK._serialized_end=200
  _IVIAMAPSEGMENT._serialized_start=202
  _IVIAMAPSEGMENT._serialized_end=304
  _IVIAMAPROUTEDATA._serialized_start=307
  _IVIAMAPROUTEDATA._serialized_end=531
  _IVIAMAPREQUESTROUTE._serialized_start=533
  _IVIAMAPREQUESTROUTE._serialized_end=649
  _IVIAMAPSELECTEDNAVIPATH._serialized_start=651
  _IVIAMAPSELECTEDNAVIPATH._serialized_end=708
  _IVIAMAPREQUESTRESULT._serialized_start=711
  _IVIAMAPREQUESTRESULT._serialized_end=895
# @@protoc_insertion_point(module_scope)
