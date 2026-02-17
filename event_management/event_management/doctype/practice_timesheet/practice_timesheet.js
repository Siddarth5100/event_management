// Copyright (c) 2026, siddarth and contributors
// For license information, please see license.txt

// const { useCallback } = require("react")

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

// console.log("JS file loaded");

// frappe.ui.form.on("Practice Timesheet", {
//     refresh(frm) {
//         console.log("Form loaded");

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

//     }
// });

// frappe.ui.form.on("Practice Timesheet", {
    
//     validate(frm) {
//         console.log("-------------------")
//         console.log("Validate running");

//         if (!frm.doc.employee) {
//             frappe.throw("Employee is mandatory");
//         }
//     }
// })

// frappe.ui.form.on("Practice Timesheet", {
//     refresh(frm) {
//         console.log("custom button test")
//         frm.add_custom_button("Approve", function() {
//             frappe.msgprint("Clicked Approve button")
//         })
        
//         frm.add_custom_button("Deny", function() {
//             frappe.msgprint("Clicked Deny button")
//         })
//     }
// });

// frappe.ui.form.on("Practice Timesheet", {
//     refresh(frm) {
//         console.log("---------")
//         frm.add_custom_button("Click me", function() {
//             frappe.msgprint("Thaman clicked me")
//         })
//     }
// });

// frappe.ui.form.on("Practice Timesheet", {
//     refresh(frm) {
//         if (frm.is_new()) {
//             console.log("Test")
//             frm.set_value("status", "Draft");

//         console.log("readonly loaded")
//         if (!frm.is_new()) {
//             frm.set_df_property("currency", "read-only", 1);
//         }
//         }
//     }
// })


// frappe.ui.form.on("Practice Timesheet", {
//     refresh(frm) {
//         console.log("Working")
//     }
// })

// frappe.ui.form.on("Practice Timesheet", {
//     total_working_hours(frm) {
//         console.log("total_working_hours loaded")
//         console.log("Hours changed")
        
//         frm.doc.total_working_hours

        // if (frm.doc.total_working_hours < 0) {
        //     frappe.throw("Hours cannot be negative")
        // }
//     }
// });

// frappe.ui.form.on("Practice Timesheet", {
//     total_working_hous(frm) {
//         if (frm.doc.total_working_hours < 0) {
//             frappe.msgprint("Hours cannot be ");
//             frm.set_value("total_working_hours", "");       
//         }
//     },

//     validate(frm) {
//         if (frm.doc.total_working_hours < 0) {
//             frappe.throw("Hours cannot be negative");
//         }
//     }
// })

// simple test for frappe.call()

// frappe.ui.form.on("Practice Timesheet", {
//     refresh(frm) {
//         console.log("Referesh triggered");
//             frappe.call({
//                     method: "event_management.event_management.doctype.practice_timesheet.practice_timesheet.test_call",
//                     callback: function(r) {
//                             console.log(r);
//                 } 
//         });
//     }
// });

// frappe.ui.form.on("Practice Timesheet", {
//     refresh(frm) {
//         // console.log("ping")
//         frappe.call("ping")
//         .then(r => {
//             console.log(r)
//         })
//     }
// })

// frappe.call('ping')
// .then(ds => {
//     console.log("-------------testing ping")
// })
// .then(z => {
//     console.log("-----2")
// });

// let result = frappe.call("ping");
// console.log(result);

// let result = frappe.call("event_management.event_management.doctype.practice_timesheet.practice_timesheet.test_call");

// console.log(result);

// frappe.ui.form.on("Practice Timesheet", {
//     refresh(frm) {
//         console.log("referesh triggered");

//         frappe.call({
//             method: "event_management.event_management.doctype.practice_timesheet.practice_timesheet.say_hello",
//             args: {
//                 name: "siddhu"
//             },
//             callback: function(r) {
//                 console.log("server says", r.message);
//             }
//         });
//     }
// });

// frappe.ui.form.on("Practice Timesheet", {
//     refresh(frm) {
//         console.log("----test");

//         frappe.call({
//             method: 'frappe.core.doctype.user.user.get_role_profile',
//             args: { // not args 
//                 role_profile: 'Sales'
//             },
//             btn: $('.primary-sction'),

//             freeze: true,
//             callback: (r) => {
//                 console.log("server returned", r.message);
//             },
//             error: (r) => {
//                 console.error("Error:", r);
//             }
//         });
//     }
// });

frappe.ui.form.on("Practice Timesheet", {
    refresh(frm) {
        console.log("---------test loaded properly");

        frappe.call({
            method: 'event_management.event_management.doctype.practice_timesheet.practice_timesheet.test_recap',
            
            callback: (r) => {
                console.log("server returned", r.message);
            }
        });
    }
});

frappe.ui.form.on("Practice Timesheet", {
    refresh(frm) {
        console.log("frm testing")

        frm.call({
            method: 'event_management.event_management.doctype.practice_timesheet.practice_timesheet.combine_field',
            args: {
                title: 'title_test',
                company: 'company_test'
            },

            callback: (r) => {
                console.log("server returned", r.message);
                frm.set_value("note", r.message)
            }
        })
    }
})