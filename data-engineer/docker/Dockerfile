FROM python:3.13-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# RUN pip install pandas pyarrow

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first (better layer caching)
COPY "pyproject.toml" "uv.lock" ".python-version" ./

RUN uv sync --locked --no-install-project

# COPY pipeline.py /app/pipeline.py

# copy application code
COPY pipeline.py /app/pipeline.py

# run pipeline
ENTRYPOINT ["python", "pipeline.py"]