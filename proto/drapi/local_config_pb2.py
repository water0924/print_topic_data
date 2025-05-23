# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drapi/local_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.drapi import navigation_map_pb2 as drapi_dot_navigation__map__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x64rapi/local_config.proto\x12\x0e\x64r.localconfig\x1a\x1a\x64rapi/navigation_map.proto\"\xdf\x16\n\nUserConfig\x12\x33\n\rdriving_style\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.DrivingStyle\x12\x31\n\x0b\x66\x61st_active\x18\x02 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12=\n\x12\x61\x63\x63\x65leration_style\x18\x14 \x01(\x0e\x32!.dr.localconfig.AccelerationStyle\x12\x35\n\x0fpure_model_path\x18\x15 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x36\n\x10pure_model_speed\x18\x16 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12:\n\x14ilqr_lon_safety_cost\x18\x17 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12:\n\x14ilqr_lat_safety_cost\x18\x18 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x36\n\x10wait_area_enable\x18\x19 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12>\n\x18obstacle_collision_check\x18\x1a \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x42\n\x1cno_front_vehicle_speed_check\x18\x1b \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x36\n\x10wrong_lane_check\x18\x1c \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x42\n\x1ctraffic_light_abnormal_check\x18\x1d \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x38\n\x12will_out_odd_check\x18\x1e \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12/\n\tdms_check\x18\x1f \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12<\n\x16vehicle_lat_dist_check\x18  \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12>\n\x18vehicle_angle_diff_check\x18! \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12>\n\x18speed_switch_fault_check\x18\" \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x41\n\x1btime_gap_switch_fault_check\x18# \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12;\n\x15\x65mergency_light_check\x18$ \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12/\n\tota_check\x18% \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x36\n\x10\x65sa_active_check\x18& \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x36\n\x10\x61\x65\x62_active_check\x18\' \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12<\n\x16\x63ruise_cancel_exit_all\x18( \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12/\n\tdemo_mode\x18) \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12=\n\x17traffic_light_attention\x18* \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x32\n\x0c\x63\x61mera_check\x18+ \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x35\n\x0flane_miss_latem\x18, \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x37\n\x11lane_narrow_latem\x18- \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x46\n turnarround_roundabout_downgrade\x18. \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12=\n\x17\x66orce_lane_change_check\x18/ \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x35\n\x0fsnowy_day_check\x18\x30 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12-\n\nacc_config\x18\x33 \x01(\x0b\x32\x19.dr.localconfig.ACCConfig\x12-\n\nica_config\x18\x34 \x01(\x0b\x32\x19.dr.localconfig.ICAConfig\x12-\n\nnca_config\x18\x35 \x01(\x0b\x32\x19.dr.localconfig.NCAConfig\x12-\n\navm_config\x18\x36 \x01(\x0b\x32\x19.dr.localconfig.AVMConfig\x12-\n\nlas_config\x18\x37 \x01(\x0b\x32\x19.dr.localconfig.LASConfig\x12-\n\ntjp_config\x18\x38 \x01(\x0b\x32\x19.dr.localconfig.TJPConfig\x12-\n\napa_config\x18\x39 \x01(\x0b\x32\x19.dr.localconfig.APAConfig\x12-\n\nrpa_config\x18: \x01(\x0b\x32\x19.dr.localconfig.RPAConfig\x12-\n\nhut_config\x18; \x01(\x0b\x32\x19.dr.localconfig.HUTConfig\x12-\n\ne2e_config\x18< \x01(\x0b\x32\x19.dr.localconfig.E2EConfig\x12=\n\x17\x62rake_light_fault_check\x18\x64 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x34\n\x0eip_error_check\x18\x65 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x35\n\x0fvcu_error_check\x18\x66 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x39\n\x13vcu_com_error_check\x18g \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x39\n\x13\x65ps_lka_fault_check\x18h \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12=\n\x17turn_signal_error_check\x18i \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12:\n\x14privacy_switch_check\x18j \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12;\n\x15gps_auth_switch_check\x18k \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12=\n\x17map_status_switch_check\x18l \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x42\n\x1cplanning_failed_switch_check\x18m \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"\x82\x02\n\tACCConfig\x12:\n\x14\x65nable_switch_status\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x37\n\x11isl_switch_status\x18\x02 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12<\n\x16tsr_warn_switch_status\x18\x03 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x42\n\x1c\x62rake_detecter_switch_status\x18\x14 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"\x9b\x03\n\tICAConfig\x12:\n\x14\x65nable_switch_status\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x39\n\x13\x61uto_upgrade_status\x18\x02 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12=\n\x17pole_lane_change_switch\x18\x03 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x30\n\nalc_switch\x18\x04 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12:\n\x11lane_change_snvty\x18\x05 \x01(\x0e\x32\x1f.dr.localconfig.LaneChangeSnvty\x12\x33\n\rdetour_switch\x18\x06 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x35\n\x0fhands_on_switch\x18\x14 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"\xb5\x03\n\tNCAConfig\x12:\n\x14\x65nable_switch_status\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12>\n\x13speed_offset_config\x18\x02 \x01(\x0b\x32!.dr.localconfig.SpeedOffsetConfig\x12@\n\x1a\x65xceed_speed_limit_warning\x18\x03 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x37\n\x0fnavigation_mode\x18\x04 \x01(\x0e\x32\x1e.dr.localconfig.NavigationMode\x12\x39\n\x10handsoff_timeset\x18\x05 \x01(\x0e\x32\x1f.dr.localconfig.HandsOffTimeSet\x12\x44\n\x15odd_type_limit_config\x18\x06 \x01(\x0b\x32%.dr.localconfig.NCAODDTypeLimitConfig\x12\x30\n\nodd_config\x18\x14 \x01(\x0b\x32\x1c.dr.localconfig.NCAODDConfig\"D\n\x0cNCAODDConfig\x12\x34\n\x0eroad_class_set\x18\x01 \x03(\x0e\x32\x1c.dr.navigation_map.RoadClass\"|\n\x11SpeedOffsetConfig\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.dr.localconfig.SpeedOffsetConfig.Type\x12\x0e\n\x06offset\x18\x02 \x01(\x05\"!\n\x04Type\x12\t\n\x05\x46IXED\x10\x00\x12\x0e\n\nPERCENTAGE\x10\x01\"\x89\x03\n\tLASConfig\x12\x37\n\nlas_switch\x18\x01 \x01(\x0e\x32#.dr.localconfig.LASConfig.LasSwitch\x12\x37\n\x11gw_warning_switch\x18\x02 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12<\n\x0bmute_config\x18\x03 \x01(\x0e\x32\'.dr.localconfig.LASConfig.MuteKeyConfig\x12<\n\x16pnc_lat_control_switch\x18\x04 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"O\n\tLasSwitch\x12\x12\n\x0eUNKNOWN_SWITCH\x10\x00\x12\r\n\tCLOSE_ALL\x10\x01\x12\x11\n\rONLY_OPEN_LDW\x10\x02\x12\x0c\n\x08OPEN_ALL\x10\x03\"=\n\rMuteKeyConfig\x12\x10\n\x0cUNKNOWN_MUTE\x10\x00\x12\x0c\n\x08MUTE_ALL\x10\x01\x12\x0c\n\x08MUTE_ELK\x10\x02\"\x93\t\n\tAVMConfig\x12\x42\n\x1clow_speed_roation_activation\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x45\n\x1f\x63\x61r_body_transparent_activation\x18\x02 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12J\n\x0b\x61ssist_type\x18\x03 \x01(\x0e\x32\x35.dr.localconfig.AVMConfig.NarrowPathAndObstacleAssist\x12\x44\n\x1epdc_active_avm_only_on_level_4\x18\x04 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12<\n\x12\x61vm_driving_config\x18\x05 \x01(\x0b\x32 .dr.localconfig.AVMDrivingConfig\x12\x33\n\x0c\x65nable_debug\x18\xe8\x07 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x44\n\x1donly_show_ultrasonic_obstacle\x18\xe9\x07 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x35\n\x0epdc_bev_enable\x18\xea\x07 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12=\n\x0bspeed_limit\x18\xeb\x07 \x01(\x0e\x32\'.dr.localconfig.AVMConfig.AvmSpeedLimit\x12=\n\ravm_turn_mode\x18\xec\x07 \x01(\x0e\x32%.dr.localconfig.AVMConfig.AvmTurnMode\x12\x34\n\rfpas_auto_mod\x18\xed\x07 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12<\n\x15open_visualizer_image\x18\xee\x07 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x36\n\x0fwheel_view_mode\x18\xef\x07 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x37\n\rwheel_vie_sts\x18\xf0\x07 \x01(\x0e\x32\x1f.dr.localconfig.WheelVieStsType\"X\n\x1bNarrowPathAndObstacleAssist\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x44ISABLE\x10\x01\x12\n\n\x06NEARLY\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x07\n\x03\x46\x41R\x10\x04\"T\n\rAvmSpeedLimit\x12\x17\n\x13SPEED_LIMIT_UNKNOWN\x10\x00\x12\x14\n\x10SPEED_LIMIT_15KM\x10\x01\x12\x14\n\x10SPEED_LIMIT_30KM\x10\x02\"f\n\x0b\x41vmTurnMode\x12\x15\n\x11TURN_MODE_UNKNOWN\x10\x00\x12\x11\n\rTURN_MODE_OFF\x10\x01\x12\x12\n\x0eTURN_MODE_CARD\x10\x02\x12\x19\n\x15TURN_MODE_FULL_SCREEN\x10\x03\"\xba\x01\n\x10\x41VMDrivingConfig\x12\x38\n\x05style\x18\x01 \x01(\x0e\x32).dr.localconfig.AVMDrivingConfig.AVMStyle\x12\x34\n\x0eturning_enable\x18\x02 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"6\n\x08\x41VMStyle\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0b\x46ULL_SCREEN\x10\x01\x12\x0c\n\x08\x46LOATING\x10\x02\"G\n\tTJPConfig\x12:\n\x14\x65nable_switch_status\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"\x9d\x02\n\tAPAConfig\x12\x32\n\x0c\x66\x61st_parking\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x30\n\nenable_apa\x18\x02 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x32\n\x0c\x61uto_parkout\x18\x03 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x44\n\x11\x61pa_parking_speed\x18\x04 \x01(\x0e\x32).dr.localconfig.APAConfig.APAParkingSpeed\"0\n\x0f\x41PAParkingSpeed\x12\x07\n\x03Low\x10\x00\x12\n\n\x06Medium\x10\x01\x12\x08\n\x04High\x10\x02\"G\n\tRPAConfig\x12:\n\x14ignore_side_obstacle\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"o\n\tHUTConfig\x12\x30\n\nenable_hut\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x30\n\nenable_viz\x18\x02 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"=\n\tE2EConfig\x12\x30\n\nenable_e2e\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"D\n\tCMSConfig\x12\x37\n\x11side_bsd_disp_sts\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\"\xf6\x01\n\x15NCAODDTypeLimitConfig\x12\x37\n\x11\x66ixed_odd_passive\x18\x01 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12;\n\x15temporary_odd_passive\x18\x02 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12\x38\n\x12\x64ynamic_static_odd\x18\x03 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus\x12-\n\x07roi_odd\x18\x04 \x01(\x0e\x32\x1c.dr.localconfig.SwitchStatus*H\n\x0cSwitchStatus\x12\x19\n\x15SWITCH_STATUS_UNKNOWN\x10\x00\x12\r\n\tSWITCH_ON\x10\x01\x12\x0e\n\nSWITCH_OFF\x10\x02*T\n\x0c\x44rivingStyle\x12\x10\n\x0cUNKNOWN_MODE\x10\x00\x12\x0f\n\x0b\x43\x41SUAL_MODE\x10\x01\x12\x11\n\rSTANDARD_MODE\x10\x02\x12\x0e\n\nSPORT_MODE\x10\x03*\x84\x01\n\x11\x41\x63\x63\x65lerationStyle\x12\x18\n\x14UNKNOWN_ACCELERATION\x10\x00\x12\x19\n\x15STANDARD_ACCELERATION\x10\x01\x12\x1d\n\x19\x43ONSERVATIVE_ACCELERATION\x10\x02\x12\x1b\n\x17\x41GGRESSIVE_ACCELERATION\x10\x03*K\n\x0eNavigationMode\x12\x15\n\x11UNKNOWN_NAVI_MODE\x10\x00\x12\x0f\n\x0b\x44R_NAVIMODE\x10\x01\x12\x11\n\rAMAP_NAVIMODE\x10\x02*g\n\x0fLaneChangeSnvty\x12\x11\n\rSNVTY_UNKNOWN\x10\x00\x12\x16\n\x12NORMAL_SENSITIVITY\x10\x01\x12\x14\n\x10HIGH_SENSITIVITY\x10\x02\x12\x13\n\x0fLOW_SENSITIVITY\x10\x03*O\n\x0fHandsOffTimeSet\x12\x14\n\x10HANDSOFF_UNKNOWN\x10\x00\x12\x13\n\x0fHANDSOFF_NORMAL\x10\x01\x12\x11\n\rHANDSOFF_LONG\x10\x02*\x8b\x01\n\x0fWheelVieStsType\x12\x1d\n\x19WHEELVIESTS_INITIAL_VALUE\x10\x00\x12\x1e\n\x1aWHEELVIESTS_TWO_WHEEL_MODE\x10\x01\x12\x1f\n\x1bWHEELVIESTS_FOUR_WHEEL_MODE\x10\x02\x12\x18\n\x14WHEELVIESTS_REVERSED\x10\x03\x62\x06proto3')

