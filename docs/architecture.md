# System architecture

## Components
- `apps/web`: Next.js + TypeScript + Tailwind, website and authenticated user interface.
- `apps/api`: FastAPI Python backend, owns business logic/permissions, REST endpoints and integrations.
- `apps/discord-bot`: discord.py worker consuming backend API (not its own independent database).
- `apps/wow-addon`: Lua addon, optional only after compatibility verification.
- `packages/contracts`: OpenAPI/schema-generated clients or other shared contracts.
- PostgreSQL database via Docker for local development.

## Data flow
Blizzard REST (verified endpoints) --> provider adapter --> API/background sync --> PostgreSQL
WoW addon --> SavedVariables (on logout/reload) --> optional consented desktop importer --> API --> PostgreSQL
Discord interactions <--> Discord bot <--> API <--> PostgreSQL
Website <--> API <--> PostgreSQL

## Deployment path
- Phase 0: WSL2 Ubuntu source filesystem; VS Code Remote WSL; Docker Desktop Linux engine integrated with WSL.
- Phase 1: Docker Compose for API + Postgres, add web and bot services once implemented.
- Phase 2: AWS containers (e.g., ECS/Fargate) + managed Postgres (RDS) + secrets management + Cloudflare DNS. Hosting choice not yet finalized.

## Boundaries
- Canonical guild member and calendar records owned by the platform; game/Discord events are imports/projections.
- `game_provider` adapter encapsulates API capabilities and version differences.
- Idempotent imports keyed by provider/object IDs plus provenance and timestamps.
- No direct browser access to Blizzard client secrets or Discord bot tokens.
- Add authorization for every guild-scoped data query/mutation.
