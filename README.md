#Orbit-Checker

Once a potential orbit has been found, the most common 'next step' is to validate that the lambda value of this orbit corresponds with what it should be. This script performs that validation, finding the difference of each item in the list, and then returning a count of the most commonly occuring item(s). This allows the lambda value to quickly be determined, verifying that an (n, k, λ)-difference set is correct. 

Example: setting orbit = [1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 18] and n = 23, the script prints the following:

Results: [22, 21, 20, 18, 16, 15, 12, 11, 8, 6, 1, 22, 21, 19, 17, 16, 13, 12, 9, 7, 2, 1, 22, 20, 18, 17, 14, 13, 10, 8, 3, 2, 1, 21, 19, 18, 15, 14, 11, 9, 5, 4, 3, 2, 21, 20, 17, 16, 13, 11, 7, 6, 5, 4, 2, 22, 19, 18, 15, 13, 8, 7, 6, 5, 3, 1, 20, 19, 16, 14, 11, 10, 9, 8, 6, 4, 3, 22, 19, 17, 12, 11, 10, 9, 7, 5, 4, 1, 20, 18, 15, 14, 13, 12, 10, 8, 7, 4, 3, 21, 17, 16, 15, 14, 12, 10, 9, 6, 5, 2]
Sorted : [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22]
Lambda = 5
