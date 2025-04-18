# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drapi/gl/gl_driving.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.drapi.gl import gl_driving_common_pb2 as drapi_dot_gl_dot_gl__driving__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x64rapi/gl/gl_driving.proto\x12\ngl.driving\x1a drapi/gl/gl_driving_common.proto\"\xb1\x03\n\x14\x44rivingVehicleRender\x12&\n\x08obstacle\x18\x01 \x03(\x0b\x32\x14.gl.driving.Obstacle\x12/\n\rplanning_line\x18\x02 \x01(\x0b\x32\x18.gl.driving.PlanningLine\x12\x39\n\x11hwa_leading_point\x18\x03 \x01(\x0b\x32\x1e.gl.driving.EthHWALeadingPoint\x12;\n\x11lane_change_color\x18\x04 \x01(\x0e\x32 .gl.driving.EthAsyLanChgColorDsp\x12\x34\n\x10slow_down_status\x18\x05 \x01(\x0e\x32\x1a.gl.driving.EthSlowDownSts\x12,\n\nstop_point\x18\x06 \x01(\x0b\x32\x18.gl.driving.EthStopPoint\x12%\n\x06narrow\x18\x07 \x01(\x0b\x32\x15.gl.driving.EthNarrow\x12=\n\x13\x63ross_planning_line\x18\x08 \x01(\x0b\x32 .gl.driving.EthCrossPlanningLine\"\xfa\x03\n\x1a\x44rivingVehicleAdditionInfo\x12&\n\x07hmi_ctl\x18\x01 \x01(\x0b\x32\x15.gl.driving.EthHmiCtl\x12\x30\n\radc_ctrl_mode\x18\x02 \x01(\x0e\x32\x19.gl.driving.EthADCtrlMode\x12.\n\tlgt_indcr\x18\x03 \x01(\x0e\x32\x1b.gl.driving.EthAsyALgtIndcr\x12-\n\nlgt_status\x18\x04 \x01(\x0e\x32\x19.gl.driving.EthAsyALgtSts\x12.\n\tlat_indcr\x18\x05 \x01(\x0e\x32\x1b.gl.driving.EthAsyALatIndcr\x12\x43\n\x15tsi_info_for_lgt_ctrl\x18\x06 \x01(\x0e\x32$.gl.driving.EthDispTSIInfoForLgtCtrl\x12\x43\n\x16speed_set_for_lgt_ctrl\x18\x07 \x01(\x0b\x32#.gl.driving.EthDispSpdSetForLgtCtrl\x12\x38\n\x11lat_offset_status\x18\x08 \x01(\x0e\x32\x1d.gl.driving.EthAsyLatOffstSts\x12/\n\nend_of_odd\x18\t \x01(\x0b\x32\x1b.gl.driving.EthOffsEndOfODD\"\xa9\x12\n\x11\x44rivingCSDMessage\x12\x35\n\x0flane_change_msg\x18\x01 \x01(\x0e\x32\x1c.gl.driving.EthAsyLanChgMesg\x12<\n\x13inform_for_drvr_msg\x18\x02 \x01(\x0e\x32\x1f.gl.driving.EthAsyInformForDrvr\x12\x38\n\x10noa_distance_msg\x18\x03 \x01(\x0e\x32\x1e.gl.driving.EthAsyNoaDistanMsg\x12\x35\n\x11lcma_left_warning\x18\x04 \x01(\x0e\x32\x1a.gl.driving.EthLcmaIndcnLe\x12\x36\n\x12lcma_right_warning\x18\x05 \x01(\x0e\x32\x1a.gl.driving.EthLcmaIndcnRi\x12\x35\n\x11\x66\x63ta_left_warning\x18\x06 \x01(\x0e\x32\x1a.gl.driving.EthFctaIndcnLe\x12\x36\n\x12\x66\x63ta_right_warning\x18\x07 \x01(\x0e\x32\x1a.gl.driving.EthFctaIndcnRi\x12\x34\n\x0brcw_warning\x18\x08 \x01(\x0e\x32\x1f.gl.driving.EthCllsnWarnReIndcn\x12\x32\n\x0f\x64rv_off_warning\x18\t \x01(\x0e\x32\x19.gl.driving.EthDrvOffWarn\x12?\n\x11lgt_ctrl_takeover\x18\n \x01(\x0e\x32$.gl.driving.EthAsyLgtCtrlTakeOverReq\x12?\n\x15ovrd_for_first_active\x18\x0b \x01(\x0e\x32 .gl.driving.EthOvrdWrnForFstActv\x12\x42\n\x15\x63ncl_lgt_for_auto_drv\x18\x0c \x01(\x0e\x32#.gl.driving.EthCnclWarnLgtForAutDrv\x12\x44\n\x18\x61vl_sts_for_long_aut_drv\x18\r \x01(\x0e\x32\".gl.driving.EthAvlStsForLongAutDrv\x12:\n\x10steer_apply_rqrd\x18\x0e \x01(\x0e\x32 .gl.driving.EthAsySteerApplyRqrd\x12\x42\n\x16steer_apply_rqrd_steer\x18\x0f \x01(\x0e\x32\".gl.driving.EthAsyWarnForSteerCncl\x12\x44\n\x12\x65mgy_lane_keep_aid\x18\x10 \x01(\x0e\x32(.gl.driving.EthWarnForAsyEmgyLaneKeepAid\x12\x34\n\x0c\x61id_post_ema\x18\x11 \x01(\x0e\x32\x1e.gl.driving.EthCllsnAidPostEMA\x12/\n\x0crcwm_brk_req\x18\x12 \x01(\x0e\x32\x19.gl.driving.EthRcwmBrkReq\x12\x33\n\x0e\x63llsn_fwd_warn\x18\x13 \x01(\x0e\x32\x1b.gl.driving.EthCllsnFwdWarn\x12\x32\n\rrcwm_aid_post\x18\x14 \x01(\x0e\x32\x1b.gl.driving.EthCllsnAidPost\x12=\n\x11\x64oor_open_warn_le\x18\x15 \x01(\x0e\x32\".gl.driving.EthDoorOpenwarnLeIndcn\x12=\n\x11\x64oor_open_warn_ri\x18\x16 \x01(\x0e\x32\".gl.driving.EthDoorOpenwarnRiIndcn\x12\x34\n\rsafe_stop_sts\x18\x17 \x01(\x0e\x32\x1d.gl.driving.EthAsySafeStopSts\x12\x38\n\reyes_off_warn\x18\x18 \x01(\x0e\x32!.gl.driving.EthAsyEyesOffWarnRqrd\x12\x37\n\x0enoa_remind_msg\x18\x19 \x01(\x0e\x32\x1f.gl.driving.EthAsyNoaRemindMesg\x12\x31\n\x06noa_tk\x18\x1a \x01(\x0e\x32!.gl.driving.EthAsyNoaTakeoverMesg\x12@\n\x11noa_deactvd_reasn\x18\x1b \x01(\x0e\x32%.gl.driving.EthAsyNoaDeactvdReasnMesg\x12\x32\n\x0c\x61uti_drv_avl\x18\x1c \x01(\x0e\x32\x1c.gl.driving.EthAsyAutDrvgAvl\x12\x35\n\x0bnoa_act_sug\x18\x1d \x01(\x0e\x32 .gl.driving.EthAsyNoaActvSuggest\x12;\n\x11\x63ncl_for_auto_drv\x18\x1e \x01(\x0e\x32 .gl.driving.EthCnclWarnForAutDrv\x12\x30\n\x0blat_deg_sts\x18\x1f \x01(\x0e\x32\x1b.gl.driving.EthAsyLatDegSts\x12\x35\n\x0cicc_max_warn\x18  \x01(\x0e\x32\x1f.gl.driving.EthAsyIccMaxWarnMsg\x12\x32\n\x08\x63noa_act\x18! \x01(\x0e\x32 .gl.driving.EthAsyCnoaCrsActvMsg\x12=\n\x0e\x63noa_act_faild\x18\" \x01(\x0e\x32%.gl.driving.EthAsyCnoaCrsActvFaildMsg\x12\x38\n\x0b\x63noa_deatcd\x18# \x01(\x0e\x32#.gl.driving.EthAsyCnoaCrsDeactvdMsg\x12\x39\n\rcnoa_lane_chg\x18$ \x01(\x0e\x32\".gl.driving.EthAsyCNoaCrsLanChgMsg\x12\x36\n\x0c\x63noa_crs_off\x18% \x01(\x0e\x32 .gl.driving.EthAsyCnoaCrsOffsMsg\x12\x36\n\x07\x63noa_tk\x18& \x01(\x0e\x32%.gl.driving.EthAsyCnoaTakeoverWarnMsg\x12?\n\x0e\x63noa_crs_cross\x18\' \x01(\x0e\x32\'.gl.driving.EthAsyCnoaCrsCrossIntsecMsg\x12\x35\n\x0c\x63noa_crs_rmn\x18( \x01(\x0e\x32\x1f.gl.driving.EthAsyCnoaCrsRmnMsg\"\xa3\x03\n\x10\x44rivingMapRender\x12\'\n\tstop_line\x18\x01 \x03(\x0b\x32\x14.gl.driving.StopLine\x12)\n\nroad_arrow\x18\x02 \x03(\x0b\x32\x15.gl.driving.RoadArrow\x12)\n\nspeed_bump\x18\x03 \x03(\x0b\x32\x15.gl.driving.SpeedBump\x12)\n\ncross_walk\x18\x04 \x03(\x0b\x32\x15.gl.driving.CrossWalk\x12\'\n\tlane_edge\x18\x05 \x03(\x0b\x32\x14.gl.driving.LaneEdge\x12/\n\rtraffic_light\x18\x06 \x03(\x0b\x32\x18.gl.driving.TrafficLight\x12-\n\x0ctraffic_sign\x18\x07 \x03(\x0b\x32\x17.gl.driving.TrafficSign\x12-\n\x0chmi_boundary\x18\x08 \x01(\x0b\x32\x17.gl.driving.HmiBoundary\x12-\n\x0c\x64riving_area\x18\t \x03(\x0b\x32\x17.gl.driving.DrivingArea\"\xf2\x02\n\x18\x44rivingMapAdditionalInfo\x12\'\n\tself_lane\x18\x01 \x01(\x0b\x32\x14.gl.driving.SelfLane\x12%\n\x08\x61\x64_theme\x18\x02 \x01(\x0b\x32\x13.gl.driving.ADTheme\x12\x31\n\rmini_adas_obj\x18\x03 \x01(\x0b\x32\x1a.gl.driving.MiniAdasObject\x12\x32\n\x06\x64ow_ri\x18\x04 \x01(\x0e\x32\".gl.driving.EthDoorOpenWarnRiIndcn\x12\x32\n\x06\x64ow_le\x18\x05 \x01(\x0e\x32\".gl.driving.EthDoorOpenWarnLeIndcn\x12\x36\n\x14traffic_light_change\x18\x06 \x01(\x0e\x32\x18.gl.driving.EthTrfcLiChg\x12\x33\n\x08time_gap\x18\x07 \x01(\x0e\x32!.gl.driving.EthTiGapSetForLgtCtrl\"\xcf\x01\n\x0e\x44rivingVehicle\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x35\n\x0brender_data\x18\x02 \x01(\x0b\x32 .gl.driving.DrivingVehicleRender\x12?\n\x0f\x61\x64\x64itional_info\x18\x03 \x01(\x0b\x32&.gl.driving.DrivingVehicleAdditionInfo\x12\x32\n\x0b\x63sd_message\x18\x04 \x01(\x0b\x32\x1d.gl.driving.DrivingCSDMessage\"\x91\x01\n\nDrivingMap\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x31\n\x0brender_data\x18\x02 \x01(\x0b\x32\x1c.gl.driving.DrivingMapRender\x12=\n\x0f\x61\x64\x64itional_info\x18\x03 \x01(\x0b\x32$.gl.driving.DrivingMapAdditionalInfob\x06proto3')



