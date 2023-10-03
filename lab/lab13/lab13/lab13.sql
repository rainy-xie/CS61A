.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where color = "blue" and pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet , song from students where color = "blue" and pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest having COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet,a.song,a.color,b.color from students as a,students as b 
        WHERE a.time < b.time AND a.pet = b.pet and a.song = b.song;

CREATE TABLE sevens AS
  SELECT a.seven from students as a, numbers as b WHERE a.time = b.time and a.number = 7 and b."7" = 'True';


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) as average_price from products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) from inventory GROUP BY item;

CREATE TABLE best_deal AS
  SELECT name, MIN(MSRP/rating) from products GROUP BY category;

CREATE TABLE shopping_list AS
  SELECT name, store from best_deal,lowest_prices where best_deal.name = lowest_prices.item;


CREATE TABLE total_bandwidth AS
  SELECT SUM(a.Mbs) FROM stores as a, shopping_list as b WHERE a.store = b.store;

