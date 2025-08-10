#!/usr/bin/env python3
import webbrowser
import subprocess

# Open Broswer links
gmail_url = "https://mail.google.com/"
linkedin_url = "https://www.linkedin.com/jobs/search-results/?keywords=remote%20NOT%20senior&origin=JOB_COLLECTION_PAGE_SEARCH_BUTTON"
job_spreadsheet = "https://docs.google.com/spreadsheets/d/1BTbenZ_DkEgKZ8tEVbYqy6KrDyoCPJ5YL999bxGVfYE/edit?gid=0#gid=0"
calendar = "https://calendar.google.com/calendar/u/0/r"
votd = "https://www.bible.com/verse-of-the-day"
life_board = "https://www.figma.com/board/D1fZyDrVqo6AsG3M9eKSBJ/Life-Board?node-id=0-1&p=f&t=Osk2iEVQ7CkKyXv4-0"

webbrowser.open(gmail_url)
webbrowser.open(linkedin_url)
webbrowser.open(job_spreadsheet)
webbrowser.open(calendar)
webbrowser.open(votd)
webbrowser.open(life_board)

# Open Apps
subprocess.run(["open", "-a", "Flow"])
subprocess.run(["open", "-a", "Todoist"])
subprocess.run(["open", "-a", "ChatGPT"])