_DRIVINGVEHICLERENDER = DESCRIPTOR.message_types_by_name['DrivingVehicleRender']
_DRIVINGVEHICLEADDITIONINFO = DESCRIPTOR.message_types_by_name['DrivingVehicleAdditionInfo']
_DRIVINGCSDMESSAGE = DESCRIPTOR.message_types_by_name['DrivingCSDMessage']
_DRIVINGMAPRENDER = DESCRIPTOR.message_types_by_name['DrivingMapRender']
_DRIVINGMAPADDITIONALINFO = DESCRIPTOR.message_types_by_name['DrivingMapAdditionalInfo']
_DRIVINGVEHICLE = DESCRIPTOR.message_types_by_name['DrivingVehicle']
_DRIVINGMAP = DESCRIPTOR.message_types_by_name['DrivingMap']
DrivingVehicleRender = _reflection.GeneratedProtocolMessageType('DrivingVehicleRender', (_message.Message,), {
  'DESCRIPTOR' : _DRIVINGVEHICLERENDER,
  '__module__' : 'drapi.gl.gl_driving_pb2'
  # @@protoc_insertion_point(class_scope:gl.driving.DrivingVehicleRender)
  })
_sym_db.RegisterMessage(DrivingVehicleRender)

DrivingVehicleAdditionInfo = _reflection.GeneratedProtocolMessageType('DrivingVehicleAdditionInfo', (_message.Message,), {
  'DESCRIPTOR' : _DRIVINGVEHICLEADDITIONINFO,
  '__module__' : 'drapi.gl.gl_driving_pb2'
  # @@protoc_insertion_point(class_scope:gl.driving.DrivingVehicleAdditionInfo)
  })
