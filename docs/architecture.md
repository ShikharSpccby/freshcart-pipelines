# FreshCart architecture

Status: planned; implementation and execution evidence pending.

Planned components:

1. GitHub repository and GitHub Actions CI.
2. FreshCart ELT: source extraction → raw landing → Snowflake Bronze → Silver → Gold.
3. Mage Iris ML pipeline: load → validate/prepare → train → evaluate/export.
4. RabbitMQ: dispatcher → topic exchange → bound driver queues.
5. Optional integration: RabbitMQ consumer → landing batch → Snowflake ingestion.

Update this document as components are implemented and verified.
