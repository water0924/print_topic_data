# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: canbus/mar_chassis_detail.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63\x61nbus/mar_chassis_detail.proto\x12\x10\x64\x65\x65proute.canbus\"N\n\x10MarChassisDetail\x12:\n\rgw_hsc2_frp00\x18\x01 \x01(\x0b\x32#.deeproute.canbus.GW_HSC2_FrP00_169\"\xd9\x13\n\x11GW_HSC2_FrP00_169\x12\x44\n\repb_available\x18\x01 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\reps_available\x18\x02 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0etccm_available\x18\x03 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rscu_available\x18\x04 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rscs_available\x18\x05 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rsdm_available\x18\x06 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rtcm_available\x18\x07 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\recm_available\x18\x08 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rtca_available\x18\t \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0eplcm_available\x18\n \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rmsm_available\x18\x0b \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0e\x66vcm_available\x18\x0c \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rhcu_available\x18\r \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rdhl_available\x18\x0e \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rsas_available\x18\x0f \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x46\n\x0fradar_available\x18\x10 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rbms_available\x18\x11 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\risc_available\x18\x12 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0e\x65scl_available\x18\x13 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0e\x66icm_available\x18\x14 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0etbox_available\x18\x15 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0epmdc_available\x18\x16 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0epeps_available\x18\x17 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\raca_available\x18\x18 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\ripc_available\x18\x19 \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rbcm_available\x18\x1a \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rp2p_available\x18\x1b \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rapa_available\x18\x1c \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12G\n\x10hvdcdc_available\x18\x1d \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x44\n\rrda_available\x18\x1e \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0etpms_available\x18\x1f \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0epacm_available\x18  \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0e\x61lcm_available\x18! \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0e\x65hbs_available\x18\" \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\x12\x45\n\x0esavm_available\x18# \x01(\x0e\x32-.deeproute.canbus.GW_HSC2_FrP00_169.Available\" \n\tAvailable\x12\t\n\x05\x46\x41LSE\x10\x00\x12\x08\n\x04TRUE\x10\x01')



_MARCHASSISDETAIL = DESCRIPTOR.message_types_by_name['MarChassisDetail']
_GW_HSC2_FRP00_169 = DESCRIPTOR.message_types_by_name['GW_HSC2_FrP00_169']
_GW_HSC2_FRP00_169_AVAILABLE = _GW_HSC2_FRP00_169.enum_types_by_name['Available']
MarChassisDetail = _reflection.GeneratedProtocolMessageType('MarChassisDetail', (_message.Message,), {
  'DESCRIPTOR' : _MARCHASSISDETAIL,
  '__module__' : 'canbus.mar_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.MarChassisDetail)
  })
_sym_db.RegisterMessage(MarChassisDetail)

GW_HSC2_FrP00_169 = _reflection.GeneratedProtocolMessageType('GW_HSC2_FrP00_169', (_message.Message,), {
  'DESCRIPTOR' : _GW_HSC2_FRP00_169,
  '__module__' : 'canbus.mar_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.GW_HSC2_FrP00_169)
  })
_sym_db.RegisterMessage(GW_HSC2_FrP00_169)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MARCHASSISDETAIL._serialized_start=53
  _MARCHASSISDETAIL._serialized_end=131
  _GW_HSC2_FRP00_169._serialized_start=134
  _GW_HSC2_FRP00_169._serialized_end=2655
  _GW_HSC2_FRP00_169_AVAILABLE._serialized_start=2623
  _GW_HSC2_FRP00_169_AVAILABLE._serialized_end=2655
# @@protoc_insertion_point(module_scope)
