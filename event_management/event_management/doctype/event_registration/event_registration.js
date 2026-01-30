// Copyright (c) 2026, siddarth and contributors
// For license information, please see license.txt

console.log("JS loaded")

frappe.ui.form.on("Event Registration", {
    event_detail(frm) {
	    console.log("Event selected:", frm.doc.event_detail);
    }
});
