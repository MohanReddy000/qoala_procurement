import frappe

def before_submit(doc, method):
    doc.custom_approved_by = frappe.session.user