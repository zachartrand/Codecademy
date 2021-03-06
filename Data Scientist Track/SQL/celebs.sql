/******************************************************************************
SQL code for creating a database table.
*******************************************************************************/

create table celebs (
    id integer,
    name text,
    age integer
);

insert into celebs (id, name, age)
values (1, 'Penn Jillette', 66);

insert into celebs (id, name, age)
values (2, 'Teller', 73);

insert into celebs (id, name, age)
values (3, 'Joe Rogan', 53);

insert into celebs (id, name, age)
values (4, 'Eric Weinstein', 55);

alter table celebs
add column twitter_handle text;

update celebs
set twitter_handle = '@EricRWeinstein'
where id = 4;

select * from celebs;
