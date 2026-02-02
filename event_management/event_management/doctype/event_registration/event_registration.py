# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus
from frappe.utils import getdate


class EventRegistration(Document):
	def validate(self):

		# validate is user already registered to the event
		exists = frappe.db.exists(
			"Event Registration",
			{
				"participant": self.participant,
				"email": self.email,
				"event_detail": self.event_detail,
				"name": ["!=", self.name]
			}
		)
	
		if exists:
			frappe.throw("Already registered to this event, select new one")

		# Organiser validation
		organiser_name = frappe.db.exists(
			"Event Registration",
			{
				"event_date": self.event_date,
				"event_detail": ("!=", self.event_detail),
				"organiser_name": self.organiser_name,
				"from_time": ("=", self.from_time),
				"to_time": ("=", self.to_time),
				"docstatus": 0
			}
		)
		if organiser_name:
			frappe.throw("Organiser already assigned")

	def on_submit(self):
		if not self.email:
			return
		
		frappe.sendmail(
			recipients = self.email,
			subject = "Event Registration Confirmed",
			message = f"""
		Hello {self.participant},

		Your registration for the event "{self.event_detail}" has been successfully submitted.

		Thank you.
		""",
			now = True
		)

	