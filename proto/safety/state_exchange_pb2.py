# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: safety/state_exchange.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import module_event_pb2 as common_dot_module__event__pb2
from proto.safety import safety_event_pb2 as safety_dot_safety__event__pb2
from proto.safety import safety_analysis_pb2 as safety_dot_safety__analysis__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bsafety/state_exchange.proto\x12\x0f\x64r.safety.state\x1a\x19\x63ommon/module_event.proto\x1a\x19safety/safety_event.proto\x1a\x1csafety/safety_analysis.proto\"\x85\x01\n\x0eTriggeredEvent\x12\x1f\n\x05\x65vent\x18\x01 \x01(\x0e\x32\x10.dr.common.Event\x12\"\n\x04type\x18\x02 \x01(\x0e\x32\x14.dr.safety.EventType\x12\x1b\n\x13task_failure_policy\x18\x03 \x03(\r\x12\x11\n\tdtc_index\x18\x04 \x01(\x05\"B\n\x08SysTrace\x12\x10\n\x08\x63pu_temp\x18\x01 \x01(\r\x12\x10\n\x08gpu_temp\x18\x02 \x01(\r\x12\x12\n\nboard_temp\x18\x03 \x01(\r\"\xa7\x01\n\x0bSafetyState\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x39\n\x10triggered_events\x18\x02 \x03(\x0b\x32\x1f.dr.safety.state.TriggeredEvent\x12,\n\tsys_trace\x18\x03 \x01(\x0b\x32\x19.dr.safety.state.SysTrace\x12\x1c\n\x14soc_timeout_intervel\x18\x04 \x01(\x04\"\xa3\x01\n\x08SSMEvent\x12!\n\x06module\x18\x01 \x01(\x0e\x32\x11.dr.common.Module\x12\x1f\n\x05\x65vent\x18\x02 \x01(\x0e\x32\x10.dr.common.Event\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x12\x14\n\x0csequence_num\x18\x04 \x01(\x05\x12$\n\x05level\x18\x07 \x01(\x0e\x32\x15.dr.safety.EventLevelJ\x04\x08\x05\x10\x07\"\x8c\x01\n\x0eSSMPolicyEvent\x12&\n\ttask_type\x18\x01 \x01(\x0e\x32\x13.dr.safety.TaskType\x12\x30\n\x0e\x66\x61ilure_policy\x18\x02 \x01(\x0e\x32\x18.dr.safety.FailurePolicy\x12 \n\x06\x65vents\x18\x03 \x03(\x0e\x32\x10.dr.common.Event\"\xd7\x01\n\x08SSMState\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12*\n\x0b\x66\x61ult_level\x18\x02 \x01(\x0e\x32\x15.dr.safety.FaultLevel\x12-\n\nssm_events\x18\x03 \x03(\x0b\x32\x19.dr.safety.state.SSMEvent\x12!\n\x19\x65vent_config_sequence_num\x18\x04 \x01(\x05\x12:\n\x11ssm_policy_events\x18\x05 \x03(\x0b\x32\x1f.dr.safety.state.SSMPolicyEvent\"m\n\x11TaskFailurePolicy\x12&\n\ttask_type\x18\x01 \x01(\x0e\x32\x13.dr.safety.TaskType\x12\x30\n\x0e\x66\x61ilure_policy\x18\x02 \x01(\x0e\x32\x18.dr.safety.FailurePolicy\"Q\n\x11\x45ventPolicyConfig\x12\x1f\n\x05\x65vent\x18\x01 \x01(\x0e\x32\x10.dr.common.Event\x12\x1b\n\x13task_failure_policy\x18\x02 \x03(\r\"/\n\x08\x42lcState\x12\x10\n\x08\x62lc_type\x18\x01 \x01(\x05\x12\x11\n\tblc_state\x18\x02 \x01(\x05\"\x97\x01\n\x13PolicyMonitorConfig\x12\x30\n\x0e\x66\x61ilure_policy\x18\x01 \x01(\x0e\x32\x18.dr.safety.FailurePolicy\x12\x16\n\x0e\x63heck_interval\x18\x02 \x01(\x04\x12\x36\n\x13status_check_config\x18\x03 \x03(\x0b\x32\x19.dr.safety.state.BlcState\"\xb3\x01\n\x0fSafetyMcuConfig\x12\x38\n\x0c\x65vent_config\x18\x01 \x03(\x0b\x32\".dr.safety.state.EventPolicyConfig\x12\x43\n\x15policy_monitor_config\x18\x02 \x03(\x0b\x32$.dr.safety.state.PolicyMonitorConfig\x12!\n\x19\x65vent_config_sequence_num\x18\x03 \x01(\x05\":\n\tBlcStatus\x12-\n\nblc_status\x18\x01 \x03(\x0b\x32\x19.dr.safety.state.BlcState\"!\n\x07SocDtcs\x12\x16\n\x0esoc_dtc_indics\x18\x01 \x03(\r\"\x96\x01\n\x0eSocSafetyState\x12\x14\n\x0ctimestamp_ms\x18\x01 \x01(\x04\x12\x16\n\x0esoc_timeout_ms\x18\x02 \x01(\r\x12\x39\n\x10soc_failure_info\x18\x03 \x01(\x0e\x32\x1f.dr.safety.state.SocFailureInfo\x12\x1b\n\x13\x66ull_detect_enabled\x18\x04 \x01(\x08\"&\n\x0eMcuSafetyState\x12\x14\n\x0ctimestamp_ms\x18\x01 \x01(\x04\"R\n\x0cMcuEventInfo\x12\x1f\n\x05\x65vent\x18\x01 \x01(\x0e\x32\x10.dr.common.Event\x12!\n\x06module\x18\x02 \x01(\x0e\x32\x11.dr.common.Module\"F\n\rMcuEventsInfo\x12\x35\n\x0emcu_event_info\x18\x01 \x03(\x0b\x32\x1d.dr.safety.state.McuEventInfo*;\n\x0eSocFailureInfo\x12\x0e\n\nNO_FAILURE\x10\x00\x12\x19\n\x15\x44\x45M_HEARTBEAT_TIMEOUT\x10\x01')

