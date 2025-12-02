# --- ÉTAPE 1: Construction (Build Stage) ---
FROM python:3.11-slim as builder
WORKDIR /install
ENV PYTHONUNBUFFERED=1
RUN pip install uv
COPY pyproject.toml .
COPY requirements.txt .
RUN uv pip install --no-cache-dir -r requirements.txt --system

# --- ÉTAPE 2: Production (Final Stage) ---
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

# Security setup (Non-root user)
RUN adduser --system --group fastapiuser
USER fastapiuser

# 1. Copy installed packages (libraries/site-packages)
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# 2. 🔥 FIX: Copy the executables (uvicorn, fastapi, etc.) to the $PATH location
# The user (fastapiuser) needs permissions for this directory, which is handled
# by ensuring the $PATH includes /usr/local/bin (it usually does by default).
# Note: We must use a full path copy here, not relative.
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . .

# Start the application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]