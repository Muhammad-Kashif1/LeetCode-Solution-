# Write your MySQL query statement below
-- Query to find the IDs of invalid tweets using a subquery
SELECT tweet_id
FROM Tweets
WHERE tweet_id IN (
    SELECT tweet_id
    FROM Tweets
    WHERE LENGTH(content) > 15
);
