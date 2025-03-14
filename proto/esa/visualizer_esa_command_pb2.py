# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: esa/visualizer_esa_command.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import header_pb2 as common_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n esa/visualizer_esa_command.proto\x12\rdeeproute.esa\x1a\x13\x63ommon/header.proto\"\xb1\x02\n\x11VisualizerCommand\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.deeproute.common.Header\x12\x12\n\nrequest_id\x18\x02 \x01(\x05\x12\x42\n\x10vis_cmd_function\x18\x03 \x01(\x0b\x32(.deeproute.esa.VisualizerCommandFunction\x12K\n\x15vis_cmd_state_machine\x18\x04 \x01(\x0b\x32,.deeproute.esa.VisualizerCommandStateMachine\x12M\n\x16vis_cmd_internal_param\x18\x05 \x01(\x0b\x32-.deeproute.esa.VisualizerCommandInternalParam\"\xab\x02\n\x19VisualizerCommandFunction\x12J\n\nesa_enable\x18\x01 \x01(\x0e\x32\x36.deeproute.esa.VisualizerCommandFunction.EsaEnableType\x12\x46\n\x08\x65sa_mode\x18\x02 \x01(\x0e\x32\x34.deeproute.esa.VisualizerCommandFunction.EsaModeType\"<\n\rEsaEnableType\x12\x12\n\x0eUNKNOWN_SWITCH\x10\x00\x12\n\n\x06\x45NABLE\x10\x01\x12\x0b\n\x07\x44ISABLE\x10\x02\"<\n\x0b\x45saModeType\x12\x10\n\x0cUNKNOWN_MODE\x10\x00\x12\r\n\tCLOSELOOP\x10\x01\x12\x0c\n\x08OPENLOOP\x10\x02\"\xa9\x04\n\x1dVisualizerCommandStateMachine\x12!\n\x19state_active_lookup_speed\x18\x01 \x03(\x01\x12\'\n\x1fstate_active_lookup_steer_angle\x18\x02 \x03(\x01\x12&\n\x1estate_active_lookup_steer_rate\x18\x03 \x03(\x01\x12\x18\n\x10state_active_ttc\x18\x04 \x01(\x01\x12)\n!actv_cond_obj_standstil_max_speed\x18\x05 \x01(\x01\x12#\n\x1b\x61\x63tv_cond_obj_max_lat_speed\x18\x06 \x01(\x01\x12(\n state_quit_parallel_heading_diff\x18\x0b \x01(\x01\x12$\n\x1c\x65xit_cond_traj_deviation_lon\x18\x0c \x01(\x01\x12$\n\x1c\x65xit_cond_traj_deviation_lat\x18\r \x01(\x01\x12!\n\x19inhib_cond_lookup_speed_1\x18\x15 \x03(\x01\x12%\n\x1dinhib_cond_lookup_steer_angle\x18\x16 \x03(\x01\x12$\n\x1cinhib_cond_lookup_steer_rate\x18\x17 \x03(\x01\x12!\n\x19inhib_cond_lookup_speed_2\x18\x18 \x03(\x01\x12!\n\x19inhib_cond_lookup_lat_acc\x18\x19 \x03(\x01\"\xbe\x02\n\x1eVisualizerCommandInternalParam\x12)\n!path_sample_points_num_each_level\x18\x01 \x01(\r\x12.\n&path_sample_points_lat_dist_each_level\x18\x02 \x01(\x01\x12.\n&path_cost_unknown_unmovable_dist_thres\x18\x0b \x01(\x01\x12#\n\x1bpath_cost_others_dist_thres\x18\x0c \x01(\x01\x12\x1f\n\x17path_check_lookup_speed\x18\x15 \x03(\x01\x12%\n\x1dpath_check_lookup_steer_angle\x18\x16 \x03(\x01\x12$\n\x1cpath_check_lookup_steer_rate\x18\x17 \x03(\x01\"0\n\x19VisualizerCommandResponse\x12\x13\n\x0bresponse_id\x18\x01 \x01(\x05')



