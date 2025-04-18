# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: routing/local_routing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.common import geometry_pb2 as common_dot_geometry__pb2
from proto.map import common_type_pb2 as map_dot_common__type__pb2
from proto.map import map_common_pb2 as map_dot_map__common__pb2
from proto.odd import odd_pb2 as odd_dot_odd__pb2
from proto.map import deeproute_map_guidance_action_pb2 as map_dot_deeproute__map__guidance__action__pb2
from proto.localization import localization_internal_messages_pb2 as localization_dot_localization__internal__messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1brouting/local_routing.proto\x12\x11\x64\x65\x65proute.routing\x1a\x15\x63ommon/geometry.proto\x1a\x15map/common_type.proto\x1a\x14map/map_common.proto\x1a\rodd/odd.proto\x1a\'map/deeproute_map_guidance_action.proto\x1a\x31localization/localization_internal_messages.proto\"\xc5\x04\n\x0fLaneRoutingInfo\x12\x0f\n\x07lane_id\x18\x01 \x03(\x05\x12\x10\n\x08priority\x18\x02 \x01(\x05\x12\x1c\n\x14\x63rossing_remaining_s\x18\x03 \x01(\x01\x12%\n\x1d\x66inal_destination_remaining_s\x18\x04 \x01(\x01\x12\x1d\n\x15\x63losest_possible_tl_s\x18\x05 \x01(\x01\x12\x42\n\x0blane_action\x18\x06 \x01(\x0e\x32-.deeproute.routing.LaneRoutingInfo.LaneAction\x12=\n\x11lane_segment_info\x18\x07 \x03(\x0b\x32\".deeproute.routing.LaneSegmentInfo\x12,\n\x0b\x61\x63tual_turn\x18\x08 \x03(\x0e\x32\x17.deeproute.map.LaneTurn\x12*\n\tlane_type\x18\t \x03(\x0e\x32\x17.deeproute.map.LaneType\x12_\n\"passable_lane_type_before_junction\x18\n \x01(\x0e\x32\x33.deeproute.routing.LaneRoutingInfo.PassableLaneType\".\n\nLaneAction\x12\x0b\n\x07\x46ORWARD\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\"=\n\x10PassableLaneType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nUNPASSABLE\x10\x01\x12\x0c\n\x08PASSABLE\x10\x02\"\x89\r\n\x1aNavigationInfoForVisualize\x12/\n\x0enext_turn_type\x18\x01 \x01(\x0e\x32\x17.deeproute.map.LaneTurn\x12\x1d\n\x15next_turn_remaining_s\x18\x02 \x01(\x01\x12\x30\n\x0fnext2_turn_type\x18\x03 \x01(\x0e\x32\x17.deeproute.map.LaneTurn\x12\x1e\n\x16next2_turn_remaining_s\x18\x04 \x01(\x01\x12\x17\n\x0fmap_speed_limit\x18\x05 \x01(\x01\x12\x1c\n\x14strategy_speed_limit\x18\x06 \x01(\x01\x12V\n\x10speed_limit_type\x18\x07 \x01(\x0e\x32<.deeproute.routing.NavigationInfoForVisualize.SpeedLimitType\x12!\n\x19next_strategy_speed_limit\x18\x08 \x01(\x01\x12-\n%next_strategy_speed_limit_remaining_s\x18\t \x01(\x01\x12\x34\n\x12\x63urrent_road_class\x18\n \x01(\x0e\x32\x18.deeproute.map.RoadClass\x12\x31\n\x0fnext_road_class\x18\x0b \x01(\x0e\x32\x18.deeproute.map.RoadClass\x12#\n\x1bnext_road_class_remaining_s\x18\x0c \x01(\x01\x12Z\n\x12speed_limit_status\x18\r \x01(\x0e\x32>.deeproute.routing.NavigationInfoForVisualize.SpeedLimitStatus\x12\x1d\n\x15real_time_speed_limit\x18\x0e \x01(\x05\x12#\n\x1bvalid_real_time_speed_limit\x18\x0f \x01(\x05\x12%\n\x1dinvalid_real_time_speed_limit\x18\x10 \x01(\x05\x12X\n\x11junction_spl_info\x18\x11 \x01(\x0b\x32=.deeproute.routing.NavigationInfoForVisualize.JunctionSplInfo\x12\x16\n\x0e\x65xp_spl_enable\x18\x12 \x01(\x08\x1a\x35\n\x0fJunctionSplInfo\x12\x11\n\tspl_ratio\x18\x01 \x01(\x01\x12\x0f\n\x07min_spl\x18\x02 \x01(\x01\"\xdb\x04\n\x0eSpeedLimitType\x12\x0b\n\x07INVALID\x10\x00\x12\x16\n\x12GLOBAL_SPEED_LIMIT\x10\x01\x12\x14\n\x10RAMP_SPEED_LIMIT\x10\x02\x12\x18\n\x14JUNCTION_SPEED_LIMIT\x10\x03\x12\x15\n\x11MERGE_SPEED_LIMIT\x10\x04\x12\x14\n\x10\x45XIT_SPEED_LIMIT\x10\x05\x12\x19\n\x15\x45XIT_RAMP_SPEED_LIMIT\x10\x06\x12\x1d\n\x19MERGE_SPEED_LIMIT_EXPRESS\x10\x07\x12\x1b\n\x17IN_JUNCTION_SPEED_LIMIT\x10\x08\x12\x1c\n\x18\x45XIT_SPEED_LIMIT_EXPRESS\x10\t\x12\x1c\n\x18\x45NTER_TUNNEL_SPEED_LIMIT\x10\n\x12\x1c\n\x18LEAVE_TUNNEL_SPEED_LIMIT\x10\x0b\x12!\n\x1dSECONDARY_TO_MAIN_SPEED_LIMIT\x10\x0c\x12!\n\x1dMAIN_TO_SECONDARY_SPEED_LIMIT\x10\r\x12\x18\n\x14\x45NTRANCE_SPEED_LIMIT\x10\x0e\x12\x14\n\x10TOLL_SPEED_LIMIT\x10\x0f\x12\x19\n\x15REST_AREA_SPEED_LIMIT\x10\x10\x12\x16\n\x12\x43\x41MERA_SPEED_LIMIT\x10\x11\x12\x19\n\x15IN_TUNNEL_SPEED_LIMIT\x10\x12\x12\x16\n\x12\x46ORCED_SPEED_LIMIT\x10\x13\x12\x1c\n\x18\x41MAP_HIGHWAY_SPEED_LIMIT\x10\x14\x12\x1c\n\x18\x41MAP_EXPRESS_SPEED_LIMIT\x10\x15\"\x8b\x01\n\x10SpeedLimitStatus\x12\x08\n\x04NONE\x10\x00\x12(\n$ONLINE_CURRENT_ONLINE_NEXT_ONLINE_RS\x10\x01\x12\"\n\x1eONLINE_CURRENT_MAP_NEXT_MAP_RS\x10\x02\x12\x1f\n\x1bMAP_CURRENT_MAP_NEXT_MAP_RS\x10\x03\"\xe2\x0b\n\x0cLocalRouting\x12\x12\n\nrequest_id\x18\x13 \x01(\t\x12=\n\x11lane_routing_info\x18\x01 \x03(\x0b\x32\".deeproute.routing.LaneRoutingInfo\x12\x42\n\x16next_lane_routing_info\x18\x1a \x03(\x0b\x32\".deeproute.routing.LaneRoutingInfo\x12\x17\n\x0f\x63urrent_lane_id\x18\x02 \x01(\x05\x12-\n\ndest_point\x18\x03 \x01(\x0b\x32\x19.deeproute.common.Point3D\x12&\n\x1e\x61\x64\x63_to_destination_remaining_s\x18\x04 \x01(\x01\x12\x14\n\ttimestamp\x18\x05 \x01(\x03:\x01\x30\x12/\n\x0enext_turn_type\x18\x06 \x01(\x0e\x32\x17.deeproute.map.LaneTurn\x12\x1d\n\x15next_turn_remaining_s\x18\x07 \x01(\x01\x12\x30\n\x0fnext2_turn_type\x18\x08 \x01(\x0e\x32\x17.deeproute.map.LaneTurn\x12\x1e\n\x16next2_turn_remaining_s\x18\t \x01(\x01\x12\x1b\n\x13\x63urrent_speed_limit\x18\n \x01(\x01\x12\x18\n\x10next_speed_limit\x18\x0b \x01(\x01\x12$\n\x1cnext_speed_limit_remaining_s\x18\x0c \x01(\x01\x12T\n\x1dnavigation_info_for_visualize\x18\r \x01(\x0b\x32-.deeproute.routing.NavigationInfoForVisualize\x12\x12\n\nis_on_ramp\x18\x0e \x01(\x08\x12\x62\n\x1broad_instance_to_priorities\x18\x0f \x03(\x0b\x32=.deeproute.routing.LocalRouting.RoadInstanceToPrioritiesEntry\x12\x30\n\ndebug_info\x18\x10 \x01(\x0b\x32\x1c.deeproute.routing.DebugInfo\x12/\n\x0csd_road_info\x18\x11 \x01(\x0b\x32\x19.deeproute.map.SdRoadInfo\x12*\n\tarea_info\x18\x12 \x03(\x0b\x32\x17.deeproute.map.AreaInfo\x12\x1b\n\x13junction_link_ni_id\x18\x14 \x01(\t\x12\x34\n\x0crouting_mask\x18\x15 \x01(\x0b\x32\x1e.deeproute.routing.RoutingMask\x12\x37\n\x0fimpassable_mask\x18\x1d \x01(\x0b\x32\x1e.deeproute.routing.RoutingMask\x12\x33\n\x0eodd_limit_info\x18\x16 \x01(\x0b\x32\x1b.deeproute.odd.OddLimitInfo\x12#\n\x15is_routing_mask_valid\x18\x17 \x01(\x08:\x04true\x12\x45\n\x16sd_crossing_navi_infos\x18\x18 \x03(\x0b\x32%.deeproute.routing.SdCrossingNaviInfo\x12\"\n\x1a\x66reeway_main_road_lane_ids\x18\x19 \x03(\x05\x12\x19\n\x11is_big_right_turn\x18\x1b \x01(\x08\x12\x1b\n\x13\x63rowd_source_events\x18\x1c \x03(\t\x12\x41\n\x16passable_junction_list\x18\x1e \x01(\x0b\x32!.deeproute.map.GuidanceActionList\x12L\n\x11vpa_local_routing\x18\x1f \x01(\x0b\x32\x31.deeproute.localization.message.GlobalRoutingInfo\x1a?\n\x1dRoadInstanceToPrioritiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"%\n\x12SingleGroupLaneIDs\x12\x0f\n\x07lane_id\x18\x01 \x03(\x05\"\xa4\x02\n\tDebugInfo\x12\x34\n\x11matched_bias_pose\x18\x01 \x01(\x0b\x32\x19.deeproute.common.Vector3\x12!\n\x19\x63hoosed_lane_ids_by_match\x18\x02 \x03(\x05\x12\x41\n\x0escene_strategy\x18\x03 \x01(\x0b\x32).deeproute.routing.SceneStrategyDebugInfo\x12\x0b\n\x03pgp\x18\x04 \x03(\t\x12:\n\x0blane_groups\x18\x05 \x03(\x0b\x32%.deeproute.routing.SingleGroupLaneIDs\x12\x10\n\x08is_yawed\x18\x06 \x01(\x08\x12 \n\x18routing_input_debug_info\x18\x07 \x03(\t\"B\n\x0fLaneSegmentInfo\x12\x0f\n\x07lane_id\x18\x01 \x01(\x05\x12\x0f\n\x07start_s\x18\x02 \x01(\x01\x12\r\n\x05\x65nd_s\x18\x03 \x01(\x01\"\xf5\x01\n\x0bRoutingMask\x12\r\n\x05min_x\x18\x01 \x01(\x02\x12\r\n\x05max_x\x18\x02 \x01(\x02\x12\r\n\x05min_y\x18\x03 \x01(\x02\x12\r\n\x05max_y\x18\x04 \x01(\x02\x12\r\n\x05width\x18\x05 \x01(\x05\x12\x0e\n\x06height\x18\x06 \x01(\x05\x12\x0f\n\x07indices\x18\x07 \x03(\r\x12\x18\n\x10time_measurement\x18\x08 \x01(\x04\x12/\n\x0c\x61\x64\x63_position\x18\t \x01(\x0b\x32\x19.deeproute.common.Point3D\x12/\n\x0c\x61\x64\x63_rotation\x18\n \x01(\x0b\x32\x19.deeproute.common.Point3D\"l\n\x18LaneSelectorForYCrossing\x12\x19\n\x11\x63lassify_lane_ret\x18\x01 \x01(\x08\x12\x1a\n\x12\x63lassify_lane_type\x18\x02 \x01(\t\x12\x19\n\x11keep_current_lane\x18\x03 \x01(\x08\"\x98\x01\n\x1eLaneSelectorForFreewayMergeOut\x12\x18\n\x10merge_in_link_id\x18\x01 \x01(\t\x12\x19\n\x11merge_out_link_id\x18\x02 \x01(\t\x12&\n\x1eturn_right_most_threshold_dist\x18\x03 \x01(\x01\x12\x19\n\x11\x64ist_to_turn_type\x18\x04 \x01(\x01\"Z\n\x1fLaneSelectorForNormalWayMergeIn\x12\x18\n\x10merge_in_link_id\x18\x01 \x01(\t\x12\x1d\n\x15\x64ist_to_merge_in_link\x18\x02 \x01(\x01\"j\n\x15LaneSelectorForNormal\x12\x19\n\x11left_add_lane_ids\x18\x01 \x03(\x05\x12\x1d\n\x15right_reduce_lane_ids\x18\x02 \x03(\x05\x12\x17\n\x0f\x61ligned_link_id\x18\x03 \x01(\t\"^\n\x18LaneSelectorForLaneClose\x12\x13\n\x0b\x65go_lane_id\x18\x01 \x01(\x05\x12\x15\n\rego_lane_attr\x18\x02 \x01(\t\x12\x16\n\x0eturn_type_attr\x18\x03 \x01(\x05\"\xd5\x01\n\x19LaneMarkStrategyForNormal\x12\x15\n\rcross_link_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63ross_link_arr\x18\x02 \x01(\x05\x12\x15\n\rcorrected_arr\x18\x03 \x01(\x05\x12\x16\n\x0e\x63ross_link_crs\x18\x04 \x01(\x01\x12\x13\n\x07lane_id\x18\x05 \x01(\x05\x42\x02\x18\x01\x12\x1a\n\x0elane_mark_type\x18\x06 \x01(\x05\x42\x02\x18\x01\x12\x10\n\x08lane_ids\x18\x07 \x03(\x05\x12\x17\n\x0flane_mark_types\x18\x08 \x03(\x05\"\x85\x01\n\x1eLaneSelectorForFreewayEntrance\x12 \n\x18\x66reeway_entrance_link_id\x18\x01 \x01(\t\x12%\n\x1d\x64ist_to_freeway_entrance_link\x18\x02 \x01(\x01\x12\x1a\n\x12\x61lign_topo_link_id\x18\x03 \x01(\t\"F\n\x13LaneSelectorForToll\x12\x14\n\x0ctoll_link_id\x18\x01 \x01(\t\x12\x19\n\x11\x64ist_to_toll_link\x18\x02 \x01(\x01\"\x83\x01\n\x10Sd3yCrossingInfo\x12\x18\n\x10\x63rossing_link_id\x18\x01 \x01(\t\x12\x19\n\x11\x63rossing_link_dir\x18\x02 \x01(\x05\x12\x1d\n\x15\x64ist_to_crossing_link\x18\x03 \x01(\x01\x12\x1b\n\x13sorted_out_link_ids\x18\x04 \x03(\t\"\xb3\x01\n\x15Special3yCrossingInfo\x12\x15\n\rpre_y_link_id\x18\x01 \x01(\t\x12\x16\n\x0epre_y_link_dir\x18\x02 \x01(\x05\x12\x16\n\x0epost_y_link_id\x18\x03 \x01(\t\x12\x17\n\x0fpost_y_link_dir\x18\x04 \x01(\x05\x12\x1d\n\x15\x64ist_to_crossing_link\x18\x05 \x01(\x01\x12\x1b\n\x13sorted_out_link_ids\x18\x06 \x03(\t\"\xbb\x01\n+LaneSelectorForFreewayThreeOutLinksCrossing\x12@\n\x13sd_3y_crossing_info\x18\x01 \x01(\x0b\x32#.deeproute.routing.Sd3yCrossingInfo\x12J\n\x18special_3y_crossing_info\x18\x02 \x01(\x0b\x32(.deeproute.routing.Special3yCrossingInfo\"\xba\x01\n*LaneSelectorForNormalThreeOutLinksCrossing\x12@\n\x13sd_3y_crossing_info\x18\x01 \x01(\x0b\x32#.deeproute.routing.Sd3yCrossingInfo\x12J\n\x18special_3y_crossing_info\x18\x02 \x01(\x0b\x32(.deeproute.routing.Special3yCrossingInfo\"Z\n\x1dLaneSelectorForNormalMergeOut\x12\x19\n\x11merge_out_link_id\x18\x01 \x01(\t\x12\x1e\n\x16\x64ist_to_merge_out_link\x18\x02 \x01(\x01\":\n\x1cLaneSelectorForRightTurnLane\x12\x1a\n\x12\x61lign_topo_link_id\x18\x01 \x01(\t\"\x9c\x01\n+LaneSelectorForNormalMultiTurnRightCrossing\x12\x15\n\rscene_link_id\x18\x01 \x01(\t\x12\x1e\n\x16pre_turn_right_link_id\x18\x02 \x01(\t\x12\x1a\n\x12\x64ist_to_scene_link\x18\x03 \x01(\x01\x12\x1a\n\x12\x64ist_between_links\x18\x04 \x01(\x01\"^\n)LaneSelectorForNormalTurnRightTwoOutlinks\x12\x15\n\rscene_link_id\x18\x01 \x01(\t\x12\x1a\n\x12\x64ist_to_scene_link\x18\x02 \x01(\x01\"u\n$LaneSelectorForLongFreewayMergeInOut\x12\x1a\n\x12lane_keep_selector\x18\x01 \x01(\t\x12\x15\n\rscene_link_id\x18\x02 \x01(\t\x12\x1a\n\x12\x64ist_to_scene_link\x18\x03 \x01(\x01\"\xe3\n\n\x16SceneStrategyDebugInfo\x12\x1e\n\x16trigger_strategy_names\x18\x01 \x03(\t\x12\x16\n\x0epre_p0_lane_id\x18\x02 \x01(\x05\x12K\n\x16y_crossing_for_freeway\x18\x03 \x01(\x0b\x32+.deeproute.routing.LaneSelectorForYCrossing\x12J\n\x15y_crossing_for_normal\x18\x04 \x01(\x0b\x32+.deeproute.routing.LaneSelectorForYCrossing\x12L\n\x11\x66reeway_merge_out\x18\x05 \x01(\x0b\x32\x31.deeproute.routing.LaneSelectorForFreewayMergeOut\x12N\n\x12normalway_merge_in\x18\x06 \x01(\x0b\x32\x32.deeproute.routing.LaneSelectorForNormalWayMergeIn\x12\x38\n\x06normal\x18\x07 \x01(\x0b\x32(.deeproute.routing.LaneSelectorForNormal\x12?\n\nlane_close\x18\x08 \x01(\x0b\x32+.deeproute.routing.LaneSelectorForLaneClose\x12J\n\x14lane_mark_for_normal\x18\t \x01(\x0b\x32,.deeproute.routing.LaneMarkStrategyForNormal\x12K\n\x10\x66reeway_entrance\x18\n \x01(\x0b\x32\x31.deeproute.routing.LaneSelectorForFreewayEntrance\x12\x34\n\x04toll\x18\x0b \x01(\x0b\x32&.deeproute.routing.LaneSelectorForToll\x12g\n\x1f\x66reeway_three_outlinks_crossing\x18\x0c \x01(\x0b\x32>.deeproute.routing.LaneSelectorForFreewayThreeOutLinksCrossing\x12\x65\n\x1enormal_three_outlinks_crossing\x18\r \x01(\x0b\x32=.deeproute.routing.LaneSelectorForNormalThreeOutLinksCrossing\x12J\n\x10normal_merge_out\x18\x0e \x01(\x0b\x32\x30.deeproute.routing.LaneSelectorForNormalMergeOut\x12H\n\x0fright_turn_lane\x18\x0f \x01(\x0b\x32/.deeproute.routing.LaneSelectorForRightTurnLane\x12h\n normal_multi_turn_right_crossing\x18\x10 \x01(\x0b\x32>.deeproute.routing.LaneSelectorForNormalMultiTurnRightCrossing\x12\x64\n\x1enormal_turn_right_two_outlinks\x18\x11 \x01(\x0b\x32<.deeproute.routing.LaneSelectorForNormalTurnRightTwoOutlinks\x12Z\n\x19long_freeway_merge_in_out\x18\x12 \x01(\x0b\x32\x37.deeproute.routing.LaneSelectorForLongFreewayMergeInOut\"_\n\x12SdCrossingNaviInfo\x12\x19\n\x11\x63rossing_distance\x18\x01 \x01(\x01\x12.\n\rcrossing_turn\x18\x02 \x01(\x0e\x32\x17.deeproute.map.LaneTurn')



