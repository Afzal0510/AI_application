#!/bin/bash
# Run backend
cd backend && uvicorn app:app --reload &

# Run frontend
cd ../frontend && streamlit run app.py
