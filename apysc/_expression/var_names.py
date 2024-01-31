"""This module is for the constants definitions of
the expression's variable names.
"""

from typing_extensions import Final

DOCUMENT: Final[str] = "document"
BLANK_OBJECT: Final[str] = "bo"
DISPLAY_OBJECT: Final[str] = "do"
SVG_FOREIGN_OBJECT_CHILD: Final[str] = "sfoc"
ANY_DISPLAY_OBJECT: Final[str] = "ado"
PARENT: Final[str] = "parent"
GRAPHICS: Final[str] = "g"
POINT2D: Final[str] = "p2d"
RECTANGLE: Final[str] = "rect"
CIRCLE: Final[str] = "circle"
ELLIPSE: Final[str] = "ellipse"
LINE: Final[str] = "line"
POLYLINE: Final[str] = "pline"
POLYGON: Final[str] = "poly"
TRIANGLE: Final[str] = "tri"
PATH: Final[str] = "path"
SPRITE: Final[str] = "sp"
SVG_TEXT: Final[str] = "stxt"
SVG_TEXT_SPAN: Final[str] = "stxtspan"
MULTILINE_TEXT: Final[str] = "mtxt"
ARRAY: Final[str] = "arr"
DICTIONARY: Final[str] = "dct"
INDEX: Final[str] = "idx"
BOOLEAN: Final[str] = "b"
INT: Final[str] = "i"
NUMBER: Final[str] = "n"
STRING: Final[str] = "s"
SNAPSHOT: Final[str] = "snapshot"
ANY: Final[str] = "any"
EVENT: Final[str] = "evt"
MOUSE_EVENT: Final[str] = "mevt"
WHEEL_EVENT: Final[str] = "wevt"
TIMER_EVENT: Final[str] = "tevt"
ANIMATION_EVENT: Final[str] = "aevt"
ENTER_FRAME_EVENT: Final[str] = "eevt"
TIMER: Final[str] = "timer"
DATETIME: Final[str] = "dt"
TIME_DELTA: Final[str] = "td"
LOOP: Final[str] = "loop"
ANIMATION_MOVE: Final[str] = "animmove"
ANIMATION_X: Final[str] = "animx"
ANIMATION_Y: Final[str] = "animy"
ANIMATION_CX: Final[str] = "animcx"
ANIMATION_CY: Final[str] = "animcy"
ANIMATION_WIDTH: Final[str] = "animwidth"
ANIMATION_HEIGHT: Final[str] = "animheight"
ANIMATION_WIDTH_FOR_ELLIPSE: Final[str] = "animwidthforellipse"
ANIMATION_HEIGHT_FOR_ELLIPSE: Final[str] = "animheightforellipse"
ANIMATION_FILL_ALPHA: Final[str] = "animfillalpha"
ANIMATION_FILL_COLOR: Final[str] = "animfillcolor"
ANIMATION_LINE_COLOR: Final[str] = "animlinecolor"
ANIMATION_LINE_ALPHA: Final[str] = "animlinealpha"
ANIMATION_LINE_THICKNESS: Final[str] = "animlinethickness"
ANIMATION_RADIUS: Final[str] = "animradius"
ANIMATION_ROTATION_AROUND_CENTER: Final[str] = "animrotardcenter"
ANIMATION_ROTATION_AROUND_POINT: Final[str] = "animrotardpoint"
ANIMATION_SCALE_X_FROM_CENTER: Final[str] = "animscalexfromcenter"
ANIMATION_SCALE_Y_FROM_CENTER: Final[str] = "animscaleyfromcenter"
ANIMATION_SCALE_X_FROM_POINT: Final[str] = "animscalexfrompoint"
ANIMATION_SCALE_Y_FROM_POINT: Final[str] = "animscaleyfrompoint"
ANIMATION_PARALLEL: Final[str] = "animparallel"
MATCHED: Final[str] = "matched"
MATERIAL_ICON: Final[str] = "mi"
MATERIAL_SEARCH_ICON: Final[str] = "msearchi"
MATERIAL_HOME_ICON: Final[str] = "mhomei"
MATERIAL_ACCOUNT_CIRCLE_ICON: Final[str] = "maccountcirclei"
MATERIAL_SETTINGS_ICON: Final[str] = "msettingsi"
MATERIAL_DONE_ICON: Final[str] = "mdonei"
MATERIAL_INFO_ICON: Final[str] = "minfoi"
MATERIAL_CHECK_CIRCLE_ICON: Final[str] = "mcheckcirclei"
MATERIAL_SHOPPING_CART_ICON: Final[str] = "mshoppingcarti"
MATERIAL_FAVORITE_ICON: Final[str] = "mfavoritei"
MATERIAL_DESCRIPTION_ICON: Final[str] = "mdescriptioni"
MATERIAL_LOGOUT_ICON: Final[str] = "mlogouti"
MATERIAL_FAVORITE_BORDER_ICON: Final[str] = "mfavoriteborderi"
MATERIAL_LOCK_ICON: Final[str] = "mlocki"
MATERIAL_SCHEDULE_ICON: Final[str] = "mschedulei"
MATERIAL_FACE_ICON: Final[str] = "mfacei"
MATERIAL_MANAGE_ACCOUNTS_ICON: Final[str] = "mmanageaccountsi"
MATERIAL_VERIFIED_ICON: Final[str] = "mverifiedi"
MATERIAL_FILTER_ALT_ICON: Final[str] = "mfilteralti"
MATERIAL_THUMB_UP_ICON: Final[str] = "mthumbupi"
MATERIAL_EVENT_ICON: Final[str] = "meventi"
MATERIAL_FINGERPRINT_ICON: Final[str] = "mfingerprinti"
MATERIAL_DASHBOARD_ICON: Final[str] = "mdashboardi"
MATERIAL_LIST_ICON: Final[str] = "mlisti"
MATERIAL_LOGIN_ICON: Final[str] = "mlogini"
MATERIAL_CALENDAR_TODAY_ICON: Final[str] = "mcalendartodayi"
MATERIAL_HIGHLIGHT_OFF_ICON: Final[str] = "mhighlightoffi"
MATERIAL_HELP_ICON: Final[str] = "mhelpi"
MATERIAL_PAID_ICON: Final[str] = "mpaidi"
MATERIAL_TASK_ALT_ICON: Final[str] = "mtaskalti"
MATERIAL_QUESTION_ANSWER_ICON: Final[str] = "mquestionansweri"
MATERIAL_DATE_RANGE_ICON: Final[str] = "mdaterangei"
MATERIAL_ARTICLE_ICON: Final[str] = "marticlei"
MATERIAL_LIGHT_BULB_ICON: Final[str] = "mlightbulbi"
MATERIAL_CREDIT_CARD_ICON: Final[str] = "mcreditcardi"
MATERIAL_PERM_IDENTITY_ICON: Final[str] = "mpermidentityi"
MATERIAL_HISTORY_ICON: Final[str] = "mhistoryi"
MATERIAL_TRENDING_UP_ICON: Final[str] = "mtrendingupi"
MATERIAL_DELETE_OUTLINE_ICON: Final[str] = "mdeleteoutlinei"
MATERIAL_FACT_CHECK_ICON: Final[str] = "mfactchecki"
MATERIAL_ASSIGNMENT_ICON: Final[str] = "massignmenti"
MATERIAL_ARROW_RIGHT_ALT_ICON: Final[str] = "marrowrightalti"
MATERIAL_VIEW_LIST_ICON: Final[str] = "mviewlisti"
MATERIAL_BUILD_ICON: Final[str] = "mbuildi"
MATERIAL_STORE_ICON: Final[str] = "mstorei"
MATERIAL_WORK_ICON: Final[str] = "mworki"
MATERIAL_PRINT_ICON: Final[str] = "mprinti"
MATERIAL_ANALYTICS_ICON: Final[str] = "manalyticsi"
MATERIAL_CALENDAR_MONTH_ICON: Final[str] = "mcalendarmonthi"
MATERIAL_DELETE_FOREVER_ICON: Final[str] = "mdeleteforeveri"
MATERIAL_TODAY_ICON: Final[str] = "mtodayi"
MATERIAL_GRADE_ICON: Final[str] = "mgradei"
MATERIAL_UPDATE_ICON: Final[str] = "mupdatei"
MATERIAL_SAVINGS_ICON: Final[str] = "msavingsi"
MATERIAL_ROOM_ICON: Final[str] = "mroomi"
MATERIAL_CODE_ICON: Final[str] = "mcodei"
MATERIAL_ADD_SHOPPING_CART_ICON: Final[str] = "maddshoppingcarti"
MATERIAL_CONTRACT_SUPPORT_ICON: Final[str] = "mcontractsupporti"
MATERIAL_RECEIPT_ICON: Final[str] = "mreceipti"
MATERIAL_PETS_ICON: Final[str] = "mpetsi"
MATERIAL_EXPLORE_ICON: Final[str] = "mexplorei"
MATERIAL_BOOKMARK_ICON: Final[str] = "mbookmarki"
MATERIAL_ACCOUNT_BOX_ICON: Final[str] = "maccountboxi"
MATERIAL_NOTE_ADD_ICON: Final[str] = "mnoteaddi"
MATERIAL_REORDER_ICON: Final[str] = "mreorderi"
MATERIAL_BOOKMARK_BORDER_ICON: Final[str] = "mbookmarkborderi"
MATERIAL_PENDING_ACTIONS_ICON: Final[str] = "mpendingactionsi"
MATERIAL_SHOPPING_BASKET_ICON: Final[str] = "mshoppingbasketi"
MATERIAL_DRAG_INDICATOR_ICON: Final[str] = "mdragindicatori"
MATERIAL_TOUCH_APP_ICON: Final[str] = "mtouchappi"
MATERIAL_SUPERVISOR_ACCOUNT_ICON: Final[str] = "msupervisoraccounti"
MATERIAL_PENDING_ICON: Final[str] = "mpendingi"
MATERIAL_ZOOM_IN_ICON: Final[str] = "mzoomini"
MATERIAL_ASSESSMENT_ICON: Final[str] = "massessmenti"
MATERIAL_LEADER_BOARD_ICON: Final[str] = "mleaderboardi"
MATERIAL_THUMB_UP_OFF_ALT_ICON: Final[str] = "mthumbupoffalti"
MATERIAL_EXIT_TO_APP_ICON: Final[str] = "mexittoappi"
MATERIAL_ASSIGNMENT_IND_ICON: Final[str] = "massignmentindi"
MATERIAL_PUBLISHED_WITH_CHANGES_ICON: Final[str] = "mpublishedwithchangesi"
MATERIAL_CARD_GIFTCARD_ICON: Final[str] = "mcardgiftcardi"
MATERIAL_VIEW_IN_AR_ICON: Final[str] = "mviewinari"
MATERIAL_FEEDBACK_ICON: Final[str] = "mfeedbacki"
MATERIAL_WORK_OUTLINE_ICON: Final[str] = "mworkoutlinei"
MATERIAL_TIMELINE_ICON: Final[str] = "mtimelinei"
MATERIAL_SWAP_HORIZ_ICON: Final[str] = "mswaphorizi"
MATERIAL_ASSIGNMENT_TURNED_IN_ICON: Final[str] = "massignmentturnedini"
MATERIAL_TIPS_AND_UPDATES_ICON: Final[str] = "mtipsandupdatesi"
