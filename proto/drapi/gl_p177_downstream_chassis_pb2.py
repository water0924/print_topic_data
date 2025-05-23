# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drapi/gl_p177_downstream_chassis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.canbus import gl_p177_chassis_detail_pb2 as canbus_dot_gl__p177__chassis__detail__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&drapi/gl_p177_downstream_chassis.proto\x12\ndr.blc.mcu\x1a#canbus/gl_p177_chassis_detail.proto\"c\n\rGLP177Request\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr02_1f0\x18\x01 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR02_1F0\"\x93\x19\n\x17GLP177DownstreamChassis\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr10_1b5\x18\x01 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR10_1B5\x12J\n\x13\x61sdm_chas1_fr07_117\x18\x02 \x01(\x0b\x32-.deeproute.canbus.gl.p177.ASDM_CHAS1_FR07_117\x12P\n\x16\x64hu_zcucanfd1_fr01_1e8\x18\x03 \x01(\x0b\x32\x30.deeproute.canbus.gl.p177.DHU_ZCUCANFD1_FR01_1E8\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr06_1ff\x18\x04 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR06_1FF\x12P\n\x16\x64hu_zcucanfd1_fr13_367\x18\x05 \x01(\x0b\x32\x30.deeproute.canbus.gl.p177.DHU_ZCUCANFD1_FR13_367\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr13_190\x18\x06 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR13_190\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr02_1f0\x18\x07 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR02_1F0\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr19_226\x18\x08 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR19_226\x12J\n\x13\x61sdm_chas1_fr06_131\x18\t \x01(\x0b\x32-.deeproute.canbus.gl.p177.ASDM_CHAS1_FR06_131\x12N\n\x15paszcucanfd1_fr05_335\x18\n \x01(\x0b\x32/.deeproute.canbus.gl.p177.PASZCUCANFD1_FR05_335\x12Z\n\x1b\x61\x64\x63u_to_dhu_sec_oc_fr01_132\x18\x0b \x01(\x0b\x32\x35.deeproute.canbus.gl.p177.ADCU_TO_DHU_SEC_OC_FR01_132\x12N\n\x15paszcucanfd1_fr20_112\x18\x0c \x01(\x0b\x32/.deeproute.canbus.gl.p177.PASZCUCANFD1_FR20_112\x12N\n\x15paszcucanfd1_fr02_311\x18\r \x01(\x0b\x32/.deeproute.canbus.gl.p177.PASZCUCANFD1_FR02_311\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr08_120\x18\x0e \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR08_120\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr09_360\x18\x0f \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR09_360\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr07_280\x18\x10 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR07_280\x12N\n\x15paszcucanfd1_fr06_210\x18\x11 \x01(\x0b\x32/.deeproute.canbus.gl.p177.PASZCUCANFD1_FR06_210\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr04_1a0\x18\x12 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR04_1A0\x12P\n\x16\x64hu_zcucanfd1_fr04_175\x18\x13 \x01(\x0b\x32\x30.deeproute.canbus.gl.p177.DHU_ZCUCANFD1_FR04_175\x12L\n\x14paszcucanfd1_fr07_60\x18\x14 \x01(\x0b\x32..deeproute.canbus.gl.p177.PASZCUCANFD1_FR07_60\x12N\n\x15paszcucanfd1_fr15_24b\x18\x15 \x01(\x0b\x32/.deeproute.canbus.gl.p177.PASZCUCANFD1_FR15_24B\x12N\n\x15paszcucanfd1_fr04_211\x18\x16 \x01(\x0b\x32/.deeproute.canbus.gl.p177.PASZCUCANFD1_FR04_211\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr03_2f0\x18\x17 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR03_2F0\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr11_1e0\x18\x18 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR11_1E0\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr01_1c0\x18\x19 \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR01_1C0\x12N\n\x15paszcucanfd1_fr18_310\x18\x1a \x01(\x0b\x32/.deeproute.canbus.gl.p177.PASZCUCANFD1_FR18_310\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr21_1c6\x18\x1b \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR21_1C6\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr14_220\x18\x1c \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR14_220\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr23_116\x18\x1d \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR23_116\x12P\n\x16\x64hu_zcucanfd1_fr02_307\x18\x1e \x01(\x0b\x32\x30.deeproute.canbus.gl.p177.DHU_ZCUCANFD1_FR02_307\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr22_1ca\x18\x1f \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR22_1CA\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr12_370\x18  \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR12_370\x12H\n\x12pscm_chas1_fr01_f6\x18! \x01(\x0b\x32,.deeproute.canbus.gl.p177.PSCM_CHAS1_FR01_F6\x12H\n\x12\x61sdm_chas1_fr10_54\x18\" \x01(\x0b\x32,.deeproute.canbus.gl.p177.ASDM_CHAS1_FR10_54\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr20_30a\x18# \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR20_30A\x12R\n\x17\x61\x64\x63u_zcucanfd1_fr05_480\x18$ \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ADCU_ZCUCANFD1_FR05_480\x12H\n\x12\x61sdm_chas1_fr01_93\x18% \x01(\x0b\x32,.deeproute.canbus.gl.p177.ASDM_CHAS1_FR01_93\x12P\n\x16\x64hu_zcucanfd1_fr14_1f8\x18& \x01(\x0b\x32\x30.deeproute.canbus.gl.p177.DHU_ZCUCANFD1_FR14_1F8\x12R\n\x17zcud_zcucanfd1_fr07_1c3\x18\' \x01(\x0b\x32\x31.deeproute.canbus.gl.p177.ZCUD_ZCUCANFD1_FR07_1C3\"k\n\x0fUpstreamChassis\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x45\n\x0e\x63hassis_detail\x18\x02 \x01(\x0b\x32-.deeproute.canbus.gl.p177.GlP177ChassisDetail\"c\n\x11\x44ownstreamChassis\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12;\n\x0e\x63hassis_detail\x18\x02 \x01(\x0b\x32#.dr.blc.mcu.GLP177DownstreamChassis')



