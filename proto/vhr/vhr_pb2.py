# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vhr/vhr.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rvhr/vhr.proto\x12\x06\x64r.vhr\"x\n\tVhrHeader\x12\x11\n\ttrip_name\x18\x01 \x01(\t\x12\x0e\n\x06\x63\x61r_id\x18\x02 \x01(\t\x12\x16\n\x0e\x64river_version\x18\x03 \x01(\t\x12\x12\n\noem_car_id\x18\x04 \x01(\t\x12\x1c\n\x14\x64river_short_version\x18\x05 \x01(\t* \n\x07VhrType\x12\n\n\x06HEADER\x10\x00\x12\t\n\x05\x45VENT\x10\x01')

_VHRTYPE = DESCRIPTOR.enum_types_by_name['VhrType']
VhrType = enum_type_wrapper.EnumTypeWrapper(_VHRTYPE)
HEADER = 0
EVENT = 1


_VHRHEADER = DESCRIPTOR.message_types_by_name['VhrHeader']
VhrHeader = _reflection.GeneratedProtocolMessageType('VhrHeader', (_message.Message,), {
  'DESCRIPTOR' : _VHRHEADER,
  '__module__' : 'vhr.vhr_pb2'
  # @@protoc_insertion_point(class_scope:dr.vhr.VhrHeader)
  })
_sym_db.RegisterMessage(VhrHeader)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VHRTYPE._serialized_start=147
  _VHRTYPE._serialized_end=179
  _VHRHEADER._serialized_start=25
  _VHRHEADER._serialized_end=145
# @@protoc_insertion_point(module_scope)
