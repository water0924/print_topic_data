# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drdtu/debug_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.drapi import operation_status_pb2 as drapi_dot_operation__status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x64rdtu/debug_info.proto\x12\x06\x64r.blc\x1a\x1c\x64rapi/operation_status.proto\"n\n\x0c\x42lcDebugInfo\x12,\n\nnavigation\x18\x01 \x01(\x0b\x32\x18.dr.blc.NavigationNotify\x12\x30\n\x10speed_limit_info\x18\x02 \x01(\x0b\x32\x16.dr.blc.SpeedLimitInfo\")\n\x0eSpeedLimitInfo\x12\x17\n\x0fuse_model_speed\x18\x01 \x01(\x08\"\xd6\x02\n\x10NavigationNotify\x12\x14\n\x0ctimestamp_ms\x18\x01 \x01(\x04\x12@\n\x12nca_passive_reason\x18\x02 \x01(\x0b\x32$.dr.operationstatus.NCAPassiveReason\x12/\n\x0bpreview_cmd\x18\x03 \x01(\x0b\x32\x1a.dr.blc.PreviewCommandInfo\x12/\n\x0b\x65xecute_cmd\x18\x04 \x01(\x0b\x32\x1a.dr.blc.ExecuteCommandInfo\x12\x37\n\rrealtime_navi\x18\x05 \x01(\x0b\x32 .dr.blc.RealTimeNavigationStatus\x12,\n\nlor_status\x18\x06 \x01(\x0b\x32\x18.dr.blc.LockOnRoadStatus\x12!\n\x08odd_info\x18\x07 \x01(\x0b\x32\x0f.dr.blc.OddInfo\"x\n\x12PreviewCommandInfo\x12\x34\n\x05\x61ttrs\x18\x01 \x03(\x0b\x32%.dr.blc.PreviewCommandInfo.AttrsEntry\x1a,\n\nAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"x\n\x12\x45xecuteCommandInfo\x12\x34\n\x05\x61ttrs\x18\x01 \x03(\x0b\x32%.dr.blc.ExecuteCommandInfo.AttrsEntry\x1a,\n\nAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x84\x01\n\x18RealTimeNavigationStatus\x12:\n\x05\x61ttrs\x18\x01 \x03(\x0b\x32+.dr.blc.RealTimeNavigationStatus.AttrsEntry\x1a,\n\nAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"t\n\x10LockOnRoadStatus\x12\x32\n\x05\x61ttrs\x18\x01 \x03(\x0b\x32#.dr.blc.LockOnRoadStatus.AttrsEntry\x1a,\n\nAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"b\n\x07OddInfo\x12)\n\x05\x61ttrs\x18\x01 \x03(\x0b\x32\x1a.dr.blc.OddInfo.AttrsEntry\x1a,\n\nAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')



_BLCDEBUGINFO = DESCRIPTOR.message_types_by_name['BlcDebugInfo']
_SPEEDLIMITINFO = DESCRIPTOR.message_types_by_name['SpeedLimitInfo']
_NAVIGATIONNOTIFY = DESCRIPTOR.message_types_by_name['NavigationNotify']
_PREVIEWCOMMANDINFO = DESCRIPTOR.message_types_by_name['PreviewCommandInfo']
_PREVIEWCOMMANDINFO_ATTRSENTRY = _PREVIEWCOMMANDINFO.nested_types_by_name['AttrsEntry']
_EXECUTECOMMANDINFO = DESCRIPTOR.message_types_by_name['ExecuteCommandInfo']
_EXECUTECOMMANDINFO_ATTRSENTRY = _EXECUTECOMMANDINFO.nested_types_by_name['AttrsEntry']
_REALTIMENAVIGATIONSTATUS = DESCRIPTOR.message_types_by_name['RealTimeNavigationStatus']
_REALTIMENAVIGATIONSTATUS_ATTRSENTRY = _REALTIMENAVIGATIONSTATUS.nested_types_by_name['AttrsEntry']
_LOCKONROADSTATUS = DESCRIPTOR.message_types_by_name['LockOnRoadStatus']
_LOCKONROADSTATUS_ATTRSENTRY = _LOCKONROADSTATUS.nested_types_by_name['AttrsEntry']
_ODDINFO = DESCRIPTOR.message_types_by_name['OddInfo']
_ODDINFO_ATTRSENTRY = _ODDINFO.nested_types_by_name['AttrsEntry']
BlcDebugInfo = _reflection.GeneratedProtocolMessageType('BlcDebugInfo', (_message.Message,), {
  'DESCRIPTOR' : _BLCDEBUGINFO,
  '__module__' : 'drdtu.debug_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.BlcDebugInfo)
  })
