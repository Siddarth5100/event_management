import frappe
from frappe.utils import getdate, add_days

# Daily reminder function
def send_event_reminders():
    # Step 1: find tomorrow's date
    tomorrow = add_days(getdate(), 1)
    print("------tomorrow date", tomorrow)

    # Step 2: fetch all submitted registrations for tomorrow
    registrations = frappe.get_all(
        "Event Registration",
        filters={
            "event_date": tomorrow,
            "docstatus": 1  # only submitted
        },
        fields=["participant", "email", "event_detail"]
    )
    print("---------registrations", registrations)
    
    # Step 3: loop through and send emails
    for reg in registrations:
        frappe.sendmail(
            recipients=reg["email"],
            subject="Event Reminder",
            message=f"""
Hello {reg['participant']},

This is a reminder that your event "{reg['event_detail']}"
is scheduled for tomorrow.

See you there!
"""
        )

    print(f"Reminder mails sent: {len(registrations)}")
