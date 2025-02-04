# Consider the table winner and display the record of those winner which won the prize between year 1971-1972.
# -- Select the columns to display from the 'winner' table
# SELECT 
#     id,         -- Unique identifier for each record
#     year,       -- Year the prize was won
#     subject,    -- Subject of the prize
#     winner,     -- Name of the winner
#     country     -- Country of the winner
# FROM 
#     winner      -- Source table containing the records of winners
# WHERE 
#     year BETWEEN 1971 AND 1972 -- Filter for records where the year is between 1971 and 1972 (inclusive)
# ORDER BY 
#     year,       -- Sort the results by year in ascending order
#     subject,    -- Then by subject for better organization
#     winner;     -- Finally, sort by winner's name alphabetically
