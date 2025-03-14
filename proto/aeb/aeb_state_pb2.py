# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aeb/aeb_state.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.aeb import visualizer_aeb_command_pb2 as aeb_dot_visualizer__aeb__command__pb2
from proto.esa import esa_state_pb2 as esa_dot_esa__state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x61\x65\x62/aeb_state.proto\x12\rdeeproute.aeb\x1a aeb/visualizer_aeb_command.proto\x1a\x13\x65sa/esa_state.proto\"\xcb\x03\n\tStateInfo\x12*\n\tfcw_state\x18\x01 \x01(\x0e\x32\x17.deeproute.aeb.FCWState\x12*\n\taeb_state\x18\x02 \x01(\x0e\x32\x17.deeproute.aeb.AEBState\x12,\n\nfcta_state\x18\x03 \x01(\x0e\x32\x18.deeproute.aeb.FCTAState\x12,\n\nraeb_state\x18\x04 \x01(\x0e\x32\x18.deeproute.aeb.RAEBState\x12,\n\nrctb_state\x18\x05 \x01(\x0e\x32\x18.deeproute.aeb.RCTBState\x12,\n\nfctb_state\x18\x06 \x01(\x0e\x32\x18.deeproute.aeb.FCTBState\x12*\n\tmeb_state\x18\x07 \x01(\x0e\x32\x17.deeproute.aeb.MEBState\x12*\n\tabp_state\x18\x08 \x01(\x0e\x32\x17.deeproute.aeb.ABPState\x12*\n\tawb_state\x18\t \x01(\x0e\x32\x17.deeproute.aeb.AWBState\x12*\n\tesa_state\x18\n \x01(\x0e\x32\x17.deeproute.esa.ESAState\"\xb5\r\n\x0cStateWrapper\x12,\n\nstate_info\x18\x01 \x01(\x0b\x32\x18.deeproute.aeb.StateInfo\x12\x1a\n\x0e\x63losest_obj_id\x18\x02 \x01(\tB\x02\x18\x01\x12=\n\x0e\x63losest_reason\x18\x03 \x01(\x0e\x32\x1c.deeproute.aeb.ClosestReason:\x07UNKNOWN\x12\x1e\n\x12\x63losest_obj_num_id\x18\x04 \x01(\x05:\x02-1\x12\x1a\n\x12\x66\x63w_inhibit_reason\x18\x05 \x01(\t\x12\x16\n\x0e\x66\x63w_off_reason\x18\x06 \x01(\t\x12\x1b\n\x13\x66\x63ta_inhibit_reason\x18\x07 \x01(\t\x12\x17\n\x0f\x66\x63ta_off_reason\x18\x08 \x01(\t\x12\x1a\n\x12\x61wb_inhibit_reason\x18\t \x01(\t\x12\x16\n\x0e\x61wb_off_reason\x18\n \x01(\t\x12\x1a\n\x12\x61\x62p_inhibit_reason\x18\x0b \x01(\t\x12\x16\n\x0e\x61\x62p_off_reason\x18\x0c \x01(\t\x12\x1a\n\x12\x61\x65\x62_inhibit_reason\x18\r \x01(\t\x12\x16\n\x0e\x61\x65\x62_off_reason\x18\x0e \x01(\t\x12\x1a\n\x12\x65\x62\x61_inhibit_reason\x18\x0f \x01(\t\x12\x16\n\x0e\x65\x62\x61_off_reason\x18\x10 \x01(\t\x12\x14\n\x0c\x63losest_type\x18\x11 \x01(\x05\x12\x1a\n\x12\x63losest_obj_length\x18\x12 \x01(\x01\x12\x19\n\x11\x63losest_obj_width\x18\x13 \x01(\x01\x12\x1b\n\x13\x63losest_obj_lat_ttc\x18\x14 \x01(\x01\x12\x19\n\x11\x63losest_obj_speed\x18\x15 \x01(\x01\x12\x1f\n\x17\x63losest_obj_rel_heading\x18\x16 \x01(\x01\x12\x13\n\x0bttc_display\x18\x17 \x01(\x01\x12\x18\n\x10\x63losest_aeb_type\x18\x18 \x01(\t\x12\x1c\n\x11\x63losest_obj_accel\x18\x19 \x01(\x01:\x01\x30\x12\x17\n\x0fraeb_off_reason\x18\x1a \x01(\t\x12\x1b\n\x13raeb_inhibit_reason\x18\x1b \x01(\t\x12\x1b\n\x13rctb_inhibit_reason\x18\x1c \x01(\t\x12\x17\n\x0frctb_off_reason\x18\x1d \x01(\t\x12X\n\x17\x63rossing_warning_status\x18\x1e \x01(\x0e\x32\x31.deeproute.aeb.StateWrapper.CrossingWarningStatus:\x04NONE\x12\x1f\n\x17\x63losest_obj_lat_ttc_fcw\x18\x1f \x01(\x01\x12\x17\n\x0fttc_fcw_display\x18  \x01(\x01\x12\x18\n\x10ttc_fcta_display\x18! \x01(\x01\x12\x18\n\x10ttc_rcta_display\x18\" \x01(\x01\x12\x18\n\x10ttc_rctb_display\x18# \x01(\x01\x12\x18\n\x10\x63losest_obj_dist\x18$ \x01(\x01\x12$\n\x1c\x63losest_obj_confidence_score\x18% \x01(\x01\x12!\n\x19\x63losest_obj_tracking_time\x18& \x01(\x01\x12\x1b\n\x13\x63losest_obj_overlap\x18\' \x01(\x01\x12\x12\n\nblc_msg_id\x18( \x01(\x05\x12\x16\n\x0e\x64isplay_reason\x18\x64 \x01(\t\x12\'\n\x18\x65nable_cruise_speed_mode\x18\x65 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x10\x63ruise_speed_cmd\x18\x66 \x01(\x01:\x04\x35.56\x12(\n\x19\x63ruise_speed_mode_turn_on\x18g \x01(\x08:\x05\x66\x61lse\x12G\n\x0f\x61\x65\x62_enable_type\x18h \x01(\x0e\x32..deeproute.aeb.VisualizerCommand.AebEnableType\x12=\n\taeb_level\x18i \x01(\x0e\x32*.deeproute.aeb.VisualizerCommand.LevelType\x12=\n\tfcw_level\x18j \x01(\x0e\x32*.deeproute.aeb.VisualizerCommand.LevelType\x12\x11\n\tlon_accel\x18k \x01(\x01\x12\x11\n\tlat_accel\x18l \x01(\x01\x12\x19\n\x11\x66ront_wheel_angle\x18m \x01(\x01\x12\x18\n\x10\x66ront_wheel_rate\x18n \x01(\x01\"@\n\x15\x43rossingWarningStatus\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\x12\x08\n\x04\x42OTH\x10\x03*Z\n\x08\x46\x43WState\x12\x0b\n\x07\x46\x43W_OFF\x10\x00\x12\x0f\n\x0b\x46\x43W_FAILURE\x10\x01\x12\x0f\n\x0b\x46\x43W_PASSIVE\x10\x02\x12\x0e\n\nFCW_ACTIVE\x10\x03\x12\x0f\n\x0b\x46\x43W_STANDBY\x10\x04*\xa3\x01\n\x08\x41\x45\x42State\x12\x0b\n\x07\x41\x45\x42_OFF\x10\x00\x12\x0f\n\x0b\x41\x45\x42_FAILURE\x10\x01\x12\x12\n\x0e\x41\x45\x42_AWB_ACTIVE\x10\x02\x12\x12\n\x0e\x41\x45\x42_ABP_ACTIVE\x10\x03\x12\x0f\n\x0b\x41\x45\x42_PASSIVE\x10\x04\x12\x0e\n\nAEB_ACTIVE\x10\x05\x12\x0e\n\nEBA_ACTIVE\x10\x06\x12\x0f\n\x0bSTAND_STILL\x10\x07\x12\x0f\n\x0b\x41\x45\x42_STANDBY\x10\x08*`\n\tFCTAState\x12\x0c\n\x08\x46\x43TA_OFF\x10\x00\x12\x10\n\x0c\x46\x43TA_FAILURE\x10\x01\x12\x10\n\x0c\x46\x43TA_PASSIVE\x10\x02\x12\x0f\n\x0b\x46\x43TA_ACTIVE\x10\x03\x12\x10\n\x0c\x46\x43TA_STANDBY\x10\x04*v\n\tFCTBState\x12\x0c\n\x08\x46\x43TB_OFF\x10\x00\x12\x10\n\x0c\x46\x43TB_FAILURE\x10\x01\x12\x10\n\x0c\x46\x43TB_PASSIVE\x10\x02\x12\x0f\n\x0b\x46\x43TB_ACTIVE\x10\x03\x12\x14\n\x10\x46\x43TB_STAND_STILL\x10\x04\x12\x10\n\x0c\x46\x43TB_STANDBY\x10\x05*o\n\x08MEBState\x12\x0b\n\x07MEB_OFF\x10\x00\x12\x0f\n\x0bMEB_FAILURE\x10\x01\x12\x0f\n\x0bMEB_PASSIVE\x10\x02\x12\x0e\n\nMEB_ACTIVE\x10\x03\x12\x13\n\x0fMEB_STAND_STILL\x10\x04\x12\x0f\n\x0bMEB_STANDBY\x10\x05*v\n\tRCTBState\x12\x0c\n\x08RCTB_OFF\x10\x00\x12\x10\n\x0cRCTB_FAILURE\x10\x01\x12\x10\n\x0cRCTB_PASSIVE\x10\x02\x12\x0f\n\x0bRCTB_ACTIVE\x10\x03\x12\x14\n\x10RCTB_STAND_STILL\x10\x04\x12\x10\n\x0cRCTB_STANDBY\x10\x05*v\n\tRAEBState\x12\x0c\n\x08RAEB_OFF\x10\x00\x12\x10\n\x0cRAEB_FAILURE\x10\x01\x12\x10\n\x0cRAEB_PASSIVE\x10\x02\x12\x0f\n\x0bRAEB_ACTIVE\x10\x03\x12\x14\n\x10RAEB_STAND_STILL\x10\x04\x12\x10\n\x0cRAEB_STANDBY\x10\x05*Z\n\x08\x41\x42PState\x12\x0b\n\x07\x41\x42P_OFF\x10\x00\x12\x0f\n\x0b\x41\x42P_FAILURE\x10\x01\x12\x0f\n\x0b\x41\x42P_PASSIVE\x10\x02\x12\x0e\n\nABP_ACTIVE\x10\x03\x12\x0f\n\x0b\x41\x42P_STANDBY\x10\x04*Z\n\x08\x41WBState\x12\x0b\n\x07\x41WB_OFF\x10\x00\x12\x0f\n\x0b\x41WB_FAILURE\x10\x01\x12\x0f\n\x0b\x41WB_PASSIVE\x10\x02\x12\x0e\n\nAWB_ACTIVE\x10\x03\x12\x0f\n\x0b\x41WB_STANDBY\x10\x04*p\n\rClosestReason\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x46\x43W\x10\x01\x12\x07\n\x03\x41\x42P\x10\x02\x12\x07\n\x03\x41WB\x10\x03\x12\x07\n\x03\x41\x45\x42\x10\x04\x12\x07\n\x03\x45\x42\x41\x10\x05\x12\x08\n\x04RAEB\x10\x06\x12\x08\n\x04RCTB\x10\x07\x12\x08\n\x04\x46\x43TB\x10\x08\x12\x07\n\x03MEB\x10\t')

