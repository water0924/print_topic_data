# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drapi/blc_to_aeb.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.drapi import operation_status_pb2 as drapi_dot_operation__status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x64rapi/blc_to_aeb.proto\x12\x06\x64r.blc\x1a\x1c\x64rapi/operation_status.proto\"\xde\x03\n\x12PolicyResultsToAeb\x12\x0e\n\x06msg_id\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12(\n\naeb_result\x18\x03 \x01(\x0e\x32\x14.dr.blc.PolicyResult\x12(\n\nesa_result\x18\x04 \x01(\x0e\x32\x14.dr.blc.PolicyResult\x12(\n\nmeb_result\x18\x05 \x01(\x0e\x32\x14.dr.blc.PolicyResult\x12(\n\nfcw_result\x18\x06 \x01(\x0e\x32\x14.dr.blc.PolicyResult\x12)\n\x0b\x66\x63tb_result\x18\x07 \x01(\x0e\x32\x14.dr.blc.PolicyResult\x12)\n\x0b\x66\x63ta_result\x18\x08 \x01(\x0e\x32\x14.dr.blc.PolicyResult\x12)\n\x0brctb_result\x18\t \x01(\x0e\x32\x14.dr.blc.PolicyResult\x12(\n\nabp_result\x18\n \x01(\x0e\x32\x14.dr.blc.PolicyResult\x12(\n\nawb_result\x18\x0b \x01(\x0e\x32\x14.dr.blc.PolicyResult\x12(\n\naba_result\x18\x0c \x01(\x0e\x32\x14.dr.blc.PolicyResult\"\xa4\x02\n\x11\x41\x45\x42StateCondition\x12\x0e\n\x06is_off\x18\x01 \x01(\x08\x12\x12\n\nis_failure\x18\x02 \x01(\x08\x12\x16\n\x0eis_aeb_passive\x18\x03 \x01(\x08\x12\x1a\n\x12is_aeb_active_exit\x18\x04 \x01(\x08\x12\x16\n\x0eis_eba_passive\x18\x05 \x01(\x08\x12\x1a\n\x12is_eba_active_exit\x18\x06 \x01(\x08\x12\x1a\n\x12is_standstill_exit\x18\x07 \x01(\x08\x12\x1b\n\x13is_standstill_enter\x18\x08 \x01(\x08\x12\x15\n\ris_eba_active\x18\t \x01(\x08\x12\x33\n\x0breason_info\x18\x14 \x01(\x0b\x32\x1e.dr.operationstatus.ReasonInfo\"\x98\x01\n\x11\x41WBStateCondition\x12\x0e\n\x06is_off\x18\x01 \x01(\x08\x12\x12\n\nis_failure\x18\x02 \x01(\x08\x12\x12\n\nis_passive\x18\x03 \x01(\x08\x12\x16\n\x0eis_active_exit\x18\x04 \x01(\x08\x12\x33\n\x0breason_info\x18\x14 \x01(\x0b\x32\x1e.dr.operationstatus.ReasonInfo\"\x98\x01\n\x11\x41\x42PStateCondition\x12\x0e\n\x06is_off\x18\x01 \x01(\x08\x12\x12\n\nis_failure\x18\x02 \x01(\x08\x12\x12\n\nis_passive\x18\x03 \x01(\x08\x12\x16\n\x0eis_active_exit\x18\x04 \x01(\x08\x12\x33\n\x0breason_info\x18\x14 \x01(\x0b\x32\x1e.dr.operationstatus.ReasonInfo\"\xd1\x01\n\x11MEBStateCondition\x12\x0e\n\x06is_off\x18\x01 \x01(\x08\x12\x12\n\nis_failure\x18\x02 \x01(\x08\x12\x12\n\nis_passive\x18\x03 \x01(\x08\x12\x16\n\x0eis_active_exit\x18\x04 \x01(\x08\x12\x1a\n\x12is_standstill_exit\x18\x05 \x01(\x08\x12\x1b\n\x13is_standstill_enter\x18\x06 \x01(\x08\x12\x33\n\x0breason_info\x18\x14 \x01(\x0b\x32\x1e.dr.operationstatus.ReasonInfo\"\x98\x01\n\x11\x46\x43WStateCondition\x12\x0e\n\x06is_off\x18\x01 \x01(\x08\x12\x12\n\nis_failure\x18\x02 \x01(\x08\x12\x12\n\nis_passive\x18\x03 \x01(\x08\x12\x16\n\x0eis_active_exit\x18\x04 \x01(\x08\x12\x33\n\x0breason_info\x18\x14 \x01(\x0b\x32\x1e.dr.operationstatus.ReasonInfo\"\xd2\x01\n\x12RCTBStateCondition\x12\x0e\n\x06is_off\x18\x01 \x01(\x08\x12\x12\n\nis_failure\x18\x02 \x01(\x08\x12\x12\n\nis_passive\x18\x03 \x01(\x08\x12\x16\n\x0eis_active_exit\x18\x04 \x01(\x08\x12\x1a\n\x12is_standstill_exit\x18\x05 \x01(\x08\x12\x1b\n\x13is_standstill_enter\x18\x06 \x01(\x08\x12\x33\n\x0breason_info\x18\x14 \x01(\x0b\x32\x1e.dr.operationstatus.ReasonInfo\"\xd2\x01\n\x12\x46\x43TBStateCondition\x12\x0e\n\x06is_off\x18\x01 \x01(\x08\x12\x12\n\nis_failure\x18\x02 \x01(\x08\x12\x12\n\nis_passive\x18\x03 \x01(\x08\x12\x16\n\x0eis_active_exit\x18\x04 \x01(\x08\x12\x1a\n\x12is_standstill_exit\x18\x05 \x01(\x08\x12\x1b\n\x13is_standstill_enter\x18\x06 \x01(\x08\x12\x33\n\x0breason_info\x18\x14 \x01(\x0b\x32\x1e.dr.operationstatus.ReasonInfo\"\x99\x01\n\x12\x46\x43TAStateCondition\x12\x0e\n\x06is_off\x18\x01 \x01(\x08\x12\x12\n\nis_failure\x18\x02 \x01(\x08\x12\x12\n\nis_passive\x18\x03 \x01(\x08\x12\x16\n\x0eis_active_exit\x18\x04 \x01(\x08\x12\x33\n\x0breason_info\x18\x14 \x01(\x0b\x32\x1e.dr.operationstatus.ReasonInfo\"\x98\x01\n\x11\x45SAStateCondition\x12\x0e\n\x06is_off\x18\x01 \x01(\x08\x12\x12\n\nis_failure\x18\x02 \x01(\x08\x12\x12\n\nis_passive\x18\x03 \x01(\x08\x12\x16\n\x0eis_active_exit\x18\x04 \x01(\x08\x12\x33\n\x0breason_info\x18\x14 \x01(\x0b\x32\x1e.dr.operationstatus.ReasonInfo\"\xad\x03\n\x13SensitivityLevelSet\x12+\n\taeb_level\x18\x01 \x01(\x0e\x32\x18.dr.blc.SensitivityLevel\x12+\n\tabp_level\x18\x02 \x01(\x0e\x32\x18.dr.blc.SensitivityLevel\x12+\n\tawb_level\x18\x03 \x01(\x0e\x32\x18.dr.blc.SensitivityLevel\x12+\n\tfcw_level\x18\x04 \x01(\x0e\x32\x18.dr.blc.SensitivityLevel\x12,\n\nfcta_level\x18\x05 \x01(\x0e\x32\x18.dr.blc.SensitivityLevel\x12,\n\nfctb_level\x18\x06 \x01(\x0e\x32\x18.dr.blc.SensitivityLevel\x12,\n\nrctb_level\x18\x07 \x01(\x0e\x32\x18.dr.blc.SensitivityLevel\x12+\n\tesa_level\x18\x08 \x01(\x0e\x32\x18.dr.blc.SensitivityLevel\x12+\n\tmeb_level\x18\t \x01(\x0e\x32\x18.dr.blc.SensitivityLevel\";\n\x08ODDFlags\x12\x14\n\x0cis_snow_mode\x18\x01 \x01(\x08\x12\x19\n\x11is_nca_in_control\x18\x02 \x01(\x08\"\xdf\x04\n\x0fStateConditions\x12\x30\n\raeb_condition\x18\x01 \x01(\x0b\x32\x19.dr.blc.AEBStateCondition\x12\x30\n\rawb_condition\x18\x02 \x01(\x0b\x32\x19.dr.blc.AWBStateCondition\x12\x30\n\rabp_condition\x18\x03 \x01(\x0b\x32\x19.dr.blc.ABPStateCondition\x12\x30\n\rfcw_condition\x18\x04 \x01(\x0b\x32\x19.dr.blc.FCWStateCondition\x12\x32\n\x0e\x66\x63tb_condition\x18\x05 \x01(\x0b\x32\x1a.dr.blc.FCTBStateCondition\x12\x32\n\x0e\x66\x63ta_condition\x18\x06 \x01(\x0b\x32\x1a.dr.blc.FCTAStateCondition\x12\x32\n\x0erctb_condition\x18\x07 \x01(\x0b\x32\x1a.dr.blc.RCTBStateCondition\x12\x30\n\resa_condition\x18\x08 \x01(\x0b\x32\x19.dr.blc.ESAStateCondition\x12\x30\n\rmeb_condition\x18\t \x01(\x0b\x32\x19.dr.blc.MEBStateCondition\x12#\n\tmai_state\x18\n \x01(\x0e\x32\x10.dr.blc.MAIState\x12#\n\todd_flags\x18\x14 \x01(\x0b\x32\x10.dr.blc.ODDFlags\x12:\n\x15sensitivity_level_set\x18\x15 \x01(\x0b\x32\x1b.dr.blc.SensitivityLevelSet*2\n\x0cPolicyResult\x12\n\n\x06NORMAL\x10\x00\x12\x0b\n\x07INHIBIT\x10\x01\x12\t\n\x05\x45RROR\x10\x02*1\n\x10SensitivityLevel\x12\n\n\x06MIDDLE\x10\x00\x12\x08\n\x04HIGH\x10\x01\x12\x07\n\x03LOW\x10\x02*Z\n\x08MAIState\x12\x0b\n\x07MAI_OFF\x10\x00\x12\x0f\n\x0bMAI_FAILURE\x10\x01\x12\x0f\n\x0bMAI_PASSIVE\x10\x02\x12\x0f\n\x0bMAI_STANDBY\x10\x03\x12\x0e\n\nMAI_ACTIVE\x10\x04\x62\x06proto3')