_SWITCHSTATUS = DESCRIPTOR.enum_types_by_name['SwitchStatus']
SwitchStatus = enum_type_wrapper.EnumTypeWrapper(_SWITCHSTATUS)
_DRIVINGSTYLE = DESCRIPTOR.enum_types_by_name['DrivingStyle']
DrivingStyle = enum_type_wrapper.EnumTypeWrapper(_DRIVINGSTYLE)
_ACCELERATIONSTYLE = DESCRIPTOR.enum_types_by_name['AccelerationStyle']
AccelerationStyle = enum_type_wrapper.EnumTypeWrapper(_ACCELERATIONSTYLE)
_NAVIGATIONMODE = DESCRIPTOR.enum_types_by_name['NavigationMode']
NavigationMode = enum_type_wrapper.EnumTypeWrapper(_NAVIGATIONMODE)
_LANECHANGESNVTY = DESCRIPTOR.enum_types_by_name['LaneChangeSnvty']
LaneChangeSnvty = enum_type_wrapper.EnumTypeWrapper(_LANECHANGESNVTY)
_HANDSOFFTIMESET = DESCRIPTOR.enum_types_by_name['HandsOffTimeSet']
HandsOffTimeSet = enum_type_wrapper.EnumTypeWrapper(_HANDSOFFTIMESET)
_WHEELVIESTSTYPE = DESCRIPTOR.enum_types_by_name['WheelVieStsType']
WheelVieStsType = enum_type_wrapper.EnumTypeWrapper(_WHEELVIESTSTYPE)
SWITCH_STATUS_UNKNOWN = 0
SWITCH_ON = 1
SWITCH_OFF = 2
UNKNOWN_MODE = 0
CASUAL_MODE = 1
STANDARD_MODE = 2
SPORT_MODE = 3
UNKNOWN_ACCELERATION = 0
STANDARD_ACCELERATION = 1
CONSERVATIVE_ACCELERATION = 2
AGGRESSIVE_ACCELERATION = 3
UNKNOWN_NAVI_MODE = 0
DR_NAVIMODE = 1
AMAP_NAVIMODE = 2
SNVTY_UNKNOWN = 0
NORMAL_SENSITIVITY = 1
HIGH_SENSITIVITY = 2
LOW_SENSITIVITY = 3
HANDSOFF_UNKNOWN = 0
HANDSOFF_NORMAL = 1
HANDSOFF_LONG = 2
WHEELVIESTS_INITIAL_VALUE = 0
WHEELVIESTS_TWO_WHEEL_MODE = 1
WHEELVIESTS_FOUR_WHEEL_MODE = 2
WHEELVIESTS_REVERSED = 3


