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

## Open

1. **Stack**: to decide next. Claude's proposal (not approved): Django with server-rendered pages.
2. **Project structure**: after the stack.
3. **Automation design** (R4.5): its own discussion, under the owner's criteria.
4. `aeth_ext` in the app process (alerts, central logging, healthchecks.io ping).
5. Coolify server upgrade: currently 2 GB with heavy swap use.
6. **Python 3.15 port** (owner interested, for PEP 810 lazy imports; not now). 3.15.0 shipped 2026-10-09; uv publishes
   a `python3.15-trixie-slim` image; devkit-container's template hard-codes the 3.14 base image.