_POLICYRESULT = DESCRIPTOR.enum_types_by_name['PolicyResult']
PolicyResult = enum_type_wrapper.EnumTypeWrapper(_POLICYRESULT)
_SENSITIVITYLEVEL = DESCRIPTOR.enum_types_by_name['SensitivityLevel']
SensitivityLevel = enum_type_wrapper.EnumTypeWrapper(_SENSITIVITYLEVEL)
_MAISTATE = DESCRIPTOR.enum_types_by_name['MAIState']
MAIState = enum_type_wrapper.EnumTypeWrapper(_MAISTATE)
NORMAL = 0
INHIBIT = 1
ERROR = 2
MIDDLE = 0
HIGH = 1
LOW = 2
MAI_OFF = 0
MAI_FAILURE = 1
MAI_PASSIVE = 2
MAI_STANDBY = 3
MAI_ACTIVE = 4


_POLICYRESULTSTOAEB = DESCRIPTOR.message_types_by_name['PolicyResultsToAeb']
_AEBSTATECONDITION = DESCRIPTOR.message_types_by_name['AEBStateCondition']
_AWBSTATECONDITION = DESCRIPTOR.message_types_by_name['AWBStateCondition']
_ABPSTATECONDITION = DESCRIPTOR.message_types_by_name['ABPStateCondition']
_MEBSTATECONDITION = DESCRIPTOR.message_types_by_name['MEBStateCondition']
_FCWSTATECONDITION = DESCRIPTOR.message_types_by_name['FCWStateCondition']
_RCTBSTATECONDITION = DESCRIPTOR.message_types_by_name['RCTBStateCondition']
_FCTBSTATECONDITION = DESCRIPTOR.message_types_by_name['FCTBStateCondition']
_FCTASTATECONDITION = DESCRIPTOR.message_types_by_name['FCTAStateCondition']
_ESASTATECONDITION = DESCRIPTOR.message_types_by_name['ESAStateCondition']
_SENSITIVITYLEVELSET = DESCRIPTOR.message_types_by_name['SensitivityLevelSet']
_ODDFLAGS = DESCRIPTOR.message_types_by_name['ODDFlags']
_STATECONDITIONS = DESCRIPTOR.message_types_by_name['StateConditions']
PolicyResultsToAeb = _reflection.GeneratedProtocolMessageType('PolicyResultsToAeb', (_message.Message,), {
  'DESCRIPTOR' : _POLICYRESULTSTOAEB,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.PolicyResultsToAeb)
  })
