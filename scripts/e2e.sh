#!/bin/bash
set -e

PORT=8000

echo "Starting E2E validation..."

# Kill anything running on port 8000
lsof -ti tcp:$PORT | xargs kill -9 2>/dev/null || true

uvicorn app.api.main:app --host 127.0.0.1 --port $PORT &
SERVER_PID=$!

sleep 3

echo "Checking health endpoint..."
curl -f http://127.0.0.1:$PORT/health/ | grep ok

echo "Checking premium lock (expected 402)..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:$PORT/premium/video-inspection)

if [ "$HTTP_CODE" != "402" ]; then
  echo "Expected HTTP 402, got $HTTP_CODE"
  kill $SERVER_PID
  exit 1
fi

kill $SERVER_PID

echo "E2E validation PASSED."
