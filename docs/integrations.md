# Integration capability register

Status tags: **planned**, **verify**, **unsupported until proven**.

| Integration | Capability | Status / constraint |
|---|---|---|
| Blizzard Battle.net API | General OAuth and reference data | Planned; register app credentials; confirm permitted use |
| Blizzard character/guild endpoints | Roster, profile, completed quests | VERIFY compatibility and actual data/permission for WoW: Forever; retail endpoint existence alone is not proof |
| Discord API | OAuth login, slash commands, event alerts/RSVP | Planned; bot required permissions and scopes, avoid unnecessary privileged intents |
| WoW Lua addon API | In-client character/quest/calendar snapshots | VERIFY available Forever functions and permissions in target client |
| SavedVariables | Export game data | Only saved on logout/UI reload; companion should read safely, only after files are flushed |
| Desktop sync companion | Post approved snapshots via HTTPS | Optional future component; user consent/data minimization |
| Cloudflare | DNS/domain routing, TLS/proxy where appropriate | Future deployment; account exists, no credentials in repo |

## Spike checklist
1. Verify product/version naming and API namespaces/region; don't assume retail or Classic parity.
2. Check a public sample guild roster endpoint and a sample character endpoint with test credentials (no secrets in logs).
3. Map fields actually returned and identify account-specific/private scopes.
4. Test addon capability in game, not only against web examples.
5. Record outcomes and constraints in `docs/decisions.md`.
