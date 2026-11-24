# Decisions

Owner decisions are marked **(owner)**; Claude's implementation calls are marked **(Claude)** and stand until the owner
says otherwise.

## Settled

1. **Foundation: our own application, built from scratch** (owner, 2026-11-24: Odoo is "just too heavy for what we
   need"). Replaces Odoo Community 20 (chosen 2026-11-20, trialled, then dropped). Stripped to the modules we needed,
   Odoo still carried about 178k lines of Python, 242k of JavaScript and 56k of XML; its strengths, breadth and live
   configurability, were what we were removing; and the simple interface and modes (R5.1, R5.3) meant patching its
   web client. The Odoo-era decisions (fork, module cuts, launcher, trial) are in git history up to commit ca3c8a7.
2. **Public repository, devkit-managed** (owner, 2026-11-20).
3. **Reachable from the open internet** (owner, 2026-11-20), so releases with security fixes are taken promptly.
4. **Tickets are ordinary tasks** (owner, 2026-11-23). Email intake polls a Zoho inbox (such as IT's) and makes each
   new email a task in a team's queue; recategorizing is a team change, which the task's history records.
5. **Browser tests use Playwright** (Claude, at the owner's request, 2026-11-23): Python under pytest like the rest of
   the project, run in Firefox, testing what users see, interface modes included.
6. **Database: Postgres** (owner, 2026-11-24). Coolify runs it and backs it up on a schedule. Automations built or
   imported in the interface (R4.5) are stored in it as their Python source and loaded from there (owner,
   2026-11-24), so its backups cover them.
7. **Backend: Django** (owner, 2026-11-24), for its mature sign-in, sessions, CSRF protection, migrations and admin
   panel, so we don't secure those ourselves.
8. **Frontend: Django serves a JSON API to a separate frontend app** (owner, 2026-11-24). Chosen over Inertia, and
   over server-rendered pages with HTMX (too limiting for designing the frontend). Inertia's estimate was 10–15% less
   development time, but Claude's experience with the API pattern makes it the safer bet: its extra cost is
   predictable, while Inertia's Django adapter trails Inertia by months and its v3 support postdates Claude's
   training. Safeguards for the spec: one shared visibility rule and one shared edit rule used by every endpoint;
   TypeScript types generated from the API; one fixed way to refresh data after a change; a reload prompt when a
   deploy has made an open page out of date.
9. **API library: Django Ninja** (Claude, at the owner's request, 2026-11-24), over Django REST Framework. Typed
   Pydantic request and response definitions, which suit pyright and generate the API description the TypeScript
   types come from; it lists Django 6.1 and Python 3.15 support, where `drf-spectacular` (DRF's API description)
   doesn't yet list Django 6.1.
10. **Django serves the built frontend from the same address as the API** (owner, 2026-11-24), so the browser sends
    Django's session cookie with every API call and Django's CSRF protection works unchanged. A separate address
    would need cross-origin rules plus cross-site cookies or sign-in tokens.
11. **Frontend framework: React, in TypeScript, built with Vite** (owner, 2026-11-24), over Svelte: more mature
    component kits, date and schedule pickers and form libraries, and Claude's experience. Svelte's shorter, more
    readable code mattered less since Claude is the one reading it.

## Open

1. **Frontend tools**: the data-fetching and navigation libraries, and the styling approach.
2. **Project structure**: after the stack.
3. **Automation design** (R4.5): its own discussion, under the owner's criteria.
4. `aeth_ext` in the app process (alerts, central logging, healthchecks.io ping).
5. Coolify server upgrade: currently 2 GB with heavy swap use.
6. **Python 3.15 port** (owner interested, for PEP 810 lazy imports; not now). 3.15.0 shipped 2026-10-09; uv publishes
   a `python3.15-trixie-slim` image; devkit-container's template hard-codes the 3.14 base image.
