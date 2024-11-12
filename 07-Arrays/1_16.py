# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
distances_traveled.sort()
print(distances_traveled)
# Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
sorted_daily_temperatures = sorted(daily_temperatures, reverse = True)
print(sorted_daily_temperatures)
# Sort the data in ascending order
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
sorted_file_names = sorted(file_names, reverse = False)
print(sorted_file_names)