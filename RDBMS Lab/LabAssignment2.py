# Consider the table winner and List subjects with at least two winners, along with the winner names.
# -- Select the subject and winner's name from the winner table
# SELECT 
#     subject,  -- The subject in which the prize was won
#     winner    -- The name of the winner
# FROM 
#     winner    -- The table containing the winners' details
# WHERE 
#     subject IN (
#         -- Subquery to find subjects with at least two winners
#         SELECT 
#             subject  -- The subject to be checked
#         FROM 
#             winner   -- The table containing the winners' details
#         GROUP BY 
#             subject  -- Group the records by subject
#         HAVING 
#             COUNT(winner) >= 2 -- Ensure the subject has two or more winners
#     )
# -- Order the results by subject and then by winner's name for clarity
# ORDER BY 
#     subject,  -- Sort the output alphabetically by subject
#     winner;   -- Sort within each subject alphabetically by winner's name