_FCWSTATE = DESCRIPTOR.enum_types_by_name['FCWState']
FCWState = enum_type_wrapper.EnumTypeWrapper(_FCWSTATE)
_AEBSTATE = DESCRIPTOR.enum_types_by_name['AEBState']
AEBState = enum_type_wrapper.EnumTypeWrapper(_AEBSTATE)
_FCTASTATE = DESCRIPTOR.enum_types_by_name['FCTAState']
FCTAState = enum_type_wrapper.EnumTypeWrapper(_FCTASTATE)
_FCTBSTATE = DESCRIPTOR.enum_types_by_name['FCTBState']
FCTBState = enum_type_wrapper.EnumTypeWrapper(_FCTBSTATE)
_MEBSTATE = DESCRIPTOR.enum_types_by_name['MEBState']
MEBState = enum_type_wrapper.EnumTypeWrapper(_MEBSTATE)
_RCTBSTATE = DESCRIPTOR.enum_types_by_name['RCTBState']
RCTBState = enum_type_wrapper.EnumTypeWrapper(_RCTBSTATE)
_RAEBSTATE = DESCRIPTOR.enum_types_by_name['RAEBState']
RAEBState = enum_type_wrapper.EnumTypeWrapper(_RAEBSTATE)
_ABPSTATE = DESCRIPTOR.enum_types_by_name['ABPState']
ABPState = enum_type_wrapper.EnumTypeWrapper(_ABPSTATE)
_AWBSTATE = DESCRIPTOR.enum_types_by_name['AWBState']
AWBState = enum_type_wrapper.EnumTypeWrapper(_AWBSTATE)
_CLOSESTREASON = DESCRIPTOR.enum_types_by_name['ClosestReason']
ClosestReason = enum_type_wrapper.EnumTypeWrapper(_CLOSESTREASON)
FCW_OFF = 0
FCW_FAILURE = 1
FCW_PASSIVE = 2
FCW_ACTIVE = 3
FCW_STANDBY = 4
AEB_OFF = 0
AEB_FAILURE = 1
AEB_AWB_ACTIVE = 2
AEB_ABP_ACTIVE = 3
AEB_PASSIVE = 4
AEB_ACTIVE = 5
EBA_ACTIVE = 6
STAND_STILL = 7
AEB_STANDBY = 8
FCTA_OFF = 0
FCTA_FAILURE = 1
FCTA_PASSIVE = 2
FCTA_ACTIVE = 3
FCTA_STANDBY = 4
FCTB_OFF = 0
FCTB_FAILURE = 1
FCTB_PASSIVE = 2
FCTB_ACTIVE = 3
FCTB_STAND_STILL = 4
FCTB_STANDBY = 5
MEB_OFF = 0
MEB_FAILURE = 1
MEB_PASSIVE = 2
MEB_ACTIVE = 3
MEB_STAND_STILL = 4
MEB_STANDBY = 5
RCTB_OFF = 0
RCTB_FAILURE = 1
RCTB_PASSIVE = 2
RCTB_ACTIVE = 3
RCTB_STAND_STILL = 4
RCTB_STANDBY = 5
RAEB_OFF = 0
RAEB_FAILURE = 1
RAEB_PASSIVE = 2
RAEB_ACTIVE = 3
RAEB_STAND_STILL = 4
RAEB_STANDBY = 5
ABP_OFF = 0
ABP_FAILURE = 1
ABP_PASSIVE = 2
ABP_ACTIVE = 3
ABP_STANDBY = 4
AWB_OFF = 0
AWB_FAILURE = 1
AWB_PASSIVE = 2
AWB_ACTIVE = 3
AWB_STANDBY = 4
UNKNOWN = 0
FCW = 1
ABP = 2
AWB = 3
AEB = 4
EBA = 5
RAEB = 6
RCTB = 7
FCTB = 8
MEB = 9


