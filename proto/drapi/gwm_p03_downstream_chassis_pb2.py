# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drapi/gwm_p03_downstream_chassis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.canbus import gwm_p03_chassis_detail_pb2 as canbus_dot_gwm__p03__chassis__detail__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&drapi/gwm_p03_downstream_chassis.proto\x12\ndr.blc.mcu\x1a#canbus/gwm_p03_chassis_detail.proto\"\x89\n\n\x17GwmP03DownstreamChassis\x12:\n\x0bhap_fd1_15b\x18\x01 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.HAP_FD1_15B\x12:\n\x0bhap_fd2_274\x18\x02 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.HAP_FD2_274\x12:\n\x0bhap_fd6_289\x18\x03 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.HAP_FD6_289\x12:\n\x0bhap_fd3_298\x18\x04 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.HAP_FD3_298\x12:\n\x0bhap_fd7_29b\x18\x05 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.HAP_FD7_29B\x12:\n\x0b\x61\x63\x63_fd1_143\x18\x06 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.ACC_FD1_143\x12:\n\x0b\x61\x63\x63_fd2_2ab\x18\x07 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.ACC_FD2_2AB\x12:\n\x0b\x61\x63\x63_fd3_2b4\x18\x08 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.ACC_FD3_2B4\x12:\n\x0b\x61\x63\x63_fd4_2b8\x18\t \x01(\x0b\x32%.deeproute.canbus.gwm.p03.ACC_FD4_2B8\x12:\n\x0bifc_fd1_12b\x18\n \x01(\x0b\x32%.deeproute.canbus.gwm.p03.IFC_FD1_12B\x12:\n\x0bifc_fd5_19f\x18\x0b \x01(\x0b\x32%.deeproute.canbus.gwm.p03.IFC_FD5_19F\x12:\n\x0bifc_fd6_222\x18\x0c \x01(\x0b\x32%.deeproute.canbus.gwm.p03.IFC_FD6_222\x12:\n\x0bifc_fd7_2a2\x18\x0f \x01(\x0b\x32%.deeproute.canbus.gwm.p03.IFC_FD7_2A2\x12:\n\x0bifc_fd3_2cf\x18\x10 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.IFC_FD3_2CF\x12:\n\x0b\x61\x65\x62_fd1_18b\x18\x11 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.AEB_FD1_18B\x12:\n\x0b\x61\x65\x62_fd2_227\x18\x12 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.AEB_FD2_227\x12:\n\x0bmdc_fd1_312\x18\x13 \x01(\x0b\x32%.deeproute.canbus.gwm.p03.MDC_FD1_312\x12\x38\n\ncr_fd1_15e\x18\x14 \x01(\x0b\x32$.deeproute.canbus.gwm.p03.CR_FD1_15E\x12<\n\x0c\x61\x64\x61s_ad1_470\x18\x15 \x01(\x0b\x32&.deeproute.canbus.gwm.p03.ADAS_AD1_470\x12<\n\x0crsds_fd1_16f\x18\x16 \x01(\x0b\x32&.deeproute.canbus.gwm.p03.RSDS_FD1_16F\x12<\n\x0crsds_fd2_30a\x18\x17 \x01(\x0b\x32&.deeproute.canbus.gwm.p03.RSDS_FD2_30A\"n\n\x12UpstreamChassisP03\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x45\n\x0e\x63hassis_detail\x18\x02 \x01(\x0b\x32-.deeproute.canbus.gwm.p03.GwmP03ChassisDetail\"f\n\x14\x44ownstreamChassisP03\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12;\n\x0e\x63hassis_detail\x18\x02 \x01(\x0b\x32#.dr.blc.mcu.GwmP03DownstreamChassis')



_GWMP03DOWNSTREAMCHASSIS = DESCRIPTOR.message_types_by_name['GwmP03DownstreamChassis']
_UPSTREAMCHASSISP03 = DESCRIPTOR.message_types_by_name['UpstreamChassisP03']
_DOWNSTREAMCHASSISP03 = DESCRIPTOR.message_types_by_name['DownstreamChassisP03']
GwmP03DownstreamChassis = _reflection.GeneratedProtocolMessageType('GwmP03DownstreamChassis', (_message.Message,), {
  'DESCRIPTOR' : _GWMP03DOWNSTREAMCHASSIS,
  '__module__' : 'drapi.gwm_p03_downstream_chassis_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.mcu.GwmP03DownstreamChassis)
  })
_sym_db.RegisterMessage(GwmP03DownstreamChassis)

UpstreamChassisP03 = _reflection.GeneratedProtocolMessageType('UpstreamChassisP03', (_message.Message,), {
  'DESCRIPTOR' : _UPSTREAMCHASSISP03,
  '__module__' : 'drapi.gwm_p03_downstream_chassis_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.mcu.UpstreamChassisP03)
  })
_sym_db.RegisterMessage(UpstreamChassisP03)

DownstreamChassisP03 = _reflection.GeneratedProtocolMessageType('DownstreamChassisP03', (_message.Message,), {
  'DESCRIPTOR' : _DOWNSTREAMCHASSISP03,
  '__module__' : 'drapi.gwm_p03_downstream_chassis_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.mcu.DownstreamChassisP03)
  })
_sym_db.RegisterMessage(DownstreamChassisP03)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GWMP03DOWNSTREAMCHASSIS._serialized_start=92
  _GWMP03DOWNSTREAMCHASSIS._serialized_end=1381
  _UPSTREAMCHASSISP03._serialized_start=1383
  _UPSTREAMCHASSISP03._serialized_end=1493
  _DOWNSTREAMCHASSISP03._serialized_start=1495
  _DOWNSTREAMCHASSISP03._serialized_end=1597
# @@protoc_insertion_point(module_scope)
