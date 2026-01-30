# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Participant(Document):
	def validate(self):

		# validate exisitng user
		if not self.email:
			return
		
		exists = frappe.db.exists(
			"Participant",
			{
				"email": self.email,
				"name": ["!=", self.name]
			}
		)
			
		if exists:
			frappe.throw("User already exist!")

