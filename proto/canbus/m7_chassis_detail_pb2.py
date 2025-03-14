# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: canbus/m7_chassis_detail.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63\x61nbus/m7_chassis_detail.proto\x12\x10\x64\x65\x65proute.canbus\"\x9d\x03\n\x0fM7ChassisDetail\x12*\n\x07\x65ps_180\x18\x01 \x01(\x0b\x32\x19.deeproute.canbus.EPS_180\x12*\n\x07\x65sp_1f8\x18\x02 \x01(\x0b\x32\x19.deeproute.canbus.ESP_1F8\x12*\n\x07\x65sp_1fa\x18\x03 \x01(\x0b\x32\x19.deeproute.canbus.ESP_1FA\x12*\n\x07\x65sp_1b4\x18\x04 \x01(\x0b\x32\x19.deeproute.canbus.ESP_1B4\x12@\n\x12vcu_state_cha1_3a1\x18\x05 \x01(\x0b\x32$.deeproute.canbus.VCU_state_Cha1_3A1\x12@\n\x12vcu_state_cha2_185\x18\x06 \x01(\x0b\x32$.deeproute.canbus.VCU_state_Cha2_185\x12*\n\x07plg_382\x18\x07 \x01(\x0b\x32\x19.deeproute.canbus.PLG_382\x12*\n\x07\x65sp_1c2\x18\x08 \x01(\x0b\x32\x19.deeproute.canbus.ESP_1C2\"\xd1\x06\n\x07\x45PS_180\x12\x43\n\x13\x65ps_lka_ctrl_status\x18\x01 \x01(\x0e\x32&.deeproute.canbus.EPS_180.EpsLkaCtrSts\x12G\n\x13\x65ps_apa_control_sts\x18\x02 \x01(\x0e\x32*.deeproute.canbus.EPS_180.EpsApaControlSts\x12O\n\x19\x65ps_apa_control_fault_sts\x18\x03 \x01(\x0e\x32,.deeproute.canbus.EPS_180.ApaControlFaultSts\x12=\n\x0f\x65ps_mode_status\x18\x04 \x01(\x0e\x32$.deeproute.canbus.EPS_180.EpsModeSts\"r\n\x0c\x45psLkaCtrSts\x12\x0e\n\nNO_REQUEST\x10\x00\x12\x13\n\x0fREQUEST_HONORED\x10\x01\x12\x1b\n\x17REQUEST_NOT_ALLOWEDTEMP\x10\x02\x12 \n\x1cREQUEST_NOT_ALLOWEDPERMANENT\x10\x03\"z\n\x10\x45psApaControlSts\x12\x0f\n\x0b\x41PA_STANDBY\x10\x00\x12\x19\n\x15REPLY_FOR_CONTROL_EPS\x10\x01\x12\x0e\n\nAPA_ACTIVE\x10\x02\x12\r\n\tAPA_ABORT\x10\x03\x12\x1b\n\x17\x45PS_APA_CONTROL_FAILURE\x10\x07\"\xf2\x01\n\x12\x41paControlFaultSts\x12\x18\n\x14\x41PA_NORMAL_OPERATION\x10\x00\x12$\n EPS_INTERNAL_RECOVERABLE_FAILURE\x10\x01\x12\x13\n\x0f\x41\x42NORMAL_SIGNAL\x10\x02\x12\r\n\tOVERSPEED\x10\x03\x12\x17\n\x13\x44RIVER_INTERFERENCE\x10\x04\x12\x1a\n\x16\x45XCESS_ANGLE_DEVIATION\x10\x05\x12\x18\n\x14\x41\x42NORMAL_APA_REQUEST\x10\x06\x12\x14\n\x10\x41PA_LOW_PRIORITY\x10\x07\x12\x13\n\x0f\x41PA_EPS_FAILURE\x10\x0f\"C\n\nEpsModeSts\x12\x0f\n\x0bUNAVAILABLE\x10\x00\x12\x0c\n\x08RESERVED\x10\x01\x12\x0b\n\x07\x43OMFORT\x10\x02\x12\t\n\x05SPORT\x10\x03\"\xae\n\n\x07\x45SP_1F8\x12R\n\x1a\x65sp_emergency_brake_status\x18\x01 \x01(\x0e\x32..deeproute.canbus.ESP_1F8.EspEmergencyBrakeSts\x12\x44\n\x11\x65sp_hdc_available\x18\x02 \x01(\x0e\x32).deeproute.canbus.ESP_1F8.EspHdcAvailable\x12>\n\x0e\x65sp_dtc_active\x18\x03 \x01(\x0e\x32&.deeproute.canbus.ESP_1F8.EspDtcActive\x12<\n\resp_esp_fault\x18\x04 \x01(\x0e\x32%.deeproute.canbus.ESP_1F8.EspEspFault\x12<\n\resp_ebd_fault\x18\x05 \x01(\x0e\x32%.deeproute.canbus.ESP_1F8.EspEbdFault\x12;\n\x0e\x65sp_hdc_status\x18\x06 \x01(\x0e\x32#.deeproute.canbus.ESP_1F8.EspHdcSts\x12\x44\n\x11\x65sp_avh_available\x18\x07 \x01(\x0e\x32).deeproute.canbus.ESP_1F8.EspAvhAvailable\x12@\n\x0f\x65sp_avh_standby\x18\x08 \x01(\x0e\x32\'.deeproute.canbus.ESP_1F8.EspAvhStandby\x12>\n\x0e\x65sp_avh_status\x18\t \x01(\x0e\x32&.deeproute.canbus.ESP_1F8.EspAvhStatus\x12>\n\x0e\x65sp_abs_active\x18\n \x01(\x0e\x32&.deeproute.canbus.ESP_1F8.EspAbsActive\x12<\n\resp_abs_fault\x18\x0b \x01(\x0e\x32%.deeproute.canbus.ESP_1F8.EspAbsFault\"2\n\x14\x45spEmergencyBrakeSts\x12\x0e\n\nNO_REQUEST\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\";\n\x0f\x45spHdcAvailable\x12\x15\n\x11HDC_NOT_AVAILABLE\x10\x00\x12\x11\n\rHDC_AVAILABLE\x10\x01\"0\n\x0c\x45spDtcActive\x12\x10\n\x0c\x44TC_INACTIVE\x10\x00\x12\x0e\n\nDTC_ACTIVE\x10\x01\",\n\x0b\x45spEspFault\x12\x0e\n\nESP_NORMAL\x10\x00\x12\r\n\tESP_FAULT\x10\x01\",\n\x0b\x45spEbdFault\x12\x0e\n\nEBD_NORMAL\x10\x00\x12\r\n\tEBD_FAULT\x10\x01\"E\n\tEspHdcSts\x12\x0f\n\x0bHDC_STS_OFF\x10\x00\x12\x13\n\x0fHDC_STS_STANDBY\x10\x01\x12\x12\n\x0eHDC_STS_ACTIVE\x10\x02\";\n\x0f\x45spAvhAvailable\x12\x15\n\x11\x41VH_NOT_AVAILABLE\x10\x00\x12\x11\n\rAVH_AVAILABLE\x10\x01\"5\n\rEspAvhStandby\x12\x13\n\x0f\x41VH_NOT_STANDBY\x10\x00\x12\x0f\n\x0b\x41VH_STANDBY\x10\x01\"0\n\x0c\x45spAvhStatus\x12\x10\n\x0c\x41VH_INACTIVE\x10\x00\x12\x0e\n\nAVH_ACTIVE\x10\x01\"0\n\x0c\x45spAbsActive\x12\x10\n\x0c\x41\x42S_INACTIVE\x10\x00\x12\x0e\n\nABS_ACTIVE\x10\x01\",\n\x0b\x45spAbsFault\x12\x0e\n\nABS_NORMAL\x10\x00\x12\r\n\tABS_FAULT\x10\x01\"\x90\t\n\x07\x45SP_1FA\x12<\n\resp_tcs_fault\x18\x01 \x01(\x0e\x32%.deeproute.canbus.ESP_1FA.EspTcsFault\x12<\n\resp_vdc_fault\x18\x02 \x01(\x0e\x32%.deeproute.canbus.ESP_1FA.EspVdcFault\x12=\n\x0e\x65sp_off_sw_sts\x18\x03 \x01(\x0e\x32%.deeproute.canbus.ESP_1FA.EspOffSwSts\x12\x44\n\x11\x65sp_hhc_available\x18\x04 \x01(\x0e\x32).deeproute.canbus.ESP_1FA.EspHhcAvailable\x12>\n\x0e\x65sp_hhc_active\x18\x05 \x01(\x0e\x32&.deeproute.canbus.ESP_1FA.EspHhcActive\x12\x44\n\x11\x65sp_cdp_available\x18\x06 \x01(\x0e\x32).deeproute.canbus.ESP_1FA.EspCdpAvailable\x12>\n\x0e\x65sp_vdc_active\x18\x07 \x01(\x0e\x32&.deeproute.canbus.ESP_1FA.EspVdcActive\x12>\n\x0e\x65sp_tcs_active\x18\x08 \x01(\x0e\x32&.deeproute.canbus.ESP_1FA.EspTcsActive\x12>\n\x0e\x65sp_esp_active\x18\t \x01(\x0e\x32&.deeproute.canbus.ESP_1FA.EspEspActive\x12>\n\x0e\x65sp_cdp_active\x18\n \x01(\x0e\x32&.deeproute.canbus.ESP_1FA.EspCdpActive\",\n\x0b\x45spTcsFault\x12\x0e\n\nTCS_NORMAL\x10\x00\x12\r\n\tTCS_FAULT\x10\x01\",\n\x0b\x45spVdcFault\x12\x0e\n\nVDC_NORMAL\x10\x00\x12\r\n\tVDC_FAULT\x10\x01\".\n\x0b\x45spOffSwSts\x12\x0f\n\x0b\x45SP_DISABLE\x10\x00\x12\x0e\n\nESP_ENABLE\x10\x01\";\n\x0f\x45spHhcAvailable\x12\x15\n\x11HHC_NOT_AVAILABLE\x10\x00\x12\x11\n\rHHC_AVAILABLE\x10\x01\"0\n\x0c\x45spHhcActive\x12\x10\n\x0cHHC_INACTIVE\x10\x00\x12\x0e\n\nHHC_ACTIVE\x10\x01\";\n\x0f\x45spCdpAvailable\x12\x15\n\x11\x43\x44P_NOT_AVAILABLE\x10\x00\x12\x11\n\rCDP_AVAILABLE\x10\x01\"0\n\x0c\x45spVdcActive\x12\x10\n\x0cVDC_INACTIVE\x10\x00\x12\x0e\n\nVDC_ACTIVE\x10\x01\"0\n\x0c\x45spTcsActive\x12\x10\n\x0cTCS_INACTIVE\x10\x00\x12\x0e\n\nTCS_ACTIVE\x10\x01\"0\n\x0c\x45spEspActive\x12\x10\n\x0c\x45SP_INACTIVE\x10\x00\x12\x0e\n\nESP_ACTIVE\x10\x01\"0\n\x0c\x45spCdpActive\x12\x10\n\x0c\x43\x44P_INACTIVE\x10\x00\x12\x0e\n\nCDP_ACTIVE\x10\x01\"\xaa\t\n\x07\x45SP_1B4\x12J\n\x15\x65sp_apa_long_ctrl_sts\x18\x01 \x01(\x0e\x32+.deeproute.canbus.ESP_1B4.EspApaLongCtrlSts\x12U\n\x1b\x65sp_apa_long_ctrl_fault_sts\x18\x02 \x01(\x0e\x32\x30.deeproute.canbus.ESP_1B4.EspApaLongCtrlFaultSts\x12]\n\x1f\x65sp_apa_long_ctrl_sts_available\x18\x03 \x01(\x0e\x32\x34.deeproute.canbus.ESP_1B4.EspApaLongCtrlStsAvailable\x12\x45\n\x12\x65sp_apa_cdd_active\x18\x04 \x01(\x0e\x32).deeproute.canbus.ESP_1B4.EspApaCddActive\x12\x41\n\x10\x65sp_apa_cdd_hold\x18\x05 \x01(\x0e\x32\'.deeproute.canbus.ESP_1B4.EspApaCddHold\x12\x44\n\x11\x65sp_vlc_available\x18\x06 \x01(\x0e\x32).deeproute.canbus.ESP_1B4.EspVlcAvailable\x12<\n\resp_vlc_error\x18\x07 \x01(\x0e\x32%.deeproute.canbus.ESP_1B4.EspVlcError\x12J\n\x14\x65sp_vlc_intervention\x18\x08 \x01(\x0e\x32,.deeproute.canbus.ESP_1B4.EspVlcIntervention\"T\n\x11\x45spApaLongCtrlSts\x12\x07\n\x03OFF\x10\x00\x12\x0b\n\x07STANDBY\x10\x01\x12\x19\n\x15\x41UTOMATIC_PARK_ACTIVE\x10\x02\x12\x0e\n\nCTRL_ERROR\x10\x07\"\xa7\x01\n\x16\x45spApaLongCtrlFaultSts\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x13\n\x0fVEHICLE_BLOCKED\x10\x01\x12\x1c\n\x18UNEXPECTED_GEAR_POSITION\x10\x02\x12\x19\n\x15UNEXPECTED_EPB_ACTION\x10\x03\x12 \n\x1cUNEXPECTED_GEAR_INTERVENTION\x10\x04\x12\x0f\n\x0b\x46\x41ULT_ERROR\x10\x07\"C\n\x1a\x45spApaLongCtrlStsAvailable\x12\x11\n\rNOT_AVAILABLE\x10\x00\x12\x12\n\x0e\x41UTOMATIC_PARK\x10\x01\"-\n\x0f\x45spApaCddActive\x12\x0e\n\nNOT_ACTIVE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\"\'\n\rEspApaCddHold\x12\x0c\n\x08NOT_HOLD\x10\x00\x12\x08\n\x04HOLD\x10\x01\";\n\x0f\x45spVlcAvailable\x12\x15\n\x11VLC_NOT_AVAILABLE\x10\x00\x12\x11\n\rVLC_AVAILABLE\x10\x01\"/\n\x0b\x45spVlcError\x12\x11\n\rVLC_NOT_ERROR\x10\x00\x12\r\n\tVLC_ERROR\x10\x01\"8\n\x12\x45spVlcIntervention\x12\x12\n\x0eVLC_NOT_ACTIVE\x10\x00\x12\x0e\n\nVLC_ACTIVE\x10\x01\"\xc4\x04\n\x12VCU_state_Cha1_3A1\x12I\n\x0evcu_drive_mode\x18\x01 \x01(\x0e\x32\x31.deeproute.canbus.VCU_state_Cha1_3A1.VcuDriveMode\x12K\n\x0fvcu_drive_ready\x18\x02 \x01(\x0e\x32\x32.deeproute.canbus.VCU_state_Cha1_3A1.VcuDriveReady\x12O\n\x11vcu_apa_available\x18\x03 \x01(\x0e\x32\x34.deeproute.canbus.VCU_state_Cha1_3A1.VcuApaAvailable\x12S\n\x13vcu_exhibition_mode\x18\x04 \x01(\x0e\x32\x36.deeproute.canbus.VCU_state_Cha1_3A1.VcuExhibitionMode\"O\n\x0cVcuDriveMode\x12\x08\n\x04SOFT\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x0c\n\x08POWERFUL\x10\x02\x12\x0b\n\x07\x46REEDOM\x10\x03\x12\x0e\n\nACCELERATE\x10\x04\":\n\rVcuDriveReady\x12\r\n\tNOT_READY\x10\x00\x12\x0f\n\x0bREADY_FLASH\x10\x01\x12\t\n\x05READY\x10\x02\"3\n\x0fVcuApaAvailable\x12\x11\n\rNOT_AVAILABLE\x10\x00\x12\r\n\tAVAILABLE\x10\x01\".\n\x11VcuExhibitionMode\x12\r\n\tNO_ACTIVE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\"\xd4\x03\n\x12VCU_state_Cha2_185\x12\x45\n\x0cvcu_tcm_fail\x18\x01 \x01(\x0e\x32/.deeproute.canbus.VCU_state_Cha2_185.VcuTcmfail\x12O\n\x11vcu_motor_running\x18\x02 \x01(\x0e\x32\x34.deeproute.canbus.VCU_state_Cha2_185.VcuMotorRunning\x12\x64\n\x1cvcu_acc_pedal_position_valid\x18\x03 \x01(\x0e\x32>.deeproute.canbus.VCU_state_Cha2_185.VcuAccPedalPosiotionValid\x12\x1e\n\x16vcu_acc_pedal_position\x18\x04 \x01(\x01\".\n\nVcuTcmfail\x12\x0e\n\nNORMAL_TCM\x10\x00\x12\x10\n\x0cLIMPHOME_TCM\x10\x01\";\n\x0fVcuMotorRunning\x12\x15\n\x11MOTOR_NOT_RUNNING\x10\x00\x12\x11\n\rMOTOR_RUNNING\x10\x01\"3\n\x19VcuAccPedalPosiotionValid\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05VALID\x10\x01\"\x85\x02\n\x07PLG_382\x12M\n\x16plg_tailgate_open_sts2\x18\x01 \x01(\x0e\x32-.deeproute.canbus.PLG_382.PlgTailGateOpenSts2\"\xaa\x01\n\x13PlgTailGateOpenSts2\x12\n\n\x06\x43LOSED\x10\x00\x12\n\n\x06OPENED\x10\x01\x12\x0b\n\x07\x43LOSING\x10\x02\x12\x0b\n\x07OPENING\x10\x03\x12\x0b\n\x07STOPPED\x10\x04\x12\x19\n\x15\x43LOSED_NOT_COMPLETELY\x10\x05\x12\x0b\n\x07LOCKING\x10\x06\x12\r\n\tUNLOCKING\x10\x07\x12\x1d\n\x19\x46ORCE_TO_OPEN_TO_THE_AREA\x10\x08\"\xb3\x0b\n\x07\x45SP_1C2\x12\x41\n\x10\x65sp_cdd_temp_off\x18\x01 \x01(\x0e\x32\'.deeproute.canbus.ESP_1C2.EspCddTempOff\x12<\n\resp_cdd_error\x18\x02 \x01(\x0e\x32%.deeproute.canbus.ESP_1C2.EspCddError\x12>\n\x0e\x65sp_cdd_active\x18\x03 \x01(\x0e\x32&.deeproute.canbus.ESP_1C2.EspCddActive\x12\x44\n\x11\x65sp_cdd_available\x18\x04 \x01(\x0e\x32).deeproute.canbus.ESP_1C2.EspCddAvailable\x12>\n\x0e\x65sp_aba_active\x18\x05 \x01(\x0e\x32&.deeproute.canbus.ESP_1C2.EspAbaActive\x12\x44\n\x11\x65sp_aba_available\x18\x06 \x01(\x0e\x32).deeproute.canbus.ESP_1C2.EspAbaAvailable\x12>\n\x0e\x65sp_abp_active\x18\x07 \x01(\x0e\x32&.deeproute.canbus.ESP_1C2.EspAbpActive\x12\x44\n\x11\x65sp_abp_available\x18\x08 \x01(\x0e\x32).deeproute.canbus.ESP_1C2.EspAbpAvailable\x12>\n\x0e\x65sp_aeb_active\x18\t \x01(\x0e\x32&.deeproute.canbus.ESP_1C2.EspAebActive\x12\x44\n\x11\x65sp_aeb_available\x18\n \x01(\x0e\x32).deeproute.canbus.ESP_1C2.EspAebAvailable\x12>\n\x0e\x65sp_awb_active\x18\x0b \x01(\x0e\x32&.deeproute.canbus.ESP_1C2.EspAwbActive\x12\x44\n\x11\x65sp_awb_available\x18\x0c \x01(\x0e\x32).deeproute.canbus.ESP_1C2.EspAwbAvailable\"+\n\rEspCddTempOff\x12\x0c\n\x08NOT_HIGH\x10\x00\x12\x0c\n\x08TOO_HIGH\x10\x01\"\'\n\x0b\x45spCddError\x12\r\n\tNOT_ERROR\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"2\n\x0c\x45spCddActive\x12\x12\n\x0e\x43\x44\x44_NOT_ACTIVE\x10\x00\x12\x0e\n\nCDD_ACTIVE\x10\x01\";\n\x0f\x45spCddAvailable\x12\x15\n\x11\x43\x44\x44_NOT_AVAILABLE\x10\x00\x12\x11\n\rCDD_AVAILABLE\x10\x01\"2\n\x0c\x45spAbaActive\x12\x12\n\x0e\x41\x42\x41_NOT_ACTIVE\x10\x00\x12\x0e\n\nABA_ACTIVE\x10\x01\";\n\x0f\x45spAbaAvailable\x12\x15\n\x11\x41\x42\x41_NOT_AVAILABLE\x10\x00\x12\x11\n\rABA_AVAILABLE\x10\x01\"2\n\x0c\x45spAbpActive\x12\x12\n\x0e\x41\x42P_NOT_ACTIVE\x10\x00\x12\x0e\n\nABP_ACTIVE\x10\x01\";\n\x0f\x45spAbpAvailable\x12\x15\n\x11\x41\x42P_NOT_AVAILABLE\x10\x00\x12\x11\n\rABP_AVAILABLE\x10\x01\"2\n\x0c\x45spAebActive\x12\x12\n\x0e\x41\x45\x42_NOT_ACTIVE\x10\x00\x12\x0e\n\nAEB_ACTIVE\x10\x01\";\n\x0f\x45spAebAvailable\x12\x15\n\x11\x41\x45\x42_NOT_AVAILABLE\x10\x00\x12\x11\n\rAEB_AVAILABLE\x10\x01\"2\n\x0c\x45spAwbActive\x12\x12\n\x0e\x41WB_NOT_ACTIVE\x10\x00\x12\x0e\n\nAWB_ACTIVE\x10\x01\";\n\x0f\x45spAwbAvailable\x12\x15\n\x11\x41WB_NOT_AVAILABLE\x10\x00\x12\x11\n\rAWB_AVAILABLE\x10\x01')



