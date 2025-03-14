# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: canbus/canbus_blc_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common.configs import vehicle_config_pb2 as common_dot_configs_dot_vehicle__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63\x61nbus/canbus_blc_state.proto\x12\x10\x64\x65\x65proute.canbus\x1a#common/configs/vehicle_config.proto\"\x8e\x02\n\x0f\x43\x61nStateMachine\x12\x11\n\ttime_meas\x18\x01 \x01(\x03\x12\x15\n\rrolling_count\x18\x02 \x01(\x04\x12\x31\n\tlongitude\x18\x06 \x01(\x0b\x32\x1e.deeproute.canbus.CanStateLong\x12*\n\x03lat\x18\x07 \x01(\x0b\x32\x1d.deeproute.canbus.CanStateLat\x12\x34\n\rapa_can_state\x18\x08 \x01(\x0b\x32\x1d.deeproute.canbus.ApaCanState\x12<\n\x11special_can_state\x18\x64 \x01(\x0b\x32!.deeproute.canbus.SpecialCanState\"\xc3\x02\n\x15\x43\x61nStateMachineReport\x12\x11\n\ttime_meas\x18\x01 \x01(\x03\x12\x15\n\rrolling_count\x18\x02 \x01(\x04\x12\x39\n\x0blong_report\x18\x06 \x01(\x0b\x32$.deeproute.canbus.CanStateLongReport\x12\x37\n\nlat_report\x18\x07 \x01(\x0b\x32#.deeproute.canbus.CanStateLatReport\x12\x41\n\x14\x61pa_can_state_report\x18\x08 \x01(\x0b\x32#.deeproute.canbus.ApaCanStateReport\x12I\n\x18special_can_state_report\x18\x64 \x01(\x0b\x32\'.deeproute.canbus.SpecialCanStateReport\"\xdd\x01\n\x0c\x43\x61nStateLong\x12\x37\n\x05state\x18\x01 \x01(\x0e\x32(.deeproute.canbus.CanStateLong.StateType\"\x93\x01\n\tStateType\x12\x0f\n\x0bPASSIVE_OFF\x10\x00\x12\x13\n\x0fPASSIVE_FAILURE\x10\x01\x12\x0b\n\x07PASSIVE\x10\x02\x12\x0b\n\x07STANDBY\x10\x03\x12\n\n\x06\x41\x43TIVE\x10\x04\x12\x13\n\x0f\x41\x43TIVE_OVERRIDE\x10\x05\x12\x15\n\x11\x41\x43TIVE_STANDSTILL\x10\x06\x12\x0e\n\nBRAKE_ONLY\x10\x07\"\x9e\x01\n\x0b\x43\x61nStateLat\x12\x36\n\x05state\x18\x01 \x01(\x0e\x32\'.deeproute.canbus.CanStateLat.StateType\"W\n\tStateType\x12\x0f\n\x0bPASSIVE_OFF\x10\x00\x12\x13\n\x0fPASSIVE_FAILURE\x10\x01\x12\x0b\n\x07PASSIVE\x10\x02\x12\x0b\n\x07STANDBY\x10\x03\x12\n\n\x06\x41\x43TIVE\x10\x04\"\x80\x01\n\x12\x43\x61nStateLongReport\x12\x31\n\tlongitude\x18\x01 \x01(\x0b\x32\x1e.deeproute.canbus.CanStateLong\x12\x37\n\x0epassive_reason\x18\x02 \x01(\x0b\x32\x1f.deeproute.canbus.PassiveReason\"x\n\x11\x43\x61nStateLatReport\x12*\n\x03lat\x18\x01 \x01(\x0b\x32\x1d.deeproute.canbus.CanStateLat\x12\x37\n\x0epassive_reason\x18\x02 \x01(\x0b\x32\x1f.deeproute.canbus.PassiveReason\"\x8e\x01\n\x15SpecialCanStateReport\x12<\n\x11special_can_state\x18\x01 \x01(\x0b\x32!.deeproute.canbus.SpecialCanState\x12\x37\n\x0epassive_reason\x18\x02 \x01(\x0b\x32\x1f.deeproute.canbus.PassiveReason\"\xb8\x02\n\x0b\x41paCanState\x12\x39\n\x05state\x18\x01 \x01(\x0e\x32*.deeproute.canbus.ApaCanState.ApaStateType\x12\x41\n\rfunction_type\x18\x02 \x01(\x0e\x32*.deeproute.canbus.ApaCanState.FunctionType\"f\n\x0c\x41paStateType\x12\x0f\n\x0bPASSIVE_OFF\x10\x00\x12\x13\n\x0fPASSIVE_FAILURE\x10\x01\x12\x0b\n\x07PASSIVE\x10\x02\x12\x0b\n\x07STANDBY\x10\x03\x12\n\n\x06\x41\x43TIVE\x10\x04\x12\n\n\x06\x46INISH\x10\x05\"C\n\x0c\x46unctionType\x12\x07\n\x03\x41PA\x10\x00\x12\x07\n\x03RPA\x10\x01\x12\x0b\n\x07\x41VP_HIC\x10\x02\x12\x0b\n\x07\x41VP_HOC\x10\x03\x12\x07\n\x03HPA\x10\x04\"z\n\x11\x41paCanStateReport\x12,\n\x05state\x18\x01 \x01(\x0b\x32\x1d.deeproute.canbus.ApaCanState\x12\x37\n\x0epassive_reason\x18\x02 \x01(\x0b\x32\x1f.deeproute.canbus.PassiveReason\"\xd8\x01\n\rPassiveReason\x12\x16\n\x0epassive_enable\x18\x01 \x01(\x08\x12-\n\x05\x62rand\x18\x02 \x01(\x0e\x32\x1e.deeproute.common.VehicleBrand\x12\x34\n\x05m5_m7\x18\x03 \x01(\x0b\x32#.deeproute.canbus.M5M7PassiveReasonH\x00\x12\x38\n\x07\x62yd_icv\x18\x04 \x01(\x0b\x32%.deeproute.canbus.BydIcvPassiveReasonH\x00\x42\x10\n\x0epassive_reason\"\xef\x02\n\x11M5M7PassiveReason\x12\x1a\n\x12\x64river_belt_untied\x18\x01 \x01(\x08\x12\x1d\n\x15\x65pb_parked_or_parking\x18\x02 \x01(\x08\x12\x1e\n\x16\x61\x63tual_gear_not_driver\x18\x03 \x01(\x08\x12\x16\n\x0e\x64oor_fl_opened\x18\x04 \x01(\x08\x12\x1b\n\x13\x62rake_pedal_appkied\x18\x05 \x01(\x08\x12\x15\n\rvcu_not_ready\x18\x06 \x01(\x08\x12\x11\n\tvlc_error\x18\x07 \x01(\x08\x12\x11\n\tcdd_error\x18\x08 \x01(\x08\x12\x1c\n\x14\x61\x62normal_apa_request\x18\t \x01(\x08\x12\x18\n\x10\x61pa_low_priority\x18\n \x01(\x08\x12\x16\n\x0esteer_override\x18\x0b \x01(\x08\x12\x13\n\x0b\x65ps_failure\x18\x0c \x01(\x08\x12\x14\n\x0c\x63trl_no_auto\x18\x65 \x01(\x08\x12\x12\n\naeb_active\x18\x66 \x01(\x08\"\xc6\x01\n\x13\x42ydIcvPassiveReason\x12\x15\n\rvcu_not_ready\x18\x01 \x01(\x08\x12\x11\n\tvlc_error\x18\x02 \x01(\x08\x12\x11\n\tcdd_error\x18\x03 \x01(\x08\x12\x13\n\x0b\x65ps_failure\x18\x04 \x01(\x08\x12\x16\n\x0esteer_override\x18\x05 \x01(\x08\x12\x1b\n\x13\x62rake_pedal_appkied\x18\x06 \x01(\x08\x12\x14\n\x0c\x63trl_no_auto\x18\x65 \x01(\x08\x12\x12\n\naeb_active\x18\x66 \x01(\x08\"\xbb\x01\n\x0fSpecialCanState\x12-\n\x05\x62rand\x18\x01 \x01(\x0e\x32\x1e.deeproute.common.VehicleBrand\x12:\n\x0b\x62yd_icv_tjp\x18\x02 \x01(\x0b\x32#.deeproute.canbus.BydIcvTjpCanStateH\x00\x12\x30\n\x03gwm\x18\x03 \x01(\x0b\x32!.deeproute.canbus.GwmStateMachineH\x00\x42\x0b\n\tcan_state\"\xf1\x02\n\x11\x42ydIcvTjpCanState\x12\x42\n\tlongitude\x18\x01 \x01(\x0e\x32/.deeproute.canbus.BydIcvTjpCanState.TjpLongType\x12;\n\x03lat\x18\x02 \x01(\x0e\x32..deeproute.canbus.BydIcvTjpCanState.TjpLatType\"o\n\x0bTjpLongType\x12\x0f\n\x0bPASSIVE_OFF\x10\x00\x12\x0b\n\x07PASSIVE\x10\x01\x12\x0b\n\x07STANDBY\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\x12\x11\n\rPASSIVE_FAULT\x10\x04\x12\x07\n\x03MRC\x10\x05\x12\r\n\tFORBIDDEN\x10\x06\"j\n\nTjpLatType\x12\x13\n\x0fLAT_PASSIVE_OFF\x10\x00\x12\x0f\n\x0bLAT_PASSIVE\x10\x01\x12\x0f\n\x0bLAT_STANDBY\x10\x02\x12\x0e\n\nLAT_ACTIVE\x10\x03\x12\x15\n\x11LAT_PASSIVE_FAULT\x10\x04\"\xaa\x07\n\x0fGwmStateMachine\x12M\n\x11parking_longitude\x18\x01 \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12G\n\x0bparking_lat\x18\x02 \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12M\n\x11\x64riving_longitude\x18\x03 \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12G\n\x0b\x64riving_lat\x18\x04 \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12?\n\x03\x61\x65\x62\x18\x05 \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12?\n\x03\x61\x62p\x18\x06 \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12?\n\x03\x61wb\x18\x07 \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12?\n\x03\x61\x62\x61\x18\x08 \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12?\n\x03\x65\x62\x61\x18\t \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12?\n\x03\x65sa\x18\n \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12?\n\x03meb\x18\x0b \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\x12@\n\x04rctb\x18\x0c \x01(\x0e\x32\x32.deeproute.canbus.GwmStateMachine.StateMachineType\"^\n\x10StateMachineType\x12\x0b\n\x07PASSIVE\x10\x00\x12\x0b\n\x07STANDBY\x10\x01\x12\x0b\n\x07TIMEOUT\x10\x02\x12\r\n\tHANDSHAKE\x10\x03\x12\n\n\x06\x41\x43TIVE\x10\x04\x12\x08\n\x04\x45XIT\x10\x05')



