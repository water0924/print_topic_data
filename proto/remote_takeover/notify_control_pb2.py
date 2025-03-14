# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_takeover/notify_control.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.canbus import chassis_pb2 as canbus_dot_chassis__pb2
from proto.common import header_pb2 as common_dot_header__pb2
from proto.common.vehicle_state import vehicle_state_pb2 as common_dot_vehicle__state_dot_vehicle__state__pb2
from proto.common import vehicle_signal_pb2 as common_dot_vehicle__signal__pb2
from proto.common import error_code_pb2 as common_dot_error__code__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$remote_takeover/notify_control.proto\x12\x19\x64\x65\x65proute.remote_takeover\x1a\x14\x63\x61nbus/chassis.proto\x1a\x13\x63ommon/header.proto\x1a(common/vehicle_state/vehicle_state.proto\x1a\x1b\x63ommon/vehicle_signal.proto\x1a\x17\x63ommon/error_code.proto\"\xeb\x04\n\rNotifyControl\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.deeproute.common.Header\x12\x18\n\x10longitudinal_cmd\x18\x02 \x01(\x01\x12\x15\n\rsteering_rate\x18\x03 \x01(\x01\x12\x17\n\x0fsteering_target\x18\x04 \x01(\x01\x12;\n\x0c\x64riving_mode\x18\x05 \x01(\x0e\x32%.deeproute.canbus.Chassis.DrivingMode\x12=\n\rgear_location\x18\x06 \x01(\x0e\x32&.deeproute.canbus.Chassis.GearPosition\x12\x41\n\nturnsignal\x18\x07 \x01(\x0e\x32).deeproute.common.VehicleState.TurnSignalB\x02\x18\x01\x12H\n\x0bstatus_type\x18\x08 \x01(\x0e\x32\x33.deeproute.remote_takeover.NotifyControl.StatusType\x12/\n\x06signal\x18\t \x01(\x0b\x32\x1f.deeproute.common.VehicleSignal\"\xab\x01\n\nStatusType\x12\x16\n\x12STATUSTYPE_INVALID\x10\x00\x12\x15\n\x11STATUSTYPE_CANCEL\x10\x01\x12#\n\x1fSTATUSTYPE_REQUEST_CONTROL_MODE\x10\x02\x12\x1f\n\x1bSTATUSTYPE_REQUEST_ADS_MODE\x10\x03\x12(\n$STATUSTYPE_REQUEST_SEND_AUTO_REQUEST\x10\x04\"\x83\x01\n\x15NotifyControlResponse\x12@\n\x0enotify_control\x18\x01 \x01(\x0b\x32(.deeproute.remote_takeover.NotifyControl\x12(\n\x08\x65rr_code\x18\x02 \x01(\x0e\x32\x16.deeproute.common.Code')



_NOTIFYCONTROL = DESCRIPTOR.message_types_by_name['NotifyControl']
_NOTIFYCONTROLRESPONSE = DESCRIPTOR.message_types_by_name['NotifyControlResponse']
_NOTIFYCONTROL_STATUSTYPE = _NOTIFYCONTROL.enum_types_by_name['StatusType']
NotifyControl = _reflection.GeneratedProtocolMessageType('NotifyControl', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFYCONTROL,
  '__module__' : 'remote_takeover.notify_control_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.remote_takeover.NotifyControl)
  })
_sym_db.RegisterMessage(NotifyControl)

NotifyControlResponse = _reflection.GeneratedProtocolMessageType('NotifyControlResponse', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFYCONTROLRESPONSE,
  '__module__' : 'remote_takeover.notify_control_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.remote_takeover.NotifyControlResponse)
  })
_sym_db.RegisterMessage(NotifyControlResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOTIFYCONTROL.fields_by_name['turnsignal']._options = None
  _NOTIFYCONTROL.fields_by_name['turnsignal']._serialized_options = b'\030\001'
  _NOTIFYCONTROL._serialized_start=207
  _NOTIFYCONTROL._serialized_end=826
  _NOTIFYCONTROL_STATUSTYPE._serialized_start=655
  _NOTIFYCONTROL_STATUSTYPE._serialized_end=826
  _NOTIFYCONTROLRESPONSE._serialized_start=829
  _NOTIFYCONTROLRESPONSE._serialized_end=960
# @@protoc_insertion_point(module_scope)
