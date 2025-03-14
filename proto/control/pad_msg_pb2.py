# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: control/pad_msg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import header_pb2 as common_dot_header__pb2
from proto.canbus import chassis_pb2 as canbus_dot_chassis__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ontrol/pad_msg.proto\x12\x11\x64\x65\x65proute.control\x1a\x13\x63ommon/header.proto\x1a\x14\x63\x61nbus/chassis.proto\"\xa5\x01\n\nPadMessage\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.deeproute.common.Header\x12;\n\x0c\x64riving_mode\x18\x02 \x01(\x0e\x32%.deeproute.canbus.Chassis.DrivingMode\x12\x30\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32 .deeproute.control.DrivingAction*/\n\rDrivingAction\x12\x08\n\x04STOP\x10\x00\x12\t\n\x05START\x10\x01\x12\t\n\x05RESET\x10\x02')

_DRIVINGACTION = DESCRIPTOR.enum_types_by_name['DrivingAction']
DrivingAction = enum_type_wrapper.EnumTypeWrapper(_DRIVINGACTION)
STOP = 0
START = 1
RESET = 2


_PADMESSAGE = DESCRIPTOR.message_types_by_name['PadMessage']
PadMessage = _reflection.GeneratedProtocolMessageType('PadMessage', (_message.Message,), {
  'DESCRIPTOR' : _PADMESSAGE,
  '__module__' : 'control.pad_msg_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.control.PadMessage)
  })
_sym_db.RegisterMessage(PadMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DRIVINGACTION._serialized_start=255
  _DRIVINGACTION._serialized_end=302
  _PADMESSAGE._serialized_start=88
  _PADMESSAGE._serialized_end=253
# @@protoc_insertion_point(module_scope)
