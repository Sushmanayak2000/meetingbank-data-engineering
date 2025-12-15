-- ================================
-- STEP 4: DATABASE SCHEMA
-- Group 3 – Advanced Database Architects
-- ================================

-- ---------- DIMENSION TABLES ----------

-- City Dimension
CREATE TABLE IF NOT EXISTS dim_city (
    city_id SERIAL PRIMARY KEY,
    city_name TEXT UNIQUE NOT NULL
);

-- ---------- 3NF CORE TABLES ----------

-- Meetings (Source-of-truth table)
CREATE TABLE IF NOT EXISTS meetings (
    meeting_pk TEXT PRIMARY KEY,
    meeting_id_raw TEXT,
    city_id INT REFERENCES dim_city(city_id),
    meeting_date DATE,
    video_url TEXT,
    agenda_url TEXT
);

-- Speakers table
CREATE TABLE IF NOT EXISTS speakers (
    speaker_id SERIAL PRIMARY KEY,
    speaker_label TEXT UNIQUE NOT NULL
);

-- Junction table: Meetings ↔ Speakers (Many-to-Many)
CREATE TABLE IF NOT EXISTS meeting_speakers (
    meeting_pk TEXT REFERENCES meetings(meeting_pk),
    speaker_id INT REFERENCES speakers(speaker_id),
    total_words INT,
    total_speaking_time_sec INT,
    PRIMARY KEY (meeting_pk, speaker_id)
);

-- ---------- FACT TABLE (STAR SCHEMA) ----------

CREATE TABLE IF NOT EXISTS fact_meetings (
    meeting_pk TEXT PRIMARY KEY REFERENCES meetings(meeting_pk),
    city_id INT REFERENCES dim_city(city_id),
    transcript_word_count INT,
    summary_word_count INT,
    speaker_count INT
);

-- ---------- INDEXES (QUERY OPTIMIZATION) ----------

-- Foreign key indexes
CREATE INDEX IF NOT EXISTS idx_fact_city_id
    ON fact_meetings(city_id);

CREATE INDEX IF NOT EXISTS idx_dim_city_name
    ON dim_city(city_name);
-- End of Schema