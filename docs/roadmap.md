# Delivery roadmap

## M0 — Local environment (now)
- WSL Ubuntu + VS Code Remote WSL + Docker integration
- repo structure, docs, AGENTS.md, minimal API/health and DB containers
- Confirm `docker compose up --build` and `curl localhost:8000/health`

## M1 — Website usable without integrations
- Next.js scaffold with responsive shell/dashboard
- secure Discord OAuth identity/login, invitation/membership restrictions
- manual linked characters, calendar events and RSVPs, basic roles/settings
- PostgreSQL migrations and tests

## M2 — Game data proof-of-concept
- research/verify WoW: Forever API support; provider interfaces
- selective roster/profile sync only for confirmed endpoints
- show sync freshness/error states

## M3 — Discord
- slash commands, calendar reminders, event notification, RSVP synchronization

## M4 — Addon bridge
- validate in-game APIs; minimal Lua data snapshot
- permitted export/import + optional local sync companion

## M5 — Guild insights
- shared objective matching, scheduling suggestions, dashboards, AI assisted explanations (optional)
