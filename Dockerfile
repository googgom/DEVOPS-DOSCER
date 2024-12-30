FROM python:3.11-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

WORKDIR /app

COPY --chown=appuser:appgroup requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appgroup ./src ./src

RUN ls /app/src

EXPOSE 3456

CMD ["sh", "-c", "python ./src/migration.py && python ./src/server.py"]
