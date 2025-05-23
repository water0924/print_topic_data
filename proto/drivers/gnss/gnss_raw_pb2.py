# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drivers/gnss/gnss_raw.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import geometry_pb2 as common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x64rivers/gnss/gnss_raw.proto\x12\x16\x64\x65\x65proute.drivers.gnss\x1a\x15\x63ommon/geometry.proto\";\n\x0bShortHeader\x12\x18\n\x10measurement_time\x18\x01 \x01(\x03\x12\x12\n\nmessage_id\x18\x02 \x01(\r\"\x96\x02\n\nLongHeader\x12\x18\n\x10measurement_time\x18\x01 \x01(\x03\x12\x12\n\nmessage_id\x18\x02 \x01(\r\x12\x14\n\x0cmessage_type\x18\x03 \x01(\r\x12\x14\n\x0cport_address\x18\x04 \x01(\r\x12\x10\n\x08sequence\x18\x05 \x01(\r\x12\x11\n\tidle_time\x18\x06 \x01(\r\x12\x13\n\x0btime_status\x18\x07 \x01(\r\x12?\n\x0freceiver_status\x18\x08 \x01(\x0e\x32&.deeproute.drivers.gnss.ReceiverStatus\x12\x10\n\x08reserved\x18\t \x01(\r\x12!\n\x19receiver_software_version\x18\n \x01(\r\"\xc8\x06\n\x0cGnssPosition\x12\x32\n\x06header\x18\x01 \x01(\x0b\x32\".deeproute.drivers.gnss.LongHeader\x12?\n\x0fsolution_status\x18\x02 \x01(\x0e\x32&.deeproute.drivers.gnss.SolutionStatus\x12\x43\n\rposition_type\x18\x03 \x01(\x0e\x32,.deeproute.drivers.gnss.PositionVelocityType\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x11\n\tlongitude\x18\x05 \x01(\x01\x12\x0e\n\x06height\x18\x06 \x01(\x01\x12\x12\n\nundulation\x18\x07 \x01(\x02\x12\x10\n\x08\x64\x61tum_id\x18\x08 \x01(\r\x12\x14\n\x0cstd_latitude\x18\t \x01(\x02\x12\x15\n\rstd_longitude\x18\n \x01(\x02\x12\x12\n\nstd_height\x18\x0b \x01(\x02\x12\x17\n\x0f\x62\x61se_station_id\x18\x0c \x01(\t\x12\x18\n\x10\x64ifferential_age\x18\r \x01(\x02\x12\x14\n\x0csolution_age\x18\x0e \x01(\x02\x12\x19\n\x11number_satellites\x18\x0f \x01(\r\x12\'\n\x1fnumber_solution_used_satellites\x18\x10 \x01(\r\x12;\n3number_solution_used_satellites_on_L1_B1_E1_signals\x18\x11 \x01(\r\x12=\n5number_solution_used_satellites_on_multi_freq_signals\x18\x12 \x01(\r\x12\x10\n\x08reserved\x18\x13 \x01(\r\x12 \n\x18\x65xtended_solution_status\x18\x14 \x01(\r\x12\'\n\x1fsignals_mask_Galileo_and_BeiDou\x18\x15 \x01(\r\x12$\n\x1csignals_mask_Gps_and_Glonass\x18\x16 \x01(\r\x12V\n\x1breference_coordinate_system\x18\x17 \x01(\x0e\x32\x31.deeproute.drivers.gnss.ReferenceCoordinateSystem\"\xda\x02\n\x0cGnssVelocity\x12\x32\n\x06header\x18\x01 \x01(\x0b\x32\".deeproute.drivers.gnss.LongHeader\x12?\n\x0fsolution_status\x18\x02 \x01(\x0e\x32&.deeproute.drivers.gnss.SolutionStatus\x12\x43\n\rvelocity_type\x18\x03 \x01(\x0e\x32,.deeproute.drivers.gnss.PositionVelocityType\x12\x17\n\x0fmeasure_latency\x18\x04 \x01(\x02\x12\x18\n\x10\x64ifferential_age\x18\x05 \x01(\x02\x12\x18\n\x10horizontal_speed\x18\x06 \x01(\x01\x12\x19\n\x11track_over_ground\x18\x07 \x01(\x01\x12\x16\n\x0evertical_speed\x18\x08 \x01(\x01\x12\x10\n\x08reserved\x18\t \x01(\x02\"\xf8\x04\n\x12\x44ualAntennaHeading\x12\x32\n\x06header\x18\x01 \x01(\x0b\x32\".deeproute.drivers.gnss.LongHeader\x12?\n\x0fsolution_status\x18\x02 \x01(\x0e\x32&.deeproute.drivers.gnss.SolutionStatus\x12\x43\n\rposition_type\x18\x03 \x01(\x0e\x32,.deeproute.drivers.gnss.PositionVelocityType\x12\x17\n\x0f\x62\x61seline_length\x18\x04 \x01(\x02\x12\x0f\n\x07heading\x18\x05 \x01(\x02\x12\r\n\x05pitch\x18\x06 \x01(\x02\x12\x10\n\x08reserved\x18\x07 \x01(\x02\x12\x13\n\x0bstd_heading\x18\x08 \x01(\x02\x12\x11\n\tstd_pitch\x18\t \x01(\x02\x12\x12\n\nstation_id\x18\n \x01(\t\x12\x1e\n\x16num_satellites_tracked\x18\x0b \x01(\r\x12\x1f\n\x17num_satellites_solution\x18\x0c \x01(\r\x12\'\n\x1fnum_satellites_above_mask_angle\x18\r \x01(\r\x12-\n%num_satellites_above_mask_angle_on_L2\x18\x0e \x01(\r\x12\x17\n\x0fsolution_source\x18\x0f \x01(\r\x12 \n\x18\x65xtended_solution_status\x18\x10 \x01(\r\x12\'\n\x1fsignals_mask_Galileo_and_BeiDou\x18\x11 \x01(\r\x12$\n\x1csignals_mask_Gps_and_Glonass\x18\x12 \x01(\r\"\xe8\x04\n\x07InsPvaX\x12\x32\n\x06header\x18\x01 \x01(\x0b\x32\".deeproute.drivers.gnss.LongHeader\x12\x34\n\x06status\x18\x02 \x01(\x0e\x32$.deeproute.drivers.gnss.InsRawStatus\x12:\n\x04type\x18\x03 \x01(\x0e\x32,.deeproute.drivers.gnss.PositionVelocityType\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x11\n\tlongitude\x18\x05 \x01(\x01\x12\x12\n\nheight_msl\x18\x06 \x01(\x01\x12\x12\n\nundulation\x18\x07 \x01(\x02\x12\x16\n\x0enorth_velocity\x18\x08 \x01(\x01\x12\x15\n\reast_velocity\x18\t \x01(\x01\x12\x13\n\x0bup_velocity\x18\n \x01(\x01\x12\x0c\n\x04roll\x18\x0b \x01(\x01\x12\r\n\x05pitch\x18\x0c \x01(\x01\x12\x0f\n\x07\x61zimuth\x18\r \x01(\x01\x12\x14\n\x0clatitude_std\x18\x0e \x01(\x02\x12\x15\n\rlongitude_std\x18\x0f \x01(\x02\x12\x12\n\nheight_std\x18\x10 \x01(\x02\x12\x1a\n\x12north_velocity_std\x18\x11 \x01(\x02\x12\x19\n\x11\x65\x61st_velocity_std\x18\x12 \x01(\x02\x12\x17\n\x0fup_velocity_std\x18\x13 \x01(\x02\x12\x10\n\x08roll_std\x18\x14 \x01(\x02\x12\x11\n\tpitch_std\x18\x15 \x01(\x02\x12\x13\n\x0b\x61zimuth_std\x18\x16 \x01(\x02\x12\x12\n\next_status\x18\x17 \x01(\r\x12\x19\n\x11time_since_update\x18\x18 \x01(\r\"\xc2\x02\n\x07InsPvaS\x12\x33\n\x06header\x18\x01 \x01(\x0b\x32#.deeproute.drivers.gnss.ShortHeader\x12\x10\n\x08gps_week\x18\x02 \x01(\r\x12\x13\n\x0bgps_seconds\x18\x03 \x01(\x01\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x11\n\tlongitude\x18\x05 \x01(\x01\x12\x0e\n\x06height\x18\x06 \x01(\x01\x12\x16\n\x0enorth_velocity\x18\x07 \x01(\x01\x12\x15\n\reast_velocity\x18\x08 \x01(\x01\x12\x13\n\x0bup_velocity\x18\t \x01(\x01\x12\x0c\n\x04roll\x18\n \x01(\x01\x12\r\n\x05pitch\x18\x0b \x01(\x01\x12\x0f\n\x07\x61zimuth\x18\x0c \x01(\x01\x12\x34\n\x06status\x18\r \x01(\x0e\x32$.deeproute.drivers.gnss.InsRawStatus\"\xa4\x02\n\x0bShortRawImu\x12\x33\n\x06header\x18\x01 \x01(\x0b\x32#.deeproute.drivers.gnss.ShortHeader\x12\x10\n\x08gps_week\x18\x02 \x01(\r\x12\x13\n\x0bgps_seconds\x18\x03 \x01(\x01\x12\x12\n\nimu_status\x18\x04 \x01(\r\x12\x0e\n\x06z_acce\x18\x05 \x01(\x05\x12\x0e\n\x06y_acce\x18\x06 \x01(\x05\x12\x0e\n\x06x_acce\x18\x07 \x01(\x05\x12\x0e\n\x06z_gyro\x18\x08 \x01(\x05\x12\x0e\n\x06y_gyro\x18\t \x01(\x05\x12\x0e\n\x06x_gyro\x18\n \x01(\x05\x12\x13\n\x0btemperature\x18\x0b \x01(\x02\x12\x17\n\x0fimu_gyro_status\x18\x0c \x01(\r\x12\x17\n\x0fimu_acce_status\x18\r \x01(\r\"3\n\x06RawGga\x12\x18\n\x10measurement_time\x18\x01 \x01(\x03\x12\x0f\n\x07raw_gga\x18\x02 \x01(\t\"\xc0\x03\n\x10InuInternalState\x12\x33\n\x06header\x18\x01 \x01(\x0b\x32#.deeproute.drivers.gnss.ShortHeader\x12\x31\n\x0e\x61ttitude_error\x18\x02 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12\x31\n\x0evelocity_error\x18\x03 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12\x31\n\x0eposition_error\x18\x04 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12\x32\n\x0fgyro_bias_error\x18\x05 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12\x32\n\x0f\x61\x63\x63\x65_bias_error\x18\x06 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12,\n\tgyro_bias\x18\x07 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12,\n\tacce_bias\x18\x08 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12\x1a\n\x12wheel_radius_error\x18\t \x01(\x02\"\xdb\x02\n\x13InuInternalStateStd\x12\x33\n\x06header\x18\x01 \x01(\x0b\x32#.deeproute.drivers.gnss.ShortHeader\x12/\n\x0c\x61ttitude_std\x18\x02 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12/\n\x0cvelocity_std\x18\x03 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12/\n\x0cposition_std\x18\x04 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12\x30\n\rgyro_bias_std\x18\x05 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12\x30\n\racce_bias_std\x18\x06 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12\x18\n\x10wheel_radius_std\x18\x07 \x01(\x02*\xfd\x07\n\x0eReceiverStatus\x12\x18\n\x14RECEIVER_STATUS_NONE\x10\x00\x12\x19\n\x15RECEIVER_STATUS_ERROR\x10\x01\x12\'\n#RECEIVER_STATUS_TEMPERATURE_WARNING\x10\x02\x12*\n&RECEIVER_STATUS_VOLTAGE_SUPPLY_WARNING\x10\x03\x12%\n!RECEIVER_STATUS_ANTENNA_UNPOWERED\x10\x04\x12\x1f\n\x1bRECEIVER_STATUS_LNA_FAILURE\x10\x05\x12 \n\x1cRECEIVER_STATUS_ANTENNA_OPEN\x10\x06\x12#\n\x1fRECEIVER_STATUS_ANTENNA_SHORTED\x10\x07\x12\"\n\x1eRECEIVER_STATUS_CPU_OVERLOADED\x10\x08\x12\'\n#RECEIVER_STATUS_COM1_BUFFER_OVERRUN\x10\t\x12\'\n#RECEIVER_STATUS_COM2_BUFFER_OVERRUN\x10\n\x12\'\n#RECEIVER_STATUS_COM3_BUFFER_OVERRUN\x10\x0b\x12!\n\x1dRECEIVER_STATUS_LINK_OVERLOAD\x10\x0c\x12(\n$RECEIVER_STATUS_AUX_TRANSMIT_OVERRUN\x10\r\x12$\n RECEIVER_STATUS_AGC_OUT_OF_RANGE\x10\x0e\x12\x1d\n\x19RECEIVER_STATUS_INS_RESET\x10\x0f\x12#\n\x1fRECEIVER_STATUS_ALMANAC_INVALID\x10\x10\x12-\n)RECEIVER_STATUS_POSITION_SOLUTION_INVALID\x10\x11\x12&\n\"RECEIVER_STATUS_POSITION_NOT_FIXED\x10\x12\x12+\n\'RECEIVER_STATUS_CLOCK_STEERING_DISABLED\x10\x13\x12\'\n#RECEIVER_STATUS_CLOCK_MODEL_INVALID\x10\x14\x12.\n*RECEIVER_STATUS_EXTERNAL_OSCILLATOR_LOCKED\x10\x15\x12-\n)RECEIVER_STATUS_SOFTWARE_RESOURCE_WARNING\x10\x16\x12$\n RECEIVER_STATUS_AUXILIARY3_EVENT\x10\x17\x12$\n RECEIVER_STATUS_AUXILIARY2_EVENT\x10\x18\x12$\n RECEIVER_STATUS_AUXILIARY1_EVENT\x10\x19*\xf8\x04\n\x0eSolutionStatus\x12%\n!SOLUTION_STATUS_SOLUTION_COMPUTED\x10\x00\x12-\n)SOLUTION_STATUS_INSUFFICIENT_OBSERVATIONS\x10\x01\x12\"\n\x1eSOLUTION_STATUS_NO_CONVERGENCE\x10\x02\x12\x34\n0SOLUTION_STATUS_SINGULARITY_AT_PARAMETERS_MATRIX\x10\x03\x12\x34\n0SOLUTION_STATUS_COVARIANCE_TRACE_EXCEEDS_MAXIMUM\x10\x04\x12*\n&SOLUTION_STATUS_TEST_DISTANCE_EXCEEDED\x10\x05\x12\x1e\n\x1aSOLUTION_STATUS_COLD_START\x10\x06\x12\x35\n1SOLUTION_STATUS_VELOCITY_OR_HEIGHT_LIMIT_EXCEEDED\x10\x07\x12+\n\'SOLUTION_STATUS_VARIANCE_EXCEEDS_LIMITS\x10\x08\x12\'\n#SOLUTION_STATUS_RESIDUALS_TOO_LARGE\x10\t\x12%\n!SOLUTION_STATUS_INTEGRITY_WARNING\x10\r\x12\x1b\n\x17SOLUTION_STATUS_PENDING\x10\x12\x12\x1f\n\x1bSOLUTION_STATUS_INVALID_FIX\x10\x13\x12 \n\x1cSOLUTION_STATUS_UNAUTHORIZED\x10\x14\x12 \n\x1cSOLUTION_STATUS_INVALID_RATE\x10\x16*\x8c\x08\n\x14PositionVelocityType\x12\x16\n\x12POSITION_TYPE_NONE\x10\x00\x12\x17\n\x13POSITION_TYPE_FIXED\x10\x01\x12\x1d\n\x19POSITION_TYPE_FIXEDHEIGHT\x10\x02\x12\x1b\n\x17POSITION_TYPE_FLOATCONV\x10\x04\x12\x1a\n\x16POSITION_TYPE_WIDELANE\x10\x05\x12\x1c\n\x18POSITION_TYPE_NARROWLANE\x10\x06\x12\"\n\x1ePOSITION_TYPE_DOPPLER_VELOCITY\x10\x08\x12\x18\n\x14POSITION_TYPE_SINGLE\x10\x10\x12\x19\n\x15POSITION_TYPE_PSRDIFF\x10\x11\x12\x16\n\x12POSITION_TYPE_WAAS\x10\x12\x12\x1c\n\x18POSITION_TYPE_PROPAGATED\x10\x13\x12\x1a\n\x16POSITION_TYPE_OMNISTAR\x10\x14\x12\x1a\n\x16POSITION_TYPE_L1_FLOAT\x10 \x12 \n\x1cPOSITION_TYPE_IONOFREE_FLOAT\x10!\x12\x1e\n\x1aPOSITION_TYPE_NARROW_FLOAT\x10\"\x12\x18\n\x14POSITION_TYPE_L1_INT\x10\x30\x12\x1a\n\x16POSITION_TYPE_WIDE_INT\x10\x31\x12\x1c\n\x18POSITION_TYPE_NARROW_INT\x10\x32\x12 \n\x1cPOSITION_TYPE_RTK_DIRECT_INS\x10\x33\x12\x1a\n\x16POSITION_TYPE_INS_SBAS\x10\x34\x12\x1b\n\x17POSITION_TYPE_INS_PSRSP\x10\x35\x12\x1d\n\x19POSITION_TYPE_INS_PSRDIFF\x10\x36\x12\x1e\n\x1aPOSITION_TYPE_INS_RTKFLOAT\x10\x37\x12\x1e\n\x1aPOSITION_TYPE_INS_RTKFIXED\x10\x38\x12\x1e\n\x1aPOSITION_TYPE_INS_OMNISTAR\x10\x39\x12!\n\x1dPOSITION_TYPE_INS_OMNISTAR_HP\x10:\x12!\n\x1dPOSITION_TYPE_INS_OMNISTAR_XP\x10;\x12\x1d\n\x19POSITION_TYPE_OMNISTAR_HP\x10@\x12\x1d\n\x19POSITION_TYPE_OMNISTAR_XP\x10\x41\x12 \n\x1cPOSITION_TYPE_PPP_CONVERGING\x10\x44\x12\x15\n\x11POSITION_TYPE_PPP\x10\x45\x12$\n POSITION_TYPE_INS_PPP_CONVERGING\x10I\x12\x19\n\x15POSITION_TYPE_INS_PPP\x10J\x12\x18\n\x14POSITION_TYPE_INS_DR\x10K*\xe0\x02\n\x0cInsRawStatus\x12\x17\n\x13INS_STATUS_INACTIVE\x10\x00\x12\x17\n\x13INS_STATUS_ALIGNING\x10\x01\x12\x1c\n\x18INS_STATUS_HIGH_VARIANCE\x10\x02\x12\x1c\n\x18INS_STATUS_SOLUTION_GOOD\x10\x03\x12\x1c\n\x18INS_STATUS_SOLUTION_FREE\x10\x06\x12!\n\x1dINS_STATUS_ALIGNMENT_COMPLETE\x10\x07\x12&\n\"INS_STATUS_DETERMINING_ORIENTATION\x10\x08\x12\"\n\x1eINS_STATUS_WAITING_INITIAL_POS\x10\t\x12\x1c\n\x18INS_STATUS_UNCONVERGE_DR\x10\n\x12\x18\n\x14INS_STATUS_GNSS_LOST\x10\x0b\x12\x1d\n\x19INS_STATUS_ABNORMAL_STATE\x10\x0c*>\n\x19ReferenceCoordinateSystem\x12\t\n\x05WGS84\x10\x00\x12\t\n\x05GCJ02\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x62\x06proto3')

