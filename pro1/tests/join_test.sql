select e.name,e.id,e.job_role,d.department_name,d.depart_id 
from employee e join department d 
on e.depart_id = d.depart_id;