select activity_date as day ,count(distinct user_id) active_users
from Activity
where activity_date < '2019-07-27' 
and DATEDIFF(day,activity_date,'2019-07-27') <=29  
group by activity_date