_LANEROUTINGINFO = DESCRIPTOR.message_types_by_name['LaneRoutingInfo']
_NAVIGATIONINFOFORVISUALIZE = DESCRIPTOR.message_types_by_name['NavigationInfoForVisualize']
_NAVIGATIONINFOFORVISUALIZE_JUNCTIONSPLINFO = _NAVIGATIONINFOFORVISUALIZE.nested_types_by_name['JunctionSplInfo']
_LOCALROUTING = DESCRIPTOR.message_types_by_name['LocalRouting']
_LOCALROUTING_ROADINSTANCETOPRIORITIESENTRY = _LOCALROUTING.nested_types_by_name['RoadInstanceToPrioritiesEntry']
_SINGLEGROUPLANEIDS = DESCRIPTOR.message_types_by_name['SingleGroupLaneIDs']
_DEBUGINFO = DESCRIPTOR.message_types_by_name['DebugInfo']
_LANESEGMENTINFO = DESCRIPTOR.message_types_by_name['LaneSegmentInfo']
_ROUTINGMASK = DESCRIPTOR.message_types_by_name['RoutingMask']
_LANESELECTORFORYCROSSING = DESCRIPTOR.message_types_by_name['LaneSelectorForYCrossing']
_LANESELECTORFORFREEWAYMERGEOUT = DESCRIPTOR.message_types_by_name['LaneSelectorForFreewayMergeOut']
_LANESELECTORFORNORMALWAYMERGEIN = DESCRIPTOR.message_types_by_name['LaneSelectorForNormalWayMergeIn']
_LANESELECTORFORNORMAL = DESCRIPTOR.message_types_by_name['LaneSelectorForNormal']
_LANESELECTORFORLANECLOSE = DESCRIPTOR.message_types_by_name['LaneSelectorForLaneClose']
_LANEMARKSTRATEGYFORNORMAL = DESCRIPTOR.message_types_by_name['LaneMarkStrategyForNormal']
_LANESELECTORFORFREEWAYENTRANCE = DESCRIPTOR.message_types_by_name['LaneSelectorForFreewayEntrance']
_LANESELECTORFORTOLL = DESCRIPTOR.message_types_by_name['LaneSelectorForToll']
_SD3YCROSSINGINFO = DESCRIPTOR.message_types_by_name['Sd3yCrossingInfo']
_SPECIAL3YCROSSINGINFO = DESCRIPTOR.message_types_by_name['Special3yCrossingInfo']
_LANESELECTORFORFREEWAYTHREEOUTLINKSCROSSING = DESCRIPTOR.message_types_by_name['LaneSelectorForFreewayThreeOutLinksCrossing']
_LANESELECTORFORNORMALTHREEOUTLINKSCROSSING = DESCRIPTOR.message_types_by_name['LaneSelectorForNormalThreeOutLinksCrossing']
_LANESELECTORFORNORMALMERGEOUT = DESCRIPTOR.message_types_by_name['LaneSelectorForNormalMergeOut']
_LANESELECTORFORRIGHTTURNLANE = DESCRIPTOR.message_types_by_name['LaneSelectorForRightTurnLane']
_LANESELECTORFORNORMALMULTITURNRIGHTCROSSING = DESCRIPTOR.message_types_by_name['LaneSelectorForNormalMultiTurnRightCrossing']
_LANESELECTORFORNORMALTURNRIGHTTWOOUTLINKS = DESCRIPTOR.message_types_by_name['LaneSelectorForNormalTurnRightTwoOutlinks']
_LANESELECTORFORLONGFREEWAYMERGEINOUT = DESCRIPTOR.message_types_by_name['LaneSelectorForLongFreewayMergeInOut']
_SCENESTRATEGYDEBUGINFO = DESCRIPTOR.message_types_by_name['SceneStrategyDebugInfo']
_SDCROSSINGNAVIINFO = DESCRIPTOR.message_types_by_name['SdCrossingNaviInfo']
_LANEROUTINGINFO_LANEACTION = _LANEROUTINGINFO.enum_types_by_name['LaneAction']
_LANEROUTINGINFO_PASSABLELANETYPE = _LANEROUTINGINFO.enum_types_by_name['PassableLaneType']
_NAVIGATIONINFOFORVISUALIZE_SPEEDLIMITTYPE = _NAVIGATIONINFOFORVISUALIZE.enum_types_by_name['SpeedLimitType']
_NAVIGATIONINFOFORVISUALIZE_SPEEDLIMITSTATUS = _NAVIGATIONINFOFORVISUALIZE.enum_types_by_name['SpeedLimitStatus']
LaneRoutingInfo = _reflection.GeneratedProtocolMessageType('LaneRoutingInfo', (_message.Message,), {
  'DESCRIPTOR' : _LANEROUTINGINFO,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneRoutingInfo)
  })
