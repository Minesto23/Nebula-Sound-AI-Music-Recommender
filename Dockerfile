# --- Base image ---
FROM python:3.11-slim

# --- Set working directory ---
WORKDIR /app

# --- Set PYTHONPATH ---
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1


# --- Copy requirements and install ---
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy project ---
COPY . .

# --- Expose ports ---
EXPOSE 7860
EXPOSE 8000

# --- Default command ---
CMD ["python", "-u", "ui/app.py"]
