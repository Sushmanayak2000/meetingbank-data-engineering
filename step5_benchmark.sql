-- ================================
-- STEP 5: QUERY BENCHMARKING
-- Group 3 – Advanced Database Architects
-- ================================

-- --------------------------------
-- PART A: BEFORE INDEX (Baseline)
-- --------------------------------

DROP INDEX IF EXISTS idx_fact_city_id;

-- Baseline query plan
EXPLAIN ANALYZE
SELECT
    dc.city_name,
    AVG(fm.transcript_word_count) AS avg_transcript_length
FROM fact_meetings fm
JOIN dim_city dc
    ON fm.city_id = dc.city_id
GROUP BY dc.city_name;

-- --------------------------------
-- PART B: AFTER INDEX (Optimized)
-- --------------------------------

-- Create index for optimization
CREATE INDEX idx_fact_city_id
ON fact_meetings(city_id);
-- Optimized query plan
EXPLAIN ANALYZE
SELECT
    dc.city_name,
    AVG(fm.transcript_word_count) AS avg_transcript_length
FROM fact_meetings fm
JOIN dim_city dc
    ON fm.city_id = dc.city_id
GROUP BY dc.city_name;