_USERCONFIG = DESCRIPTOR.message_types_by_name['UserConfig']
_ACCCONFIG = DESCRIPTOR.message_types_by_name['ACCConfig']
_ICACONFIG = DESCRIPTOR.message_types_by_name['ICAConfig']
_NCACONFIG = DESCRIPTOR.message_types_by_name['NCAConfig']
_NCAODDCONFIG = DESCRIPTOR.message_types_by_name['NCAODDConfig']
_SPEEDOFFSETCONFIG = DESCRIPTOR.message_types_by_name['SpeedOffsetConfig']
_LASCONFIG = DESCRIPTOR.message_types_by_name['LASConfig']
_AVMCONFIG = DESCRIPTOR.message_types_by_name['AVMConfig']
_AVMDRIVINGCONFIG = DESCRIPTOR.message_types_by_name['AVMDrivingConfig']
_TJPCONFIG = DESCRIPTOR.message_types_by_name['TJPConfig']
_APACONFIG = DESCRIPTOR.message_types_by_name['APAConfig']
_RPACONFIG = DESCRIPTOR.message_types_by_name['RPAConfig']
_HUTCONFIG = DESCRIPTOR.message_types_by_name['HUTConfig']
_E2ECONFIG = DESCRIPTOR.message_types_by_name['E2EConfig']
_CMSCONFIG = DESCRIPTOR.message_types_by_name['CMSConfig']
_NCAODDTYPELIMITCONFIG = DESCRIPTOR.message_types_by_name['NCAODDTypeLimitConfig']
_SPEEDOFFSETCONFIG_TYPE = _SPEEDOFFSETCONFIG.enum_types_by_name['Type']
_LASCONFIG_LASSWITCH = _LASCONFIG.enum_types_by_name['LasSwitch']
_LASCONFIG_MUTEKEYCONFIG = _LASCONFIG.enum_types_by_name['MuteKeyConfig']
_AVMCONFIG_NARROWPATHANDOBSTACLEASSIST = _AVMCONFIG.enum_types_by_name['NarrowPathAndObstacleAssist']
_AVMCONFIG_AVMSPEEDLIMIT = _AVMCONFIG.enum_types_by_name['AvmSpeedLimit']
_AVMCONFIG_AVMTURNMODE = _AVMCONFIG.enum_types_by_name['AvmTurnMode']
_AVMDRIVINGCONFIG_AVMSTYLE = _AVMDRIVINGCONFIG.enum_types_by_name['AVMStyle']
_APACONFIG_APAPARKINGSPEED = _APACONFIG.enum_types_by_name['APAParkingSpeed']
UserConfig = _reflection.GeneratedProtocolMessageType('UserConfig', (_message.Message,), {
  'DESCRIPTOR' : _USERCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.UserConfig)
  })