_sym_db.RegisterMessage(PolicyResultsToAeb)

AEBStateCondition = _reflection.GeneratedProtocolMessageType('AEBStateCondition', (_message.Message,), {
  'DESCRIPTOR' : _AEBSTATECONDITION,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.AEBStateCondition)
  })
_sym_db.RegisterMessage(AEBStateCondition)

AWBStateCondition = _reflection.GeneratedProtocolMessageType('AWBStateCondition', (_message.Message,), {
  'DESCRIPTOR' : _AWBSTATECONDITION,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.AWBStateCondition)
  })
_sym_db.RegisterMessage(AWBStateCondition)

ABPStateCondition = _reflection.GeneratedProtocolMessageType('ABPStateCondition', (_message.Message,), {
  'DESCRIPTOR' : _ABPSTATECONDITION,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.ABPStateCondition)
  })
_sym_db.RegisterMessage(ABPStateCondition)

MEBStateCondition = _reflection.GeneratedProtocolMessageType('MEBStateCondition', (_message.Message,), {
  'DESCRIPTOR' : _MEBSTATECONDITION,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.MEBStateCondition)
  })
_sym_db.RegisterMessage(MEBStateCondition)

FCWStateCondition = _reflection.GeneratedProtocolMessageType('FCWStateCondition', (_message.Message,), {
  'DESCRIPTOR' : _FCWSTATECONDITION,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.FCWStateCondition)
  })