_CANSTATEMACHINE = DESCRIPTOR.message_types_by_name['CanStateMachine']
_CANSTATEMACHINEREPORT = DESCRIPTOR.message_types_by_name['CanStateMachineReport']
_CANSTATELONG = DESCRIPTOR.message_types_by_name['CanStateLong']
_CANSTATELAT = DESCRIPTOR.message_types_by_name['CanStateLat']
_CANSTATELONGREPORT = DESCRIPTOR.message_types_by_name['CanStateLongReport']
_CANSTATELATREPORT = DESCRIPTOR.message_types_by_name['CanStateLatReport']
_SPECIALCANSTATEREPORT = DESCRIPTOR.message_types_by_name['SpecialCanStateReport']
_APACANSTATE = DESCRIPTOR.message_types_by_name['ApaCanState']
_APACANSTATEREPORT = DESCRIPTOR.message_types_by_name['ApaCanStateReport']
_PASSIVEREASON = DESCRIPTOR.message_types_by_name['PassiveReason']
_M5M7PASSIVEREASON = DESCRIPTOR.message_types_by_name['M5M7PassiveReason']
_BYDICVPASSIVEREASON = DESCRIPTOR.message_types_by_name['BydIcvPassiveReason']
_SPECIALCANSTATE = DESCRIPTOR.message_types_by_name['SpecialCanState']
_BYDICVTJPCANSTATE = DESCRIPTOR.message_types_by_name['BydIcvTjpCanState']
_GWMSTATEMACHINE = DESCRIPTOR.message_types_by_name['GwmStateMachine']
_CANSTATELONG_STATETYPE = _CANSTATELONG.enum_types_by_name['StateType']
_CANSTATELAT_STATETYPE = _CANSTATELAT.enum_types_by_name['StateType']
_APACANSTATE_APASTATETYPE = _APACANSTATE.enum_types_by_name['ApaStateType']
_APACANSTATE_FUNCTIONTYPE = _APACANSTATE.enum_types_by_name['FunctionType']
_BYDICVTJPCANSTATE_TJPLONGTYPE = _BYDICVTJPCANSTATE.enum_types_by_name['TjpLongType']
_BYDICVTJPCANSTATE_TJPLATTYPE = _BYDICVTJPCANSTATE.enum_types_by_name['TjpLatType']
_GWMSTATEMACHINE_STATEMACHINETYPE = _GWMSTATEMACHINE.enum_types_by_name['StateMachineType']
CanStateMachine = _reflection.GeneratedProtocolMessageType('CanStateMachine', (_message.Message,), {
  'DESCRIPTOR' : _CANSTATEMACHINE,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.CanStateMachine)
  })
