# 1. Base Image: Start with a lightweight version of Python 3.10
FROM python:3.10-slim

# 2. Set Working Directory: This is the folder inside the container where we work
WORKDIR /app

# 3. Copy Dependencies: We copy just the requirements first (for caching speed)
COPY requirements.txt .

# 4. Install Dependencies: Run pip install inside the container
# We add --no-cache-dir to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Code: Move your entire project into the container
COPY . .

# 6. Expose Port: Streamlit runs on port 8501 by default
EXPOSE 8501

# 7. Run Command: What happens when the container starts?
# We point to the specific port and address to make it accessible outside
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]