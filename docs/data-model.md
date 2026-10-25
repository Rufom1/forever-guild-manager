# Conceptual entities (not migrations yet)

- `Guild`: identity, realm, region, settings, external game ids.
- `Member`: human guild participant, preferences, status, role/permissions.
- `Identity`: member-linked Discord / Battle.net identifiers with explicit consent and verification state.
- `Character`: game character; realm, region, class, level, main/alt label, member_id nullable until verified.
- `Event`: canonical guild activity, time zone, start/end, recurrence, party size, description, type, owner.
- `RSVP`: member_id, event_id, character_id optional, intended role, status, timestamp.
- `Objective`: quest, achievement, unlock, profession or manually defined goal; static reference link optional.
- `Progress`: character/member objective state, status, observed_at, source and confidence.
- `SyncRun`: provider, object type/id, started/completed, success/error and freshness.
- `NotificationPreference`: member, channel, event types, opt-in flags.

Every imported field should be traceable to provider/source and capture observation time. API response caching may differ from actual player-state freshness.
