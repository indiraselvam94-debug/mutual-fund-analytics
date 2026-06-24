-- 1. Total NAV records
SELECT COUNT(*) FROM fact_nav;

-- 2. Average NAV
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 3. Maximum NAV
SELECT MAX(nav) AS max_nav
FROM fact_nav;

-- 4. Minimum NAV
SELECT MIN(nav) AS min_nav
FROM fact_nav;

-- 5. Latest NAV by scheme
SELECT scheme_name, MAX(nav) AS latest_nav
FROM fact_nav
GROUP BY scheme_name;

-- 6. NAV records per scheme
SELECT scheme_name, COUNT(*) AS records_count
FROM fact_nav
GROUP BY scheme_name;

-- 7. Average NAV by fund house
SELECT fund_house, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY fund_house;

-- 8. Top 5 NAV values
SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 5;

-- 9. Earliest date
SELECT MIN(date) AS earliest_date
FROM fact_nav;

-- 10. Latest date
SELECT MAX(date) AS latest_date
FROM fact_nav;