_GLP177REQUEST = DESCRIPTOR.message_types_by_name['GLP177Request']
_GLP177DOWNSTREAMCHASSIS = DESCRIPTOR.message_types_by_name['GLP177DownstreamChassis']
_UPSTREAMCHASSIS = DESCRIPTOR.message_types_by_name['UpstreamChassis']
_DOWNSTREAMCHASSIS = DESCRIPTOR.message_types_by_name['DownstreamChassis']
GLP177Request = _reflection.GeneratedProtocolMessageType('GLP177Request', (_message.Message,), {
  'DESCRIPTOR' : _GLP177REQUEST,
  '__module__' : 'drapi.gl_p177_downstream_chassis_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.mcu.GLP177Request)
  })
_sym_db.RegisterMessage(GLP177Request)

GLP177DownstreamChassis = _reflection.GeneratedProtocolMessageType('GLP177DownstreamChassis', (_message.Message,), {
  'DESCRIPTOR' : _GLP177DOWNSTREAMCHASSIS,
  '__module__' : 'drapi.gl_p177_downstream_chassis_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.mcu.GLP177DownstreamChassis)
  })
_sym_db.RegisterMessage(GLP177DownstreamChassis)

UpstreamChassis = _reflection.GeneratedProtocolMessageType('UpstreamChassis', (_message.Message,), {
  'DESCRIPTOR' : _UPSTREAMCHASSIS,
  '__module__' : 'drapi.gl_p177_downstream_chassis_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.mcu.UpstreamChassis)
  })
_sym_db.RegisterMessage(UpstreamChassis)

DownstreamChassis = _reflection.GeneratedProtocolMessageType('DownstreamChassis', (_message.Message,), {
  'DESCRIPTOR' : _DOWNSTREAMCHASSIS,
  '__module__' : 'drapi.gl_p177_downstream_chassis_pb2'
  # @@protoc_insertion_point(class_scope:dr.blc.mcu.DownstreamChassis)
  })
_sym_db.RegisterMessage(DownstreamChassis)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GLP177REQUEST._serialized_start=91
  _GLP177REQUEST._serialized_end=190
  _GLP177DOWNSTREAMCHASSIS._serialized_start=193
  _GLP177DOWNSTREAMCHASSIS._serialized_end=3412
  _UPSTREAMCHASSIS._serialized_start=3414
  _UPSTREAMCHASSIS._serialized_end=3521
  _DOWNSTREAMCHASSIS._serialized_start=3523
  _DOWNSTREAMCHASSIS._serialized_end=3622
# @@protoc_insertion_point(module_scope)