_sym_db.RegisterMessage(LaneRoutingInfo)

NavigationInfoForVisualize = _reflection.GeneratedProtocolMessageType('NavigationInfoForVisualize', (_message.Message,), {

  'JunctionSplInfo' : _reflection.GeneratedProtocolMessageType('JunctionSplInfo', (_message.Message,), {
    'DESCRIPTOR' : _NAVIGATIONINFOFORVISUALIZE_JUNCTIONSPLINFO,
    '__module__' : 'routing.local_routing_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.routing.NavigationInfoForVisualize.JunctionSplInfo)
    })
  ,
  'DESCRIPTOR' : _NAVIGATIONINFOFORVISUALIZE,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.NavigationInfoForVisualize)
  })
_sym_db.RegisterMessage(NavigationInfoForVisualize)
_sym_db.RegisterMessage(NavigationInfoForVisualize.JunctionSplInfo)

LocalRouting = _reflection.GeneratedProtocolMessageType('LocalRouting', (_message.Message,), {

  'RoadInstanceToPrioritiesEntry' : _reflection.GeneratedProtocolMessageType('RoadInstanceToPrioritiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOCALROUTING_ROADINSTANCETOPRIORITIESENTRY,
    '__module__' : 'routing.local_routing_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.routing.LocalRouting.RoadInstanceToPrioritiesEntry)
    })
  ,
  'DESCRIPTOR' : _LOCALROUTING,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LocalRouting)
  })
