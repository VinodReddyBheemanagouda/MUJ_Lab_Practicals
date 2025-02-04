# Write a program in PL/SQL to print the prime numbers between 1 to 50.

# DECLARE
#     -- Declare variables to store the number, divisor, and a flag to check primality
#     num INTEGER;
#     divisor INTEGER;
#     is_prime BOOLEAN;
# BEGIN
#     -- Loop through numbers from 1 to 50
#     FOR num IN 1..50 LOOP
#         -- Assume the number is prime initially
#         is_prime := TRUE;
        
#         -- Check divisibility from 2 to num-1
#         FOR divisor IN 2..num-1 LOOP
#             -- If num is divisible by any number, it's not prime
#             IF num MOD divisor = 0 THEN
#                 is_prime := FALSE;
#                 EXIT;  -- Exit the loop as we already know the number is not prime
#             END IF;
#         END LOOP;

#         -- If the number is prime and greater than 1, print it
#         IF is_prime AND num > 1 THEN
#             DBMS_OUTPUT.PUT(num || ' ');
#         END IF;
#     END LOOP;
#     -- Print a newline after the list of prime numbers
#     DBMS_OUTPUT.PUT_LINE('');
# END;



