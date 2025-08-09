# Python CRUD User Management System

This is a simple command-line User Management System built with Python and PostgreSQL. It allows you to **Create**, **Read**, **Update**, and **Delete** user records.

## Features

- Add new users
- View all users
- Update user details
- Delete users

## Requirements

- Python 3.x
- [psycopg2](https://pypi.org/project/psycopg2/) library
- PostgreSQL server

## Setup

1. **Install dependencies:**
   ```bash
   pip install psycopg2
   ```

2. **Configure your database:**
   - Create a PostgreSQL database (e.g., `db`).
   - Update the `user` and `password` fields in `app.py` with your credentials.

3. **Run the app:**
   ```bash
   python app.py
   ```

## Usage

Follow the on-screen menu to manage users.

## Notes

- Make sure your PostgreSQL server is running.
- The app will create a `users` table if it does not exist.