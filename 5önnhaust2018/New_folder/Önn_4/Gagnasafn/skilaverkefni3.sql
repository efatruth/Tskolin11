
-- 1

create table deptsal (
	depnt_no int not null,
    totalsalary int not null
);

-- 2

delimiter //
create procedure updateSalary(in departmentID int)
begin
	update deptsal set totalsalary = (SELECT SUM(salary) from employee where dept_no = departmentID) where depnt_no = departmentID;
end //

-- 3

delimiter ;

-- 4

insert into deptsal values 
(1, 0),
(2, 0),
(3, 0);
call updateSalary(1);
call updateSalary(2);
call updateSalary(3);

-- 5
select * from deptsal;

- 4
show procedure status;

- 5
drop procedure updateSalary;

- 6
update deptsal set totalsalary = 0;

- 7
delimiter //
create procedure updateSalary()
begin
	declare i int;
    set i = 1;
    repeat
		update deptsal set totalsalary = (SELECT SUM(salary) from employee where dept_no = i) where depnt_no = i;
        set i = i + 1;
        until i >= 4
	end repeat;
end //

-- 9

delimiter //
create procedure updateSalaryBy10p()
begin
	declare i int;
    set i = 1;
    repeat
		update deptsal set totalsalary = (SELECT totalsalary) * 1.10 where depnt_no = i;
        set i = i + 1;
        until i >= 4
	end repeat;
end //