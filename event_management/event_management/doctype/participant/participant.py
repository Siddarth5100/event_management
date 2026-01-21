# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Participant(Document):
	def validate(self):
		if self.email:
			exists = frappe.db.exists(
				"Participant",
				{
					"email": self.email,
					"name": ["!=", self.name]
				}
			)
			
			if exists:
				frappe.throw(
					"User already exist"
				)
				
	