_SOCFAILUREINFO = DESCRIPTOR.enum_types_by_name['SocFailureInfo']
SocFailureInfo = enum_type_wrapper.EnumTypeWrapper(_SOCFAILUREINFO)
NO_FAILURE = 0
DEM_HEARTBEAT_TIMEOUT = 1


_TRIGGEREDEVENT = DESCRIPTOR.message_types_by_name['TriggeredEvent']
_SYSTRACE = DESCRIPTOR.message_types_by_name['SysTrace']
_SAFETYSTATE = DESCRIPTOR.message_types_by_name['SafetyState']
_SSMEVENT = DESCRIPTOR.message_types_by_name['SSMEvent']
_SSMPOLICYEVENT = DESCRIPTOR.message_types_by_name['SSMPolicyEvent']
_SSMSTATE = DESCRIPTOR.message_types_by_name['SSMState']
_TASKFAILUREPOLICY = DESCRIPTOR.message_types_by_name['TaskFailurePolicy']
_EVENTPOLICYCONFIG = DESCRIPTOR.message_types_by_name['EventPolicyConfig']
_BLCSTATE = DESCRIPTOR.message_types_by_name['BlcState']
_POLICYMONITORCONFIG = DESCRIPTOR.message_types_by_name['PolicyMonitorConfig']
_SAFETYMCUCONFIG = DESCRIPTOR.message_types_by_name['SafetyMcuConfig']
_BLCSTATUS = DESCRIPTOR.message_types_by_name['BlcStatus']
_SOCDTCS = DESCRIPTOR.message_types_by_name['SocDtcs']
_SOCSAFETYSTATE = DESCRIPTOR.message_types_by_name['SocSafetyState']
_MCUSAFETYSTATE = DESCRIPTOR.message_types_by_name['McuSafetyState']
_MCUEVENTINFO = DESCRIPTOR.message_types_by_name['McuEventInfo']
_MCUEVENTSINFO = DESCRIPTOR.message_types_by_name['McuEventsInfo']
TriggeredEvent = _reflection.GeneratedProtocolMessageType('TriggeredEvent', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGEREDEVENT,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.TriggeredEvent)
  })
_sym_db.RegisterMessage(TriggeredEvent)

SysTrace = _reflection.GeneratedProtocolMessageType('SysTrace', (_message.Message,), {
  'DESCRIPTOR' : _SYSTRACE,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.SysTrace)
  })
_sym_db.RegisterMessage(SysTrace)

SafetyState = _reflection.GeneratedProtocolMessageType('SafetyState', (_message.Message,), {
  'DESCRIPTOR' : _SAFETYSTATE,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.SafetyState)
  })
_sym_db.RegisterMessage(SafetyState)

SSMEvent = _reflection.GeneratedProtocolMessageType('SSMEvent', (_message.Message,), {
  'DESCRIPTOR' : _SSMEVENT,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.SSMEvent)
  })
_sym_db.RegisterMessage(SSMEvent)

SSMPolicyEvent = _reflection.GeneratedProtocolMessageType('SSMPolicyEvent', (_message.Message,), {
  'DESCRIPTOR' : _SSMPOLICYEVENT,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.SSMPolicyEvent)
  })
_sym_db.RegisterMessage(SSMPolicyEvent)

SSMState = _reflection.GeneratedProtocolMessageType('SSMState', (_message.Message,), {
  'DESCRIPTOR' : _SSMSTATE,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.SSMState)
  })
_sym_db.RegisterMessage(SSMState)

TaskFailurePolicy = _reflection.GeneratedProtocolMessageType('TaskFailurePolicy', (_message.Message,), {
  'DESCRIPTOR' : _TASKFAILUREPOLICY,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.TaskFailurePolicy)
  })
