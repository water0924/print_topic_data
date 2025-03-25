# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: control/control_cmd.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.canbus import chassis_pb2 as canbus_dot_chassis__pb2
from proto.common import header_pb2 as common_dot_header__pb2
from proto.common import vehicle_signal_pb2 as common_dot_vehicle__signal__pb2
from proto.common import drive_state_pb2 as common_dot_drive__state__pb2
from proto.control import pad_msg_pb2 as control_dot_pad__msg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63ontrol/control_cmd.proto\x12\x11\x64\x65\x65proute.control\x1a\x14\x63\x61nbus/chassis.proto\x1a\x13\x63ommon/header.proto\x1a\x1b\x63ommon/vehicle_signal.proto\x1a\x18\x63ommon/drive_state.proto\x1a\x15\x63ontrol/pad_msg.proto\"^\n\x0cLatencyStats\x12\x15\n\rtotal_time_ms\x18\x01 \x01(\x01\x12\x1a\n\x12\x63ontroller_time_ms\x18\x02 \x03(\x01\x12\x1b\n\x13total_time_exceeded\x18\x03 \x01(\x08\"\x9b\x05\n\nAEBCommand\x12\x32\n\x03\x66\x63w\x18\x01 \x01(\x0b\x32%.deeproute.control.AEBCommand.AEBMode\x12\x32\n\x03\x61\x65\x62\x18\x02 \x01(\x0b\x32%.deeproute.control.AEBCommand.AEBMode\x12\x32\n\x03\x61\x62p\x18\x03 \x01(\x0b\x32%.deeproute.control.AEBCommand.AEBMode\x12\x32\n\x03\x61wb\x18\x04 \x01(\x0b\x32%.deeproute.control.AEBCommand.AEBMode\x12\x32\n\x03\x65\x62\x61\x18\x05 \x01(\x0b\x32%.deeproute.control.AEBCommand.AEBMode\x12\x32\n\x03\x61\x62\x61\x18\x06 \x01(\x0b\x32%.deeproute.control.AEBCommand.AEBMode\x12\x33\n\x04rctb\x18\x08 \x01(\x0b\x32%.deeproute.control.AEBCommand.AEBMode\x12\x32\n\x03meb\x18\t \x01(\x0b\x32%.deeproute.control.AEBCommand.AEBMode\x12\x1c\n\x14\x61\x65\x62_interface_enable\x18\x07 \x01(\x08\x12\x18\n\x10time_measurement\x18\n \x01(\x03\x1a\xb3\x01\n\x07\x41\x45\x42Mode\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12:\n\x05level\x18\x02 \x01(\x0e\x32+.deeproute.control.AEBCommand.AEBMode.Level\x12\x15\n\rrequest_value\x18\x03 \x01(\x01\"E\n\x05Level\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07LEVEL_1\x10\x01\x12\x0b\n\x07LEVEL_2\x10\x02\x12\x0b\n\x07LEVEL_3\x10\x03\x12\x0b\n\x07LEVEL_4\x10\x04\"\xdd\r\n\x0e\x43ontrolCommand\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.deeproute.common.Header\x12\x10\n\x08throttle\x18\x03 \x01(\x01\x12\r\n\x05\x62rake\x18\x04 \x01(\x01\x12\x15\n\rsteering_rate\x18\x06 \x01(\x01\x12\x17\n\x0fsteering_target\x18\x07 \x01(\x01\x12\x15\n\rparking_brake\x18\x08 \x01(\x08\x12\r\n\x05speed\x18\t \x01(\x01\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\n \x01(\x01\x12\x15\n\thigh_beam\x18\x0b \x01(\x08\x42\x02\x18\x01\x12\x14\n\x08low_beam\x18\x0c \x01(\x08\x42\x02\x18\x01\x12\x15\n\tleft_turn\x18\r \x01(\x08\x42\x02\x18\x01\x12\x16\n\nright_turn\x18\x0e \x01(\x08\x42\x02\x18\x01\x12\x10\n\x04horn\x18\x0f \x01(\x08\x42\x02\x18\x01\x12\x17\n\x0breset_model\x18\x10 \x01(\x08\x42\x02\x18\x01\x12\x15\n\rengine_on_off\x18\x11 \x01(\x08\x12\x1b\n\x13trajectory_fraction\x18\x12 \x01(\x01\x12;\n\x0c\x64riving_mode\x18\x13 \x01(\x0e\x32%.deeproute.canbus.Chassis.DrivingMode\x12=\n\rgear_location\x18\x14 \x01(\x0e\x32&.deeproute.canbus.Chassis.GearPosition\x12\x35\n\nturnsignal\x18\x15 \x01(\x0e\x32\x1d.deeproute.control.TurnSignalB\x02\x18\x01\x12/\n\x06signal\x18\x17 \x01(\x0b\x32\x1f.deeproute.common.VehicleSignal\x12\x36\n\rlatency_stats\x18\x18 \x01(\x0b\x32\x1f.deeproute.control.LatencyStats\x12\x32\n\x07pad_msg\x18\x19 \x01(\x0b\x32\x1d.deeproute.control.PadMessageB\x02\x18\x01\x12\x35\n\rengage_advice\x18\x1a \x01(\x0b\x32\x1e.deeproute.common.EngageAdvice\x12\x1e\n\x0fis_in_safe_mode\x18\x1b \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0b\x66lag_reinit\x18\x1c \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0breset_count\x18\x1d \x01(\x05:\x01\x30\x12\x1e\n\x13node_abnormal_count\x18\x1e \x01(\x05:\x01\x30\x12\x13\n\x08time_cur\x18\x1f \x01(\x01:\x01\x30\x12\x14\n\ttimestamp\x18  \x01(\x03:\x01\x30\x12\x0e\n\x06torque\x18! \x01(\x01\x12+\n\x1fphysical_throttle_pedal_request\x18\" \x01(\x01\x42\x02\x18\x01\x12(\n\x1cphysical_brake_pedal_request\x18# \x01(\x01\x42\x02\x18\x01\x12\x18\n\x10longitudinal_cmd\x18$ \x01(\x01\x12\x1e\n\x16torque_table_steer_deg\x18% \x01(\x01\x12#\n\x1btorque_table_steer_deg_rate\x18& \x01(\x01\x12\x1a\n\x12rear_steering_rate\x18\' \x01(\x01\x12\x1c\n\x14rear_steering_target\x18( \x01(\x01\x12\'\n\x1ftrajectory_perception_timestamp\x18) \x01(\x03\x12\x1d\n\x15received_mode_request\x18* \x01(\x08\x12\x18\n\x10\x61\x63\x63\x65leration_cmd\x18+ \x01(\x01\x12\x1b\n\x13\x61\x63\x63\x65leration_desire\x18, \x01(\x01\x12\x0f\n\x07use_apa\x18- \x01(\x08\x12!\n\x19longitudinal_cmd_distance\x18. \x01(\x01\x12\x18\n\x10lateral_cmd_rate\x18/ \x01(\x01\x12\x13\n\x0blateral_cmd\x18\x30 \x01(\x01\x12\x36\n\x0b\x61\x65\x62_command\x18\x31 \x01(\x0b\x32\x1d.deeproute.control.AEBCommandB\x02\x18\x01\x12$\n\x18\x64ynamic_jerk_limit_upper\x18\x33 \x01(\x01:\x02\x31\x30\x12%\n\x18\x64ynamic_jerk_limit_lower\x18\x34 \x01(\x01:\x03-10\x12!\n\x12\x64\x65\x63\x65lerate_to_stop\x18\x35 \x01(\x08:\x05\x66\x61lse\x12\'\n\x18slope_decelerate_to_stop\x18\x36 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x61pa_emergency_brake\x18\x37 \x01(\x08:\x05\x66\x61lse\x12(\n\x1cuse_full_feedback_controller\x18\x38 \x01(\x08\x42\x02\x18\x01\x12\x19\n\nstandstill\x18\x39 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x08\x64riveoff\x18: \x01(\x08:\x05\x66\x61lse\"\x97\x03\n\nESACommand\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.deeproute.common.Header\x12\x0e\n\x06\x65nable\x18\x02 \x01(\x08\x12\x1b\n\x13\x61\x63\x63\x65leration_desire\x18\x03 \x01(\x01\x12\x15\n\rsteering_rate\x18\x04 \x01(\x01\x12\x17\n\x0fsteering_target\x18\x05 \x01(\x01\x12/\n\x06signal\x18\x06 \x01(\x0b\x32\x1f.deeproute.common.VehicleSignal\x12=\n\rgear_location\x18\x07 \x01(\x0e\x32&.deeproute.canbus.Chassis.GearPosition\x12\x18\n\x10time_measurement\x18\x08 \x01(\x03\x12\x10\n\x08throttle\x18\x65 \x01(\x01\x12\r\n\x05\x62rake\x18\x66 \x01(\x01\x12\x18\n\x10longitudinal_cmd\x18g \x01(\x01\x12\x18\n\x10lateral_cmd_rate\x18h \x01(\x01\x12\x13\n\x0blateral_cmd\x18i \x01(\x01\x12\x0e\n\x06torque\x18j \x01(\x01*:\n\nTurnSignal\x12\r\n\tTURN_NONE\x10\x00\x12\r\n\tTURN_LEFT\x10\x01\x12\x0e\n\nTURN_RIGHT\x10\x02')

