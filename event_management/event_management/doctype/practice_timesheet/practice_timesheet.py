# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PracticeTimesheet(Document):
	def validate(self):
		if not self.employee:
			frappe.throw("Employee required (server)")