_sym_db.RegisterMessage(LocalRouting)
_sym_db.RegisterMessage(LocalRouting.RoadInstanceToPrioritiesEntry)

SingleGroupLaneIDs = _reflection.GeneratedProtocolMessageType('SingleGroupLaneIDs', (_message.Message,), {
  'DESCRIPTOR' : _SINGLEGROUPLANEIDS,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.SingleGroupLaneIDs)
  })
_sym_db.RegisterMessage(SingleGroupLaneIDs)

DebugInfo = _reflection.GeneratedProtocolMessageType('DebugInfo', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGINFO,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.DebugInfo)
  })
_sym_db.RegisterMessage(DebugInfo)

LaneSegmentInfo = _reflection.GeneratedProtocolMessageType('LaneSegmentInfo', (_message.Message,), {
  'DESCRIPTOR' : _LANESEGMENTINFO,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSegmentInfo)
  })
_sym_db.RegisterMessage(LaneSegmentInfo)

RoutingMask = _reflection.GeneratedProtocolMessageType('RoutingMask', (_message.Message,), {
  'DESCRIPTOR' : _ROUTINGMASK,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.RoutingMask)
  })
_sym_db.RegisterMessage(RoutingMask)

LaneSelectorForYCrossing = _reflection.GeneratedProtocolMessageType('LaneSelectorForYCrossing', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORYCROSSING,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForYCrossing)
  })
