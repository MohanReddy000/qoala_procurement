app_name = "qoala_procurement"
app_title = "Qoala Procurement"
app_publisher = "Mohan"
app_description = "Qoala Procurement"
app_email = "mohan.k@promantia.com"
app_license = "MIT"

# Includes in <head>
# ------------------

fixtures = ["Workflow", "Workflow State",
            {"dt": "Role", "filters": [["Name", "in", [
                "AVP/VP Finance", "Department Head - 1", "Bu Head", "Department Head", "Procurement"]]]},
            {"dt": "Custom Field", "filters": [
                ["module", "=", "Qoala Procurement"]]},
            {"dt": "Property Setter", "filters": [
                ["module", "=", "Qoala Procurement"]]},
            ]

# include js, css files in header of desk.html
# app_include_css = "/assets/qoala_procurement/css/qoala_procurement.css"
# app_include_js = "/assets/qoala_procurement/js/qoala_procurement.js"

# include js, css files in header of web template
# web_include_css = "/assets/qoala_procurement/css/qoala_procurement.css"
# web_include_js = "/assets/qoala_procurement/js/qoala_procurement.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "qoala_procurement/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

doctype_js = {
    "Material Request": "qoala_procurement/doctype/material_request/material_request.js"
}
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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
# 	"methods": "qoala_procurement.utils.jinja_methods",
# 	"filters": "qoala_procurement.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "qoala_procurement.install.before_install"
# after_install = "qoala_procurement.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "qoala_procurement.uninstall.before_uninstall"
# after_uninstall = "qoala_procurement.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "qoala_procurement.utils.before_app_install"
# after_app_install = "qoala_procurement.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "qoala_procurement.utils.before_app_uninstall"
# after_app_uninstall = "qoala_procurement.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qoala_procurement.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
    "Material Request": {
        "validate": "qoala_procurement.qoala_procurement.doctype.material_request.material_request.validate"
    },
    "Purchase Order": {
        "validate": "qoala_procurement.qoala_procurement.doctype.purchase_order.purchase_order.before_submit"
    },
}


# Scheduled Tasks
# ---------------

scheduler_events = {
	"hourly": [
		"qoala_procurement.scheduler_events.update_sla_status"
	]
}

# Testing
# -------

# before_tests = "qoala_procurement.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "qoala_procurement.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "qoala_procurement.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["qoala_procurement.utils.before_request"]
# after_request = ["qoala_procurement.utils.after_request"]

# Job Events
# ----------
# before_job = ["qoala_procurement.utils.before_job"]
# after_job = ["qoala_procurement.utils.after_job"]

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
# 	"qoala_procurement.auth.validate"
# ]