_sym_db.RegisterMessage(TaskFailurePolicy)

EventPolicyConfig = _reflection.GeneratedProtocolMessageType('EventPolicyConfig', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPOLICYCONFIG,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.EventPolicyConfig)
  })
_sym_db.RegisterMessage(EventPolicyConfig)

BlcState = _reflection.GeneratedProtocolMessageType('BlcState', (_message.Message,), {
  'DESCRIPTOR' : _BLCSTATE,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.BlcState)
  })
_sym_db.RegisterMessage(BlcState)

PolicyMonitorConfig = _reflection.GeneratedProtocolMessageType('PolicyMonitorConfig', (_message.Message,), {
  'DESCRIPTOR' : _POLICYMONITORCONFIG,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.PolicyMonitorConfig)
  })
_sym_db.RegisterMessage(PolicyMonitorConfig)

SafetyMcuConfig = _reflection.GeneratedProtocolMessageType('SafetyMcuConfig', (_message.Message,), {
  'DESCRIPTOR' : _SAFETYMCUCONFIG,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.SafetyMcuConfig)
  })
_sym_db.RegisterMessage(SafetyMcuConfig)

BlcStatus = _reflection.GeneratedProtocolMessageType('BlcStatus', (_message.Message,), {
  'DESCRIPTOR' : _BLCSTATUS,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.BlcStatus)
  })
_sym_db.RegisterMessage(BlcStatus)

SocDtcs = _reflection.GeneratedProtocolMessageType('SocDtcs', (_message.Message,), {
  'DESCRIPTOR' : _SOCDTCS,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.SocDtcs)
  })
_sym_db.RegisterMessage(SocDtcs)

SocSafetyState = _reflection.GeneratedProtocolMessageType('SocSafetyState', (_message.Message,), {
  'DESCRIPTOR' : _SOCSAFETYSTATE,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.SocSafetyState)
  })
_sym_db.RegisterMessage(SocSafetyState)

McuSafetyState = _reflection.GeneratedProtocolMessageType('McuSafetyState', (_message.Message,), {
  'DESCRIPTOR' : _MCUSAFETYSTATE,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.McuSafetyState)
  })
_sym_db.RegisterMessage(McuSafetyState)

McuEventInfo = _reflection.GeneratedProtocolMessageType('McuEventInfo', (_message.Message,), {
  'DESCRIPTOR' : _MCUEVENTINFO,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.McuEventInfo)
  })
_sym_db.RegisterMessage(McuEventInfo)

McuEventsInfo = _reflection.GeneratedProtocolMessageType('McuEventsInfo', (_message.Message,), {
  'DESCRIPTOR' : _MCUEVENTSINFO,
  '__module__' : 'safety.state_exchange_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.state.McuEventsInfo)
  })
_sym_db.RegisterMessage(McuEventsInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SOCFAILUREINFO._serialized_start=2056
  _SOCFAILUREINFO._serialized_end=2115
  _TRIGGEREDEVENT._serialized_start=133
  _TRIGGEREDEVENT._serialized_end=266
  _SYSTRACE._serialized_start=268
  _SYSTRACE._serialized_end=334
  _SAFETYSTATE._serialized_start=337
  _SAFETYSTATE._serialized_end=504
  _SSMEVENT._serialized_start=507
  _SSMEVENT._serialized_end=670
  _SSMPOLICYEVENT._serialized_start=673
  _SSMPOLICYEVENT._serialized_end=813
  _SSMSTATE._serialized_start=816
  _SSMSTATE._serialized_end=1031
  _TASKFAILUREPOLICY._serialized_start=1033
  _TASKFAILUREPOLICY._serialized_end=1142
  _EVENTPOLICYCONFIG._serialized_start=1144
  _EVENTPOLICYCONFIG._serialized_end=1225
  _BLCSTATE._serialized_start=1227
  _BLCSTATE._serialized_end=1274
  _POLICYMONITORCONFIG._serialized_start=1277
  _POLICYMONITORCONFIG._serialized_end=1428
  _SAFETYMCUCONFIG._serialized_start=1431
  _SAFETYMCUCONFIG._serialized_end=1610
  _BLCSTATUS._serialized_start=1612
  _BLCSTATUS._serialized_end=1670
  _SOCDTCS._serialized_start=1672
  _SOCDTCS._serialized_end=1705
  _SOCSAFETYSTATE._serialized_start=1708
  _SOCSAFETYSTATE._serialized_end=1858
  _MCUSAFETYSTATE._serialized_start=1860
  _MCUSAFETYSTATE._serialized_end=1898
  _MCUEVENTINFO._serialized_start=1900
  _MCUEVENTINFO._serialized_end=1982
  _MCUEVENTSINFO._serialized_start=1984
  _MCUEVENTSINFO._serialized_end=2054
# @@protoc_insertion_point(module_scope)
