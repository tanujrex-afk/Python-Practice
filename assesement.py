import numpy as np
import pandas as pd
orders= pd.DataFrame({
    "order_id":[101,102,103,104,105,106],
    "cust_id": [1,2,1,3,2,1],
    "product":["laptop", "phone", "mouse", "keyboard", "speaker", "SD"],
    "amount": [80000,30000,1500,75000,28000,5000],
    "order_date": ["2026-01-10", "2026-01-15","2026-02-05","2026-02-10","2026-03-01","2026-03-15"]})
#converting order to datetime and extract the month for the time based questions
orders["order_date"]=pd.to_datetime(orders["order_date"])
orders["month"]=orders["order_date"].dt.to_period("M")
print("-----Answers------")
#finding total revenue
tr=orders["amount"].sum()
print(f"total revenue:${tr:,}")
#finding revenue by customer
rbc=orders.groupby("cust_id")["amount"].sum()
print("\n Rvenue by customer:")
print(rbc.to_string())
# highest valaue customer
hvc=rbc.idxmax()
print(f"\n Hihest valkue customer Id:{hvc}")
#monthly revenue
mr=orders.groupby("month")["amount"].sum()
print("\n monthly revenue:")
print(mr.to_string())
#highest_selling product
hsp=orders.groupby("product")["amount"].sum().idxmax()
print(f"\n. highest selling product by revenue:{hsp}")
#highest spending customers
hsc=rbc[rbc> 50000].index.to_list()
print(f"\n customers spending over 50000(IDs):{hsc}")
#cumiliative spending over time
orders=orders.sort_values(by=["cust_id","order_date"])
orders["cumilative_Spending"]=orders.groupby("cust_id")["amount"].cumsum()
print("\n Cumilative spending over time:")
print(orders[["cust_id","order_date","amount","cumilative_Spending"]].to_string(index=False))
#average order value
aov=orders["amount"].mean()
print(f"\n Average_order_value:${aov:,.2f}")
#highest revenue month
hrm=mr.idxmax()
print(f"\n.month with the highest revenue:{hrm}")
# aadd a colum shopwing "high value" if amount> 50000, otherwise "regular"
orders["order_type"]=orders["amount"].apply(lambda x:"high value" if x>50000 else "regular")
print("\n. Dataframe with order type column:")
print(orders[["order_id","amount","order_type"]].to_string(index=False))