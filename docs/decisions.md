# Decisions

Owner decisions are marked **(owner)**; Claude's implementation calls are marked **(Claude)** and stand until the owner
says otherwise.

## Settled

1. **Foundation: Odoo Community 20** (owner, 2026-11-20), over Vikunja, Kanboard, Plane and hosted tools. Chosen for
   its free automation rules (reminders, nagging, escalation), subtasks with their own assignees and deadlines,
   repeating tasks, timesheets, and configuration as code in our own add-on.
2. **Public repository, devkit-managed** (owner, 2026-11-20).
3. **Reachable from the open internet** (owner, 2026-11-20), so releases with security fixes are taken promptly.
4. **Odoo's source becomes our own fork in its own repository** (owner, 2026-11-20), so we can patch Odoo's files and own
   its packaging and pipeline. Not set up yet, but needed before the first release, which builds on it (item 9;
   owner, 2026-11-23); see **Planned: Odoo fork** below. Until then the dependency is Odoo's dated source release,
   pinned in `pyproject.toml`.
5. **Trial data lives in its own module, `company_tasks_trial`** (Claude): the Mailpit mail server and sample
   users/tasks must never reach production, where `company_tasks` alone is installed.
6. **The launcher installs `company_tasks` on a fresh database and updates it on every start** (Claude), so a deploy
   applies the release's rules and templates without a manual step.
7. **Heartbeat from the launcher, probing `/web/health`** (Claude), for devkit-container's healthcheck. No `aeth_ext`
   yet (see open item 1).
8. **Dark mode is its own add-on, `company_dark_mode`** (owner asked for it in the trial, 2026-11-20; separate module is
   Claude's call, open to the structure discussion). Community ships the dark theme (`web.assets_web_dark`) but its
   `ir.http.color_scheme()` always answers light and has no switch (Enterprise has both); the add-on adds a user-menu
   switch that sets the `color_scheme` cookie and overrides `color_scheme()` to honour it. Installed in the trial
   only; whether production installs it is open.
   **It does nothing visible**: Community's dark bundle carries only per-widget touch-ups (~60 lines in `web`); the dark
   palette itself (primary/secondary variables, Bootstrap overrides) is Enterprise's. OCA's `web_dark_mode` (AGPL-3,
   18.0 and 19.0, not yet ported to 20.0) supplies it. Owner declined porting it for now (2026-11-20); when dark mode
   comes back, the OCA port replaces `company_dark_mode`.
9. **Odoo modules: minimal** (owner, 2026-11-23; requirement R10.6).
   - No time tracking: `hr_timesheet` is dropped (R2.4 struck), and with it the Employees app and its extras.
   - Kept from what Odoo auto-installs: `auth_totp` and `auth_passkey` (with their portal and mail parts) for
     two-factor and passkey sign-in, and `base_import`.
   - Dropped from what Odoo auto-installs: `project_todo`, `project_sms`, `partner_autocomplete`, `mail_bot`,
     `google_gmail`, `microsoft_outlook`, `hr_skills`, `project_hr_skills`, the spreadsheet and dashboard modules,
     `web_unsplash`, `api_doc`, `rpc`, `base_import_module`, `base_install_request`, `mysubscription`,
     `privacy_lookup`, `base_report_wkhtmltox`, `portal_discuss`.
   - They are kept out by removing them from Odoo itself, in our fork, from the very beginning (owner, 2026-11-23).
     The stripped fork is the base we build on: nothing outside our list exists to install, and a redeploy does no
     install-then-remove work (downtime matters). The fork deletes them from its source tree, which keeps the tree
     easy to navigate (owner, 2026-11-23). 29 of Odoo's 698 modules remain.
   - `resource_mail` is dropped too (owner, 2026-11-23).
   - `auth_ldap` stays in the fork, for directory sign-in later (owner, 2026-11-23; R7.2). It needs only `base` and
     `base_setup`, and its `python-ldap` library is Odoo's optional `ldap` extra, needed only once it is installed.
   - Odoo's live install, upgrade and uninstall actions become stubs in the fork's code (owner, 2026-11-23). Startup's
     `-i`/`-u` uses separate methods, so it is unaffected: stub `_button_immediate_function` (behind the Apps screen,
     Settings checkboxes and the uninstall wizard) and the upgrade wizard, and mark `button_install`,
     `button_upgrade` and `button_uninstall` `@api.private` so a browser session can't queue a change for the next
     restart. About 5 small changes in 3 files.
   - Settings that involve a module we've cut are removed (owner, 2026-11-23).
   - Cut from the modules that are kept only because a kept module depends on them (owner, 2026-11-23, after a
     survey of the edits each cut needs in the modules we keep):
     - `digest`: easy; its own files in `project` and `base_automation`, two manifest lines, one import.
     - SMS chain (`sms`, `iap_mail`, `iap`, `phone_validation`): easy. `base_automation` depends on it in one
       manifest line; `html_editor` uses IAP for two paid online features (AI text, Google translation), which go
       with it. Adopting SMS later means restoring these or connecting another provider in our add-on.
     - `web_tour`: small in code (two tours, two manifests, 3 lines in `portal`), but it is Odoo's browser-test
       runner; 51 tour-based test files in kept modules go with it (see item 11).
     - `analytic`, `uom`: moderate; about 10 edits in `project_project.py` plus whole files. Nothing we need uses them.
   - `rating`, `portal_rating`: owner leaning toward cutting (2026-11-23), so that nothing about customer ratings is
     left in the interface. Large: 222 lines in 16 `project` files, in the files upstream changes most, so rebases
     will conflict there.
10. **Tickets are ordinary tasks; no helpdesk module** (owner, 2026-11-23). Odoo's Helpdesk is Enterprise (paid per
    user) and OCA's `helpdesk_mgmt` is not yet ported to 20.0 and keeps tickets apart from tasks. Email intake polls a
    Zoho inbox (such as IT's) and makes each new email a task in a team's queue; recategorizing is a team change,
    which the task's history records.
11. **Browser tests use Playwright, not Odoo's tours** (Claude, at the owner's request, 2026-11-23). Written in Python
    under pytest like the rest of the project, run in Firefox, and test what users see, interface modes included,
    from outside the product, so no test machinery ships in it. Tours need Chrome and `web_tour` in the build.
    Server logic keeps Odoo's own Python tests, which need no browser. Cost: a harness that starts Odoo on a fresh
    database, where a tour gets a rolled-back transaction for free.

