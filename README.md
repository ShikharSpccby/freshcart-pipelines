# FreshCart – From Git to Gold

**Project owner:** Shikhar Pandey  
**Roll number:** 26pcso05  
**Repository:** `freshcart-pipelines`

An end-to-end Data Engineering project covering Git/CI, Snowflake ELT, Mage ML orchestration, RabbitMQ event streaming, and (later) streaming-to-warehouse integration.

## Project status

This repository is a clean starter scaffold. Components are marked pending until they are implemented and executed successfully. No external service execution is claimed by this scaffold.

## Planned components

- `elt/`: FreshCart extraction, Snowflake loading, SQL transformations, and notebook.
- `iris_project/`: Mage Iris classification pipeline.
- `stream/`: RabbitMQ dispatcher, drivers, and future lakehouse consumer.
- `tests/`: Local automated tests.
- `.github/workflows/`: GitHub Actions CI.
- `docs/`: Architecture and implementation notes.

## Local setup

See `docs/setup-wsl.md` for WSL Ubuntu instructions.

## Configuration and secrets

Copy `.env.example` to `.env` and fill in credentials locally. Never commit `.env`.
