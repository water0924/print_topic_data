# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/vehicle_state/vehicle_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.canbus import chassis_pb2 as canbus_dot_chassis__pb2
from proto.common import geometry_pb2 as common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(common/vehicle_state/vehicle_state.proto\x12\x10\x64\x65\x65proute.common\x1a\x14\x63\x61nbus/chassis.proto\x1a\x15\x63ommon/geometry.proto\"\xaf\x0c\n\x0cVehicleState\x12\x14\n\ttimestamp\x18\x04 \x01(\x03:\x01\x30\x12\x34\n\x04gear\x18\r \x01(\x0e\x32&.deeproute.canbus.Chassis.GearPosition\x12;\n\x0c\x64riving_mode\x18\x0e \x01(\x0e\x32%.deeproute.canbus.Chassis.DrivingMode\x12+\n\x08position\x18\x10 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12/\n\x0cvelocity_enu\x18\x11 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12/\n\x0cvelocity_flu\x18\x12 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x31\n\x0eroll_pitch_yaw\x18\x13 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x37\n\x14\x61ngular_velocity_flu\x18\x14 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x33\n\x10\x61\x63\x63\x65leration_flu\x18\x15 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x19\n\x11\x66ront_wheel_angle\x18\x16 \x01(\x02\x12>\n\x0bturn_signal\x18\x17 \x01(\x0e\x32).deeproute.common.VehicleState.TurnSignal\x12\x1a\n\x12warning_blinker_on\x18\x18 \x01(\x08\x12 \n\x18\x61\x63\x63\x65leration_over_ground\x18\x19 \x01(\x02\x12\x31\n\x0bwheel_speed\x18\x1a \x01(\x0b\x32\x1c.deeproute.canbus.WheelSpeed\x12\x14\n\x0clongitudinal\x18\x1b \x01(\x02\x12\r\n\x05speed\x18\x1c \x01(\x02\x12\x1e\n\x16\x66ront_wheel_angle_rate\x18\x1d \x01(\x01\x12 \n\x18has_physical_pedal_input\x18\x1e \x01(\x08\x12\x1b\n\x10rear_wheel_angle\x18\x1f \x01(\x02:\x01\x30\x12 \n\x15rear_wheel_angle_rate\x18  \x01(\x02:\x01\x30\x12O\n\x14vehicle_mode_request\x18! \x01(\x0b\x32\x31.deeproute.common.VehicleState.VehicleModeRequest\x12\x44\n\x0e\x63ontrol_source\x18\" \x01(\x0e\x32,.deeproute.common.VehicleState.ControlSource\x12!\n\x16localization_timestamp\x18# \x01(\x03:\x01\x30\x12!\n\x19revised_front_wheel_angle\x18$ \x01(\x01\x12 \n\x18\x66ront_wheel_angle_offset\x18% \x01(\x01\x12\x1e\n\x16\x65nable_offset_observer\x18& \x01(\x08\x12\x19\n\x11observer_yaw_rate\x18\' \x01(\x01\x12\x1a\n\x12\x61\x63t_driving_torque\x18( \x01(\x01\x12\x18\n\x10\x61\x63t_brake_torque\x18) \x01(\x01\x12\x39\n\x07\x65pb_sts\x18+ \x01(\x0e\x32(.deeproute.common.VehicleState.EpbStatus\x1aR\n\x12VehicleModeRequest\x12\x1c\n\x14vehicle_auto_request\x18\x01 \x01(\x08\x12\x1e\n\x16vehicle_manual_request\x18\x02 \x01(\x08\"0\n\nTurnSignal\x12\r\n\tNONE_TURN\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\"a\n\rControlSource\x12\n\n\x06MANUAL\x10\x00\x12\x08\n\x04\x41UTO\x10\x01\x12\x06\n\x02RC\x10\x02\x12\x10\n\x0cRC_EMERGENCY\x10\x03\x12\n\n\x06REMOTE\x10\x04\x12\x14\n\x10REMOTE_EMERGENCY\x10\x05\"N\n\tEpbStatus\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\n\n\x06PARKED\x10\x01\x12\x0c\n\x08RELEASED\x10\x02\x12\x0b\n\x07PARKING\x10\x03\x12\r\n\tRELEASING\x10\x04J\x04\x08\x01\x10\x04J\x04\x08\x05\x10\rJ\x04\x08\x0f\x10\x10')



_VEHICLESTATE = DESCRIPTOR.message_types_by_name['VehicleState']
_VEHICLESTATE_VEHICLEMODEREQUEST = _VEHICLESTATE.nested_types_by_name['VehicleModeRequest']
_VEHICLESTATE_TURNSIGNAL = _VEHICLESTATE.enum_types_by_name['TurnSignal']
_VEHICLESTATE_CONTROLSOURCE = _VEHICLESTATE.enum_types_by_name['ControlSource']
_VEHICLESTATE_EPBSTATUS = _VEHICLESTATE.enum_types_by_name['EpbStatus']
VehicleState = _reflection.GeneratedProtocolMessageType('VehicleState', (_message.Message,), {

  'VehicleModeRequest' : _reflection.GeneratedProtocolMessageType('VehicleModeRequest', (_message.Message,), {
    'DESCRIPTOR' : _VEHICLESTATE_VEHICLEMODEREQUEST,
    '__module__' : 'common.vehicle_state.vehicle_state_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.common.VehicleState.VehicleModeRequest)
    })
  ,
  'DESCRIPTOR' : _VEHICLESTATE,
  '__module__' : 'common.vehicle_state.vehicle_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.common.VehicleState)
  })
_sym_db.RegisterMessage(VehicleState)
_sym_db.RegisterMessage(VehicleState.VehicleModeRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VEHICLESTATE._serialized_start=108
  _VEHICLESTATE._serialized_end=1691
  _VEHICLESTATE_VEHICLEMODEREQUEST._serialized_start=1362
  _VEHICLESTATE_VEHICLEMODEREQUEST._serialized_end=1444
  _VEHICLESTATE_TURNSIGNAL._serialized_start=1446
  _VEHICLESTATE_TURNSIGNAL._serialized_end=1494
  _VEHICLESTATE_CONTROLSOURCE._serialized_start=1496
  _VEHICLESTATE_CONTROLSOURCE._serialized_end=1593
  _VEHICLESTATE_EPBSTATUS._serialized_start=1595
  _VEHICLESTATE_EPBSTATUS._serialized_end=1673
# @@protoc_insertion_point(module_scope)
