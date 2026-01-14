# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EventDetail(Document):
	def validate(self):
		if self.capacity <= 0:
			frappe.throw("Capacity should not be in negative or empty")