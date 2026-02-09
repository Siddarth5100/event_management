# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Testing(Document):

	def on_load(self):
		if self.qty and self.rate:
			self.total = self.qty * self.rate
		else:
		 	self.total = 0