# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_takeover/mode_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n remote_takeover/mode_state.proto\x12\x19\x64\x65\x65proute.remote_takeover\"\x9c\x01\n\tModeState\x12;\n\x04mode\x18\x01 \x01(\x0e\x32-.deeproute.remote_takeover.ModeState.ModeType\"R\n\x08ModeType\x12\r\n\tMODE_NONE\x10\x00\x12\x10\n\x0cMODE_MONITOR\x10\x01\x12\x12\n\x0eMODE_SUPERVISE\x10\x02\x12\x11\n\rMODE_TAKEOVER\x10\x03')



_MODESTATE = DESCRIPTOR.message_types_by_name['ModeState']
_MODESTATE_MODETYPE = _MODESTATE.enum_types_by_name['ModeType']
ModeState = _reflection.GeneratedProtocolMessageType('ModeState', (_message.Message,), {
  'DESCRIPTOR' : _MODESTATE,
  '__module__' : 'remote_takeover.mode_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.remote_takeover.ModeState)
  })
_sym_db.RegisterMessage(ModeState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODESTATE._serialized_start=64
  _MODESTATE._serialized_end=220
  _MODESTATE_MODETYPE._serialized_start=138
  _MODESTATE_MODETYPE._serialized_end=220
# @@protoc_insertion_point(module_scope)