## Planned: Odoo fork

- A repository holding Odoo's 20.0 branch plus our patches, rebased onto upstream now and then, mainly for fixes that
  could compromise the server (R9.3; owner, 2026-11-23).
- Ships only the modules we use (item 9), from the first release on. A release step runs a script that accounts for
  our module deletions (owner, 2026-11-23).
- Devkit-managed (owner: "almost certainly"), but not self-deployable: devkit-container's features are off and it
  has no Docker setup (owner, 2026-11-23).
- Its own pipeline builds Odoo's wheel (pure Python, so one wheel serves Linux and Windows) and publishes it to
  SFTPyPI; this project then depends on that version instead of the source tarball, a one-line change here.
- Side benefit: no more building Odoo from source on each machine (minutes on Windows).
- To decide when it is set up: the version/tag scheme for our patch releases, and how devkit fits a project that
  Odoo builds with setuptools.

## Open

1. `aeth_ext` in the Odoo process (alerts, central logging, healthchecks.io ping). Both it and Odoo install signal
   handlers, so this needs a look before adopting.
2. White-label scope: owner leaned toward full white label (logo, colors, emails, "Powered by Odoo" footer).
3. Coolify server upgrade: currently 2 GB with heavy swap use; Odoo plus Postgres idle at about 210 MB.
4. **The deployment image does not start yet: Odoo refuses `PYTHONOPTIMIZE`**, which devkit-container's Dockerfile
   template sets in every image (after the project windows, so a window cannot override it). Odoo's guard in
   `odoo/init.py` exists because its code relies on 530 `assert` statements (173 files, none in tests) as real
   checks. Options discussed, none chosen:
   - `PYTHONOPTIMIZE=` (empty, i.e. off) in `docker/compose.yaml`;
   - the launcher re-execs itself without it;
   - a devkit-container opt-out (dependency repo: owner's go-ahead and merge);
   - in the fork, rewrite the asserts as `if` guards at build time, keeping `AssertionError` (7 callers catch it).
     Under `-O` that behaves the same as no `-O`; it only satisfies the template.
   - `-OO` additionally strips docstrings: crashes `base_sparse_field` and `odoo upgrade_code`, and blanks the
     model info text, API doc descriptions and CLI help; the memory saved is unmeasured.
5. **Python 3.15 port** (owner interested, for PEP 810 lazy imports; not now). Findings so far: 3.15.0 shipped
   2026-10-09; uv publishes a `python3.15-trixie-slim` image; greenlet, gevent, psycopg2, lxml, pillow and
   cryptography ship cp315 wheels, reportlab builds from its sdist; Odoo's one known break is `UpgradeHook.load_module`
   in `odoo/modules/module.py` (3.15 no longer calls `load_module`); devkit-container's template hard-codes the
   3.14 base image. Lazy imports must keep `odoo.*` eager (models register by import side effect), e.g. through
   `sys.set_lazy_imports_filter` in the launcher. The memory gain is unmeasured.
6. **Project structure**: to be discussed next.
7. **Foundation reconsidered: owner leaning toward building from scratch** (2026-11-24), since Odoo is too heavy for
   what we need. Estimate behind it: about even to a first release, from scratch clearly less after; Odoo's
   strengths are breadth and live configurability, which item 9 removes, while the simple interface and modes
   (R5.1, R5.3) mean patching its web client. A stripped fork still carries about 178k lines of Python, 242k of
   JavaScript and 56k of XML. Not decided; ratings (item 9) and the fork setup wait on it. The new automation
   builder (R4.5) counts for Odoo, but only Settings administrators can create Odoo's automation rules, which can
   run Python code.