_sym_db.RegisterMessage(UserConfig)

ACCConfig = _reflection.GeneratedProtocolMessageType('ACCConfig', (_message.Message,), {
  'DESCRIPTOR' : _ACCCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.ACCConfig)
  })
_sym_db.RegisterMessage(ACCConfig)

ICAConfig = _reflection.GeneratedProtocolMessageType('ICAConfig', (_message.Message,), {
  'DESCRIPTOR' : _ICACONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.ICAConfig)
  })
_sym_db.RegisterMessage(ICAConfig)

NCAConfig = _reflection.GeneratedProtocolMessageType('NCAConfig', (_message.Message,), {
  'DESCRIPTOR' : _NCACONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.NCAConfig)
  })
_sym_db.RegisterMessage(NCAConfig)

NCAODDConfig = _reflection.GeneratedProtocolMessageType('NCAODDConfig', (_message.Message,), {
  'DESCRIPTOR' : _NCAODDCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.NCAODDConfig)
  })
_sym_db.RegisterMessage(NCAODDConfig)

SpeedOffsetConfig = _reflection.GeneratedProtocolMessageType('SpeedOffsetConfig', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDOFFSETCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.SpeedOffsetConfig)
  })
_sym_db.RegisterMessage(SpeedOffsetConfig)

LASConfig = _reflection.GeneratedProtocolMessageType('LASConfig', (_message.Message,), {
  'DESCRIPTOR' : _LASCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.LASConfig)
  })
