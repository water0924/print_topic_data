# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: safety/vehicle_info.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import geometry_pb2 as common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19safety/vehicle_info.proto\x12\x16\x64r.safety.vehicle_info\x1a\x15\x63ommon/geometry.proto\"\xe0\x08\n\x0bVehicleInfo\x12\r\n\x05speed\x18\x01 \x01(\x02\x12\x18\n\x10lateral_velocity\x18\x02 \x01(\x02\x12\x1d\n\x15longitudinal_velocity\x18\x03 \x01(\x02\x12\x19\n\x11vertical_velocity\x18\x04 \x01(\x02\x12\x1c\n\x14lateral_acceleration\x18\x05 \x01(\x02\x12!\n\x19longitudinal_acceleration\x18\x06 \x01(\x02\x12\x1d\n\x15vertical_acceleration\x18\x07 \x01(\x02\x12\x13\n\x0bwheel_angle\x18\x08 \x01(\x02\x12\x13\n\x0bwheel_speed\x18\t \x01(\x02\x12\x1b\n\x13\x61\x63\x63\x65lerator_pressed\x18\n \x01(\x08\x12 \n\x18\x61\x63\x63\x65lerator_actual_pedal\x18\x0b \x01(\x02\x12\x1c\n\x14steering_wheel_angle\x18\x0c \x01(\x02\x12\x15\n\rbrake_pressed\x18\r \x01(\x08\x12\x13\n\x0b\x62rake_pedal\x18\x0e \x01(\x02\x12\x12\n\nabs_active\x18\x0f \x01(\x08\x12\x13\n\x07wgs_lng\x18\x10 \x01(\x01\x42\x02\x18\x01\x12\x13\n\x07wgs_lat\x18\x11 \x01(\x01\x42\x02\x18\x01\x12\x13\n\x07wgs_alt\x18\x12 \x01(\x01\x42\x02\x18\x01\x12\x31\n\x04mode\x18\x13 \x01(\x0e\x32#.dr.safety.vehicle_info.DrivingMode\x12\x17\n\x0f\x66ront_left_door\x18\x14 \x01(\x08\x12\x18\n\x10\x66ront_right_door\x18\x15 \x01(\x08\x12\x16\n\x0erear_left_door\x18\x16 \x01(\x08\x12\x17\n\x0frear_right_door\x18\x17 \x01(\x08\x12\r\n\x05trunk\x18\x18 \x01(\x08\x12\x0c\n\x04hood\x18\x19 \x01(\x08\x12*\n\x04\x62\x65\x61m\x18\x1a \x01(\x0e\x32\x1c.dr.safety.vehicle_info.Beam\x12\x17\n\x0fleft_turn_light\x18\x1b \x01(\x08\x12\x18\n\x10right_turn_light\x18\x1c \x01(\x08\x12\x15\n\rwarning_light\x18\x1d \x01(\x08\x12\x18\n\x10\x64river_seat_belt\x18\x1e \x01(\x08\x12\x1b\n\x13passenger_seat_belt\x18\x1f \x03(\x08\x12\x0b\n\x03lng\x18  \x01(\x01\x12\x0b\n\x03lat\x18! \x01(\x01\x12\x0b\n\x03\x61lt\x18\" \x01(\x01\x12\x46\n\x0f\x63oordinate_type\x18# \x01(\x0e\x32&.dr.safety.vehicle_info.CoordinateType:\x05WGS84\x12\x1e\n\x16\x61\x63\x63\x65lerator_pedal_rate\x18( \x01(\x01\x12\x1c\n\x14steering_wheel_speed\x18) \x01(\x01\x12\x16\n\x0etotal_odometer\x18* \x01(\x01\x12\x1a\n\x12\x63urrent_road_class\x18+ \x01(\r\x12\x31\n\x0eroll_pitch_yaw\x18\x32 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12\x13\n\x0bprivacy_sts\x18\x33 \x01(\x08*U\n\x0b\x44rivingMode\x12\x10\n\x0cMODE_UNKNOWN\x10\x00\x12\n\n\x06MANUAL\x10\x01\x12\x14\n\x10\x41SSISTED_DRIVING\x10\x02\x12\x12\n\x0eREMOTE_DRIVING\x10\x03*(\n\x04\x42\x65\x61m\x12\r\n\tBEAM_NULL\x10\x00\x12\x08\n\x04HIGH\x10\x01\x12\x07\n\x03LOW\x10\x02*&\n\x0e\x43oordinateType\x12\t\n\x05WGS84\x10\x00\x12\t\n\x05GCJ02\x10\x01')

_DRIVINGMODE = DESCRIPTOR.enum_types_by_name['DrivingMode']
DrivingMode = enum_type_wrapper.EnumTypeWrapper(_DRIVINGMODE)
_BEAM = DESCRIPTOR.enum_types_by_name['Beam']
Beam = enum_type_wrapper.EnumTypeWrapper(_BEAM)
_COORDINATETYPE = DESCRIPTOR.enum_types_by_name['CoordinateType']
CoordinateType = enum_type_wrapper.EnumTypeWrapper(_COORDINATETYPE)
MODE_UNKNOWN = 0
MANUAL = 1
ASSISTED_DRIVING = 2
REMOTE_DRIVING = 3
BEAM_NULL = 0
HIGH = 1
LOW = 2
WGS84 = 0
GCJ02 = 1


_VEHICLEINFO = DESCRIPTOR.message_types_by_name['VehicleInfo']
VehicleInfo = _reflection.GeneratedProtocolMessageType('VehicleInfo', (_message.Message,), {
  'DESCRIPTOR' : _VEHICLEINFO,
  '__module__' : 'safety.vehicle_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.vehicle_info.VehicleInfo)
  })
_sym_db.RegisterMessage(VehicleInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VEHICLEINFO.fields_by_name['wgs_lng']._options = None
  _VEHICLEINFO.fields_by_name['wgs_lng']._serialized_options = b'\030\001'
  _VEHICLEINFO.fields_by_name['wgs_lat']._options = None
  _VEHICLEINFO.fields_by_name['wgs_lat']._serialized_options = b'\030\001'
  _VEHICLEINFO.fields_by_name['wgs_alt']._options = None
  _VEHICLEINFO.fields_by_name['wgs_alt']._serialized_options = b'\030\001'
  _DRIVINGMODE._serialized_start=1199
  _DRIVINGMODE._serialized_end=1284
  _BEAM._serialized_start=1286
  _BEAM._serialized_end=1326
  _COORDINATETYPE._serialized_start=1328
  _COORDINATETYPE._serialized_end=1366
  _VEHICLEINFO._serialized_start=77
  _VEHICLEINFO._serialized_end=1197
# @@protoc_insertion_point(module_scope)
