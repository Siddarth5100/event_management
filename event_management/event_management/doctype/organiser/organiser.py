# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Organiser(Document):
	def validate(self):
		
		# # if empty field will return
		# if not self.email_id:
		# 	return

		# if not self.mobile_number:
		# 	frappe.msgprint("Error")

		# validate organiser is already exist
		exists = frappe.db.exists(
			"Organiser",
			{
				"email_id": self.email_id
				# "name": ["!=", self.name]
			}
		)

		if exists:
			frappe.throw("Organiser already exist!")