_M7CHASSISDETAIL = DESCRIPTOR.message_types_by_name['M7ChassisDetail']
_EPS_180 = DESCRIPTOR.message_types_by_name['EPS_180']
_ESP_1F8 = DESCRIPTOR.message_types_by_name['ESP_1F8']
_ESP_1FA = DESCRIPTOR.message_types_by_name['ESP_1FA']
_ESP_1B4 = DESCRIPTOR.message_types_by_name['ESP_1B4']
_VCU_STATE_CHA1_3A1 = DESCRIPTOR.message_types_by_name['VCU_state_Cha1_3A1']
_VCU_STATE_CHA2_185 = DESCRIPTOR.message_types_by_name['VCU_state_Cha2_185']
_PLG_382 = DESCRIPTOR.message_types_by_name['PLG_382']
_ESP_1C2 = DESCRIPTOR.message_types_by_name['ESP_1C2']
_EPS_180_EPSLKACTRSTS = _EPS_180.enum_types_by_name['EpsLkaCtrSts']
_EPS_180_EPSAPACONTROLSTS = _EPS_180.enum_types_by_name['EpsApaControlSts']
_EPS_180_APACONTROLFAULTSTS = _EPS_180.enum_types_by_name['ApaControlFaultSts']
_EPS_180_EPSMODESTS = _EPS_180.enum_types_by_name['EpsModeSts']
_ESP_1F8_ESPEMERGENCYBRAKESTS = _ESP_1F8.enum_types_by_name['EspEmergencyBrakeSts']
_ESP_1F8_ESPHDCAVAILABLE = _ESP_1F8.enum_types_by_name['EspHdcAvailable']
_ESP_1F8_ESPDTCACTIVE = _ESP_1F8.enum_types_by_name['EspDtcActive']
_ESP_1F8_ESPESPFAULT = _ESP_1F8.enum_types_by_name['EspEspFault']
_ESP_1F8_ESPEBDFAULT = _ESP_1F8.enum_types_by_name['EspEbdFault']
_ESP_1F8_ESPHDCSTS = _ESP_1F8.enum_types_by_name['EspHdcSts']
_ESP_1F8_ESPAVHAVAILABLE = _ESP_1F8.enum_types_by_name['EspAvhAvailable']
_ESP_1F8_ESPAVHSTANDBY = _ESP_1F8.enum_types_by_name['EspAvhStandby']
_ESP_1F8_ESPAVHSTATUS = _ESP_1F8.enum_types_by_name['EspAvhStatus']
_ESP_1F8_ESPABSACTIVE = _ESP_1F8.enum_types_by_name['EspAbsActive']
_ESP_1F8_ESPABSFAULT = _ESP_1F8.enum_types_by_name['EspAbsFault']
_ESP_1FA_ESPTCSFAULT = _ESP_1FA.enum_types_by_name['EspTcsFault']
_ESP_1FA_ESPVDCFAULT = _ESP_1FA.enum_types_by_name['EspVdcFault']
_ESP_1FA_ESPOFFSWSTS = _ESP_1FA.enum_types_by_name['EspOffSwSts']
_ESP_1FA_ESPHHCAVAILABLE = _ESP_1FA.enum_types_by_name['EspHhcAvailable']
_ESP_1FA_ESPHHCACTIVE = _ESP_1FA.enum_types_by_name['EspHhcActive']
_ESP_1FA_ESPCDPAVAILABLE = _ESP_1FA.enum_types_by_name['EspCdpAvailable']
_ESP_1FA_ESPVDCACTIVE = _ESP_1FA.enum_types_by_name['EspVdcActive']
_ESP_1FA_ESPTCSACTIVE = _ESP_1FA.enum_types_by_name['EspTcsActive']
_ESP_1FA_ESPESPACTIVE = _ESP_1FA.enum_types_by_name['EspEspActive']
_ESP_1FA_ESPCDPACTIVE = _ESP_1FA.enum_types_by_name['EspCdpActive']
_ESP_1B4_ESPAPALONGCTRLSTS = _ESP_1B4.enum_types_by_name['EspApaLongCtrlSts']
_ESP_1B4_ESPAPALONGCTRLFAULTSTS = _ESP_1B4.enum_types_by_name['EspApaLongCtrlFaultSts']
_ESP_1B4_ESPAPALONGCTRLSTSAVAILABLE = _ESP_1B4.enum_types_by_name['EspApaLongCtrlStsAvailable']
_ESP_1B4_ESPAPACDDACTIVE = _ESP_1B4.enum_types_by_name['EspApaCddActive']
_ESP_1B4_ESPAPACDDHOLD = _ESP_1B4.enum_types_by_name['EspApaCddHold']
_ESP_1B4_ESPVLCAVAILABLE = _ESP_1B4.enum_types_by_name['EspVlcAvailable']
_ESP_1B4_ESPVLCERROR = _ESP_1B4.enum_types_by_name['EspVlcError']
_ESP_1B4_ESPVLCINTERVENTION = _ESP_1B4.enum_types_by_name['EspVlcIntervention']
_VCU_STATE_CHA1_3A1_VCUDRIVEMODE = _VCU_STATE_CHA1_3A1.enum_types_by_name['VcuDriveMode']
_VCU_STATE_CHA1_3A1_VCUDRIVEREADY = _VCU_STATE_CHA1_3A1.enum_types_by_name['VcuDriveReady']
_VCU_STATE_CHA1_3A1_VCUAPAAVAILABLE = _VCU_STATE_CHA1_3A1.enum_types_by_name['VcuApaAvailable']
_VCU_STATE_CHA1_3A1_VCUEXHIBITIONMODE = _VCU_STATE_CHA1_3A1.enum_types_by_name['VcuExhibitionMode']
_VCU_STATE_CHA2_185_VCUTCMFAIL = _VCU_STATE_CHA2_185.enum_types_by_name['VcuTcmfail']
_VCU_STATE_CHA2_185_VCUMOTORRUNNING = _VCU_STATE_CHA2_185.enum_types_by_name['VcuMotorRunning']
_VCU_STATE_CHA2_185_VCUACCPEDALPOSIOTIONVALID = _VCU_STATE_CHA2_185.enum_types_by_name['VcuAccPedalPosiotionValid']
_PLG_382_PLGTAILGATEOPENSTS2 = _PLG_382.enum_types_by_name['PlgTailGateOpenSts2']
_ESP_1C2_ESPCDDTEMPOFF = _ESP_1C2.enum_types_by_name['EspCddTempOff']
_ESP_1C2_ESPCDDERROR = _ESP_1C2.enum_types_by_name['EspCddError']
_ESP_1C2_ESPCDDACTIVE = _ESP_1C2.enum_types_by_name['EspCddActive']
_ESP_1C2_ESPCDDAVAILABLE = _ESP_1C2.enum_types_by_name['EspCddAvailable']
_ESP_1C2_ESPABAACTIVE = _ESP_1C2.enum_types_by_name['EspAbaActive']
_ESP_1C2_ESPABAAVAILABLE = _ESP_1C2.enum_types_by_name['EspAbaAvailable']
_ESP_1C2_ESPABPACTIVE = _ESP_1C2.enum_types_by_name['EspAbpActive']
_ESP_1C2_ESPABPAVAILABLE = _ESP_1C2.enum_types_by_name['EspAbpAvailable']
_ESP_1C2_ESPAEBACTIVE = _ESP_1C2.enum_types_by_name['EspAebActive']
_ESP_1C2_ESPAEBAVAILABLE = _ESP_1C2.enum_types_by_name['EspAebAvailable']
_ESP_1C2_ESPAWBACTIVE = _ESP_1C2.enum_types_by_name['EspAwbActive']
_ESP_1C2_ESPAWBAVAILABLE = _ESP_1C2.enum_types_by_name['EspAwbAvailable']
M7ChassisDetail = _reflection.GeneratedProtocolMessageType('M7ChassisDetail', (_message.Message,), {
  'DESCRIPTOR' : _M7CHASSISDETAIL,
  '__module__' : 'canbus.m7_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.M7ChassisDetail)
  })
