# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smart/smart_common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18smart/smart_common.proto\x12\x05smart\"\x1d\n\x05Pnt2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"(\n\x05Pnt3D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"$\n\x07Polygon\x12\x19\n\x03pnt\x18\x01 \x03(\x0b\x32\x0c.smart.Pnt3D\"%\n\x08Polyline\x12\x19\n\x03pnt\x18\x01 \x03(\x0b\x32\x0c.smart.Pnt3D\"!\n\tTimestamp\x12\x14\n\x0cmilliseconds\x18\x01 \x01(\r*\xa1\x01\n\x0cSwitchStatus\x12\x17\n\x13SwitchStatusInvalid\x10\x00\x12\x15\n\x11SwitchStatusClose\x10\x01\x12\x14\n\x10SwitchStatusOpen\x10\x02\x12\x17\n\x13SwitchStatusDisable\x10\x03\x12\x18\n\x14SwitchStatusReserve1\x10\x04\x12\x18\n\x14SwitchStatusReserve2\x10\x05*R\n\x0b\x42uttonState\x12\x16\n\x12\x42uttonStateInitial\x10\x00\x12\x13\n\x0f\x42uttonStateGrey\x10\x01\x12\x16\n\x12\x42uttonStateNotGrey\x10\x02\x62\x06proto3')

_SWITCHSTATUS = DESCRIPTOR.enum_types_by_name['SwitchStatus']
SwitchStatus = enum_type_wrapper.EnumTypeWrapper(_SWITCHSTATUS)
_BUTTONSTATE = DESCRIPTOR.enum_types_by_name['ButtonState']
ButtonState = enum_type_wrapper.EnumTypeWrapper(_BUTTONSTATE)
SwitchStatusInvalid = 0
SwitchStatusClose = 1
SwitchStatusOpen = 2
SwitchStatusDisable = 3
SwitchStatusReserve1 = 4
SwitchStatusReserve2 = 5
ButtonStateInitial = 0
ButtonStateGrey = 1
ButtonStateNotGrey = 2


_PNT2D = DESCRIPTOR.message_types_by_name['Pnt2D']
_PNT3D = DESCRIPTOR.message_types_by_name['Pnt3D']
_POLYGON = DESCRIPTOR.message_types_by_name['Polygon']
_POLYLINE = DESCRIPTOR.message_types_by_name['Polyline']
_TIMESTAMP = DESCRIPTOR.message_types_by_name['Timestamp']
Pnt2D = _reflection.GeneratedProtocolMessageType('Pnt2D', (_message.Message,), {
  'DESCRIPTOR' : _PNT2D,
  '__module__' : 'smart.smart_common_pb2'
  # @@protoc_insertion_point(class_scope:smart.Pnt2D)
  })
_sym_db.RegisterMessage(Pnt2D)

Pnt3D = _reflection.GeneratedProtocolMessageType('Pnt3D', (_message.Message,), {
  'DESCRIPTOR' : _PNT3D,
  '__module__' : 'smart.smart_common_pb2'
  # @@protoc_insertion_point(class_scope:smart.Pnt3D)
  })
_sym_db.RegisterMessage(Pnt3D)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), {
  'DESCRIPTOR' : _POLYGON,
  '__module__' : 'smart.smart_common_pb2'
  # @@protoc_insertion_point(class_scope:smart.Polygon)
  })
_sym_db.RegisterMessage(Polygon)

Polyline = _reflection.GeneratedProtocolMessageType('Polyline', (_message.Message,), {
  'DESCRIPTOR' : _POLYLINE,
  '__module__' : 'smart.smart_common_pb2'
  # @@protoc_insertion_point(class_scope:smart.Polyline)
  })
_sym_db.RegisterMessage(Polyline)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'smart.smart_common_pb2'
  # @@protoc_insertion_point(class_scope:smart.Timestamp)
  })
_sym_db.RegisterMessage(Timestamp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SWITCHSTATUS._serialized_start=221
  _SWITCHSTATUS._serialized_end=382
  _BUTTONSTATE._serialized_start=384
  _BUTTONSTATE._serialized_end=466
  _PNT2D._serialized_start=35
  _PNT2D._serialized_end=64
  _PNT3D._serialized_start=66
  _PNT3D._serialized_end=106
  _POLYGON._serialized_start=108
  _POLYGON._serialized_end=144
  _POLYLINE._serialized_start=146
  _POLYLINE._serialized_end=183
  _TIMESTAMP._serialized_start=185
  _TIMESTAMP._serialized_end=218
# @@protoc_insertion_point(module_scope)
