import frappe
from frappe.utils import now, add_to_date

def validate(self, method):
    total_amount = 0
    for item in self.items:
        total_amount += item.amount
    self.custom_total_amount = total_amount
    self.custom_expiry_time = get_expiry_datetime(now())


@frappe.whitelist()
def update_start_time(name):
    # Get the current time
    current_time = now()

    # Calculate the expiry time based on the approval time limit
    expiry_time = get_expiry_datetime(current_time)

    # Set the custom start time to the current time
    frappe.db.set_value("Material Request", name, "custom_start_time", current_time)
    
    # Set the custom expiry time
    frappe.db.set_value("Material Request", name, "custom_expiry_time", expiry_time)

def get_expiry_datetime(current_time):
    # Fetch the approval time limit from the Qoala Procurement Configuration
    time_limit = frappe.get_single("Qoala Procurement Configuration")
    
    # Calculate the expiry time based on the approval time limit
    return add_to_date(current_time, hours=time_limit.approval_time_limit)