_sym_db.RegisterMessage(CanStateMachine)

CanStateMachineReport = _reflection.GeneratedProtocolMessageType('CanStateMachineReport', (_message.Message,), {
  'DESCRIPTOR' : _CANSTATEMACHINEREPORT,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.CanStateMachineReport)
  })
_sym_db.RegisterMessage(CanStateMachineReport)

CanStateLong = _reflection.GeneratedProtocolMessageType('CanStateLong', (_message.Message,), {
  'DESCRIPTOR' : _CANSTATELONG,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.CanStateLong)
  })
_sym_db.RegisterMessage(CanStateLong)

CanStateLat = _reflection.GeneratedProtocolMessageType('CanStateLat', (_message.Message,), {
  'DESCRIPTOR' : _CANSTATELAT,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.CanStateLat)
  })
_sym_db.RegisterMessage(CanStateLat)

CanStateLongReport = _reflection.GeneratedProtocolMessageType('CanStateLongReport', (_message.Message,), {
  'DESCRIPTOR' : _CANSTATELONGREPORT,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.CanStateLongReport)
  })
_sym_db.RegisterMessage(CanStateLongReport)

CanStateLatReport = _reflection.GeneratedProtocolMessageType('CanStateLatReport', (_message.Message,), {
  'DESCRIPTOR' : _CANSTATELATREPORT,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.CanStateLatReport)
  })
