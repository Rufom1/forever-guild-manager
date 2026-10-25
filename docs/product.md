# Product requirements v0.1

## Vision
A private, friendly guild hub for mostly real-life friends playing WoW: Forever. Reduce coordination overhead and help members discover overlapping goals, not enforce attendance/performance.

## User-facing priorities
1. **Website:** dashboard/home, member profiles and character roster, guild event calendar with RSVPs and roles, guild announcements, shared quest/progression goals, visualizations and tools, permissions/settings, integration/sync status.
2. **Discord:** OAuth linking, slash commands, event posts/RSVP/reminders, alerts, coordination; website and Discord are representations of the same records.
3. **Game integration:** retail Blizzard web API where actually supported for the target game; separate addon/desktop companion for permitted character snapshots, quest state, professions and calendar capabilities where obtainable.

## Examples
- A member signs in with Discord, links main and alt characters, sets availability, RSVPs to Friday's dungeon run.
- Event organizer creates an activity on the website; bot posts it and accepts RSVPs; both surfaces reflect one event.
- Group asks what can be accomplished tonight; app identifies overlapping quest prerequisites from fresh, consented data, shows source/freshness and any uncertainty.

## Design values
- Friends-first: lightweight roles, no mandatory performance scoring.
- Useful even without live Blizzard data: manual entry/fallback, visible staleness.
- Desktop-friendly but responsive for mobile.
- Game data may be incomplete/private/unavailable. Never represent unsupported data as live.

## Explicit non-goals for first release
- Autonomous in-game play, botting, invasive client modifications.
- Full two-way synchronization with the in-game WoW calendar without verified permitted mechanisms.
- Public recruitment/social network platform.
