app_name = "envision_crm"
app_title = "Envision CRM"
app_publisher = "Envision"
app_description = "Envision CRM"
app_email = "harsh@sanskartechnolab.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/envision_crm/css/envision_crm.css"
app_include_js = [
    # "/assets/envision_crm/js/quotation.js",
    # "/assets/envision_crm/js/opportunity.js",
    # "/assets/envision_crm/js/cost_estimation.js",
]

# include js, css files in header of web template
# web_include_css = "/assets/envision_crm/css/envision_crm.css"
# web_include_js = "/assets/envision_crm/js/envision_crm.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "envision_crm/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Cost Estimation": "public/js/cost_estimation.js",
    "Opportunity": "public/js/opportunity.js",
    "Lead": "public/js/lead.js",
    "Quotation": "public/js/quotation.js",
}


override_doctype_dashboards = {
    "Opportunity": "envision_crm.override.opportunity_dashboard.get_data",
    # "Quotation": "envision_crm.override.quotation_dashboard.get_data",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "envision_crm/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "envision_crm.utils.jinja_methods",
# 	"filters": "envision_crm.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "envision_crm.install.before_install"
# after_install = "envision_crm.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "envision_crm.uninstall.before_uninstall"
# after_uninstall = "envision_crm.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "envision_crm.utils.before_app_install"
# after_app_install = "envision_crm.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "envision_crm.utils.before_app_uninstall"
# after_app_uninstall = "envision_crm.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "envision_crm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    # "Lead": {
    #     "before_save": "envision_crm.envision_crm.api.lead.naming_series",
    # },
    # "Opportunity": {
    #     "before_save": "envision_crm.envision_crm.api.opportunity.naming_series",
    # },
    "Quotation": {
        "on_submit": "envision_crm.envision_crm.api.quotation_submission.quotation_submission",
    },
    # "Quotation": {
    #     "on_submit": "your_app_path.quotation.submit_cost_estimation",
    # }
    # "Cost Estimation": {
    #     "before_save": "envision_crm.envision_crm.api.cost_estimation.naming_series",
    # },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"envision_crm.tasks.all"
# 	],
# 	"daily": [
# 		"envision_crm.tasks.daily"
# 	],
# 	"hourly": [
# 		"envision_crm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"envision_crm.tasks.weekly"
# 	],
# 	"monthly": [
# 		"envision_crm.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "envision_crm.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "envision_crm.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "envision_crm.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["envision_crm.utils.before_request"]
# after_request = ["envision_crm.utils.after_request"]

# Job Events
# ----------
# before_job = ["envision_crm.utils.before_job"]
# after_job = ["envision_crm.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"envision_crm.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


# fixtures = [
#     {
#         "doctype": "Property Setter",
#         "filters": [
#             ["doc_type", "in", ["Lead", "Opportunity"]],
#             ["property", "=", "naming_series"],
#         ],
#     },
#     {
#         "doctype": "Print Format",
#         "filters": ["name", "in", ["Print Offer"]],
#     },
#     {
#         "doctype": "Letter Head",
#         "filters": ["name", "in", ["Offer Print"]],
#     },
# ]

# fixtures = [
#     # {
#     #     "dt": "Property Setter",
#     #     "filters": [
#     #         ["doc_type", "in", ["Lead", "Opportunity"]],
#     #         ["property", "=", "naming_series"],
#     #     ],
#     # },
#     {
#         "dt": "Print Format",
#         "filters": ["name", "in", ["Print Offer"]],
#     },
#     {
#         "dt": "Letter Head",
#         "filters": ["name", "in", ["Offer Print"]],
#     },
# ]

fixtures = [
    # {
    #     "dt": "Property Setter",
    #     "filters": [
    #         ["doc_type", "in", ["Lead", "Opportunity"]],
    #         ["property", "=", "naming_series"],
    #     ],
    # },

#     {
#      "dt": "Custom DocPerm",
#         "filters": [
#             ["parent", "in", ["Lead","Opportunity","Cost Estimation","Quotation","Quotation Print Templates"]]
#         ],
# },


    # # "Role",
    # {"dt": "Workspace", "filters": [["name", "=", "CRM"]]},                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    {"dt": "Print Format", "filters": [["name", "in", ["Print Offer","Print Offer PDF","Quotation-EnTech"]]]},
    # # {
    # #     "dt": "Letter Head",                                                                                                                                                                                                            
    # #     "filters": [["name", "in", ["Offer Print", "Continuous Head"]]],
    # # },
    # {
    #     "dt": "Workflow State",
    #     "filters": [
    #         ["name", "in", ["Reviewed ", "Submitted", "Pending", "Rework", "Cancelled"]]
    #     ],
    # },
    # {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    #     "dt": "Workflow Action Master",
    #     "filters": [
    #         [
    #             "name",
    #             "in",
    #             ["Review ", "Reject","Rework", "Approve", "Submit for Review", "Cancel"],
    #         ]
    #     ],
    # },
    # {
    #     "dt": "Workflow",
    #     "filters": [["name", "in", ["Quotation Workflow"]]],
    # },
]