_sym_db.RegisterMessage(M7ChassisDetail)

EPS_180 = _reflection.GeneratedProtocolMessageType('EPS_180', (_message.Message,), {
  'DESCRIPTOR' : _EPS_180,
  '__module__' : 'canbus.m7_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.EPS_180)
  })
_sym_db.RegisterMessage(EPS_180)

ESP_1F8 = _reflection.GeneratedProtocolMessageType('ESP_1F8', (_message.Message,), {
  'DESCRIPTOR' : _ESP_1F8,
  '__module__' : 'canbus.m7_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.ESP_1F8)
  })
_sym_db.RegisterMessage(ESP_1F8)

ESP_1FA = _reflection.GeneratedProtocolMessageType('ESP_1FA', (_message.Message,), {
  'DESCRIPTOR' : _ESP_1FA,
  '__module__' : 'canbus.m7_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.ESP_1FA)
  })
_sym_db.RegisterMessage(ESP_1FA)

ESP_1B4 = _reflection.GeneratedProtocolMessageType('ESP_1B4', (_message.Message,), {
  'DESCRIPTOR' : _ESP_1B4,
  '__module__' : 'canbus.m7_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.ESP_1B4)
  })
_sym_db.RegisterMessage(ESP_1B4)

VCU_state_Cha1_3A1 = _reflection.GeneratedProtocolMessageType('VCU_state_Cha1_3A1', (_message.Message,), {
  'DESCRIPTOR' : _VCU_STATE_CHA1_3A1,
  '__module__' : 'canbus.m7_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.VCU_state_Cha1_3A1)
  })
