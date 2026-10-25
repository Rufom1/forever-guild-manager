# Agent instructions

Read README.md and all docs/ before substantive changes. Treat documented product choices as requirements, not as implemented features.

- Website first. Website and Discord bot must use the same FastAPI backend and database; no duplicate business logic or independent membership/calendar stores.
- Model a person/member separately from their WoW characters (main and alts) and their Discord account.
- First-class provenance: source, fetched_at, observed_at, sync status, and freshness for imported data.
- Keep game integrations behind provider interfaces; NEVER assume WoW: Forever has parity with retail Blizzard REST APIs or in-game addon APIs. Verify supported endpoints against current official documentation and the actual game client before implementation.
- Do not design addon automation that sends arbitrary HTTP requests from WoW, automates gameplay, injects into processes, or writes game files while the client is running. SavedVariables import/export must be explicitly scoped and consent-based.
- Store OAuth secrets/server tokens only in environment/secrets management, never client bundles, SavedVariables, repo or logs. Do not commit .env.
- Use typed interfaces/schemas; add migrations and automated tests before adding persistent features.
- Prefer a modular monolith; Docker Compose locally, deployable containers later. No premature microservices or Kubernetes.
- Favor pragmatic incremental delivery. Ask for user-facing choices only when irreversible or security relevant. Record decisions in docs/decisions.md.
- External integrations should degrade gracefully and display stale/unavailable status rather than fabricate data.

Initial implementation milestone: scaffold Next.js website with a basic dashboard, establish API connectivity, implement Discord OAuth login securely, member profile, manual character registration and event calendar. Before any Blizzard-dependent feature, build a tiny proof-of-concept that checks actual Forever data availability.