_STATEINFO = DESCRIPTOR.message_types_by_name['StateInfo']
_STATEWRAPPER = DESCRIPTOR.message_types_by_name['StateWrapper']
_STATEWRAPPER_CROSSINGWARNINGSTATUS = _STATEWRAPPER.enum_types_by_name['CrossingWarningStatus']
StateInfo = _reflection.GeneratedProtocolMessageType('StateInfo', (_message.Message,), {
  'DESCRIPTOR' : _STATEINFO,
  '__module__' : 'aeb.aeb_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.aeb.StateInfo)
  })
_sym_db.RegisterMessage(StateInfo)

StateWrapper = _reflection.GeneratedProtocolMessageType('StateWrapper', (_message.Message,), {
  'DESCRIPTOR' : _STATEWRAPPER,
  '__module__' : 'aeb.aeb_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.aeb.StateWrapper)
  })
_sym_db.RegisterMessage(StateWrapper)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATEWRAPPER.fields_by_name['closest_obj_id']._options = None
  _STATEWRAPPER.fields_by_name['closest_obj_id']._serialized_options = b'\030\001'
  _FCWSTATE._serialized_start=2275
  _FCWSTATE._serialized_end=2365
  _AEBSTATE._serialized_start=2368
  _AEBSTATE._serialized_end=2531
  _FCTASTATE._serialized_start=2533
  _FCTASTATE._serialized_end=2629
  _FCTBSTATE._serialized_start=2631
  _FCTBSTATE._serialized_end=2749
  _MEBSTATE._serialized_start=2751
  _MEBSTATE._serialized_end=2862
  _RCTBSTATE._serialized_start=2864
  _RCTBSTATE._serialized_end=2982
  _RAEBSTATE._serialized_start=2984
  _RAEBSTATE._serialized_end=3102
  _ABPSTATE._serialized_start=3104
  _ABPSTATE._serialized_end=3194
  _AWBSTATE._serialized_start=3196
  _AWBSTATE._serialized_end=3286
  _CLOSESTREASON._serialized_start=3288
  _CLOSESTREASON._serialized_end=3400
  _STATEINFO._serialized_start=94
  _STATEINFO._serialized_end=553
  _STATEWRAPPER._serialized_start=556
  _STATEWRAPPER._serialized_end=2273
  _STATEWRAPPER_CROSSINGWARNINGSTATUS._serialized_start=2209
  _STATEWRAPPER_CROSSINGWARNINGSTATUS._serialized_end=2273
# @@protoc_insertion_point(module_scope)
