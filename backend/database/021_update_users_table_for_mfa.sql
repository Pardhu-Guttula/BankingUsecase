-- Epic Title: User Authentication and Security

ALTER TABLE users 
ADD COLUMN mfa_enabled BOOLEAN DEFAULT FALSE,
ADD COLUMN mfa_secret VARCHAR(16);