_RECEIVERSTATUS = DESCRIPTOR.enum_types_by_name['ReceiverStatus']
ReceiverStatus = enum_type_wrapper.EnumTypeWrapper(_RECEIVERSTATUS)
_SOLUTIONSTATUS = DESCRIPTOR.enum_types_by_name['SolutionStatus']
SolutionStatus = enum_type_wrapper.EnumTypeWrapper(_SOLUTIONSTATUS)
_POSITIONVELOCITYTYPE = DESCRIPTOR.enum_types_by_name['PositionVelocityType']
PositionVelocityType = enum_type_wrapper.EnumTypeWrapper(_POSITIONVELOCITYTYPE)
_INSRAWSTATUS = DESCRIPTOR.enum_types_by_name['InsRawStatus']
InsRawStatus = enum_type_wrapper.EnumTypeWrapper(_INSRAWSTATUS)
_REFERENCECOORDINATESYSTEM = DESCRIPTOR.enum_types_by_name['ReferenceCoordinateSystem']
ReferenceCoordinateSystem = enum_type_wrapper.EnumTypeWrapper(_REFERENCECOORDINATESYSTEM)
RECEIVER_STATUS_NONE = 0
RECEIVER_STATUS_ERROR = 1
RECEIVER_STATUS_TEMPERATURE_WARNING = 2
RECEIVER_STATUS_VOLTAGE_SUPPLY_WARNING = 3
RECEIVER_STATUS_ANTENNA_UNPOWERED = 4
RECEIVER_STATUS_LNA_FAILURE = 5
RECEIVER_STATUS_ANTENNA_OPEN = 6
RECEIVER_STATUS_ANTENNA_SHORTED = 7
RECEIVER_STATUS_CPU_OVERLOADED = 8
RECEIVER_STATUS_COM1_BUFFER_OVERRUN = 9
RECEIVER_STATUS_COM2_BUFFER_OVERRUN = 10
RECEIVER_STATUS_COM3_BUFFER_OVERRUN = 11
RECEIVER_STATUS_LINK_OVERLOAD = 12
RECEIVER_STATUS_AUX_TRANSMIT_OVERRUN = 13
RECEIVER_STATUS_AGC_OUT_OF_RANGE = 14
RECEIVER_STATUS_INS_RESET = 15
RECEIVER_STATUS_ALMANAC_INVALID = 16
RECEIVER_STATUS_POSITION_SOLUTION_INVALID = 17
RECEIVER_STATUS_POSITION_NOT_FIXED = 18
RECEIVER_STATUS_CLOCK_STEERING_DISABLED = 19
RECEIVER_STATUS_CLOCK_MODEL_INVALID = 20
RECEIVER_STATUS_EXTERNAL_OSCILLATOR_LOCKED = 21
RECEIVER_STATUS_SOFTWARE_RESOURCE_WARNING = 22
RECEIVER_STATUS_AUXILIARY3_EVENT = 23
RECEIVER_STATUS_AUXILIARY2_EVENT = 24
RECEIVER_STATUS_AUXILIARY1_EVENT = 25
SOLUTION_STATUS_SOLUTION_COMPUTED = 0
SOLUTION_STATUS_INSUFFICIENT_OBSERVATIONS = 1
SOLUTION_STATUS_NO_CONVERGENCE = 2
SOLUTION_STATUS_SINGULARITY_AT_PARAMETERS_MATRIX = 3
SOLUTION_STATUS_COVARIANCE_TRACE_EXCEEDS_MAXIMUM = 4
SOLUTION_STATUS_TEST_DISTANCE_EXCEEDED = 5
SOLUTION_STATUS_COLD_START = 6
SOLUTION_STATUS_VELOCITY_OR_HEIGHT_LIMIT_EXCEEDED = 7
SOLUTION_STATUS_VARIANCE_EXCEEDS_LIMITS = 8
SOLUTION_STATUS_RESIDUALS_TOO_LARGE = 9
SOLUTION_STATUS_INTEGRITY_WARNING = 13
SOLUTION_STATUS_PENDING = 18
SOLUTION_STATUS_INVALID_FIX = 19
SOLUTION_STATUS_UNAUTHORIZED = 20
SOLUTION_STATUS_INVALID_RATE = 22
POSITION_TYPE_NONE = 0
POSITION_TYPE_FIXED = 1
POSITION_TYPE_FIXEDHEIGHT = 2
POSITION_TYPE_FLOATCONV = 4
POSITION_TYPE_WIDELANE = 5
POSITION_TYPE_NARROWLANE = 6
POSITION_TYPE_DOPPLER_VELOCITY = 8
POSITION_TYPE_SINGLE = 16
POSITION_TYPE_PSRDIFF = 17
POSITION_TYPE_WAAS = 18
POSITION_TYPE_PROPAGATED = 19
POSITION_TYPE_OMNISTAR = 20
POSITION_TYPE_L1_FLOAT = 32
POSITION_TYPE_IONOFREE_FLOAT = 33
POSITION_TYPE_NARROW_FLOAT = 34
POSITION_TYPE_L1_INT = 48
POSITION_TYPE_WIDE_INT = 49
POSITION_TYPE_NARROW_INT = 50
POSITION_TYPE_RTK_DIRECT_INS = 51
POSITION_TYPE_INS_SBAS = 52
POSITION_TYPE_INS_PSRSP = 53
POSITION_TYPE_INS_PSRDIFF = 54
POSITION_TYPE_INS_RTKFLOAT = 55
POSITION_TYPE_INS_RTKFIXED = 56
POSITION_TYPE_INS_OMNISTAR = 57
POSITION_TYPE_INS_OMNISTAR_HP = 58
POSITION_TYPE_INS_OMNISTAR_XP = 59
POSITION_TYPE_OMNISTAR_HP = 64
POSITION_TYPE_OMNISTAR_XP = 65
POSITION_TYPE_PPP_CONVERGING = 68
POSITION_TYPE_PPP = 69
POSITION_TYPE_INS_PPP_CONVERGING = 73
POSITION_TYPE_INS_PPP = 74
POSITION_TYPE_INS_DR = 75
INS_STATUS_INACTIVE = 0
INS_STATUS_ALIGNING = 1
INS_STATUS_HIGH_VARIANCE = 2
INS_STATUS_SOLUTION_GOOD = 3
INS_STATUS_SOLUTION_FREE = 6
INS_STATUS_ALIGNMENT_COMPLETE = 7
INS_STATUS_DETERMINING_ORIENTATION = 8
INS_STATUS_WAITING_INITIAL_POS = 9
INS_STATUS_UNCONVERGE_DR = 10
INS_STATUS_GNSS_LOST = 11
INS_STATUS_ABNORMAL_STATE = 12
WGS84 = 0
GCJ02 = 1
UNKNOWN = 2