_sym_db.RegisterMessage(BlcDebugInfo)

SpeedLimitInfo = _reflection.GeneratedProtocolMessageType('SpeedLimitInfo', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDLIMITINFO,
  '__module__' : 'drdtu.debug_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.SpeedLimitInfo)
  })
_sym_db.RegisterMessage(SpeedLimitInfo)

NavigationNotify = _reflection.GeneratedProtocolMessageType('NavigationNotify', (_message.Message,), {
  'DESCRIPTOR' : _NAVIGATIONNOTIFY,
  '__module__' : 'drdtu.debug_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.NavigationNotify)
  })
_sym_db.RegisterMessage(NavigationNotify)

PreviewCommandInfo = _reflection.GeneratedProtocolMessageType('PreviewCommandInfo', (_message.Message,), {

  'AttrsEntry' : _reflection.GeneratedProtocolMessageType('AttrsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREVIEWCOMMANDINFO_ATTRSENTRY,
    '__module__' : 'drdtu.debug_info_pb2'
    # @@protoc_insertion_point(class_scope:dr.blc.PreviewCommandInfo.AttrsEntry)
    })
  ,
  'DESCRIPTOR' : _PREVIEWCOMMANDINFO,
  '__module__' : 'drdtu.debug_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.PreviewCommandInfo)
  })
_sym_db.RegisterMessage(PreviewCommandInfo)
_sym_db.RegisterMessage(PreviewCommandInfo.AttrsEntry)

ExecuteCommandInfo = _reflection.GeneratedProtocolMessageType('ExecuteCommandInfo', (_message.Message,), {

  'AttrsEntry' : _reflection.GeneratedProtocolMessageType('AttrsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXECUTECOMMANDINFO_ATTRSENTRY,
    '__module__' : 'drdtu.debug_info_pb2'
    # @@protoc_insertion_point(class_scope:dr.blc.ExecuteCommandInfo.AttrsEntry)
    })
  ,
  'DESCRIPTOR' : _EXECUTECOMMANDINFO,
  '__module__' : 'drdtu.debug_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.ExecuteCommandInfo)
  })
_sym_db.RegisterMessage(ExecuteCommandInfo)
_sym_db.RegisterMessage(ExecuteCommandInfo.AttrsEntry)

RealTimeNavigationStatus = _reflection.GeneratedProtocolMessageType('RealTimeNavigationStatus', (_message.Message,), {

  'AttrsEntry' : _reflection.GeneratedProtocolMessageType('AttrsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REALTIMENAVIGATIONSTATUS_ATTRSENTRY,
    '__module__' : 'drdtu.debug_info_pb2'
    # @@protoc_insertion_point(class_scope:dr.blc.RealTimeNavigationStatus.AttrsEntry)
    })
  ,
  'DESCRIPTOR' : _REALTIMENAVIGATIONSTATUS,
  '__module__' : 'drdtu.debug_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.RealTimeNavigationStatus)
  })
_sym_db.RegisterMessage(RealTimeNavigationStatus)
_sym_db.RegisterMessage(RealTimeNavigationStatus.AttrsEntry)