_sym_db.RegisterMessage(LASConfig)

AVMConfig = _reflection.GeneratedProtocolMessageType('AVMConfig', (_message.Message,), {
  'DESCRIPTOR' : _AVMCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.AVMConfig)
  })
_sym_db.RegisterMessage(AVMConfig)

AVMDrivingConfig = _reflection.GeneratedProtocolMessageType('AVMDrivingConfig', (_message.Message,), {
  'DESCRIPTOR' : _AVMDRIVINGCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.AVMDrivingConfig)
  })
_sym_db.RegisterMessage(AVMDrivingConfig)

TJPConfig = _reflection.GeneratedProtocolMessageType('TJPConfig', (_message.Message,), {
  'DESCRIPTOR' : _TJPCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.TJPConfig)
  })
_sym_db.RegisterMessage(TJPConfig)

APAConfig = _reflection.GeneratedProtocolMessageType('APAConfig', (_message.Message,), {
  'DESCRIPTOR' : _APACONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.APAConfig)
  })
_sym_db.RegisterMessage(APAConfig)

RPAConfig = _reflection.GeneratedProtocolMessageType('RPAConfig', (_message.Message,), {
  'DESCRIPTOR' : _RPACONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.RPAConfig)
  })
_sym_db.RegisterMessage(RPAConfig)