_SHORTHEADER = DESCRIPTOR.message_types_by_name['ShortHeader']
_LONGHEADER = DESCRIPTOR.message_types_by_name['LongHeader']
_GNSSPOSITION = DESCRIPTOR.message_types_by_name['GnssPosition']
_GNSSVELOCITY = DESCRIPTOR.message_types_by_name['GnssVelocity']
_DUALANTENNAHEADING = DESCRIPTOR.message_types_by_name['DualAntennaHeading']
_INSPVAX = DESCRIPTOR.message_types_by_name['InsPvaX']
_INSPVAS = DESCRIPTOR.message_types_by_name['InsPvaS']
_SHORTRAWIMU = DESCRIPTOR.message_types_by_name['ShortRawImu']
_RAWGGA = DESCRIPTOR.message_types_by_name['RawGga']
_INUINTERNALSTATE = DESCRIPTOR.message_types_by_name['InuInternalState']
_INUINTERNALSTATESTD = DESCRIPTOR.message_types_by_name['InuInternalStateStd']
ShortHeader = _reflection.GeneratedProtocolMessageType('ShortHeader', (_message.Message,), {
  'DESCRIPTOR' : _SHORTHEADER,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.ShortHeader)
  })
_sym_db.RegisterMessage(ShortHeader)