_VISUALIZERCOMMAND = DESCRIPTOR.message_types_by_name['VisualizerCommand']
_VISUALIZERCOMMANDFUNCTION = DESCRIPTOR.message_types_by_name['VisualizerCommandFunction']
_VISUALIZERCOMMANDSTATEMACHINE = DESCRIPTOR.message_types_by_name['VisualizerCommandStateMachine']
_VISUALIZERCOMMANDINTERNALPARAM = DESCRIPTOR.message_types_by_name['VisualizerCommandInternalParam']
_VISUALIZERCOMMANDRESPONSE = DESCRIPTOR.message_types_by_name['VisualizerCommandResponse']
_VISUALIZERCOMMANDFUNCTION_ESAENABLETYPE = _VISUALIZERCOMMANDFUNCTION.enum_types_by_name['EsaEnableType']
_VISUALIZERCOMMANDFUNCTION_ESAMODETYPE = _VISUALIZERCOMMANDFUNCTION.enum_types_by_name['EsaModeType']
VisualizerCommand = _reflection.GeneratedProtocolMessageType('VisualizerCommand', (_message.Message,), {
  'DESCRIPTOR' : _VISUALIZERCOMMAND,
  '__module__' : 'esa.visualizer_esa_command_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.esa.VisualizerCommand)
  })
_sym_db.RegisterMessage(VisualizerCommand)

VisualizerCommandFunction = _reflection.GeneratedProtocolMessageType('VisualizerCommandFunction', (_message.Message,), {
  'DESCRIPTOR' : _VISUALIZERCOMMANDFUNCTION,
  '__module__' : 'esa.visualizer_esa_command_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.esa.VisualizerCommandFunction)
  })
_sym_db.RegisterMessage(VisualizerCommandFunction)

VisualizerCommandStateMachine = _reflection.GeneratedProtocolMessageType('VisualizerCommandStateMachine', (_message.Message,), {
  'DESCRIPTOR' : _VISUALIZERCOMMANDSTATEMACHINE,
  '__module__' : 'esa.visualizer_esa_command_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.esa.VisualizerCommandStateMachine)
  })
_sym_db.RegisterMessage(VisualizerCommandStateMachine)

VisualizerCommandInternalParam = _reflection.GeneratedProtocolMessageType('VisualizerCommandInternalParam', (_message.Message,), {
  'DESCRIPTOR' : _VISUALIZERCOMMANDINTERNALPARAM,
  '__module__' : 'esa.visualizer_esa_command_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.esa.VisualizerCommandInternalParam)
  })
_sym_db.RegisterMessage(VisualizerCommandInternalParam)

VisualizerCommandResponse = _reflection.GeneratedProtocolMessageType('VisualizerCommandResponse', (_message.Message,), {
  'DESCRIPTOR' : _VISUALIZERCOMMANDRESPONSE,
  '__module__' : 'esa.visualizer_esa_command_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.esa.VisualizerCommandResponse)
  })
_sym_db.RegisterMessage(VisualizerCommandResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VISUALIZERCOMMAND._serialized_start=73
  _VISUALIZERCOMMAND._serialized_end=378
  _VISUALIZERCOMMANDFUNCTION._serialized_start=381
  _VISUALIZERCOMMANDFUNCTION._serialized_end=680
  _VISUALIZERCOMMANDFUNCTION_ESAENABLETYPE._serialized_start=558
  _VISUALIZERCOMMANDFUNCTION_ESAENABLETYPE._serialized_end=618
  _VISUALIZERCOMMANDFUNCTION_ESAMODETYPE._serialized_start=620
  _VISUALIZERCOMMANDFUNCTION_ESAMODETYPE._serialized_end=680
  _VISUALIZERCOMMANDSTATEMACHINE._serialized_start=683
  _VISUALIZERCOMMANDSTATEMACHINE._serialized_end=1236
  _VISUALIZERCOMMANDINTERNALPARAM._serialized_start=1239
  _VISUALIZERCOMMANDINTERNALPARAM._serialized_end=1557
  _VISUALIZERCOMMANDRESPONSE._serialized_start=1559
  _VISUALIZERCOMMANDRESPONSE._serialized_end=1607
# @@protoc_insertion_point(module_scope)