_TURNSIGNAL = DESCRIPTOR.enum_types_by_name['TurnSignal']
TurnSignal = enum_type_wrapper.EnumTypeWrapper(_TURNSIGNAL)
TURN_NONE = 0
TURN_LEFT = 1
TURN_RIGHT = 2


_LATENCYSTATS = DESCRIPTOR.message_types_by_name['LatencyStats']
_AEBCOMMAND = DESCRIPTOR.message_types_by_name['AEBCommand']
_AEBCOMMAND_AEBMODE = _AEBCOMMAND.nested_types_by_name['AEBMode']
_CONTROLCOMMAND = DESCRIPTOR.message_types_by_name['ControlCommand']
_ESACOMMAND = DESCRIPTOR.message_types_by_name['ESACommand']
_AEBCOMMAND_AEBMODE_LEVEL = _AEBCOMMAND_AEBMODE.enum_types_by_name['Level']
LatencyStats = _reflection.GeneratedProtocolMessageType('LatencyStats', (_message.Message,), {
  'DESCRIPTOR' : _LATENCYSTATS,
  '__module__' : 'control.control_cmd_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.control.LatencyStats)
  })
_sym_db.RegisterMessage(LatencyStats)

AEBCommand = _reflection.GeneratedProtocolMessageType('AEBCommand', (_message.Message,), {

  'AEBMode' : _reflection.GeneratedProtocolMessageType('AEBMode', (_message.Message,), {
    'DESCRIPTOR' : _AEBCOMMAND_AEBMODE,
    '__module__' : 'control.control_cmd_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.control.AEBCommand.AEBMode)
    })
  ,
  'DESCRIPTOR' : _AEBCOMMAND,
  '__module__' : 'control.control_cmd_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.control.AEBCommand)
  })