LongHeader = _reflection.GeneratedProtocolMessageType('LongHeader', (_message.Message,), {
  'DESCRIPTOR' : _LONGHEADER,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.LongHeader)
  })
_sym_db.RegisterMessage(LongHeader)

GnssPosition = _reflection.GeneratedProtocolMessageType('GnssPosition', (_message.Message,), {
  'DESCRIPTOR' : _GNSSPOSITION,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.GnssPosition)
  })
_sym_db.RegisterMessage(GnssPosition)

GnssVelocity = _reflection.GeneratedProtocolMessageType('GnssVelocity', (_message.Message,), {
  'DESCRIPTOR' : _GNSSVELOCITY,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.GnssVelocity)
  })
_sym_db.RegisterMessage(GnssVelocity)

DualAntennaHeading = _reflection.GeneratedProtocolMessageType('DualAntennaHeading', (_message.Message,), {
  'DESCRIPTOR' : _DUALANTENNAHEADING,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.DualAntennaHeading)
  })
_sym_db.RegisterMessage(DualAntennaHeading)

InsPvaX = _reflection.GeneratedProtocolMessageType('InsPvaX', (_message.Message,), {
  'DESCRIPTOR' : _INSPVAX,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.InsPvaX)
  })
_sym_db.RegisterMessage(InsPvaX)

