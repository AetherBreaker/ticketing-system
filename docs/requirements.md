# Requirements

What the company needs from the ticketing system. Planning works from this document.

**Status: draft, under owner review.** Every item below is marked:

- **(owner)**: stated by the owner, with the date.
- **(open)**: not settled; needs the owner's answer before planning depends on it.
- **(learn from use)**: a usage specific that can only be known once the system is in use and pain points show
  **(owner, 2026-11-20)**. Listed in section 12; the initial build doesn't depend on them.

How these are met (Odoo, the fork, devkit) is recorded in [decisions.md](decisions.md), not here.

## 1. Purpose

1. A shared system for tracking the company's work as tasks, assigned to individual people, with automated
   reminders so tasks don't slip. **(owner, 2026-11-20)**
2. Reminders are the most important capability. **(owner, 2026-11-20)**

## 2. Work tracking

1. **R2.1** Tasks, each assignable to an individual person. **(owner, 2026-11-20)**
2. **R2.2** A task can be broken into individual steps whose completion is tracked. **(owner, 2026-11-20)**
3. **R2.3** Projects group tasks; who can see which project is controllable. **(owner, 2026-11-20)**
4. **R2.4** Time tracking on tasks. **(owner, 2026-11-20)**
5. **R2.5** A step can have its own assignee and its own deadline; both are optional. **(owner, 2026-11-20)**

## 3. Reminders

All by email at minimum. **(owner, 2026-11-20)**

1. **R3.1** Before a deadline. **(owner, 2026-11-20)**
2. **R3.2** Repeating tasks that recreate themselves on a schedule. **(owner, 2026-11-20)**
3. **R3.3** Nagging every day until the task is done. **(owner, 2026-11-20)**
4. **R3.4** Escalation to a manager when a task is overdue. **(owner, 2026-11-20)**
5. **R3.5** Reminders on individual steps, for some tasks. **(owner, 2026-11-20: "potentially, depends on the task")**
6. **R3.6** SMS, and possibly mobile push, likely later. Not part of the initial build and deploy: they come once
   the system is up and working. **(owner, 2026-11-20)**
7. **R3.7** Every reminder, whether a regular reminder, a past-due reminder or an escalation, is timed by one of
   three base timings **(owner, 2026-11-20)**:
   1. a time offset (e.g. a duration before a deadline);
   2. a cron-like schedule;
   3. an exact date and time.

## 4. Administration and oversight

1. **R4.1** An administrator view across all users and projects. **(owner, 2026-11-20)**
2. **R4.2** Audit logs of important actions. **(owner, 2026-11-20)**
3. **R4.3** Automations and configuration are set up by Claude in code, not by hand in the interface.
   **(owner, 2026-11-20: "such a massive time saver")**

## 5. Simplicity

1. **R5.1** Simple for staff to use, with no hours of training. **(owner, 2026-11-20; Jira is the counter-example)**
2. **R5.2** No hours of experimentation to set up automations. **(owner, 2026-11-20)** R4.3 covers this for whoever
   administers the system.
3. **R5.3** Interface modes, set per account, matched to how complex an interface the person can handle. Many
   employees are not technically inclined and will stop using a system that looks too complex, so a simple mode
   gives them only the bare minimum: receiving their tasks and reporting progress on them. **(owner, 2026-11-20:
   "one likely big requirement")**

## 6. Cost

1. **R6.1** No per-user monthly fees: the owner can't define who counts as a "user" up front. **(owner, 2026-11-20)**
2. **R6.2** No dependence on a vendor's waiting list or approval to get a needed feature. **(owner, 2026-11-20)**

## 7. Access

1. **R7.1** Reachable over the open internet, so people can use it away from the office. **(owner, 2026-11-20)**
2. **R7.2** How people sign in. Needs a discussion; it is likely time for the company to move to a directory service
   for user provisioning. **(open; owner, 2026-11-20)**
3. **R7.3** Staff will use it on phones. **(owner, 2026-11-20: "extremely likely")**

## 8. Branding

1. **R8.1** White label: the company's name, logo and colors in place of the vendor's, including in emails.
   **(owner, 2026-11-20: "probably full white-label")**
2. **R8.2** Dark mode. **(owner asked about it, 2026-11-20; not wanted now)**

## 9. Hosting and operations

1. **R9.1** Self-hosted. **(owner, 2026-11-20)**
2. **R9.2** Runs on the company's Coolify server. That server is low-end (2 GB, already swapping); upgrading it is
   acceptable. **(owner, 2026-11-20)**
3. **R9.3** Security fixes are taken promptly, since it is internet-facing. **(owner, 2026-11-20)**
4. **R9.4** Once settled, new features over time are not expected to be needed. **(owner, 2026-11-20)**
5. **R9.5** Backups. **(owner, 2026-11-20: "yes, most likely")**
6. **R9.6** Email goes through the company's Zoho Mail, and only within the company's own domain: every message is
   to and from a Zoho Mail account. No plans to send reminders outside the domain. **(owner, 2026-11-20)**
   To verify before go-live: Zoho's daily sending limit for the company's plan, against the expected volume
   (a daily summary per person, up to ~130).

## 10. Codebase

1. **R10.1** A public repository, managed by devkit. **(owner, 2026-11-20)**
2. **R10.2** We own and can modify the foundation's source, Odoo's core files included, with our own packaging
   and pipeline, likely in its own repository. **(owner, 2026-11-20)**
3. **R10.3** Code in languages the owner knows (Python or Rust) and that Claude is well trained in; JavaScript or
   TypeScript for the browser side is fine. **(owner, 2026-11-20)**
4. **R10.4** Python 3.15, for lazy imports. **(owner interested, 2026-11-20; not now)**
5. **R10.5** Running under Python's optimize mode. **(owner interested, 2026-11-20; not decided)**

## 11. People

1. **R11.1** Roughly 20 people to start, possibly as many as 130. **(owner, 2026-11-20)** The roles (staff,
   managers, administrators) are open.
2. **R11.2** Possibly used for the stores, either as one generic task tracker per store or with each store as a team
   and every store employee a user. **(owner, 2026-11-20: "maybe")** Which model, if any, is open.

## 12. Learn from use

Usage specifics to settle once the system is running and pain points show. **(owner, 2026-11-20)**

1. What a reminder offset is measured from (only deadlines, or other dates and events), and where timings are set
   (per task, per project, company-wide defaults).
2. Whether the mobile website is enough on phones.
3. Whether replies to reminder emails should post onto the task.
4. How much data loss is tolerable, and how long records are kept.
