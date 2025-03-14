# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drivers/orincam_image_info.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n drivers/orincam_image_info.proto\x12\x11\x64\x65\x65proute.drivers\"v\n\x0eOrinCamSetting\x12\x13\n\x0b\x63\x61mera_name\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x30\n\nimage_type\x18\x04 \x01(\x0e\x32\x1c.deeproute.drivers.ImageType\"F\n\x0fOrinCamSettings\x12\x33\n\x08settings\x18\x01 \x03(\x0b\x32!.deeproute.drivers.OrinCamSetting*S\n\tImageType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08RGBA8888\x10\x01\x12\x0c\n\x08\x42GRA8888\x10\x02\x12\x0b\n\x07YUVI420\x10\x03\x12\x07\n\x03RAW\x10\x04\x12\x07\n\x03JPG\x10\x05')

_IMAGETYPE = DESCRIPTOR.enum_types_by_name['ImageType']
ImageType = enum_type_wrapper.EnumTypeWrapper(_IMAGETYPE)
UNKNOWN = 0
RGBA8888 = 1
BGRA8888 = 2
YUVI420 = 3
RAW = 4
JPG = 5


_ORINCAMSETTING = DESCRIPTOR.message_types_by_name['OrinCamSetting']
_ORINCAMSETTINGS = DESCRIPTOR.message_types_by_name['OrinCamSettings']
OrinCamSetting = _reflection.GeneratedProtocolMessageType('OrinCamSetting', (_message.Message,), {
  'DESCRIPTOR' : _ORINCAMSETTING,
  '__module__' : 'drivers.orincam_image_info_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.OrinCamSetting)
  })
_sym_db.RegisterMessage(OrinCamSetting)

OrinCamSettings = _reflection.GeneratedProtocolMessageType('OrinCamSettings', (_message.Message,), {
  'DESCRIPTOR' : _ORINCAMSETTINGS,
  '__module__' : 'drivers.orincam_image_info_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.OrinCamSettings)
  })
_sym_db.RegisterMessage(OrinCamSettings)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGETYPE._serialized_start=247
  _IMAGETYPE._serialized_end=330
  _ORINCAMSETTING._serialized_start=55
  _ORINCAMSETTING._serialized_end=173
  _ORINCAMSETTINGS._serialized_start=175
  _ORINCAMSETTINGS._serialized_end=245
# @@protoc_insertion_point(module_scope)