InsPvaS = _reflection.GeneratedProtocolMessageType('InsPvaS', (_message.Message,), {
  'DESCRIPTOR' : _INSPVAS,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.InsPvaS)
  })
_sym_db.RegisterMessage(InsPvaS)

ShortRawImu = _reflection.GeneratedProtocolMessageType('ShortRawImu', (_message.Message,), {
  'DESCRIPTOR' : _SHORTRAWIMU,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.ShortRawImu)
  })
_sym_db.RegisterMessage(ShortRawImu)

RawGga = _reflection.GeneratedProtocolMessageType('RawGga', (_message.Message,), {
  'DESCRIPTOR' : _RAWGGA,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.RawGga)
  })
_sym_db.RegisterMessage(RawGga)

InuInternalState = _reflection.GeneratedProtocolMessageType('InuInternalState', (_message.Message,), {
  'DESCRIPTOR' : _INUINTERNALSTATE,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.InuInternalState)
  })
_sym_db.RegisterMessage(InuInternalState)

InuInternalStateStd = _reflection.GeneratedProtocolMessageType('InuInternalStateStd', (_message.Message,), {
  'DESCRIPTOR' : _INUINTERNALSTATESTD,
  '__module__' : 'drivers.gnss.gnss_raw_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.drivers.gnss.InuInternalStateStd)
  })
