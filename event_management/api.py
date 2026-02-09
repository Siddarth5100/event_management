import frappe

@frappe.whitelist()
def test_without_whitelist():
    return "You should not see this"

