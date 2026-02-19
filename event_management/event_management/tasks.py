import frappe
from frappe.utils import getdate, add_days

# daily reminder function
def send_event_reminders():
    # find tomorrow's date
    tomorrow = add_days(getdate(), 1)

    # fetch all submitted registrations for tomorrow
    registrations = frappe.get_all(
        "Event Registration",
        filters={
            "event_date": tomorrow,
            "docstatus": 1  
        },
        fields=["participant", "email", "event_detail"]
    )
    
    # loop through and send emails
    for reg in registrations:
        frappe.sendmail(
            recipients=reg["email"],
            subject="Event Reminder",
            message=f"""
Hello {reg['participant']},

This is a reminder that your event "{reg['event_detail']}"
is scheduled for tomorrow.

""",

    )

    print("Reminder mails sent")


def send_confirmation_email(doc, method):
    print("Hook Triggered")