_sym_db.RegisterMessage(FCWStateCondition)

RCTBStateCondition = _reflection.GeneratedProtocolMessageType('RCTBStateCondition', (_message.Message,), {
  'DESCRIPTOR' : _RCTBSTATECONDITION,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.RCTBStateCondition)
  })
_sym_db.RegisterMessage(RCTBStateCondition)

FCTBStateCondition = _reflection.GeneratedProtocolMessageType('FCTBStateCondition', (_message.Message,), {
  'DESCRIPTOR' : _FCTBSTATECONDITION,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.FCTBStateCondition)
  })
_sym_db.RegisterMessage(FCTBStateCondition)

FCTAStateCondition = _reflection.GeneratedProtocolMessageType('FCTAStateCondition', (_message.Message,), {
  'DESCRIPTOR' : _FCTASTATECONDITION,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.FCTAStateCondition)
  })
_sym_db.RegisterMessage(FCTAStateCondition)

ESAStateCondition = _reflection.GeneratedProtocolMessageType('ESAStateCondition', (_message.Message,), {
  'DESCRIPTOR' : _ESASTATECONDITION,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.ESAStateCondition)
  })
_sym_db.RegisterMessage(ESAStateCondition)

SensitivityLevelSet = _reflection.GeneratedProtocolMessageType('SensitivityLevelSet', (_message.Message,), {
  'DESCRIPTOR' : _SENSITIVITYLEVELSET,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.SensitivityLevelSet)
  })
_sym_db.RegisterMessage(SensitivityLevelSet)

ODDFlags = _reflection.GeneratedProtocolMessageType('ODDFlags', (_message.Message,), {
  'DESCRIPTOR' : _ODDFLAGS,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.ODDFlags)
  })
_sym_db.RegisterMessage(ODDFlags)

StateConditions = _reflection.GeneratedProtocolMessageType('StateConditions', (_message.Message,), {
  'DESCRIPTOR' : _STATECONDITIONS,
  '__module__' : 'drapi.blc_to_aeb_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.StateConditions)
  })
_sym_db.RegisterMessage(StateConditions)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POLICYRESULT._serialized_start=3357
  _POLICYRESULT._serialized_end=3407
  _SENSITIVITYLEVEL._serialized_start=3409
  _SENSITIVITYLEVEL._serialized_end=3458
  _MAISTATE._serialized_start=3460
  _MAISTATE._serialized_end=3550
  _POLICYRESULTSTOAEB._serialized_start=65
  _POLICYRESULTSTOAEB._serialized_end=543
  _AEBSTATECONDITION._serialized_start=546
  _AEBSTATECONDITION._serialized_end=838
  _AWBSTATECONDITION._serialized_start=841
  _AWBSTATECONDITION._serialized_end=993
  _ABPSTATECONDITION._serialized_start=996
  _ABPSTATECONDITION._serialized_end=1148
  _MEBSTATECONDITION._serialized_start=1151
  _MEBSTATECONDITION._serialized_end=1360
  _FCWSTATECONDITION._serialized_start=1363
  _FCWSTATECONDITION._serialized_end=1515
  _RCTBSTATECONDITION._serialized_start=1518
  _RCTBSTATECONDITION._serialized_end=1728
  _FCTBSTATECONDITION._serialized_start=1731
  _FCTBSTATECONDITION._serialized_end=1941
  _FCTASTATECONDITION._serialized_start=1944
  _FCTASTATECONDITION._serialized_end=2097
  _ESASTATECONDITION._serialized_start=2100
  _ESASTATECONDITION._serialized_end=2252
  _SENSITIVITYLEVELSET._serialized_start=2255
  _SENSITIVITYLEVELSET._serialized_end=2684
  _ODDFLAGS._serialized_start=2686
  _ODDFLAGS._serialized_end=2745
  _STATECONDITIONS._serialized_start=2748
  _STATECONDITIONS._serialized_end=3355
# @@protoc_insertion_point(module_scope)
