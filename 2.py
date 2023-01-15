import requests
# 127.0.0.1 בעצם הרצנו אותו על הכתובת  localhost אחריי שהרצנו את השרת על
# וגם עשינו זאת על פורט 8000 ולכן הכתובת המלאה היא
url = "http://127.0.0.1:8000?username=hacker&password=hacking"
#  GET לבסוף השתמשנו בפקודה מתוך ספרייה מובנת כדי לעשות בקשת
req = requests.get(url)
# הבקשה מכילה לא מעט מידע בפנים, כגון סטטוס הצלחה, תוכן מוחזר ועוד
if 199 < req.status_code < 300:
    # כאן מדפיסים את התוכן שהחוזר
    print(req.text)
else:
    # אם משהו השתבש נדפיס הודעת שגיאה
    print(f"Something went wrong, ERROR CODE: {req.status_code}")