from datetime import datetime
frm = "inr"
to = "yen"
tp = "FtoC"
outfile = open("temperature_record.txt", "a")
now = datetime.now()
outfile.write(str(now) + " " + str(frm) + " " + str(to) + " " + str(tp) + "\n")
outfile.close()