_sym_db.RegisterMessage(AEBCommand)
_sym_db.RegisterMessage(AEBCommand.AEBMode)

ControlCommand = _reflection.GeneratedProtocolMessageType('ControlCommand', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLCOMMAND,
  '__module__' : 'control.control_cmd_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.control.ControlCommand)
  })
_sym_db.RegisterMessage(ControlCommand)

ESACommand = _reflection.GeneratedProtocolMessageType('ESACommand', (_message.Message,), {
  'DESCRIPTOR' : _ESACOMMAND,
  '__module__' : 'control.control_cmd_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.control.ESACommand)
  })
_sym_db.RegisterMessage(ESACommand)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONTROLCOMMAND.fields_by_name['high_beam']._options = None
  _CONTROLCOMMAND.fields_by_name['high_beam']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['low_beam']._options = None
  _CONTROLCOMMAND.fields_by_name['low_beam']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['left_turn']._options = None
  _CONTROLCOMMAND.fields_by_name['left_turn']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['right_turn']._options = None
  _CONTROLCOMMAND.fields_by_name['right_turn']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['horn']._options = None
  _CONTROLCOMMAND.fields_by_name['horn']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['reset_model']._options = None
  _CONTROLCOMMAND.fields_by_name['reset_model']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['turnsignal']._options = None
  _CONTROLCOMMAND.fields_by_name['turnsignal']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['pad_msg']._options = None
  _CONTROLCOMMAND.fields_by_name['pad_msg']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['physical_throttle_pedal_request']._options = None
  _CONTROLCOMMAND.fields_by_name['physical_throttle_pedal_request']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['physical_brake_pedal_request']._options = None
  _CONTROLCOMMAND.fields_by_name['physical_brake_pedal_request']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['aeb_command']._options = None
  _CONTROLCOMMAND.fields_by_name['aeb_command']._serialized_options = b'\030\001'
  _CONTROLCOMMAND.fields_by_name['use_full_feedback_controller']._options = None
  _CONTROLCOMMAND.fields_by_name['use_full_feedback_controller']._serialized_options = b'\030\001'
  _TURNSIGNAL._serialized_start=3105
  _TURNSIGNAL._serialized_end=3163
  _LATENCYSTATS._serialized_start=169
  _LATENCYSTATS._serialized_end=263
  _AEBCOMMAND._serialized_start=266
  _AEBCOMMAND._serialized_end=933
  _AEBCOMMAND_AEBMODE._serialized_start=754
  _AEBCOMMAND_AEBMODE._serialized_end=933
  _AEBCOMMAND_AEBMODE_LEVEL._serialized_start=864
  _AEBCOMMAND_AEBMODE_LEVEL._serialized_end=933
  _CONTROLCOMMAND._serialized_start=936
  _CONTROLCOMMAND._serialized_end=2693
  _ESACOMMAND._serialized_start=2696
  _ESACOMMAND._serialized_end=3103
# @@protoc_insertion_point(module_scope)