_sym_db.RegisterMessage(LaneSelectorForYCrossing)

LaneSelectorForFreewayMergeOut = _reflection.GeneratedProtocolMessageType('LaneSelectorForFreewayMergeOut', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORFREEWAYMERGEOUT,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForFreewayMergeOut)
  })
_sym_db.RegisterMessage(LaneSelectorForFreewayMergeOut)

LaneSelectorForNormalWayMergeIn = _reflection.GeneratedProtocolMessageType('LaneSelectorForNormalWayMergeIn', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORNORMALWAYMERGEIN,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForNormalWayMergeIn)
  })
_sym_db.RegisterMessage(LaneSelectorForNormalWayMergeIn)

LaneSelectorForNormal = _reflection.GeneratedProtocolMessageType('LaneSelectorForNormal', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORNORMAL,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForNormal)
  })
_sym_db.RegisterMessage(LaneSelectorForNormal)

LaneSelectorForLaneClose = _reflection.GeneratedProtocolMessageType('LaneSelectorForLaneClose', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORLANECLOSE,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForLaneClose)
  })
_sym_db.RegisterMessage(LaneSelectorForLaneClose)

LaneMarkStrategyForNormal = _reflection.GeneratedProtocolMessageType('LaneMarkStrategyForNormal', (_message.Message,), {
  'DESCRIPTOR' : _LANEMARKSTRATEGYFORNORMAL,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneMarkStrategyForNormal)
  })
