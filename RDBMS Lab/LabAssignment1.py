# Consider the table winner and write a query to retrieve the details of the winners who won in subjects starting with the letter 'C'.
# id	year	subject	winner	country
# 1	1970	Physics	James	Sweden
# 2	1970	Pysics	Louis Nell	France
# 3	1970	Chemistry	Walter James	France
# 4	1971	Literature	Paul	Germany
# 5	1972	Economics	Dennis	Hungary

# SELECT
#     winner, -- Winner's name
#     subject -- Subject in which the winner won
# FROM
#     winner -- Table name
# WHERE
#     subject LIKE 'C%' -- Filter subjects starting with 'C'
# ORDER BY
#     winner; -- Optional: Order the results by winner's name
