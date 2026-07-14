import pandas as pd
import random
from faker import Faker


user = Faker("en_IN")

All_Users = []

for i in range(1,110001):
   All_Users.append({
        "User_ID": f"PP{i:07d}",
        "Name": user.name(),
        "Age": random.randint(18, 65),
        "Join_Date": user.date_between(start_date='-3y', end_date='today')
    })
Users_df = pd.DataFrame(All_Users)
print(Users_df)

All_Transactions = []
for i in range(1, 200001):
   All_Transactions.append({
         "Transaction_ID": f"T{i:07d}",
         "User_ID": random.choice(Users_df["User_ID"]),
         "Amount": round(random.uniform(10, 10000), 2),
         "service": random.choice(["Recharge Bill","Money Transfer","Loan payment","Insurance Payment"]),
         "Service_Type": random.choice(["UPI","Bank Transfer","Scan & Pay"]),
         "Transaction_Status": random.choice(["Success","Failed","Pending"]),
         "Date": user.date_between(start_date='-3y', end_date='today')
   })

Transactions_df = pd.DataFrame(All_Transactions)
print(Transactions_df)


Users_df.to_csv("All_Users.csv", index=False)
Transactions_df.to_csv("All_Transactions.csv", index=False)
print("CSV files created successfully!")