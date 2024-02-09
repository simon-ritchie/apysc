"""isort:skip_file"""

# flake8: noqa

from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.number import Number as Float
from apysc._type.boolean import Boolean
from apysc._type.boolean import Boolean as Bool
from apysc._type.string import String
from apysc._type.string import String as Str
from apysc._type.array import Array
from apysc._type.dictionary import Dictionary
from apysc._type.any_value import AnyValue
from apysc._branch._if import If
from apysc._branch._elif import Elif
from apysc._branch._else import Else
from apysc._loop.for_array_indices import ForArrayIndices
from apysc._loop.for_array_values import ForArrayValues
from apysc._loop.for_array_indices_and_values import ForArrayIndicesAndValues
from apysc._loop.for_dict_keys import ForDictKeys
from apysc._loop.for_dict_values import ForDictValues
from apysc._loop.for_dict_keys_and_values import ForDictKeysAndValues
from apysc._loop._continue import Continue
from apysc._loop._range import range
from apysc._display.display_object import DisplayObject
from apysc._display._document import document
from apysc._display.sprite import Sprite
from apysc._display.graphics import Graphics
from apysc._display.stage import Stage
from apysc._display.stage import get_stage
from apysc._display.triangle import Triangle
from apysc._display.rectangle import Rectangle
from apysc._display.circle import Circle
from apysc._display.ellipse import Ellipse
from apysc._display.line import Line
from apysc._display.polyline import Polyline
from apysc._display.polygon import Polygon
from apysc._display.line_caps import LineCaps
from apysc._display.line_joints import LineJoints
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.path import Path
from apysc._display.svg_text import SvgText
from apysc._display.svg_text_align_mixin import SvgTextAlign
from apysc._display.svg_text_span import SvgTextSpan
from apysc._display.multi_line_text import MultiLineText
from apysc._display.css_text_align import CssTextAlign
from apysc._display.css_text_align_last import CssTextAlignLast
from apysc._geom.point2d import Point2D
from apysc._geom.path_label import PathLabel
from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_move_to import PathMoveTo
from apysc._geom.path_line_to import PathLineTo
from apysc._geom.path_horizontal import PathHorizontal
from apysc._geom.path_vertical import PathVertical
from apysc._geom.path_close import PathClose
from apysc._geom.path_bezier_2d import PathBezier2D
from apysc._geom.path_bezier_2d_continual import PathBezier2DContinual
from apysc._geom.path_bezier_3d import PathBezier3D
from apysc._geom.path_bezier_3d_continual import PathBezier3DContinual
from apysc._geom.path_data import PathData
from apysc._geom.rectangle_geom import RectangleGeom
from apysc._event.event import Event
from apysc._event.mouse_event import MouseEvent
from apysc._event.wheel_event import WheelEvent
from apysc._event.timer_event import TimerEvent
from apysc._event.animation_event import AnimationEvent
from apysc._event.enter_frame_event import EnterFrameEvent
from apysc._event.mouse_event_type import MouseEventType
from apysc._console._trace import trace
from apysc._console._trace import trace as print
from apysc._console.assertion import assert_equal
from apysc._console.assertion import assert_not_equal
from apysc._console.assertion import assert_true
from apysc._console.assertion import assert_false
from apysc._console.assertion import assert_greater
from apysc._console.assertion import assert_greater_equal
from apysc._console.assertion import assert_less
from apysc._console.assertion import assert_less_equal
from apysc._console.assertion import assert_arrays_equal
from apysc._console.assertion import assert_arrays_not_equal
from apysc._console.assertion import assert_dicts_equal
from apysc._console.assertion import assert_dicts_not_equal
from apysc._console.assertion import assert_defined
from apysc._console.assertion import assert_undefined
from apysc._event.document_mouse_wheel_func import bind_wheel_event_to_document
from apysc._event.document_mouse_wheel_func import unbind_wheel_event_all_from_document
from apysc._event.document_mouse_wheel_func import unbind_wheel_event_from_document
from apysc._html.exporter import save_overall_html
from apysc._expression.expression_data_util import append_js_expression
from apysc._jupyter.jupyter_util import display_on_jupyter
from apysc._jupyter.jupyter_util import display_on_colaboratory
from apysc._time.fps import FPS
from apysc._time.timer import Timer
from apysc._time.datetime_ import DateTime
from apysc._time.timedelta_ import TimeDelta
from apysc._html.debug_mode import set_debug_mode
from apysc._html.debug_mode import unset_debug_mode
from apysc._html.debug_mode import is_debug_mode
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type._return import Return
from apysc._type._delete import delete
from apysc._animation.easing import Easing
from apysc._animation.animation_base import AnimationBase
from apysc._animation.animation_move import AnimationMove
from apysc._animation.animation_x import AnimationX
from apysc._animation.animation_y import AnimationY
from apysc._animation.animation_cx import AnimationCx
from apysc._animation.animation_cy import AnimationCy
from apysc._animation.animation_width import AnimationWidth
from apysc._animation.animation_height import AnimationHeight
from apysc._animation.animation_width_for_ellipse import AnimationWidthForEllipse
from apysc._animation.animation_height_for_ellipse import AnimationHeightForEllipse
from apysc._animation.animation_radius import AnimationRadius
from apysc._animation.animation_fill_alpha import AnimationFillAlpha
from apysc._animation.animation_fill_color import AnimationFillColor
from apysc._animation.animation_line_color import AnimationLineColor
from apysc._animation.animation_line_alpha import AnimationLineAlpha
from apysc._animation.animation_line_thickness import AnimationLineThickness
from apysc._animation.animation_rotation_around_center import AnimationRotationAroundCenter
from apysc._animation.animation_rotation_around_point import AnimationRotationAroundPoint
from apysc._animation.animation_scale_x_from_center import AnimationScaleXFromCenter
from apysc._animation.animation_scale_y_from_center import AnimationScaleYFromCenter
from apysc._animation.animation_scale_x_from_point import AnimationScaleXFromPoint
from apysc._animation.animation_scale_y_from_point import AnimationScaleYFromPoint
from apysc._animation.animation_parallel import AnimationParallel
from apysc._math.math import Math
from apysc._auto_reloading.auto_reloading_decorator import set_auto_reloading
from apysc._chart.x_axis_settings import XAxisSettings
from apysc._chart.y_axis_single_column_settings import YAxisSingleColumnSettings
from apysc._chart.x_axis_label_position import XAxisLabelPosition
from apysc._chart.y_axis_label_position import YAxisLabelPosition
from apysc._type.true import _True as __True
from apysc._type.false import _False as __False
from apysc._color.color import Color
from apysc._color.colors import Colors
from apysc._color.colors import MaterialDesignColors
from apysc._color.colorless import COLORLESS
from apysc._material_design.icon.material_icon_base import MaterialIconBase
from apysc._material_design.icon.material_search_icon import MaterialSearchIcon
from apysc._material_design.icon.material_home_icon import MaterialHomeIcon
from apysc._material_design.icon.material_account_circle_icon import MaterialAccountCircleIcon
from apysc._material_design.icon.material_settings_icon import MaterialSettingsIcon
from apysc._material_design.icon.material_done_icon import MaterialDoneIcon
from apysc._material_design.icon.material_info_icon import MaterialInfoIcon
from apysc._material_design.icon.material_check_circle_icon import MaterialCheckCircleIcon
from apysc._material_design.icon.material_shopping_cart_icon import MaterialShoppingCartIcon
from apysc._material_design.icon.material_favorite_icon import MaterialFavoriteIcon
from apysc._material_design.icon.material_description_icon import MaterialDescriptionIcon
from apysc._material_design.icon.material_logout_icon import MaterialLogoutIcon
from apysc._material_design.icon.material_favorite_border_icon import MaterialFavoriteBorderIcon
from apysc._material_design.icon.material_lock_icon import MaterialLockIcon
from apysc._material_design.icon.material_schedule_icon import MaterialScheduleIcon
from apysc._material_design.icon.material_face_icon import MaterialFaceIcon
from apysc._material_design.icon.material_manage_accounts_icon import MaterialManageAccountsIcon
from apysc._material_design.icon.material_verified_icon import MaterialVerifiedIcon
from apysc._material_design.icon.material_filter_alt_icon import MaterialFilterAltIcon
from apysc._material_design.icon.material_thumb_up_icon import MaterialThumbUpIcon
from apysc._material_design.icon.material_event_icon import MaterialEventIcon
from apysc._material_design.icon.material_fingerprint_icon import MaterialFingerprintIcon
from apysc._material_design.icon.material_dashboard_icon import MaterialDashboardIcon
from apysc._material_design.icon.material_list_icon import MaterialListIcon
from apysc._material_design.icon.material_login_icon import MaterialLoginIcon
from apysc._material_design.icon.material_calendar_today_icon import MaterialCalendarTodayIcon
from apysc._material_design.icon.material_highlight_off_icon import MaterialHighlightOffIcon
from apysc._material_design.icon.material_help_icon import MaterialHelpIcon
from apysc._material_design.icon.material_paid_icon import MaterialPaidIcon
from apysc._material_design.icon.material_task_alt_icon import MaterialTaskAltIcon
from apysc._material_design.icon.material_question_answer_icon import MaterialQuestionAnswerIcon
from apysc._material_design.icon.material_date_range_icon import MaterialDateRangeIcon
from apysc._material_design.icon.material_article_icon import MaterialArticleIcon
from apysc._material_design.icon.material_light_bulb_icon import MaterialLightBulbIcon
from apysc._material_design.icon.material_credit_card_icon import MaterialCreditCardIcon
from apysc._material_design.icon.material_perm_identity_icon import MaterialPermIdentityIcon
from apysc._material_design.icon.material_history_icon import MaterialHistoryIcon
from apysc._material_design.icon.material_trending_up_icon import MaterialTrendingUpIcon
from apysc._material_design.icon.material_delete_outline_icon import MaterialDeleteOutlineIcon
from apysc._material_design.icon.material_fact_check_icon import MaterialFactCheckIcon
from apysc._material_design.icon.material_assignment_icon import MaterialAssignmentIcon
from apysc._material_design.icon.material_arrow_right_alt_icon import MaterialArrowRightAltIcon
from apysc._material_design.icon.material_view_list_icon import MaterialViewListIcon
from apysc._material_design.icon.material_build_icon import MaterialBuildIcon
from apysc._material_design.icon.material_store_icon import MaterialStoreIcon
from apysc._material_design.icon.material_work_icon import MaterialWorkIcon
from apysc._material_design.icon.material_print_icon import MaterialPrintIcon
from apysc._material_design.icon.material_analytics_icon import MaterialAnalyticsIcon
from apysc._material_design.icon.material_calendar_month_icon import MaterialCalendarMonthIcon
from apysc._material_design.icon.material_delete_forever_icon import MaterialDeleteForeverIcon
from apysc._material_design.icon.material_today_icon import MaterialTodayIcon
from apysc._material_design.icon.material_grade_icon import MaterialGradeIcon
from apysc._material_design.icon.material_update_icon import MaterialUpdateIcon
from apysc._material_design.icon.material_savings_icon import MaterialSavingsIcon
from apysc._material_design.icon.material_room_icon import MaterialRoomIcon
from apysc._material_design.icon.material_code_icon import MaterialCodeIcon
from apysc._material_design.icon.material_add_shopping_cart_icon import MaterialAddShoppingCartIcon
from apysc._material_design.icon.material_contract_support_icon import MaterialContractSupportIcon
from apysc._material_design.icon.material_receipt_icon import MaterialReceiptIcon
from apysc._material_design.icon.material_pets_icon import MaterialPetsIcon
from apysc._material_design.icon.material_explore_icon import MaterialExploreIcon
from apysc._material_design.icon.material_bookmark_icon import MaterialBookmarkIcon
from apysc._material_design.icon.material_account_box_icon import MaterialAccountBoxIcon
from apysc._material_design.icon.material_note_add_icon import MaterialNoteAddIcon
from apysc._material_design.icon.material_reorder_icon import MaterialReorderIcon
from apysc._material_design.icon.material_bookmark_border_icon import MaterialBookmarkBorderIcon
from apysc._material_design.icon.material_pending_actions_icon import MaterialPendingActionsIcon
from apysc._material_design.icon.material_shopping_basket_icon import MaterialShoppingBasketIcon
from apysc._material_design.icon.material_drag_indicator_icon import MaterialDragIndicatorIcon
from apysc._material_design.icon.material_touch_app_icon import MaterialTouchAppIcon
from apysc._material_design.icon.material_supervisor_account_icon import MaterialSupervisorAccountIcon
from apysc._material_design.icon.material_pending_actions_icon import MaterialPendingActionsIcon
from apysc._material_design.icon.material_pending_icon import MaterialPendingIcon
from apysc._material_design.icon.material_zoom_in_icon import MaterialZoomInIcon
from apysc._material_design.icon.material_assessment_icon import MaterialAssessmentIcon
from apysc._material_design.icon.material_leader_board_icon import MaterialLeaderBoardIcon
from apysc._material_design.icon.material_thumb_up_off_alt_icon import MaterialThumbUpOffAltIcon
from apysc._material_design.icon.material_exit_to_app_icon import MaterialExitToAppIcon
from apysc._material_design.icon.material_assignment_ind_icon import MaterialAssignmentIndIcon
from apysc._material_design.icon.material_published_with_changes_icon import MaterialPublishedWithChangesIcon
from apysc._material_design.icon.material_card_giftcard_icon import MaterialCardGiftcardIcon
from apysc._material_design.icon.material_view_in_ar_icon import MaterialViewInArIcon
from apysc._material_design.icon.material_feedback_icon import MaterialFeedbackIcon
from apysc._material_design.icon.material_work_outline_icon import MaterialWorkOutlineIcon
from apysc._material_design.icon.material_timeline_icon import MaterialTimelineIcon
from apysc._material_design.icon.material_swap_horiz_icon import MaterialSwapHorizIcon
from apysc._material_design.icon.material_assignment_turned_in_icon import MaterialAssignmentTurnedInIcon
from apysc._material_design.icon.material_tips_and_updates_icon import MaterialTipsAndUpdatesIcon
from apysc._material_design.icon.material_dns_icon import MaterialDnsIcon
from apysc._material_design.icon.material_flight_takeoff_icon import MaterialFlightTakeoffIcon
from apysc._material_design.icon.material_space_dashboard_icon import MaterialSpaceDashboardIcon
from apysc._material_design.icon.material_book_icon import MaterialBookIcon
from apysc._material_design.icon.material_contact_page_icon import MaterialContactPageIcon
from apysc._material_design.icon.material_alarm_icon import MaterialAlarmIcon
from apysc._material_design.icon.material_translate_icon import MaterialTranslateIcon
from apysc._material_design.icon.material_pan_tool_icon import MaterialPanToolIcon
from apysc._material_design.icon.material_edit_calendar_icon import MaterialEditCalendarIcon
from apysc._material_design.icon.material_supervised_user_circle_icon import MaterialSupervisedUserCircleIcon
from apysc._material_design.icon.material_minimize_icon import MaterialMinimizeIcon
from apysc._material_design.icon.material_extension_icon import MaterialExtensionIcon
from apysc._material_design.icon.material_rocket_launch_icon import MaterialRocketLaunchIcon
from apysc._material_design.icon.material_question_mark_icon import MaterialQuestionMarkIcon
from apysc._material_design.icon.material_get_app_icon import MaterialGetAppIcon
from apysc._material_design.icon.material_add_task_icon import MaterialAddTaskIcon
from apysc._material_design.icon.material_help_center_icon import MaterialHelpCenterIcon
from apysc._material_design.icon.material_hourglass_empty_icon import MaterialHourglassEmptyIcon
from apysc._material_design.icon.material_trending_flat_icon import MaterialTrendingFlatIcon
from apysc._material_design.icon.material_accessibility_new_icon import MaterialAccessibilityNewIcon
from apysc._material_design.icon.material_rule_icon import MaterialRuleIcon
from apysc._material_design.icon.material_thumb_down_icon import MaterialThumbDownIcon
from apysc._material_design.icon.material_ads_click_icon import MaterialAdsClickIcon
from apysc._material_design.icon.material_source_icon import MaterialSourceIcon
from apysc._material_design.icon.material_find_in_page_icon import MaterialFindInPageIcon
from apysc._material_design.icon.material_dashboard_customize_icon import MaterialDashboardCustomizeIcon
from apysc._material_design.icon.material_support_icon import MaterialSupportIcon
from apysc._material_design.icon.material_flutter_dash_icon import MaterialFlutterDashIcon
from apysc._material_design.icon.material_redeem_icon import MaterialRedeemIcon
from apysc._material_design.icon.material_close_full_screen_icon import MaterialCloseFullScreenIcon
from apysc._material_design.icon.material_swap_vert_icon import MaterialSwapVertIcon
from apysc._material_design.icon.material_arrow_circle_right_icon import MaterialArrowCircleRightIcon
from apysc._material_design.icon.material_view_headline_icon import MaterialViewHeadlineIcon
from apysc._material_design.icon.material_restore_icon import MaterialRestoreIcon
from apysc._material_design.icon.material_dangerous_icon import MaterialDangerousIcon
from apysc._material_design.icon.material_euro_symbol_icon import MaterialEuroSymbolIcon
from apysc._material_design.icon.material_group_work_icon import MaterialGroupWorkIcon
from apysc._material_design.icon.material_sensors_icon import MaterialSensorsIcon
from apysc._material_design.icon.material_compare_arrows_icon import MaterialCompareArrowsIcon
from apysc._material_design.icon.material_table_view_icon import MaterialTableViewIcon
from apysc._material_design.icon.material_privacy_tip_icon import MaterialPrivacyTipIcon

True_: __True = __True()
False_: __False = __False()

__version__: str = "4.1.15"
