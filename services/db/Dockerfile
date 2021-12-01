FROM  postgres:12
COPY rates.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
ENV POSTGRES_PASSWORD=ratestask
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=postgres
