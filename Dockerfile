FROM ubuntu:22.04

# Use LABEL instead of deprecated MAINTAINER instruction
LABEL maintainer="John Doe <john@example.com>"

# Combine RUN commands and clean up in same layer to reduce image size
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3=3.10.* \
        python3-pip=22.0.* && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV MY_ENV_VAR=value

EXPOSE 8000

# Use python3 explicitly
CMD ["python3", "app.py"]

# Set non-root user for security
RUN useradd -m appuser
USER appuser
