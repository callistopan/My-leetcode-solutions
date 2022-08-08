# Write your MySQL query statement below
Select U.name as name, ifnull(sum(R.distance),0) as travelled_distance 
from Users U left join Rides R
on R.user_id = U.id
group by R.user_id
Order by travelled_distance desc, name