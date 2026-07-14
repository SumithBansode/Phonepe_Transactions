create database phonepe_db;

use phonepe_db;

select * from all_users;

#------Total_ID------
select
count(User_ID) as total_users
from all_users;

select
count(Transaction_ID) as total_transaction
from all_transactions;

#-----Total Amount-----
select
sum(Amount) As Total_Amount
from all_transactions;

#-----Ave Amount---------
select
avg(Amount) As Ave_Amount
from all_transactions;

#-------max Amount----
select
max(Amount) As max_Amount
from all_transactions;

#------min Amount----
select
min(Amount) As min_Amount
from all_transactions;

#-----Top 5 Hight Trasactions-----
select
User_ID,
sum(Amount) As Total_Amount
from all_transactions
group by User_ID
order by Total_Amount desc
limit 5;

#------service type-------
select
Service_Type,
count(Transaction_ID) count
from all_transactions
group by Service_Type;

#-----Transaction status----
select
Transaction_Status,
count(Transaction_ID)count
from all_transactions
group by Transaction_Status;

