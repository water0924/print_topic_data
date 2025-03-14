# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: esa/esa_state.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x65sa/esa_state.proto\x12\rdeeproute.esa\x1a\x13\x63ommon/header.proto\"t\n\tStateInfo\x12*\n\tesa_state\x18\x01 \x01(\x0e\x32\x17.deeproute.esa.ESAState\x12;\n\x12\x65sa_avoidance_side\x18\x02 \x01(\x0e\x32\x1f.deeproute.esa.ESAAvoidanceSide\"z\n\x0cStateWrapper\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.deeproute.common.Header\x12,\n\nstate_info\x18\x02 \x01(\x0b\x32\x18.deeproute.esa.StateInfo\x12\x12\n\nblc_msg_id\x18\x03 \x01(\x05*Z\n\x08\x45SAState\x12\x0b\n\x07\x45SA_OFF\x10\x00\x12\x0f\n\x0b\x45SA_FAILURE\x10\x01\x12\x0f\n\x0b\x45SA_PASSIVE\x10\x02\x12\x0f\n\x0b\x45SA_STANDBY\x10\x03\x12\x0e\n\nESA_ACTIVE\x10\x04*B\n\x10\x45SAAvoidanceSide\x12\x0f\n\x0bUNKOWN_SIDE\x10\x00\x12\r\n\tLEFT_SIDE\x10\x01\x12\x0e\n\nRIGHT_SIDE\x10\x02')

_ESASTATE = DESCRIPTOR.enum_types_by_name['ESAState']
ESAState = enum_type_wrapper.EnumTypeWrapper(_ESASTATE)
_ESAAVOIDANCESIDE = DESCRIPTOR.enum_types_by_name['ESAAvoidanceSide']
ESAAvoidanceSide = enum_type_wrapper.EnumTypeWrapper(_ESAAVOIDANCESIDE)
ESA_OFF = 0
ESA_FAILURE = 1
ESA_PASSIVE = 2
ESA_STANDBY = 3
ESA_ACTIVE = 4
UNKOWN_SIDE = 0
LEFT_SIDE = 1
RIGHT_SIDE = 2


_STATEINFO = DESCRIPTOR.message_types_by_name['StateInfo']
_STATEWRAPPER = DESCRIPTOR.message_types_by_name['StateWrapper']
StateInfo = _reflection.GeneratedProtocolMessageType('StateInfo', (_message.Message,), {
  'DESCRIPTOR' : _STATEINFO,
  '__module__' : 'esa.esa_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.esa.StateInfo)
  })
_sym_db.RegisterMessage(StateInfo)

StateWrapper = _reflection.GeneratedProtocolMessageType('StateWrapper', (_message.Message,), {
  'DESCRIPTOR' : _STATEWRAPPER,
  '__module__' : 'esa.esa_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.esa.StateWrapper)
  })
_sym_db.RegisterMessage(StateWrapper)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ESASTATE._serialized_start=301
  _ESASTATE._serialized_end=391
  _ESAAVOIDANCESIDE._serialized_start=393
  _ESAAVOIDANCESIDE._serialized_end=459
  _STATEINFO._serialized_start=59
  _STATEINFO._serialized_end=175
  _STATEWRAPPER._serialized_start=177
  _STATEWRAPPER._serialized_end=299
# @@protoc_insertion_point(module_scope)
