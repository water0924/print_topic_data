# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: safety/safety_event.proto
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
from proto.drapi import operation_status_pb2 as drapi_dot_operation__status__pb2
from vhr import event_extra_info_pb2 as vhr_dot_event__extra__info__pb2
from proto.safety import vehicle_info_pb2 as safety_dot_vehicle__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19safety/safety_event.proto\x12\tdr.safety\x1a\x19\x63ommon/module_event.proto\x1a\x1c\x64rapi/operation_status.proto\x1a\x1avhr/event_extra_info.proto\x1a\x19safety/vehicle_info.proto\"-\n\x07Modules\x12\"\n\x07modules\x18\x01 \x03(\x0e\x32\x11.dr.common.Module\"*\n\x06\x45vents\x12 \n\x06\x65vents\x18\x02 \x03(\x0e\x32\x10.dr.common.Event\"\xa1\x01\n\x0bVersionHead\x12\x13\n\x0blog_version\x18\x01 \x01(\t\x12\x17\n\x0flog_sub_version\x18\x02 \x01(\t\x12\x14\n\x0cproduct_name\x18\x03 \x01(\t\x12\x17\n\x0fproduct_version\x18\x04 \x01(\t\x12\x13\n\x0bproduct_cat\x18\x05 \x01(\t\x12\x0f\n\x07s1_code\x18\x06 \x01(\t\x12\x0f\n\x07s2_code\x18\x07 \x01(\t\"^\n\rSafetyVhrHead\x12\x11\n\ttrip_name\x18\x01 \x01(\t\x12\x0e\n\x06\x63\x61r_id\x18\x02 \x01(\t\x12\x16\n\x0e\x64river_version\x18\x03 \x01(\t\x12\x12\n\noem_car_id\x18\x04 \x01(\t\":\n\nControlMsg\x12,\n\x0cversion_head\x18\x01 \x01(\x0b\x32\x16.dr.safety.VersionHead\"\xc1\x04\n\x0bSafetyEvent\x12!\n\x06module\x18\x01 \x01(\x0e\x32\x11.dr.common.Module\x12\x1f\n\x05\x65vent\x18\x02 \x01(\x0e\x32\x10.dr.common.Event\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x12\x14\n\x0csequence_num\x18\x04 \x01(\x05\x12\x13\n\tjson_info\x18\x05 \x01(\tH\x00\x12\x1f\n\x15serialized_proto_info\x18\x06 \x01(\tH\x00\x12\x12\n\nalert_info\x18\x07 \x01(\t\x12\"\n\x04type\x18\n \x01(\x0e\x32\x14.dr.safety.EventType\x12\r\n\x05\x63ount\x18\x0b \x01(\r\x12\x10\n\x08\x64uration\x18\x0c \x01(\r\x12$\n\x05level\x18\r \x01(\x0e\x32\x15.dr.safety.EventLevel\x12*\n\x08platform\x18\x0e \x01(\x0e\x32\x13.dr.safety.PlatForm:\x03SOC\x12)\n\x04task\x18\x0f \x01(\x0e\x32\x1b.dr.operationstatus.Feature\x12*\n\nextra_info\x18\x10 \x01(\x0b\x32\x16.dr.vhr.EventExtraInfo\x12?\n\x04mode\x18\x11 \x01(\x0e\x32#.dr.safety.vehicle_info.DrivingMode:\x0cMODE_UNKNOWN\x12\x12\n\ndelay_time\x18\x12 \x01(\r\x12*\n\x07\x63tr_msg\x18\x64 \x01(\x0b\x32\x15.dr.safety.ControlMsgB\x02\x18\x01\x42\x06\n\x04infoJ\x04\x08\x08\x10\n\"M\n\x10SafetyLogMetrics\x12\x10\n\x08interval\x18\x01 \x01(\r\x12\x11\n\tlog_count\x18\x02 \x01(\r\x12\x14\n\x0cused_storage\x18\x03 \x01(\x04\"\x83\x01\n\x13SafetyUploadMetrics\x12\x11\n\tlog_count\x18\x01 \x01(\r\x12\x13\n\x0bupload_time\x18\x02 \x01(\r\x12\x11\n\tfile_size\x18\x03 \x01(\x04\x12\x15\n\rupload_status\x18\x04 \x01(\x08\x12\r\n\x05speed\x18\x05 \x01(\x01\x12\x0b\n\x03msg\x18\x06 \x01(\t\"Z\n\x0fTimeReadyReport\x12\x16\n\x0esystime_offset\x18\x01 \x01(\x03\x12\x19\n\x11local_vhr_storage\x18\x02 \x01(\x04\x12\x14\n\x0cstartup_time\x18\x03 \x01(\r*A\n\nEventLevel\x12\t\n\x05\x44\x45\x42UG\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x08\n\x04WARN\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\t\n\x05\x46\x41TAL\x10\x04*G\n\tEventType\x12\x0f\n\x0b\x45T_ONE_SHOT\x10\x00\x12\x0c\n\x08\x45T_BEGIN\x10\x01\x12\n\n\x06\x45T_END\x10\x02\x12\x0f\n\x0b\x45T_ORIGINAL\x10\x03*\x1c\n\x08PlatForm\x12\x07\n\x03SOC\x10\x00\x12\x07\n\x03MCU\x10\x01')