HUTConfig = _reflection.GeneratedProtocolMessageType('HUTConfig', (_message.Message,), {
  'DESCRIPTOR' : _HUTCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.HUTConfig)
  })
_sym_db.RegisterMessage(HUTConfig)

E2EConfig = _reflection.GeneratedProtocolMessageType('E2EConfig', (_message.Message,), {
  'DESCRIPTOR' : _E2ECONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.E2EConfig)
  })
_sym_db.RegisterMessage(E2EConfig)

CMSConfig = _reflection.GeneratedProtocolMessageType('CMSConfig', (_message.Message,), {
  'DESCRIPTOR' : _CMSCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.CMSConfig)
  })
_sym_db.RegisterMessage(CMSConfig)

NCAODDTypeLimitConfig = _reflection.GeneratedProtocolMessageType('NCAODDTypeLimitConfig', (_message.Message,), {
  'DESCRIPTOR' : _NCAODDTYPELIMITCONFIG,
  '__module__' : 'drapi.local_config_pb2'
  # @@protoc_insertion_point(class_scope:dr.localconfig.NCAODDTypeLimitConfig)
  })
_sym_db.RegisterMessage(NCAODDTypeLimitConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SWITCHSTATUS._serialized_start=6985
  _SWITCHSTATUS._serialized_end=7057
  _DRIVINGSTYLE._serialized_start=7059
  _DRIVINGSTYLE._serialized_end=7143
  _ACCELERATIONSTYLE._serialized_start=7146
  _ACCELERATIONSTYLE._serialized_end=7278
  _NAVIGATIONMODE._serialized_start=7280
  _NAVIGATIONMODE._serialized_end=7355
  _LANECHANGESNVTY._serialized_start=7357
  _LANECHANGESNVTY._serialized_end=7460
  _HANDSOFFTIMESET._serialized_start=7462
  _HANDSOFFTIMESET._serialized_end=7541
  _WHEELVIESTSTYPE._serialized_start=7544
  _WHEELVIESTSTYPE._serialized_end=7683
  _USERCONFIG._serialized_start=73
  _USERCONFIG._serialized_end=2984
  _ACCCONFIG._serialized_start=2987
  _ACCCONFIG._serialized_end=3245
  _ICACONFIG._serialized_start=3248
  _ICACONFIG._serialized_end=3659
  _NCACONFIG._serialized_start=3662
  _NCACONFIG._serialized_end=4099
  _NCAODDCONFIG._serialized_start=4101
  _NCAODDCONFIG._serialized_end=4169
  _SPEEDOFFSETCONFIG._serialized_start=4171
  _SPEEDOFFSETCONFIG._serialized_end=4295
  _SPEEDOFFSETCONFIG_TYPE._serialized_start=4262
  _SPEEDOFFSETCONFIG_TYPE._serialized_end=4295
  _LASCONFIG._serialized_start=4298
  _LASCONFIG._serialized_end=4691
  _LASCONFIG_LASSWITCH._serialized_start=4549
  _LASCONFIG_LASSWITCH._serialized_end=4628
  _LASCONFIG_MUTEKEYCONFIG._serialized_start=4630
  _LASCONFIG_MUTEKEYCONFIG._serialized_end=4691
  _AVMCONFIG._serialized_start=4694
  _AVMCONFIG._serialized_end=5865
  _AVMCONFIG_NARROWPATHANDOBSTACLEASSIST._serialized_start=5587
  _AVMCONFIG_NARROWPATHANDOBSTACLEASSIST._serialized_end=5675
  _AVMCONFIG_AVMSPEEDLIMIT._serialized_start=5677
  _AVMCONFIG_AVMSPEEDLIMIT._serialized_end=5761
  _AVMCONFIG_AVMTURNMODE._serialized_start=5763
  _AVMCONFIG_AVMTURNMODE._serialized_end=5865
  _AVMDRIVINGCONFIG._serialized_start=5868
  _AVMDRIVINGCONFIG._serialized_end=6054
  _AVMDRIVINGCONFIG_AVMSTYLE._serialized_start=6000
  _AVMDRIVINGCONFIG_AVMSTYLE._serialized_end=6054
  _TJPCONFIG._serialized_start=6056
  _TJPCONFIG._serialized_end=6127
  _APACONFIG._serialized_start=6130
  _APACONFIG._serialized_end=6415
  _APACONFIG_APAPARKINGSPEED._serialized_start=6367
  _APACONFIG_APAPARKINGSPEED._serialized_end=6415
  _RPACONFIG._serialized_start=6417
  _RPACONFIG._serialized_end=6488
  _HUTCONFIG._serialized_start=6490
  _HUTCONFIG._serialized_end=6601
  _E2ECONFIG._serialized_start=6603
  _E2ECONFIG._serialized_end=6664
  _CMSCONFIG._serialized_start=6666
  _CMSCONFIG._serialized_end=6734
  _NCAODDTYPELIMITCONFIG._serialized_start=6737
  _NCAODDTYPELIMITCONFIG._serialized_end=6983
# @@protoc_insertion_point(module_scope)
