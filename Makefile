.PHONY: help run test e2e docker docker-run clean

# Default target
help:
	@echo "Available commands:"
	@echo "  make run         - Run FastAPI locally with reload"
	@echo "  make test        - Run unit tests"
	@echo "  make e2e         - Run end-to-end validation"
	@echo "  make docker      - Build Docker image"
	@echo "  make docker-run  - Run Docker container"
	@echo "  make clean       - Clean cache and temp files"

# Run FastAPI locally
run:
	uvicorn app.api.main:app --reload

# Run unit tests
test:
	pytest

# Run end-to-end validation
e2e:
	./scripts/e2e.sh

# Build Docker image
docker:
	docker build -t industrial-cv .

# Run Docker container
docker-run:
	docker run -p 8000:8000 industrial-cv

# Clean caches and temp files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf data/uploads/*
