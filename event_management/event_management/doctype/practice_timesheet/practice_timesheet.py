# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import time

class PracticeTimesheet(Document):
	# def validate(self):
	# 	if not self.employee:
	# 		frappe.throw("Employee required (server)")


	pass
# @frappe.whitelist()
# def test_call():
# 	return "mesage from server"

# @frappe.whitelist()
# def test_call():
# 	time.sleep(5)
# 	return "Done after 5 sec"
	
# @frappe.whitelist()
# def say_hello(name):
# 	return f"Hello {name}"

@frappe.whitelist()
def test_recap(title=None, company=None):
	return f"Employee: {title}, Hours Worked: {company}"

@frappe.whitelist()
def combine_field(title=None, company=None):
	return f"{title} + {company}"