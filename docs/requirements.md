# Requirements

What the company needs from the ticketing system. Planning works from this document.

**Status: draft, under owner review.** Every item below is marked:

- **(owner)**: stated by the owner, with the date.
- **(open)**: not settled; needs the owner's answer before planning depends on it.

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
5. **R2.5** Whether a step needs its own assignee and deadline, or only a done/not-done mark, varies by task.
   **(open)**

## 3. Reminders

All by email at minimum. **(owner, 2026-11-20)**

1. **R3.1** Before a deadline. **(owner, 2026-11-20)**
2. **R3.2** Repeating tasks that recreate themselves on a schedule. **(owner, 2026-11-20)**
3. **R3.3** Nagging every day until the task is done. **(owner, 2026-11-20)**
4. **R3.4** Escalation to a manager when a task is overdue. **(owner, 2026-11-20)**
5. **R3.5** Reminders on individual steps, for some tasks. **(owner, 2026-11-20: "potentially, depends on the task")**
6. **R3.6** Channels beyond email (phone push, SMS, chat). **(open)**
7. **R3.7** The timings: how long before a deadline, when the daily nag goes out, how many days overdue before
   escalating, and whether these vary by project or task. The trial uses 1 day, 8:00 Eastern and 2 days. **(open)**

## 4. Administration and oversight

1. **R4.1** An administrator view across all users and projects. **(owner, 2026-11-20)**
2. **R4.2** Audit logs of important actions. **(owner, 2026-11-20)**
3. **R4.3** Automations and configuration are set up by Claude in code, not by hand in the interface.
   **(owner, 2026-11-20: "such a massive time saver")**

## 5. Simplicity

1. **R5.1** Simple for staff to use, with no hours of training. **(owner, 2026-11-20; Jira is the counter-example)**
2. **R5.2** No hours of experimentation to set up automations. **(owner, 2026-11-20)** R4.3 covers this for whoever
   administers the system.

## 6. Cost

1. **R6.1** No per-user monthly fees: the owner can't define who counts as a "user" up front. **(owner, 2026-11-20)**
2. **R6.2** No dependence on a vendor's waiting list or approval to get a needed feature. **(owner, 2026-11-20)**

## 7. Access

1. **R7.1** Reachable over the open internet, so people can use it away from the office. **(owner, 2026-11-20)**
2. **R7.2** How people sign in: separate passwords, or the company's existing accounts. **(open)**
3. **R7.3** Phone use: whether staff will use it on phones, and whether the mobile website is enough. **(open)**

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
5. **R9.5** Backups, how much data loss is tolerable, and how long records are kept. **(open)**
6. **R9.6** The outgoing mail service the reminders send through. **(open)**

## 10. Codebase

1. **R10.1** A public repository, managed by devkit. **(owner, 2026-11-20)**
2. **R10.2** We own and can modify the foundation's source, Odoo's core files included, with our own packaging
   and pipeline, likely in its own repository. **(owner, 2026-11-20)**
3. **R10.3** Code in languages the owner knows (Python or Rust) and that Claude is well trained in; JavaScript or
   TypeScript for the browser side is fine. **(owner, 2026-11-20)**
4. **R10.4** Python 3.15, for lazy imports. **(owner interested, 2026-11-20; not now)**
5. **R10.5** Running under Python's optimize mode. **(owner interested, 2026-11-20; not decided)**

## 11. People

1. **R11.1** How many people will use it, and in which roles (staff, managers, administrators). **(open)**
2. **R11.2** Whether anyone outside the company (customers, vendors) needs access. **(open)**