_EVENTLEVEL = DESCRIPTOR.enum_types_by_name['EventLevel']
EventLevel = enum_type_wrapper.EnumTypeWrapper(_EVENTLEVEL)
_EVENTTYPE = DESCRIPTOR.enum_types_by_name['EventType']
EventType = enum_type_wrapper.EnumTypeWrapper(_EVENTTYPE)
_PLATFORM = DESCRIPTOR.enum_types_by_name['PlatForm']
PlatForm = enum_type_wrapper.EnumTypeWrapper(_PLATFORM)
DEBUG = 0
INFO = 1
WARN = 2
ERROR = 3
FATAL = 4
ET_ONE_SHOT = 0
ET_BEGIN = 1
ET_END = 2
ET_ORIGINAL = 3
SOC = 0
MCU = 1


_MODULES = DESCRIPTOR.message_types_by_name['Modules']
_EVENTS = DESCRIPTOR.message_types_by_name['Events']
_VERSIONHEAD = DESCRIPTOR.message_types_by_name['VersionHead']
_SAFETYVHRHEAD = DESCRIPTOR.message_types_by_name['SafetyVhrHead']
_CONTROLMSG = DESCRIPTOR.message_types_by_name['ControlMsg']
_SAFETYEVENT = DESCRIPTOR.message_types_by_name['SafetyEvent']
_SAFETYLOGMETRICS = DESCRIPTOR.message_types_by_name['SafetyLogMetrics']
_SAFETYUPLOADMETRICS = DESCRIPTOR.message_types_by_name['SafetyUploadMetrics']
_TIMEREADYREPORT = DESCRIPTOR.message_types_by_name['TimeReadyReport']
Modules = _reflection.GeneratedProtocolMessageType('Modules', (_message.Message,), {
  'DESCRIPTOR' : _MODULES,
  '__module__' : 'safety.safety_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.Modules)
  })
_sym_db.RegisterMessage(Modules)

Events = _reflection.GeneratedProtocolMessageType('Events', (_message.Message,), {
  'DESCRIPTOR' : _EVENTS,
  '__module__' : 'safety.safety_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.Events)
  })
_sym_db.RegisterMessage(Events)

VersionHead = _reflection.GeneratedProtocolMessageType('VersionHead', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONHEAD,
  '__module__' : 'safety.safety_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.VersionHead)
  })
_sym_db.RegisterMessage(VersionHead)

SafetyVhrHead = _reflection.GeneratedProtocolMessageType('SafetyVhrHead', (_message.Message,), {
  'DESCRIPTOR' : _SAFETYVHRHEAD,
  '__module__' : 'safety.safety_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.SafetyVhrHead)
  })
_sym_db.RegisterMessage(SafetyVhrHead)

ControlMsg = _reflection.GeneratedProtocolMessageType('ControlMsg', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLMSG,
  '__module__' : 'safety.safety_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.ControlMsg)
  })
_sym_db.RegisterMessage(ControlMsg)

SafetyEvent = _reflection.GeneratedProtocolMessageType('SafetyEvent', (_message.Message,), {
  'DESCRIPTOR' : _SAFETYEVENT,
  '__module__' : 'safety.safety_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.SafetyEvent)
  })
_sym_db.RegisterMessage(SafetyEvent)

SafetyLogMetrics = _reflection.GeneratedProtocolMessageType('SafetyLogMetrics', (_message.Message,), {
  'DESCRIPTOR' : _SAFETYLOGMETRICS,
  '__module__' : 'safety.safety_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.SafetyLogMetrics)
  })
_sym_db.RegisterMessage(SafetyLogMetrics)

SafetyUploadMetrics = _reflection.GeneratedProtocolMessageType('SafetyUploadMetrics', (_message.Message,), {
  'DESCRIPTOR' : _SAFETYUPLOADMETRICS,
  '__module__' : 'safety.safety_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.SafetyUploadMetrics)
  })
_sym_db.RegisterMessage(SafetyUploadMetrics)

TimeReadyReport = _reflection.GeneratedProtocolMessageType('TimeReadyReport', (_message.Message,), {
  'DESCRIPTOR' : _TIMEREADYREPORT,
  '__module__' : 'safety.safety_event_pb2'
  # @@protoc_insertion_point(class_scope:dr.safety.TimeReadyReport)
  })
_sym_db.RegisterMessage(TimeReadyReport)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SAFETYEVENT.fields_by_name['ctr_msg']._options = None
  _SAFETYEVENT.fields_by_name['ctr_msg']._serialized_options = b'\030\001'
  _EVENTLEVEL._serialized_start=1448
  _EVENTLEVEL._serialized_end=1513
  _EVENTTYPE._serialized_start=1515
  _EVENTTYPE._serialized_end=1586
  _PLATFORM._serialized_start=1588
  _PLATFORM._serialized_end=1616
  _MODULES._serialized_start=152
  _MODULES._serialized_end=197
  _EVENTS._serialized_start=199
  _EVENTS._serialized_end=241
  _VERSIONHEAD._serialized_start=244
  _VERSIONHEAD._serialized_end=405
  _SAFETYVHRHEAD._serialized_start=407
  _SAFETYVHRHEAD._serialized_end=501
  _CONTROLMSG._serialized_start=503
  _CONTROLMSG._serialized_end=561
  _SAFETYEVENT._serialized_start=564
  _SAFETYEVENT._serialized_end=1141
  _SAFETYLOGMETRICS._serialized_start=1143
  _SAFETYLOGMETRICS._serialized_end=1220
  _SAFETYUPLOADMETRICS._serialized_start=1223
  _SAFETYUPLOADMETRICS._serialized_end=1354
  _TIMEREADYREPORT._serialized_start=1356
  _TIMEREADYREPORT._serialized_end=1446
# @@protoc_insertion_point(module_scope)