_sym_db.RegisterMessage(LaneMarkStrategyForNormal)

LaneSelectorForFreewayEntrance = _reflection.GeneratedProtocolMessageType('LaneSelectorForFreewayEntrance', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORFREEWAYENTRANCE,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForFreewayEntrance)
  })
_sym_db.RegisterMessage(LaneSelectorForFreewayEntrance)

LaneSelectorForToll = _reflection.GeneratedProtocolMessageType('LaneSelectorForToll', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORTOLL,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForToll)
  })
_sym_db.RegisterMessage(LaneSelectorForToll)

Sd3yCrossingInfo = _reflection.GeneratedProtocolMessageType('Sd3yCrossingInfo', (_message.Message,), {
  'DESCRIPTOR' : _SD3YCROSSINGINFO,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.Sd3yCrossingInfo)
  })
_sym_db.RegisterMessage(Sd3yCrossingInfo)

Special3yCrossingInfo = _reflection.GeneratedProtocolMessageType('Special3yCrossingInfo', (_message.Message,), {
  'DESCRIPTOR' : _SPECIAL3YCROSSINGINFO,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.Special3yCrossingInfo)
  })
_sym_db.RegisterMessage(Special3yCrossingInfo)

LaneSelectorForFreewayThreeOutLinksCrossing = _reflection.GeneratedProtocolMessageType('LaneSelectorForFreewayThreeOutLinksCrossing', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORFREEWAYTHREEOUTLINKSCROSSING,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForFreewayThreeOutLinksCrossing)
  })
