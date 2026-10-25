# Guild Platform

Private/friends-oriented World of Warcraft guild management platform. One backend, three user-facing clients: website, Discord bot, optional WoW addon/companion.

## Priorities
1. Guild website: interface, dashboard, calendar, roster, visualizations, tools, settings; ingest supported Blizzard data.
2. Discord bot: alerts, events, RSVPs, commands and coordination against the same backend.
3. WoW addon/compatibility: collect permitted in-game character/quest/calendar data where available; optional desktop sync for SavedVariables.

Read `docs/product.md`, `docs/architecture.md`, `docs/integrations.md`, `docs/data-model.md`, `docs/roadmap.md`, and `AGENTS.md` before implementing features.

## Local first run (WSL Ubuntu + Docker Desktop WSL integration)
```bash
cp .env.example .env
docker compose up --build -d
docker compose ps
curl http://localhost:8000/health
```
Expected: `{"status":"ok","service":"guild-api"}`. PostgreSQL runs in Docker, exposed only to other Compose services.

Stop: `docker compose down` (keeps database volume). Destructive reset: `docker compose down -v`.

This starter is deliberately a **minimal API and database bootstrap**, not a complete app. Do not infer integration support from scaffolding.
