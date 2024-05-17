-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Check the crime scene of all
SELECT * FROM crime_scene_reports;
-- Check the crime scene of the fiftyville CS50 duck
SELECT * FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
-- result Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery

-- Check interviews
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
-- results
-- Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.

--Check Bakery Logs
-- Sometime within ten minutes of the theft (10:15am), I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND activity = 'exit' AND hour = 10 AND minute < 25;
--license plate
-- 5P2BI95
-- 94KL13X
-- 6P58WS2
-- 4328GD8
-- G412CB7
-- L93JTIZ
-- 322W7JE
-- 0NTHK55

-- Check ATM logs
-- Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
SELECT * FROM atm_transactions  WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';
-- Result Account numbers
-- 28500762
-- 28296815
-- 76054385
-- 49610011
-- 16153065
-- 25506511
-- 81061156
-- 26013199

--Check bank accounts
SELECT * FROM bank_accounts WHERE account_number == 28500762;
-- 467400
SELECT * FROM bank_accounts WHERE account_number == 28296815;
-- 395717
SELECT * FROM bank_accounts WHERE account_number == 76054385;
-- 449774
SELECT * FROM bank_accounts WHERE account_number == 49610011;
-- 686048
SELECT * FROM bank_accounts WHERE account_number == 16153065;
-- 458378
SELECT * FROM bank_accounts WHERE account_number == 25506511;
-- 396669
SELECT * FROM bank_accounts WHERE account_number == 81061156;
-- 438727
SELECT * FROM bank_accounts WHERE account_number == 26013199;
-- 514354

-- Check Phone calls
-- they called someone who talked to them for less than a minute.
SELECT * FROM phone_calls  WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
-- Caller number
-- (130) 555-0289
-- (499) 555-9472
-- (367) 555-5533
-- (499) 555-9472
-- (286) 555-6063
-- (770) 555-1861
-- (031) 555-6622
-- (826) 555-1652
-- (338) 555-6650

--Check Flights out of Fiftyville on 2021/7/29
--In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--Check Airports
SELECT * FROM airports;
-- 8  | CSF          | Fiftyville Regional Airport             | Fiftyville
SELECT * FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id == 8 AND destination_airport_id != 8 ORDER BY hour ASC;
-- Flight number 36

-- Check passenger for Flight 36
SELECT * FROM passengers WHERE flight_id = 36;
-- Result
-- 7214083635
-- 1695452385
-- 5773159633
-- 1540955065
-- 8294398571
-- 1988161715
-- 9878712108
-- 8496433585

-- Check People
SELECT * FROM people WHERE passport_number = 7214083635;
-- No matching license plate
SELECT * FROM people WHERE passport_number = 1695452385;
-- No matching license plate
SELECT * FROM people WHERE passport_number = 5773159633;
-- Matching License plate 94KL13X person id = 686048 phone number = 555-5533 existing bank account = 686048
SELECT * FROM people WHERE passport_number = 1540955065;
-- No matching license plate
SELECT * FROM people WHERE passport_number = 8294398571;
-- Matching license plate 0NTHK55 person id = 560886 phone number = 555-9472
SELECT * FROM people WHERE passport_number = 1988161715;
-- No matching license plate
SELECT * FROM people WHERE passport_number = 9878712108;
-- No matching license plate
SELECT * FROM people WHERE passport_number = 8496433585;
-- Matching license plate 4328GD8 person id 467400 No matching phone number

--Thief
SELECT * FROM people WHERE passport_number = 5773159633;
-- Matching License plate 94KL13X person id = 686048 phone number = 555-5533 existing bank account = 686048
--Bruce

--Check Escape to
SELECT city FROM airports
    JOIN flights ON flights.destination_airport_id = airports.id
    JOIN passengers ON passengers.flight_id = flights.id
    WHERE flights.year = 2021 AND flights.month = 7 AND day = 29 AND origin_airport_id == 8 AND passengers.passport_number = 5773159633;
-- New Yok City

--Check Accomplice
SELECT * FROM phone_calls  WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 and caller = '(367) 555-5533';
-- Accomplice number (375) 555-8161
-- Check person with the phone number
SELECT * FROM people WHERE phone_number = '(375) 555-8161';
-- Robin person id = 864400 but with no passport number
