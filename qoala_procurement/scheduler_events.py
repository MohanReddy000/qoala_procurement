import frappe
from datetime import datetime, timedelta
from frappe.utils import now, today, getdate


@frappe.whitelist()
def update_sla_status():
    # Fetch the approval time limit from the Procurement Configuration doctype
    config = frappe.get_single("Qoala Procurement Configuration")
    approval_time_limit = config.approval_time_limit or 5

    # Get the current time
    now = datetime.now()

    # Fetch all materials that are pending approval and check if they exceed the time limit
    materials = frappe.get_all("Material Request", filters={"custom_sla_status": ["!=", "Expired"], "workflow_state": ["!=", "Approved by D-head"]}, fields=["name", "custom_start_time"])

    for material in materials:
        if (now - material.get('custom_start_time')).total_seconds() / 3600 > approval_time_limit:
            # Update the status to hold
            frappe.db.set_value("Material Request", material.get("name"), "custom_sla_status", "Expired")
            frappe.db.commit()
