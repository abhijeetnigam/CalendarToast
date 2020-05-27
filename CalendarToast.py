from builtins import hasattr

import win32com.client
import datetime
import time
import Log
import win10toast
# Function to pick relative path of the icon file
import sys, os

Log.callog('Start Calendar Logging\n')


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# Function for Toast Notification
def notify(mmin, msubj):
    # from win10toast import ToastNotifier  # Install Win10Toast module

    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Time to Wrapup ", str(mmin) + " Mins are left in Meeting : " + str(msubj),
                       icon_path=resource_path('lalarm.ico'),
                       duration=15)


# Main read calendar starts
i = 1
while 1 == 1:

    try:
        # Setup Date format
        dateformat = "%m/%d/%y" +" 00:00"
        # Connect to Local Outlook profile .
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        calendar = outlook.GetDefaultFolder(9)  # Read the calendar folder referred to as #9 in the folder list
        appointments = calendar.Items
        # Restrict Calendar Invites to Today
        appointments.Sort("[Start]")
        appointments.IncludeRecurrences = "True"
        # Define begin and End of calendar entries of today
        today = datetime.datetime.today()
        begin = today.date().strftime(dateformat)
        tomorrow = datetime.timedelta(days=1) + today
        end = tomorrow.date().strftime(dateformat)
        appointments = appointments.Restrict("[Start] >= '" + begin + "' AND [END] <= '" + end + "'")
        now = today.time().strftime("%H:%M:%S")
        time.sleep(60)  # wait for 60s before checking the calendar again
        # Read every appointment in the calendar
        for appointment in appointments:
            i += 1
            if 60 < i <= 70:
                # Updating Cal Log file with calendar appointments of Today
                strmeet = appointment.start.strftime("%H:%M:%S") + appointment.Subject
                Log.callog(strmeet)
                # print(i,appointment.Subject)
            if i > 70:
                i = 1

            if appointment.start.strftime("%H:%M:%S") <= now <= appointment.end.strftime("%H:%M:%S"):
                strdate = datetime.datetime.strptime(appointment.end.strftime("%m/%d/%y, %H:%M:%S"),
                                                 "%m/%d/%y, %H:%M:%S")
                meetend = strdate - today
                meetmin = int(meetend.total_seconds() / 60)
                if meetmin <= 10:
                    notify(meetmin, appointment.Subject)
                    time.sleep(60)  # wait for 60s before checking the calendar again
            else:
                continue
    except Exception as e:
        Log.exlog(e.args)
