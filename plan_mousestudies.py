import pandas as pd
import sys 

#Enter mouse arrival date in format 1/1/2018
mice_arrival_date = sys.argv[1]
Injection1= pd.to_datetime(mice_arrival_date) + pd.DateOffset(days=7)
Bleeding1 = pd.to_datetime(mice_arrival_date) + pd.DateOffset(days=21)
Injection2 = pd.to_datetime(mice_arrival_date) + pd.DateOffset(days=28)
Bleeding2 = pd.to_datetime(mice_arrival_date) + pd.DateOffset(days=42)
Injection3 = pd.to_datetime(mice_arrival_date) + pd.DateOffset(days=49)
Sac = pd.to_datetime(mice_arrival_date) + pd.DateOffset(days=63)

dates=[Injection1, Bleeding1, Injection2, Bleeding2, Injection3, Sac]
manipulation=["Injection1", "Bleeding1", "Injection2", "Bleeding2", "Injection3", "Sacrificing"]

print Injection3
print "Injection 1 is at " + str(Injection1.date())
print "Bleeding 1 is at " + str(Bleeding1.date())
print "Injection 2 is at " + str(Injection2.date())
print "Bleeding 2 is at " + str(Bleeding2.date())
print "Injection 3 is at " + str(Injection3.date())
print "Sacrificing is at " + str(Sac.date())

df = pd.DataFrame({"Dates": dates, "Manipulation": manipulation})
with open('mouse_schedule.csv', 'w') as f:
	f.write(df.to_csv(index=False))
f.close()