_sym_db.RegisterMessage(CanStateLatReport)

SpecialCanStateReport = _reflection.GeneratedProtocolMessageType('SpecialCanStateReport', (_message.Message,), {
  'DESCRIPTOR' : _SPECIALCANSTATEREPORT,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.SpecialCanStateReport)
  })
_sym_db.RegisterMessage(SpecialCanStateReport)

ApaCanState = _reflection.GeneratedProtocolMessageType('ApaCanState', (_message.Message,), {
  'DESCRIPTOR' : _APACANSTATE,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.ApaCanState)
  })
_sym_db.RegisterMessage(ApaCanState)

ApaCanStateReport = _reflection.GeneratedProtocolMessageType('ApaCanStateReport', (_message.Message,), {
  'DESCRIPTOR' : _APACANSTATEREPORT,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.ApaCanStateReport)
  })
_sym_db.RegisterMessage(ApaCanStateReport)

PassiveReason = _reflection.GeneratedProtocolMessageType('PassiveReason', (_message.Message,), {
  'DESCRIPTOR' : _PASSIVEREASON,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.PassiveReason)
  })
_sym_db.RegisterMessage(PassiveReason)

M5M7PassiveReason = _reflection.GeneratedProtocolMessageType('M5M7PassiveReason', (_message.Message,), {
  'DESCRIPTOR' : _M5M7PASSIVEREASON,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.M5M7PassiveReason)
  })
_sym_db.RegisterMessage(M5M7PassiveReason)

