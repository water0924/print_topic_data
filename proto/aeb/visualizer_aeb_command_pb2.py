# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aeb/visualizer_aeb_command.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n aeb/visualizer_aeb_command.proto\x12\rdeeproute.aeb\"\x99\x0c\n\x11VisualizerCommand\x12\x12\n\naeb_enable\x18\x01 \x01(\x08\x12\r\n\x05speed\x18\x02 \x01(\x01\x12\x18\n\x10\x65nable_set_speed\x18\x03 \x01(\x08\x12G\n\x0f\x61\x65\x62_enable_type\x18\x04 \x01(\x0e\x32..deeproute.aeb.VisualizerCommand.AebEnableType\x12V\n\x17\x61\x65\x62_cross_object_switch\x18\x05 \x01(\x0e\x32\x35.deeproute.aeb.VisualizerCommand.AebCrossObjectSwitch\x12K\n\x11\x63ruise_speed_type\x18\x06 \x01(\x0e\x32\x30.deeproute.aeb.VisualizerCommand.CruiseSpeedType\x12=\n\taeb_level\x18\x07 \x01(\x0e\x32*.deeproute.aeb.VisualizerCommand.LevelType\x12=\n\tfcw_level\x18\x08 \x01(\x0e\x32*.deeproute.aeb.VisualizerCommand.LevelType\x12G\n\x0fmeb_enable_type\x18\t \x01(\x0e\x32..deeproute.aeb.VisualizerCommand.AebEnableType\x12H\n\x10\x66\x63tb_enable_type\x18\n \x01(\x0e\x32..deeproute.aeb.VisualizerCommand.AebEnableType\x12H\n\x10rctb_enable_type\x18\x0b \x01(\x0e\x32..deeproute.aeb.VisualizerCommand.AebEnableType\x12I\n\x10pose_checker_cmd\x18W \x01(\x0b\x32/.deeproute.aeb.VisualizerCommand.PoseCheckerCmd\x12#\n\x1blat_accel_max_nudge_fcw_cmd\x18X \x01(\x01\x12%\n\x1dlat_accel_max_nudge_point_cmd\x18Y \x01(\x01\x12\x1f\n\x17lat_accel_max_nudge_cmd\x18Z \x01(\x01\x12\x1b\n\x13lat_ignore_dist_cmd\x18[ \x01(\x01\x12 \n\x18raeb_buffer_duration_cmd\x18\\ \x01(\x01\x12 \n\x18rctb_buffer_duration_cmd\x18] \x01(\x01\x12 \n\x18\x66\x63ta_buffer_duration_cmd\x18^ \x01(\x01\x12\x1f\n\x17\x66\x63w_buffer_duration_cmd\x18_ \x01(\x01\x12\x1f\n\x17\x61\x65\x62_buffer_duration_cmd\x18` \x01(\x01\x12\x1a\n\x12\x64ists_stop_vru_cmd\x18\x61 \x03(\x01\x12\x16\n\x0e\x64ists_stop_cmd\x18\x62 \x03(\x01\x12\x1b\n\x13\x65\x62\x61_decel_table_cmd\x18\x63 \x03(\x01\x12\x1b\n\x13\x61\x65\x62_decel_table_cmd\x18\x64 \x03(\x01\x1a]\n\x0ePoseCheckerCmd\x12\x1c\n\x0f\x64ist_step_thres\x18\x01 \x01(\x01:\x03\x30.5\x12\x17\n\x0c\x62uffer_thres\x18\x02 \x01(\x05:\x01\x35\x12\x14\n\x08\x64uration\x18\x03 \x01(\x01:\x02\x32\x30\"U\n\rAebEnableType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x43LOSE\x10\x01\x12\x13\n\x0fOPEN_CARE_BRAKE\x10\x02\x12\x17\n\x13OPEN_NOT_CARE_BRAKE\x10\x03\"C\n\x14\x41\x65\x62\x43rossObjectSwitch\x12\x12\n\x0eSWITCH_UNKNOWN\x10\x00\x12\n\n\x06\x45NABLE\x10\x01\x12\x0b\n\x07\x44ISABLE\x10\x02\">\n\x0f\x43ruiseSpeedType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x0b\n\x07TURN_ON\x10\x01\x12\x0c\n\x08TURN_OFF\x10\x02\"X\n\tLevelType\x12\x11\n\rLEVEL_UNKNOWN\x10\x00\x12\t\n\x05\x45\x41RLY\x10\x01\x12\n\n\x06MIDDLE\x10\x02\x12\x08\n\x04LATE\x10\x03\x12\n\n\x06\x43USTOM\x10\x04\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x05')



_VISUALIZERCOMMAND = DESCRIPTOR.message_types_by_name['VisualizerCommand']
_VISUALIZERCOMMAND_POSECHECKERCMD = _VISUALIZERCOMMAND.nested_types_by_name['PoseCheckerCmd']
_VISUALIZERCOMMAND_AEBENABLETYPE = _VISUALIZERCOMMAND.enum_types_by_name['AebEnableType']
_VISUALIZERCOMMAND_AEBCROSSOBJECTSWITCH = _VISUALIZERCOMMAND.enum_types_by_name['AebCrossObjectSwitch']
_VISUALIZERCOMMAND_CRUISESPEEDTYPE = _VISUALIZERCOMMAND.enum_types_by_name['CruiseSpeedType']
_VISUALIZERCOMMAND_LEVELTYPE = _VISUALIZERCOMMAND.enum_types_by_name['LevelType']
VisualizerCommand = _reflection.GeneratedProtocolMessageType('VisualizerCommand', (_message.Message,), {

  'PoseCheckerCmd' : _reflection.GeneratedProtocolMessageType('PoseCheckerCmd', (_message.Message,), {
    'DESCRIPTOR' : _VISUALIZERCOMMAND_POSECHECKERCMD,
    '__module__' : 'aeb.visualizer_aeb_command_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.aeb.VisualizerCommand.PoseCheckerCmd)
    })
  ,
  'DESCRIPTOR' : _VISUALIZERCOMMAND,
  '__module__' : 'aeb.visualizer_aeb_command_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.aeb.VisualizerCommand)
  })
_sym_db.RegisterMessage(VisualizerCommand)
_sym_db.RegisterMessage(VisualizerCommand.PoseCheckerCmd)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VISUALIZERCOMMAND._serialized_start=52
  _VISUALIZERCOMMAND._serialized_end=1613
  _VISUALIZERCOMMAND_POSECHECKERCMD._serialized_start=1210
  _VISUALIZERCOMMAND_POSECHECKERCMD._serialized_end=1303
  _VISUALIZERCOMMAND_AEBENABLETYPE._serialized_start=1305
  _VISUALIZERCOMMAND_AEBENABLETYPE._serialized_end=1390
  _VISUALIZERCOMMAND_AEBCROSSOBJECTSWITCH._serialized_start=1392
  _VISUALIZERCOMMAND_AEBCROSSOBJECTSWITCH._serialized_end=1459
  _VISUALIZERCOMMAND_CRUISESPEEDTYPE._serialized_start=1461
  _VISUALIZERCOMMAND_CRUISESPEEDTYPE._serialized_end=1523
  _VISUALIZERCOMMAND_LEVELTYPE._serialized_start=1525
  _VISUALIZERCOMMAND_LEVELTYPE._serialized_end=1613
# @@protoc_insertion_point(module_scope)
