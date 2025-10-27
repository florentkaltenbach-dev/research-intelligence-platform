-- Database setup for Research Intelligence Platform
-- Run with: sudo -u postgres psql < setup-db.sql

-- Create database
CREATE DATABASE research_db;

-- Create user
CREATE USER research WITH PASSWORD 'research';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE research_db TO research;

-- Change owner
ALTER DATABASE research_db OWNER TO research;
