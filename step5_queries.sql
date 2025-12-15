-- Analytical Queries on MeetingBank Data Warehouse

--average transcript length per city
--(This is a real analytical query)
SELECT city_name, AVG(transcript_word_count)
FROM fact_meetings fm
JOIN dim_city dc ON fm.city_id = dc.city_id
GROUP BY city_name;

-- Create Indexes to optimize queries

--Create index on foreign key
-- Create Indexes to optimize queries
DROP INDEX IF EXISTS idx_fact_city_id;
CREATE INDEX idx_fact_city_id ON fact_meetings(city_id);


--Create index on city_name for faster lookups
DROP INDEX IF EXISTS idx_dim_city_name;
CREATE INDEX idx_dim_city_name ON dim_city(city_name);


-- Re-run the analytical query to see performance improvement
SELECT city_name, AVG(transcript_word_count)
FROM fact_meetings fm
JOIN dim_city dc ON fm.city_id = dc.city_id
GROUP BY city_name;

EXPLAIN ANALYZE
SELECT city_name, AVG(transcript_word_count)
FROM fact_meetings fm
JOIN dim_city dc ON fm.city_id = dc.city_id
GROUP BY city_name;
-- STEP 5.1: CTE to calculate average transcript length per city
WITH city_stats AS (
    SELECT
        dc.city_name,
        AVG(fm.transcript_word_count) AS avg_transcript_length
    FROM fact_meetings fm
    JOIN dim_city dc ON fm.city_id = dc.city_id
    GROUP BY dc.city_name
)
SELECT * FROM city_stats;
-- STEP 5.2: Window Function
-- Rank meetings by transcript length (largest first)

SELECT
    meeting_id,
    transcript_word_count,
    RANK() OVER (ORDER BY transcript_word_count DESC) AS transcript_rank
FROM fact_meetings;
-- STEP 4.1: Analytical Insight
-- Top 10 longest meetings by transcript length

SELECT
    fm.meeting_id,
    dc.city_name,
    fm.transcript_word_count
FROM fact_meetings fm
JOIN dim_city dc
    ON fm.city_id = dc.city_id
ORDER BY fm.transcript_word_count DESC
LIMIT 10;
