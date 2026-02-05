# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class EventDetail(Document):
	def validate(self):

		# to avoid editing the record once created
		if not self.is_new():
			frappe.throw("Record already exist, can't edit")

		# capacity check
		if self.capacity <= 0:
			frappe.throw("Capacity should not be in negative or empty")
		
		# # just to check added this validation
		# if self.capacity >= 50:
		# 	frappe.throw("Limit exceeds! Should not be more than 50")


		# duplicate event name and date check
		if not self.event_name or not self.date:
			return
		
		exists = frappe.db.exists(
			"Event Detail",
			{
				"date": self.date,
				"from_time": self.from_time,
				"to_time": self.to_time,
				"name": ["!=", self.name]
			}
		)

		if exists:
			frappe.throw("Event with same date and time already exists")


		# validate from time and to time
		if self.from_time >= self.to_time:
			frappe.throw("From time cannot be greater than to time")
		
		if getdate(self.date) < getdate():
			frappe.throw("Enter current or future date")

		# get organiser details from db
		assign_organiser = frappe.get_all("Organiser", fields=["organiser_name", "role"])
		
		# get event detail from db
		event_detail = frappe.get_all("Event Detail", fields=["event_name","date","to_time","organiser"]) 

		for org in assign_organiser:
			check_organiser = frappe.db.exists(
				"Event Detail",
				{
					"organiser": org.organiser_name
				}
			)

			if not check_organiser:
				self.organiser = org.organiser_name
				break
			
		# if not self.organiser:
		# 	frappe.throw("No organiser")
		
		
		
		