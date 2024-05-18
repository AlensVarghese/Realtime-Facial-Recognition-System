import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendancerealtime-d829a-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data ={
    "101":
        {
            "name": "Alen",
            "major": "INMCA",
            "Starting_year": 2021,
            "Total_attendance": 0,
            "standing": "G",
            "Designation":"Student",
            "Last_attendance_time": "2022-12-11 00:54:34"
        },
    "102":
        {
            "name": "Ashlin",
            "major": "INMCA",
            "Starting_year": 2021,
            "Total_attendance": 0,
            "standing": "G",
            "Designation":"Student",
            "Last_attendance_time": "2022-12-11 00:54:34"
        },
    "103":
        {
            "name": "Jijo",
            "major": "INMCA",
            "Starting_year": 2021,
            "Total_attendance": 0,
            "standing": "G",
            "Designation": "Teacher",
            "Last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)