_sym_db.RegisterMessage(InuInternalStateStd)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECEIVERSTATUS._serialized_start=4341
  _RECEIVERSTATUS._serialized_end=5362
  _SOLUTIONSTATUS._serialized_start=5365
  _SOLUTIONSTATUS._serialized_end=5997
  _POSITIONVELOCITYTYPE._serialized_start=6000
  _POSITIONVELOCITYTYPE._serialized_end=7036
  _INSRAWSTATUS._serialized_start=7039
  _INSRAWSTATUS._serialized_end=7391
  _REFERENCECOORDINATESYSTEM._serialized_start=7393
  _REFERENCECOORDINATESYSTEM._serialized_end=7455
  _SHORTHEADER._serialized_start=78
  _SHORTHEADER._serialized_end=137
  _LONGHEADER._serialized_start=140
  _LONGHEADER._serialized_end=418
  _GNSSPOSITION._serialized_start=421
  _GNSSPOSITION._serialized_end=1261
  _GNSSVELOCITY._serialized_start=1264
  _GNSSVELOCITY._serialized_end=1610
  _DUALANTENNAHEADING._serialized_start=1613
  _DUALANTENNAHEADING._serialized_end=2245
  _INSPVAX._serialized_start=2248
  _INSPVAX._serialized_end=2864
  _INSPVAS._serialized_start=2867
  _INSPVAS._serialized_end=3189
  _SHORTRAWIMU._serialized_start=3192
  _SHORTRAWIMU._serialized_end=3484
  _RAWGGA._serialized_start=3486
  _RAWGGA._serialized_end=3537
  _INUINTERNALSTATE._serialized_start=3540
  _INUINTERNALSTATE._serialized_end=3988
  _INUINTERNALSTATESTD._serialized_start=3991
  _INUINTERNALSTATESTD._serialized_end=4338
# @@protoc_insertion_point(module_scope)
