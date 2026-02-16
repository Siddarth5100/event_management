// Copyright (c) 2026, siddarth and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Practice Timesheet", {
// 	refresh(frm) {
//         console.log("--------", frm)
//         if (!frm.is_new()) {
//             frappe.call({
//                 method: "event_management.api.get_timesheet_title",
//                 args:{
//                     name: frm.doc.name
//                 },
//                 callback: function(r) {
//                     console.log("-----------Response:", r);
//                 }
//             });
// 	    }
//     }
// });

console.log("JS file loaded");

frappe.ui.form.on("Practice Timesheet", {
    refresh(frm) {
        console.log("Form loaded");

        // frm.add_custom_button("Click Me", function() {
        //     frappe.msgprint("Button Clicked");
        // });

        // frm.set_value("title", "open");
        // console.log("-----")

        // if (frm.doc.title === "c") {
        //     frappe.msgprint("This document is closed");
        // }

        // if (!frm.is_new()) {
        //     frm.set_df_property("status", "read_only", 1);
        // }

    }
});

// frappe.ui.form.on("Practice Timesheet", {
    
//     validate(frm) {
//         console.log("-------------------")
//         console.log("Validate running");

//         if (!frm.doc.employee) {
//             frappe.throw("Employee is mandatory");
//         }
//     }
// })

frappe.ui.form.on("Practice Timesheet", {
    refresh(frm) {
        console.log("custom button test")
        frm.add_custom_button("Approve", function() {
            frappe.msgprint("Clicked Approve button")
        })
        
        frm.add_custom_button("Deny", function() {
            frappe.msgprint("Clicked Deny button")
        })
    }
});

frappe.ui.form.on("Practice Timesheet", {
    refresh(frm) {
        console.log("---------")
        frm.add_custom_button("Click me", function() {
            frappe.msgprint("Thaman clicked me")
        })
    }
});

frappe.ui.form.on("Practice Timesheet", {
    refresh(frm) {
        if (frm.is_new()) {
            console.log("Test")
            frm.set_value("status", "Draft");

        console.log("readonly loaded")
        if (!frm.is_new()) {
            frm.set_df_property("currency", "read-only", 1);
        }
        }
    }
})


