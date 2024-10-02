CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    is_admin BOOLEAN DEFAULT 'f',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    password_hash TEXT
);
CREATE TABLE femtoyaps (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    topic TEXT UNIQUE,
    is_secret BOOLEAN DEFAULT 'f',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    is_deleted BOOLEAN DEFAULT 'f'
);
CREATE TABLE attoyaps (
    id SERIAL PRIMARY KEY,
    femtoyap_id INTEGER REFERENCES femtoyaps,
    creator_id INTEGER REFERENCES users,
    title TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    is_deleted BOOLEAN DEFAULT 'f'
);
CREATE TABLE zeptoyaps (
  id SERIAL PRIMARY KEY,
  attoyap_id INTEGER REFERENCES attoyaps,
  creator_id INTEGER REFERENCES users,
  content TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  is_deleted BOOLEAN DEFAULT 'f'
);
CREATE TABLE secret_permissions (
  femtoyap_id INTEGER REFERENCES femtoyaps,
  user_id INTEGER REFERENCES users
);