_sym_db.RegisterMessage(DrivingVehicleAdditionInfo)

DrivingCSDMessage = _reflection.GeneratedProtocolMessageType('DrivingCSDMessage', (_message.Message,), {
  'DESCRIPTOR' : _DRIVINGCSDMESSAGE,
  '__module__' : 'drapi.gl.gl_driving_pb2'
  # @@protoc_insertion_point(class_scope:gl.driving.DrivingCSDMessage)
  })
_sym_db.RegisterMessage(DrivingCSDMessage)

DrivingMapRender = _reflection.GeneratedProtocolMessageType('DrivingMapRender', (_message.Message,), {
  'DESCRIPTOR' : _DRIVINGMAPRENDER,
  '__module__' : 'drapi.gl.gl_driving_pb2'
  # @@protoc_insertion_point(class_scope:gl.driving.DrivingMapRender)
  })
_sym_db.RegisterMessage(DrivingMapRender)

DrivingMapAdditionalInfo = _reflection.GeneratedProtocolMessageType('DrivingMapAdditionalInfo', (_message.Message,), {
  'DESCRIPTOR' : _DRIVINGMAPADDITIONALINFO,
  '__module__' : 'drapi.gl.gl_driving_pb2'
  # @@protoc_insertion_point(class_scope:gl.driving.DrivingMapAdditionalInfo)
  })
