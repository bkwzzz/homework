import datetime
current_datetime = datetime.datetime.now()
five_days_ago = current_datetime - datetime.timedelta(days=5)
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
filename = "save_fivedayago_time_" + formatted_datetime + ".txt"
with open(filename, "w") as file:
    file.write(str(five_days_ago))