_sym_db.RegisterMessage(VCU_state_Cha1_3A1)

VCU_state_Cha2_185 = _reflection.GeneratedProtocolMessageType('VCU_state_Cha2_185', (_message.Message,), {
  'DESCRIPTOR' : _VCU_STATE_CHA2_185,
  '__module__' : 'canbus.m7_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.VCU_state_Cha2_185)
  })
_sym_db.RegisterMessage(VCU_state_Cha2_185)

PLG_382 = _reflection.GeneratedProtocolMessageType('PLG_382', (_message.Message,), {
  'DESCRIPTOR' : _PLG_382,
  '__module__' : 'canbus.m7_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.PLG_382)
  })
_sym_db.RegisterMessage(PLG_382)

ESP_1C2 = _reflection.GeneratedProtocolMessageType('ESP_1C2', (_message.Message,), {
  'DESCRIPTOR' : _ESP_1C2,
  '__module__' : 'canbus.m7_chassis_detail_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.canbus.ESP_1C2)
  })
_sym_db.RegisterMessage(ESP_1C2)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _M7CHASSISDETAIL._serialized_start=53
  _M7CHASSISDETAIL._serialized_end=466
  _EPS_180._serialized_start=469
  _EPS_180._serialized_end=1318
  _EPS_180_EPSLKACTRSTS._serialized_start=766
  _EPS_180_EPSLKACTRSTS._serialized_end=880
  _EPS_180_EPSAPACONTROLSTS._serialized_start=882
  _EPS_180_EPSAPACONTROLSTS._serialized_end=1004
  _EPS_180_APACONTROLFAULTSTS._serialized_start=1007
  _EPS_180_APACONTROLFAULTSTS._serialized_end=1249
  _EPS_180_EPSMODESTS._serialized_start=1251
  _EPS_180_EPSMODESTS._serialized_end=1318
  _ESP_1F8._serialized_start=1321
  _ESP_1F8._serialized_end=2647
  _ESP_1F8_ESPEMERGENCYBRAKESTS._serialized_start=2061
  _ESP_1F8_ESPEMERGENCYBRAKESTS._serialized_end=2111
  _ESP_1F8_ESPHDCAVAILABLE._serialized_start=2113
  _ESP_1F8_ESPHDCAVAILABLE._serialized_end=2172
  _ESP_1F8_ESPDTCACTIVE._serialized_start=2174
  _ESP_1F8_ESPDTCACTIVE._serialized_end=2222
  _ESP_1F8_ESPESPFAULT._serialized_start=2224
  _ESP_1F8_ESPESPFAULT._serialized_end=2268
  _ESP_1F8_ESPEBDFAULT._serialized_start=2270
  _ESP_1F8_ESPEBDFAULT._serialized_end=2314
  _ESP_1F8_ESPHDCSTS._serialized_start=2316
  _ESP_1F8_ESPHDCSTS._serialized_end=2385
  _ESP_1F8_ESPAVHAVAILABLE._serialized_start=2387
  _ESP_1F8_ESPAVHAVAILABLE._serialized_end=2446
  _ESP_1F8_ESPAVHSTANDBY._serialized_start=2448
  _ESP_1F8_ESPAVHSTANDBY._serialized_end=2501
  _ESP_1F8_ESPAVHSTATUS._serialized_start=2503
  _ESP_1F8_ESPAVHSTATUS._serialized_end=2551
  _ESP_1F8_ESPABSACTIVE._serialized_start=2553
  _ESP_1F8_ESPABSACTIVE._serialized_end=2601
  _ESP_1F8_ESPABSFAULT._serialized_start=2603
  _ESP_1F8_ESPABSFAULT._serialized_end=2647
  _ESP_1FA._serialized_start=2650
  _ESP_1FA._serialized_end=3818
  _ESP_1FA_ESPTCSFAULT._serialized_start=3308
  _ESP_1FA_ESPTCSFAULT._serialized_end=3352
  _ESP_1FA_ESPVDCFAULT._serialized_start=3354
  _ESP_1FA_ESPVDCFAULT._serialized_end=3398
  _ESP_1FA_ESPOFFSWSTS._serialized_start=3400
  _ESP_1FA_ESPOFFSWSTS._serialized_end=3446
  _ESP_1FA_ESPHHCAVAILABLE._serialized_start=3448
  _ESP_1FA_ESPHHCAVAILABLE._serialized_end=3507
  _ESP_1FA_ESPHHCACTIVE._serialized_start=3509
  _ESP_1FA_ESPHHCACTIVE._serialized_end=3557
  _ESP_1FA_ESPCDPAVAILABLE._serialized_start=3559
  _ESP_1FA_ESPCDPAVAILABLE._serialized_end=3618
  _ESP_1FA_ESPVDCACTIVE._serialized_start=3620
  _ESP_1FA_ESPVDCACTIVE._serialized_end=3668
  _ESP_1FA_ESPTCSACTIVE._serialized_start=3670
  _ESP_1FA_ESPTCSACTIVE._serialized_end=3718
  _ESP_1FA_ESPESPACTIVE._serialized_start=3720
  _ESP_1FA_ESPESPACTIVE._serialized_end=3768
  _ESP_1FA_ESPCDPACTIVE._serialized_start=3770
  _ESP_1FA_ESPCDPACTIVE._serialized_end=3818
  _ESP_1B4._serialized_start=3821
  _ESP_1B4._serialized_end=5015
  _ESP_1B4_ESPAPALONGCTRLSTS._serialized_start=4436
  _ESP_1B4_ESPAPALONGCTRLSTS._serialized_end=4520
  _ESP_1B4_ESPAPALONGCTRLFAULTSTS._serialized_start=4523
  _ESP_1B4_ESPAPALONGCTRLFAULTSTS._serialized_end=4690
  _ESP_1B4_ESPAPALONGCTRLSTSAVAILABLE._serialized_start=4692
  _ESP_1B4_ESPAPALONGCTRLSTSAVAILABLE._serialized_end=4759
  _ESP_1B4_ESPAPACDDACTIVE._serialized_start=4761
  _ESP_1B4_ESPAPACDDACTIVE._serialized_end=4806
  _ESP_1B4_ESPAPACDDHOLD._serialized_start=4808
  _ESP_1B4_ESPAPACDDHOLD._serialized_end=4847
  _ESP_1B4_ESPVLCAVAILABLE._serialized_start=4849
  _ESP_1B4_ESPVLCAVAILABLE._serialized_end=4908
  _ESP_1B4_ESPVLCERROR._serialized_start=4910
  _ESP_1B4_ESPVLCERROR._serialized_end=4957
  _ESP_1B4_ESPVLCINTERVENTION._serialized_start=4959
  _ESP_1B4_ESPVLCINTERVENTION._serialized_end=5015
  _VCU_STATE_CHA1_3A1._serialized_start=5018
  _VCU_STATE_CHA1_3A1._serialized_end=5598
  _VCU_STATE_CHA1_3A1_VCUDRIVEMODE._serialized_start=5358
  _VCU_STATE_CHA1_3A1_VCUDRIVEMODE._serialized_end=5437
  _VCU_STATE_CHA1_3A1_VCUDRIVEREADY._serialized_start=5439
  _VCU_STATE_CHA1_3A1_VCUDRIVEREADY._serialized_end=5497
  _VCU_STATE_CHA1_3A1_VCUAPAAVAILABLE._serialized_start=5499
  _VCU_STATE_CHA1_3A1_VCUAPAAVAILABLE._serialized_end=5550
  _VCU_STATE_CHA1_3A1_VCUEXHIBITIONMODE._serialized_start=5552
  _VCU_STATE_CHA1_3A1_VCUEXHIBITIONMODE._serialized_end=5598
  _VCU_STATE_CHA2_185._serialized_start=5601
  _VCU_STATE_CHA2_185._serialized_end=6069
  _VCU_STATE_CHA2_185_VCUTCMFAIL._serialized_start=5909
  _VCU_STATE_CHA2_185_VCUTCMFAIL._serialized_end=5955
  _VCU_STATE_CHA2_185_VCUMOTORRUNNING._serialized_start=5957
  _VCU_STATE_CHA2_185_VCUMOTORRUNNING._serialized_end=6016
  _VCU_STATE_CHA2_185_VCUACCPEDALPOSIOTIONVALID._serialized_start=6018
  _VCU_STATE_CHA2_185_VCUACCPEDALPOSIOTIONVALID._serialized_end=6069
  _PLG_382._serialized_start=6072
  _PLG_382._serialized_end=6333
  _PLG_382_PLGTAILGATEOPENSTS2._serialized_start=6163
  _PLG_382_PLGTAILGATEOPENSTS2._serialized_end=6333
  _ESP_1C2._serialized_start=6336
  _ESP_1C2._serialized_end=7795
  _ESP_1C2_ESPCDDTEMPOFF._serialized_start=7146
  _ESP_1C2_ESPCDDTEMPOFF._serialized_end=7189
  _ESP_1C2_ESPCDDERROR._serialized_start=7191
  _ESP_1C2_ESPCDDERROR._serialized_end=7230
  _ESP_1C2_ESPCDDACTIVE._serialized_start=7232
  _ESP_1C2_ESPCDDACTIVE._serialized_end=7282
  _ESP_1C2_ESPCDDAVAILABLE._serialized_start=7284
  _ESP_1C2_ESPCDDAVAILABLE._serialized_end=7343
  _ESP_1C2_ESPABAACTIVE._serialized_start=7345
  _ESP_1C2_ESPABAACTIVE._serialized_end=7395
  _ESP_1C2_ESPABAAVAILABLE._serialized_start=7397
  _ESP_1C2_ESPABAAVAILABLE._serialized_end=7456
  _ESP_1C2_ESPABPACTIVE._serialized_start=7458
  _ESP_1C2_ESPABPACTIVE._serialized_end=7508
  _ESP_1C2_ESPABPAVAILABLE._serialized_start=7510
  _ESP_1C2_ESPABPAVAILABLE._serialized_end=7569
  _ESP_1C2_ESPAEBACTIVE._serialized_start=7571
  _ESP_1C2_ESPAEBACTIVE._serialized_end=7621
  _ESP_1C2_ESPAEBAVAILABLE._serialized_start=7623
  _ESP_1C2_ESPAEBAVAILABLE._serialized_end=7682
  _ESP_1C2_ESPAWBACTIVE._serialized_start=7684
  _ESP_1C2_ESPAWBACTIVE._serialized_end=7734
  _ESP_1C2_ESPAWBAVAILABLE._serialized_start=7736
  _ESP_1C2_ESPAWBAVAILABLE._serialized_end=7795
# @@protoc_insertion_point(module_scope)
