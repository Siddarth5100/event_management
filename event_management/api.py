import frappe


def test_without_whitelist():
    return "You should not see this"

@frappe.whitelist()
def test_custom_api():
    return "Custom API is working"

@frappe.whitelist()
def update_timesheet_value():
   return "1st API"

@frappe.whitelist()
def ping():
    return{"status": "API is reachable"}

@frappe.whitelist()
def update_timesheet(name):
    if not frappe.db.exists("Practie Timesheet", name):
        return "Timesheet not found"
    
    doc = frappe.get_doc("Practice Timesheet", name)
    return doc.name