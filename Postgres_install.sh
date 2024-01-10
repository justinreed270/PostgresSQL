#!/bin/bash

# Update system
sudo apt update
sudo apt upgrade -y

# Install PostgreSQL
sudo apt install postgresql -y

# Start and enable PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Set PostgreSQL user password
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'your_password';"

# Create a new PostgreSQL user
sudo -u postgres psql -c "CREATE USER your_username WITH PASSWORD 'your_password';"

# Create a new PostgreSQL database
sudo -u postgres psql -c "CREATE DATABASE your_database;"

# Grant privileges to the new user on the new database
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE your_database TO your_username;"

# Restart PostgreSQL service
sudo systemctl restart postgresql

# Verify PostgreSQL installation
psql --version

echo "PostgreSQL installation completed!"