_sym_db.RegisterMessage(LaneSelectorForFreewayThreeOutLinksCrossing)

LaneSelectorForNormalThreeOutLinksCrossing = _reflection.GeneratedProtocolMessageType('LaneSelectorForNormalThreeOutLinksCrossing', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORNORMALTHREEOUTLINKSCROSSING,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForNormalThreeOutLinksCrossing)
  })
_sym_db.RegisterMessage(LaneSelectorForNormalThreeOutLinksCrossing)

LaneSelectorForNormalMergeOut = _reflection.GeneratedProtocolMessageType('LaneSelectorForNormalMergeOut', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORNORMALMERGEOUT,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForNormalMergeOut)
  })
_sym_db.RegisterMessage(LaneSelectorForNormalMergeOut)

LaneSelectorForRightTurnLane = _reflection.GeneratedProtocolMessageType('LaneSelectorForRightTurnLane', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORRIGHTTURNLANE,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForRightTurnLane)
  })
_sym_db.RegisterMessage(LaneSelectorForRightTurnLane)

LaneSelectorForNormalMultiTurnRightCrossing = _reflection.GeneratedProtocolMessageType('LaneSelectorForNormalMultiTurnRightCrossing', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORNORMALMULTITURNRIGHTCROSSING,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForNormalMultiTurnRightCrossing)
  })
_sym_db.RegisterMessage(LaneSelectorForNormalMultiTurnRightCrossing)

LaneSelectorForNormalTurnRightTwoOutlinks = _reflection.GeneratedProtocolMessageType('LaneSelectorForNormalTurnRightTwoOutlinks', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORNORMALTURNRIGHTTWOOUTLINKS,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForNormalTurnRightTwoOutlinks)
  })
_sym_db.RegisterMessage(LaneSelectorForNormalTurnRightTwoOutlinks)

LaneSelectorForLongFreewayMergeInOut = _reflection.GeneratedProtocolMessageType('LaneSelectorForLongFreewayMergeInOut', (_message.Message,), {
  'DESCRIPTOR' : _LANESELECTORFORLONGFREEWAYMERGEINOUT,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.LaneSelectorForLongFreewayMergeInOut)
  })
_sym_db.RegisterMessage(LaneSelectorForLongFreewayMergeInOut)

SceneStrategyDebugInfo = _reflection.GeneratedProtocolMessageType('SceneStrategyDebugInfo', (_message.Message,), {
  'DESCRIPTOR' : _SCENESTRATEGYDEBUGINFO,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.SceneStrategyDebugInfo)
  })
_sym_db.RegisterMessage(SceneStrategyDebugInfo)

SdCrossingNaviInfo = _reflection.GeneratedProtocolMessageType('SdCrossingNaviInfo', (_message.Message,), {
  'DESCRIPTOR' : _SDCROSSINGNAVIINFO,
  '__module__' : 'routing.local_routing_pb2'
  # @@protoc_insertion_point(class_scope:deeproute.routing.SdCrossingNaviInfo)
  })
