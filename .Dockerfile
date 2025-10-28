FROM python:3.13-slim

# Set working directory
WORKDIR /app

# install uv
RUN pip install uv

COPY pyproject.toml /app/

RUN uv sync --frozen --compile-bytecode
# Copy requirements file
COPY /src .env main.py pyproject.toml /app/

ENTRYPOINT ["python", "main.py"]

