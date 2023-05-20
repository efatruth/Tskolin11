drop database if exists TriggerTestBase;
create database TriggerTestBase;
use TriggerTestBase;

create table Tasks
(
	taskID int auto_increment,
    taskName varchar(45),
    taskSalary int,
    taskHours int,
    constraint task_PK primary key(taskID)
);

create table Workers
(
	workerID int auto_increment,
    workerName varchar(55),
    constraint worker_PK primary key(workerID)
);

create table WorkerTasks
(
	workerTaskID int auto_increment,
    taskID int not null,
    workerID int not null,
    taskStart datetime,
    constraint workertask_PK primary key(workerTaskID),
    constraint workertask_task_FK foreign key(taskID) references Tasks(taskID),
    constraint workertask_worker_FK foreign key(workerID) references Workers(workerID)
);

delimiter $$
drop trigger if exists before_workertasks_insert $$

create trigger before_workertasks_insert 
before insert on WorkerTasks
for each row
begin
	declare currentHours int;
    declare newHours int;
    declare newTotal int;
    
    -- lets get how many hours the worker is working now
    select sum(Tasks.taskHours) into currentHours
    from Tasks
    inner join WorkerTasks on Tasks.taskID = WorkerTasks.taskID
    and WorkerTasks.workerID = new.workerID;
    
    -- lets also see how many hours the new task has
    select taskHours into newHours
    from Tasks
    where taskID = new.taskID;
    
    -- we add these to find out how many hours the worker will 
    -- have if the new task is added.
    set newTotal = currentHours + newHours;
    
    -- the man says each worker must not have more than 50 hours
    -- so we check.  If it is true we simply stop the insert in the 
    -- WorkerTasks table and deliver an appropriate message.
    if (newTotal > 50) then
		signal sqlstate '45000' set message_text = 'If this task is added, the worker will have too much to do';
	end if;
end $$

delimiter ;

insert into Tasks(taskName,taskSalary,taskHours)values('Dig a hole','45000','10');
insert into Tasks(taskName,taskSalary,taskHours)values('Fill a hole','20000','5');
insert into Tasks(taskName,taskSalary,taskHours)values('Traffic Control','40000','8');
insert into Tasks(taskName,taskSalary,taskHours)values('Build a Wall','75000','45');
insert into Tasks(taskName,taskSalary,taskHours)values('Limosine driver','55000','5');
insert into Tasks(taskName,taskSalary,taskHours)values('Teach','16000','8');
insert into Tasks(taskName,taskSalary,taskHours)values('Bus driver','40000','8');
insert into Tasks(taskName,taskSalary,taskHours)values('Cashier','15000','5');
insert into Tasks(taskName,taskSalary,taskHours)values('Sales assistant','20000','10');
insert into Tasks(taskName,taskSalary,taskHours)values('Handball Coach','32000','4');

insert into Workers(workerName)values('JÃ³n'),('Gunna'),('PÃ©tur'),('Sigga'),('Anna');


-- setjum Siggu Ã­ verk
insert into WorkerTasks(workerID,taskID,taskStart)values(4,6,now());	-- OK
insert into WorkerTasks(workerID,taskID,taskStart)values(4,9,now());	-- OK
insert into WorkerTasks(workerID,taskID,taskStart)values(4,4,now());	-- Stopped by the trigger


select * from Workers;
select * from Tasks;
select * from WorkerTasks;