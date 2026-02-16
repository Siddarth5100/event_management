import frappe
import json

def test_without_whitelist():
    return "You should not see this"

@frappe.whitelist()
def test_custom_api():
    return "Custom API is working"

@frappe.whitelist()
def ping():
    return{"status": "API is reachable"}

@frappe.whitelist()
def add_timesheet_value(data= None):
    #
    print("Current User:", frappe.session.user)
    print(data, type(data))
    
    # data = json.loads(data)
    # print(data, type(data))

    # doc = frappe.get_doc("Practice Timesheet",)


    return "timesheet"

@frappe.whitelist()
def get_timesheet_title(name):
    doc = frappe.get_doc("Practice Timesheet", name)
    return doc.title












    # doc = frappe.get_doc({
    #     "doctype": "Practice Timesheet",
    #     "title": data["title"],
    #     "series": data["series"],
    #     "company": data["company"],
    #     "currency": data["currency"],
    #     "exchange_rate": data["exchange_rate"],
    #     "sales_invoice": data["sales_invoice"],
    #     "status": data["status"],
    #     "project":data["project"],
    #     "employee": data["employee"],
    #     "employee_name": data["employee_name"],
    #     "department": data["department"]

    # })

    # # # insert will do later
    # # doc.insert()    

    # return doc.name