_sym_db.RegisterMessage(DrivingMapAdditionalInfo)

DrivingVehicle = _reflection.GeneratedProtocolMessageType('DrivingVehicle', (_message.Message,), {
  'DESCRIPTOR' : _DRIVINGVEHICLE,
  '__module__' : 'drapi.gl.gl_driving_pb2'
  # @@protoc_insertion_point(class_scope:gl.driving.DrivingVehicle)
  })
_sym_db.RegisterMessage(DrivingVehicle)

DrivingMap = _reflection.GeneratedProtocolMessageType('DrivingMap', (_message.Message,), {
  'DESCRIPTOR' : _DRIVINGMAP,
  '__module__' : 'drapi.gl.gl_driving_pb2'
  # @@protoc_insertion_point(class_scope:gl.driving.DrivingMap)
  })
_sym_db.RegisterMessage(DrivingMap)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DRIVINGVEHICLERENDER._serialized_start=76
  _DRIVINGVEHICLERENDER._serialized_end=509
  _DRIVINGVEHICLEADDITIONINFO._serialized_start=512
  _DRIVINGVEHICLEADDITIONINFO._serialized_end=1018
  _DRIVINGCSDMESSAGE._serialized_start=1021
  _DRIVINGCSDMESSAGE._serialized_end=3366
  _DRIVINGMAPRENDER._serialized_start=3369
  _DRIVINGMAPRENDER._serialized_end=3788
  _DRIVINGMAPADDITIONALINFO._serialized_start=3791
  _DRIVINGMAPADDITIONALINFO._serialized_end=4161
  _DRIVINGVEHICLE._serialized_start=4164
  _DRIVINGVEHICLE._serialized_end=4371
  _DRIVINGMAP._serialized_start=4374
  _DRIVINGMAP._serialized_end=4519
# @@protoc_insertion_point(module_scope)
