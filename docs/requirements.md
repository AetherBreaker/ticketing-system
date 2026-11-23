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
3. Today work is handed out by word of mouth and the occasional printed checklist. **(owner, 2026-11-23)**

## 2. Work tracking

1. **R2.1** Tasks, each assignable to an individual person. **(owner, 2026-11-20)**
2. **R2.2** A task can be broken into individual steps whose completion is tracked. **(owner, 2026-11-20)**
3. **R2.3** Projects group tasks; who can see which project is controllable. **(owner, 2026-11-20)**
4. **R2.4** Time tracking on tasks. **(owner, 2026-11-20)**
5. **R2.5** A step can have its own assignee and its own deadline; both are optional. **(owner, 2026-11-20)**
6. **R2.6** Tasks differ in shape, and progress is reported to match **(owner, 2026-11-23)**:
   1. done or not done;
   2. a series of steps;
   3. pieces, each delegated to a specific person, where each piece is itself done or not done, or has its own
      steps to check off;
   4. a checklist of items, e.g. every part and peripheral a new POS build needs.
7. **R2.7** Task lists that repeat on demand, not on a schedule (R3.2 covers scheduled repeats). The example is
   opening a new store, whose pieces go to people across the company: office staff (paperwork, permit applications,
   the store's vendor accounts), interior setup, and IT (building the POS, preparing the computers and devices).
   **(owner, 2026-11-23)**
8. **R2.8** Comments and photos on tasks, now and then. **(owner, 2026-11-23: "definitely")**
9. **R2.9** A task can require a photo before it can be marked complete. **(owner, 2026-11-23: "useful for certain
   cases")**
10. **R2.10** A progress bar or completion percentage is the least likely need. **(owner, 2026-11-23: "the rarest
    and least likely to be used or needed")**

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
   "one likely big requirement")** From the interview **(owner, 2026-11-23)**:
   1. No screen these employees already use sets the bar.
   2. A mode changes the interface, not what an account can see: a simple-mode account sees every task its access
      allows, like any other account.
   3. Simple mode includes creating tasks, for now, through creation menus kept simple. Whether that holds for every
      simple-mode account or only those whose role may create (R11.3) is **(open)**.
   4. How many modes there are, and who sets an account's mode, are **(open)**.

## 6. Cost

1. **R6.1** No per-user monthly fees: the owner can't define who counts as a "user" up front. **(owner, 2026-11-20)**
2. **R6.2** No dependence on a vendor's waiting list or approval to get a needed feature. **(owner, 2026-11-20)**

## 7. Access

1. **R7.1** Reachable over the open internet, so people can use it away from the office. **(owner, 2026-11-20)**
2. **R7.2** How people sign in. Needs a discussion; it is likely time for the company to move to a directory service
   for user provisioning. **(open; owner, 2026-11-20)**
3. **R7.3** Staff use it on Windows desktops and on Android and iOS phones. **(owner, 2026-11-20: phones "extremely
   likely"; the device list, 2026-11-23)**

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

1. **R11.1** Roughly 20 people to start, possibly as many as 130. **(owner, 2026-11-20)** For now mostly the
   corporate office. **(owner, 2026-11-23)**
2. **R11.2** Possibly used for the stores, either as one generic task tracker per store or with each store as a team
   and every store employee a user. **(owner, 2026-11-20: "maybe")** Which model, if any, is open.
3. **R11.3** Roles **(owner, 2026-11-23)**:
   1. administrators and managers create and assign tasks;
   2. a regular account completes or updates existing tasks and never creates one. Whether that also bars adding
      steps or checklist items to a task assigned to them is **(open)**.
4. **R11.4** Deleting a task **(owner, 2026-11-23)**:
   1. only its creator or an administrator can delete it;
   2. preferably, once progress has been posted on it, only an administrator can;
   3. but someone who made a mistake creating a task must not be hindered from deleting it.

   How to meet 2 and 3 together is **(open)**.

## 12. Learn from use

Usage specifics to settle once the system is running and pain points show. **(owner, 2026-11-20)**

1. What a reminder offset is measured from (only deadlines, or other dates and events), and where timings are set
   (per task, per project, company-wide defaults).
2. Whether the mobile website is enough on phones.
3. Whether replies to reminder emails should post onto the task.
4. How much data loss is tolerable, and how long records are kept.
