FROM python:3.13-slim
WORKDIR /app

# 1. install uv
RUN pip install --no-cache-dir uv==0.4

# 2. dependency layer (cache-friendly)
COPY pyproject.toml uv.lock ./
RUN uv venv && uv sync --frozen --compile-bytecode

# 3. source layer
COPY src/ ./src/
COPY main.py ./

# 4. use the venv interpreter
ENTRYPOINT ["/app/.venv/bin/python", "main.py"]