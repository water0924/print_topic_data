# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drapi/gwm/GWM-HMI-common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x64rapi/gwm/GWM-HMI-common.proto\x12\x03gwm\"\x1d\n\x05Pnt2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"(\n\x05Pnt3D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"\"\n\x07Polygon\x12\x17\n\x03pnt\x18\x01 \x03(\x0b\x32\n.gwm.Pnt3D\"#\n\x08Polyline\x12\x17\n\x03pnt\x18\x01 \x03(\x0b\x32\n.gwm.Pnt3D\"!\n\tTimestamp\x12\x14\n\x0cmilliseconds\x18\x01 \x01(\rb\x06proto3')



_PNT2D = DESCRIPTOR.message_types_by_name['Pnt2D']
_PNT3D = DESCRIPTOR.message_types_by_name['Pnt3D']
_POLYGON = DESCRIPTOR.message_types_by_name['Polygon']
_POLYLINE = DESCRIPTOR.message_types_by_name['Polyline']
_TIMESTAMP = DESCRIPTOR.message_types_by_name['Timestamp']
Pnt2D = _reflection.GeneratedProtocolMessageType('Pnt2D', (_message.Message,), {
  'DESCRIPTOR' : _PNT2D,
  '__module__' : 'drapi.gwm.GWM_HMI_common_pb2'
  # @@protoc_insertion_point(class_scope:gwm.Pnt2D)
  })
_sym_db.RegisterMessage(Pnt2D)

Pnt3D = _reflection.GeneratedProtocolMessageType('Pnt3D', (_message.Message,), {
  'DESCRIPTOR' : _PNT3D,
  '__module__' : 'drapi.gwm.GWM_HMI_common_pb2'
  # @@protoc_insertion_point(class_scope:gwm.Pnt3D)
  })
_sym_db.RegisterMessage(Pnt3D)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), {
  'DESCRIPTOR' : _POLYGON,
  '__module__' : 'drapi.gwm.GWM_HMI_common_pb2'
  # @@protoc_insertion_point(class_scope:gwm.Polygon)
  })
_sym_db.RegisterMessage(Polygon)

Polyline = _reflection.GeneratedProtocolMessageType('Polyline', (_message.Message,), {
  'DESCRIPTOR' : _POLYLINE,
  '__module__' : 'drapi.gwm.GWM_HMI_common_pb2'
  # @@protoc_insertion_point(class_scope:gwm.Polyline)
  })
_sym_db.RegisterMessage(Polyline)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'drapi.gwm.GWM_HMI_common_pb2'
  # @@protoc_insertion_point(class_scope:gwm.Timestamp)
  })
_sym_db.RegisterMessage(Timestamp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PNT2D._serialized_start=39
  _PNT2D._serialized_end=68
  _PNT3D._serialized_start=70
  _PNT3D._serialized_end=110
  _POLYGON._serialized_start=112
  _POLYGON._serialized_end=146
  _POLYLINE._serialized_start=148
  _POLYLINE._serialized_end=183
  _TIMESTAMP._serialized_start=185
  _TIMESTAMP._serialized_end=218
# @@protoc_insertion_point(module_scope)