BydIcvPassiveReason = _reflection.GeneratedProtocolMessageType('BydIcvPassiveReason', (_message.Message,), {
  'DESCRIPTOR' : _BYDICVPASSIVEREASON,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.BydIcvPassiveReason)
  })
_sym_db.RegisterMessage(BydIcvPassiveReason)

SpecialCanState = _reflection.GeneratedProtocolMessageType('SpecialCanState', (_message.Message,), {
  'DESCRIPTOR' : _SPECIALCANSTATE,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.SpecialCanState)
  })
_sym_db.RegisterMessage(SpecialCanState)

BydIcvTjpCanState = _reflection.GeneratedProtocolMessageType('BydIcvTjpCanState', (_message.Message,), {
  'DESCRIPTOR' : _BYDICVTJPCANSTATE,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.BydIcvTjpCanState)
  })
_sym_db.RegisterMessage(BydIcvTjpCanState)

GwmStateMachine = _reflection.GeneratedProtocolMessageType('GwmStateMachine', (_message.Message,), {
  'DESCRIPTOR' : _GWMSTATEMACHINE,
  '__module__' : 'canbus.canbus_blc_state_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.GwmStateMachine)
  })
_sym_db.RegisterMessage(GwmStateMachine)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CANSTATEMACHINE._serialized_start=89
  _CANSTATEMACHINE._serialized_end=359
  _CANSTATEMACHINEREPORT._serialized_start=362
  _CANSTATEMACHINEREPORT._serialized_end=685
  _CANSTATELONG._serialized_start=688
  _CANSTATELONG._serialized_end=909
  _CANSTATELONG_STATETYPE._serialized_start=762
  _CANSTATELONG_STATETYPE._serialized_end=909
  _CANSTATELAT._serialized_start=912
  _CANSTATELAT._serialized_end=1070
  _CANSTATELAT_STATETYPE._serialized_start=762
  _CANSTATELAT_STATETYPE._serialized_end=849
  _CANSTATELONGREPORT._serialized_start=1073
  _CANSTATELONGREPORT._serialized_end=1201
  _CANSTATELATREPORT._serialized_start=1203
  _CANSTATELATREPORT._serialized_end=1323
  _SPECIALCANSTATEREPORT._serialized_start=1326
  _SPECIALCANSTATEREPORT._serialized_end=1468
  _APACANSTATE._serialized_start=1471
  _APACANSTATE._serialized_end=1783
  _APACANSTATE_APASTATETYPE._serialized_start=1612
  _APACANSTATE_APASTATETYPE._serialized_end=1714
  _APACANSTATE_FUNCTIONTYPE._serialized_start=1716
  _APACANSTATE_FUNCTIONTYPE._serialized_end=1783
  _APACANSTATEREPORT._serialized_start=1785
  _APACANSTATEREPORT._serialized_end=1907
  _PASSIVEREASON._serialized_start=1910
  _PASSIVEREASON._serialized_end=2126
  _M5M7PASSIVEREASON._serialized_start=2129
  _M5M7PASSIVEREASON._serialized_end=2496
  _BYDICVPASSIVEREASON._serialized_start=2499
  _BYDICVPASSIVEREASON._serialized_end=2697
  _SPECIALCANSTATE._serialized_start=2700
  _SPECIALCANSTATE._serialized_end=2887
  _BYDICVTJPCANSTATE._serialized_start=2890
  _BYDICVTJPCANSTATE._serialized_end=3259
  _BYDICVTJPCANSTATE_TJPLONGTYPE._serialized_start=3040
  _BYDICVTJPCANSTATE_TJPLONGTYPE._serialized_end=3151
  _BYDICVTJPCANSTATE_TJPLATTYPE._serialized_start=3153
  _BYDICVTJPCANSTATE_TJPLATTYPE._serialized_end=3259
  _GWMSTATEMACHINE._serialized_start=3262
  _GWMSTATEMACHINE._serialized_end=4200
  _GWMSTATEMACHINE_STATEMACHINETYPE._serialized_start=4106
  _GWMSTATEMACHINE_STATEMACHINETYPE._serialized_end=4200
# @@protoc_insertion_point(module_scope)
