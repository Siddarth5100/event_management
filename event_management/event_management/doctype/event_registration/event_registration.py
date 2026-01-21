# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EventRegistration(Document):
	def validate(self):
		exists = frappe.db.exists(
			"Event Registration",
			{
				"participant": self.participant,
				"email": self.email,
				"event_detail": self.event_detail,
				"event_date": self.event_date,
				"name": ["!=", self.name]
			}
		)
	
		if exists:
			frappe.throw("Already registered to this event, select new one")