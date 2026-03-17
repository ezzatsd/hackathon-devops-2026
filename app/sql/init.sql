CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO users (email)
VALUES
  ('alice@example.com'),
  ('bob@example.com')
ON CONFLICT (email) DO NOTHING;