_sym_db.RegisterMessage(SdCrossingNaviInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOCALROUTING_ROADINSTANCETOPRIORITIESENTRY._options = None
  _LOCALROUTING_ROADINSTANCETOPRIORITIESENTRY._serialized_options = b'8\001'
  _LANEMARKSTRATEGYFORNORMAL.fields_by_name['lane_id']._options = None
  _LANEMARKSTRATEGYFORNORMAL.fields_by_name['lane_id']._serialized_options = b'\030\001'
  _LANEMARKSTRATEGYFORNORMAL.fields_by_name['lane_mark_type']._options = None
  _LANEMARKSTRATEGYFORNORMAL.fields_by_name['lane_mark_type']._serialized_options = b'\030\001'
  _LANEROUTINGINFO._serialized_start=226
  _LANEROUTINGINFO._serialized_end=807
  _LANEROUTINGINFO_LANEACTION._serialized_start=698
  _LANEROUTINGINFO_LANEACTION._serialized_end=744
  _LANEROUTINGINFO_PASSABLELANETYPE._serialized_start=746
  _LANEROUTINGINFO_PASSABLELANETYPE._serialized_end=807
  _NAVIGATIONINFOFORVISUALIZE._serialized_start=810
  _NAVIGATIONINFOFORVISUALIZE._serialized_end=2483
  _NAVIGATIONINFOFORVISUALIZE_JUNCTIONSPLINFO._serialized_start=1682
  _NAVIGATIONINFOFORVISUALIZE_JUNCTIONSPLINFO._serialized_end=1735
  _NAVIGATIONINFOFORVISUALIZE_SPEEDLIMITTYPE._serialized_start=1738
  _NAVIGATIONINFOFORVISUALIZE_SPEEDLIMITTYPE._serialized_end=2341
  _NAVIGATIONINFOFORVISUALIZE_SPEEDLIMITSTATUS._serialized_start=2344
  _NAVIGATIONINFOFORVISUALIZE_SPEEDLIMITSTATUS._serialized_end=2483
  _LOCALROUTING._serialized_start=2486
  _LOCALROUTING._serialized_end=3992
  _LOCALROUTING_ROADINSTANCETOPRIORITIESENTRY._serialized_start=3929
  _LOCALROUTING_ROADINSTANCETOPRIORITIESENTRY._serialized_end=3992
  _SINGLEGROUPLANEIDS._serialized_start=3994
  _SINGLEGROUPLANEIDS._serialized_end=4031
  _DEBUGINFO._serialized_start=4034
  _DEBUGINFO._serialized_end=4326
  _LANESEGMENTINFO._serialized_start=4328
  _LANESEGMENTINFO._serialized_end=4394
  _ROUTINGMASK._serialized_start=4397
  _ROUTINGMASK._serialized_end=4642
  _LANESELECTORFORYCROSSING._serialized_start=4644
  _LANESELECTORFORYCROSSING._serialized_end=4752
  _LANESELECTORFORFREEWAYMERGEOUT._serialized_start=4755
  _LANESELECTORFORFREEWAYMERGEOUT._serialized_end=4907
  _LANESELECTORFORNORMALWAYMERGEIN._serialized_start=4909
  _LANESELECTORFORNORMALWAYMERGEIN._serialized_end=4999
  _LANESELECTORFORNORMAL._serialized_start=5001
  _LANESELECTORFORNORMAL._serialized_end=5107
  _LANESELECTORFORLANECLOSE._serialized_start=5109
  _LANESELECTORFORLANECLOSE._serialized_end=5203
  _LANEMARKSTRATEGYFORNORMAL._serialized_start=5206
  _LANEMARKSTRATEGYFORNORMAL._serialized_end=5419
  _LANESELECTORFORFREEWAYENTRANCE._serialized_start=5422
  _LANESELECTORFORFREEWAYENTRANCE._serialized_end=5555
  _LANESELECTORFORTOLL._serialized_start=5557
  _LANESELECTORFORTOLL._serialized_end=5627
  _SD3YCROSSINGINFO._serialized_start=5630
  _SD3YCROSSINGINFO._serialized_end=5761
  _SPECIAL3YCROSSINGINFO._serialized_start=5764
  _SPECIAL3YCROSSINGINFO._serialized_end=5943
  _LANESELECTORFORFREEWAYTHREEOUTLINKSCROSSING._serialized_start=5946
  _LANESELECTORFORFREEWAYTHREEOUTLINKSCROSSING._serialized_end=6133
  _LANESELECTORFORNORMALTHREEOUTLINKSCROSSING._serialized_start=6136
  _LANESELECTORFORNORMALTHREEOUTLINKSCROSSING._serialized_end=6322
  _LANESELECTORFORNORMALMERGEOUT._serialized_start=6324
  _LANESELECTORFORNORMALMERGEOUT._serialized_end=6414
  _LANESELECTORFORRIGHTTURNLANE._serialized_start=6416
  _LANESELECTORFORRIGHTTURNLANE._serialized_end=6474
  _LANESELECTORFORNORMALMULTITURNRIGHTCROSSING._serialized_start=6477
  _LANESELECTORFORNORMALMULTITURNRIGHTCROSSING._serialized_end=6633
  _LANESELECTORFORNORMALTURNRIGHTTWOOUTLINKS._serialized_start=6635
  _LANESELECTORFORNORMALTURNRIGHTTWOOUTLINKS._serialized_end=6729
  _LANESELECTORFORLONGFREEWAYMERGEINOUT._serialized_start=6731
  _LANESELECTORFORLONGFREEWAYMERGEINOUT._serialized_end=6848
  _SCENESTRATEGYDEBUGINFO._serialized_start=6851
  _SCENESTRATEGYDEBUGINFO._serialized_end=8230
  _SDCROSSINGNAVIINFO._serialized_start=8232
  _SDCROSSINGNAVIINFO._serialized_end=8327
# @@protoc_insertion_point(module_scope)
