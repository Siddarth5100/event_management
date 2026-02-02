# Copyright (c) 2026, siddarth and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	# frappe.errprint(filters)
	columns = [
		{
			"fieldname": "make",
			"label": "Make",
			"fieldtype": "Data",
			"width": 150	
		}
	]
	
	
	data = [
		{"make": "Hyundai"}, {"make": "BMW"}, {"make":"Tata"}
	]

	event_register = frappe.get_all(
			"Event Registration",
			fields = ["docstatus", ""]
		)
	


	return columns, data