LockOnRoadStatus = _reflection.GeneratedProtocolMessageType('LockOnRoadStatus', (_message.Message,), {

  'AttrsEntry' : _reflection.GeneratedProtocolMessageType('AttrsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOCKONROADSTATUS_ATTRSENTRY,
    '__module__' : 'drdtu.debug_info_pb2'
    # @@protoc_insertion_point(class_scope:dr.blc.LockOnRoadStatus.AttrsEntry)
    })
  ,
  'DESCRIPTOR' : _LOCKONROADSTATUS,
  '__module__' : 'drdtu.debug_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.LockOnRoadStatus)
  })
_sym_db.RegisterMessage(LockOnRoadStatus)
_sym_db.RegisterMessage(LockOnRoadStatus.AttrsEntry)

OddInfo = _reflection.GeneratedProtocolMessageType('OddInfo', (_message.Message,), {

  'AttrsEntry' : _reflection.GeneratedProtocolMessageType('AttrsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ODDINFO_ATTRSENTRY,
    '__module__' : 'drdtu.debug_info_pb2'
    # @@protoc_insertion_point(class_scope:dr.blc.OddInfo.AttrsEntry)
    })
  ,
  'DESCRIPTOR' : _ODDINFO,
  '__module__' : 'drdtu.debug_info_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.OddInfo)
  })
_sym_db.RegisterMessage(OddInfo)
_sym_db.RegisterMessage(OddInfo.AttrsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PREVIEWCOMMANDINFO_ATTRSENTRY._options = None
  _PREVIEWCOMMANDINFO_ATTRSENTRY._serialized_options = b'8\001'
  _EXECUTECOMMANDINFO_ATTRSENTRY._options = None
  _EXECUTECOMMANDINFO_ATTRSENTRY._serialized_options = b'8\001'
  _REALTIMENAVIGATIONSTATUS_ATTRSENTRY._options = None
  _REALTIMENAVIGATIONSTATUS_ATTRSENTRY._serialized_options = b'8\001'
  _LOCKONROADSTATUS_ATTRSENTRY._options = None
  _LOCKONROADSTATUS_ATTRSENTRY._serialized_options = b'8\001'
  _ODDINFO_ATTRSENTRY._options = None
  _ODDINFO_ATTRSENTRY._serialized_options = b'8\001'
  _BLCDEBUGINFO._serialized_start=64
  _BLCDEBUGINFO._serialized_end=174
  _SPEEDLIMITINFO._serialized_start=176
  _SPEEDLIMITINFO._serialized_end=217
  _NAVIGATIONNOTIFY._serialized_start=220
  _NAVIGATIONNOTIFY._serialized_end=562
  _PREVIEWCOMMANDINFO._serialized_start=564
  _PREVIEWCOMMANDINFO._serialized_end=684
  _PREVIEWCOMMANDINFO_ATTRSENTRY._serialized_start=640
  _PREVIEWCOMMANDINFO_ATTRSENTRY._serialized_end=684
  _EXECUTECOMMANDINFO._serialized_start=686
  _EXECUTECOMMANDINFO._serialized_end=806
  _EXECUTECOMMANDINFO_ATTRSENTRY._serialized_start=640
  _EXECUTECOMMANDINFO_ATTRSENTRY._serialized_end=684
  _REALTIMENAVIGATIONSTATUS._serialized_start=809
  _REALTIMENAVIGATIONSTATUS._serialized_end=941
  _REALTIMENAVIGATIONSTATUS_ATTRSENTRY._serialized_start=640
  _REALTIMENAVIGATIONSTATUS_ATTRSENTRY._serialized_end=684
  _LOCKONROADSTATUS._serialized_start=943
  _LOCKONROADSTATUS._serialized_end=1059
  _LOCKONROADSTATUS_ATTRSENTRY._serialized_start=640
  _LOCKONROADSTATUS_ATTRSENTRY._serialized_end=684
  _ODDINFO._serialized_start=1061
  _ODDINFO._serialized_end=1159
  _ODDINFO_ATTRSENTRY._serialized_start=640
  _ODDINFO_ATTRSENTRY._serialized_end=684
# @@protoc_insertion_point(module_scope)
