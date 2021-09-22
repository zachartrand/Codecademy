-- 1
-- What are the column names?
select *
from orders
limit 10;
-- id, user_id, order_date, restaurant_id, item_name, special_instructions

-- 2
-- How recent is this data?
select distinct order_date
from orders
order by order_date desc;
-- The most recent order date is 2017-06-30

-- 3
-- Instead of selecting all the columns using *,
-- write a query that selects only the special_instructions column.

-- Limit the result to 20 rows.
select special_instructions
from orders
-- where special_instructions not null
limit 20;

-- 4
-- Can you edit the query so that we are only
-- returning the special instructions that are not empty?
select special_instructions
from orders
where special_instructions not null
limit 20;

-- 5
-- Let’s go even further and sort the instructions
-- in alphabetical order (A-Z).
select special_instructions
from orders
where special_instructions not null
order by special_instructions asc
limit 20;

-- 6
-- Let’s search for special instructions that have the word ‘sauce’.
select item_name, special_instructions
from orders
where special_instructions not null
    and special_instructions like "%sauce%"
order by special_instructions asc
limit 20;
-- Are there any funny or interesting ones?
-- Extra cheese pizza with bbq sauce

-- 7
-- Let’s search for special instructions that have the word ‘door’.
select special_instructions
from orders
where special_instructions not null
    and special_instructions like "%door%"
order by special_instructions asc
limit 20;
-- Any funny or interesting ones?
-- super hungover. let yourself in pass the fridge turn left and double doors my bedroom. im in my pajamas watching james bond 1love

-- 8
-- Let’s search for special instructions that have the word ‘box’.
select special_instructions
from orders
where special_instructions not null
    and special_instructions like "%box%"
order by special_instructions asc
limit 20;
-- Any funny or interesting ones?
-- beat me tic-tac-toe on the pizza box for $5 tip
-- Cleanse yourself with the sage in the mailbox.
-- Draw Yoda on pizza box.
-- my coworker and i are working overtime. can u write some inspiration/motivations on the box. u rock!
-- write me a poem on the pizza box.

-- 9
-- Instead of just returning the special instructions, also return their order ids.

-- For more readability:
-- Rename id as ‘#’
-- Rename special_instructions as ‘Notes’
select distinct id as "#", special_instructions as "Notes"
from orders
where special_instructions not null
order by id asc
limit 20;

-- 10
-- Challenge
-- They have asked you to query the customer who made the phrase.
-- Return the item_name restaurant_id, and user_id for the person created the phrase.
select item_name, restaurant_id, user_id
from orders
where special_instructions like "%narwhal%";
