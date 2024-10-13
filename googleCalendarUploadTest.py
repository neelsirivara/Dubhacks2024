from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Workout plan
    workout_time = datetime.datetime(2024, 10, 14, 9, 0, 0)
    workouts = [
        ('Full Body Workout', workout_time),
        ('Full Body Workout', workout_time + datetime.timedelta(days=2)),
        ('Full Body Workout', workout_time + datetime.timedelta(days=4)),
    ]

    upper_body_time = workout_time + datetime.timedelta(weeks=2)
    lower_body_time = upper_body_time + datetime.timedelta(days=1)

    for i in range(4):
        workouts.append(("Upper Body Workout", upper_body_time + datetime.timedelta(days=i*2)))
        workouts.append(("Lower Body Workout", lower_body_time + datetime.timedelta(days=i*2)))

    for title, start_time in workouts:
        event = {
            'summary': title,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': 'Your_Time_Zone',
            },
            'end': {
                'dateTime': (start_time + datetime.timedelta(hours=1)).isoformat(),
                'timeZone': 'Your_Time_Zone',
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")

if __name__ == '__main__':
    main()