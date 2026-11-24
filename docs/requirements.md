# Requirements

What the company needs from the ticketing system. Planning works from this document.

**Status: draft, under owner review.** Every item below is marked:

- **(owner)**: stated by the owner, with the date.
- **(open)**: not settled; needs the owner's answer before planning depends on it.
- **(learn from use)**: a usage specific that can only be known once the system is in use and pain points show
  **(owner, 2026-11-20)**. Listed in section 12; the initial build doesn't depend on them.

How these are met (the stack, devkit) is recorded in [decisions.md](decisions.md), not here.

## 1. Purpose

1. A shared system for tracking the company's work as tasks, assigned to individual people, with automated
   reminders so tasks don't slip. **(owner, 2026-11-20)**
2. Reminders are the most important capability. **(owner, 2026-11-20)**
3. Today work is handed out by word of mouth and the occasional printed checklist. **(owner, 2026-11-23)**

## 2. Work tracking

1. **R2.1** Tasks, each assignable to an individual person. **(owner, 2026-11-20)**
2. **R2.2** A task can be broken into individual steps whose completion is tracked. **(owner, 2026-11-20)**
3. **R2.3** Projects group tasks; who can see which project is controllable. **(owner, 2026-11-20)**
4. ~~**R2.4** Time tracking on tasks.~~ Struck **(owner, 2026-11-23)**: the office's own timeclock system covers it;
   the two can be integrated later if ever needed.
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
11. **R2.11** Ongoing tasks that never complete, kept as a list of general things to do when other work runs out.
    Possibly just a flag set when creating the task, so it can't be marked complete and never leaves anyone's list.
    **(owner, 2026-11-23)**
12. **R2.12** Teams with shared task queues **(owner, 2026-11-23)**:
    1. A task assigned to a team appears in the queue of everyone on it, and any of them can report progress on it.
    2. A task's assignees are always the union of its teams' members and its individual assignees; all of them can
       report progress.
    3. A task can have more than one team and more than one individual assigned.
    4. Each step follows the same pattern, with its own teams and individuals.
13. **R2.13** Tickets from the stores **(owner, 2026-11-23)**:
    1. A store can open a ticket with the corporate office about an issue it's having: by emailing an inbox such as
       IT's, which creates the ticket automatically, or through a special interface for stores (see R11.2).
    2. A ticket is basically a task: it appears in the relevant team's queue just as tasks do.
    3. Stores often send an issue to the wrong place, so managers and above can recategorize a ticket. That moves it
       to the newly assigned team's queue, and likely leaves a breadcrumb on the ticket showing where it was first
       sent.
    4. Email intake is part of the first release. A store interface other than email comes some time after it and
       must not hold it up.

## 3. Reminders

All by email at minimum. **(owner, 2026-11-20)**

1. **R3.1** Before a deadline. **(owner, 2026-11-20)**
2. **R3.2** Repeating tasks that recreate themselves on a schedule, optional per task, e.g. weekly on a set day.
   **(owner, 2026-11-20; example, 2026-11-23)**
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
8. **R3.8** People hear of a new task by email, and from the web page, which they can be expected to check often.
   Mobile push may follow the first release (R3.6). **(owner, 2026-11-23)**

## 4. Administration and oversight

1. **R4.1** An administrator view across all users and projects. **(owner, 2026-11-20)**
2. **R4.2** Audit logs of important actions. **(owner, 2026-11-20)**
3. **R4.3** Automations and configuration are set up by Claude in code, not by hand in the interface.
   **(owner, 2026-11-20: "such a massive time saver")**
4. **R4.4** Changes to the interface and configuration ship only as redeploys triggered by new GitHub releases,
   through the same release workflow as the company's other projects. Everything is declarative and reproducible;
   nothing relies on live state that a careless redeploy could lose. **(owner, 2026-11-23)** Automations built or
   imported in the interface (R4.5) are the exception: they are data, like tasks.
5. **R4.5** An automation builder in the interface, so people other than the owner can build automations
   **(owner, 2026-11-24)**:
   1. The editor is where complexity is the biggest risk, so its design follows two criteria: there is generally
      one way to do a thing, never more; and that one way is simple and versatile enough that a second is never
      needed.
   2. Automations create and assign tasks, their primary use, as well as send reminders.
   3. Built live in the interface and stored as data; a proven one can be exported into code.
   4. Advanced automations are plain Python files imported through the interface. We choose which imports they get
      and leave it at that: security comes from controlling who is an administrator, not from restricting the
      automations.
   5. Builders: likely administrators only. **(owner leaning)**

## 5. Simplicity

1. **R5.1** Simple for staff to use, with no hours of training. **(owner, 2026-11-20; Jira is the counter-example)**
2. **R5.2** No hours of experimentation to set up automations. **(owner, 2026-11-20)** R4.3 covers this for whoever
   administers the system.
3. **R5.3** Interface modes, set per account, matched to how complex an interface the person can handle. Many
   employees are not technically inclined and will stop using a system that looks too complex, so a simple mode
   gives them only the bare minimum: receiving their tasks and reporting progress on them. **(owner, 2026-11-20:
   "one likely big requirement")** From the interview **(owner, 2026-11-23)**:
   1. No screen these employees already use sets the bar.
   2. A mode is independent of role and changes only the interface: simple mode omits things the account could
      otherwise see or do, but a simple-mode account still sees every task its access allows.
   3. Managers and regular accounts can be put in simple mode; administrators cannot. A manager in simple mode still
      creates tasks, through creation menus kept simple.
   4. Two modes, simple and full, to start; more tiers may be added. Only an administrator can change an account's
      mode.
   5. Each mode is defined in one container (e.g. one file per mode; the format doesn't matter, the pattern does):
      a list of what it omits, and a list of interface elements it replaces, each naming the alternate element or
      class that replaces it. Everything a mode changes lives in that one definition, so a new tier is a new
      definition.

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
3. **R9.3** Security fixes are taken promptly, since it is internet-facing. **(owner, 2026-11-20)** Narrowed: it is only
   task tracking, so the real concern is anything that could compromise the server it runs on. **(owner, 2026-11-23)**
4. **R9.4** Once settled, new features over time are not expected to be needed. **(owner, 2026-11-20)**
5. **R9.5** Backups. **(owner, 2026-11-20: "yes, most likely")**
6. **R9.6** Email goes through the company's Zoho Mail, and only within the company's own domain: every message is
   to and from a Zoho Mail account. No plans to send reminders outside the domain. **(owner, 2026-11-20)**
   To verify before go-live: Zoho's daily sending limit for the company's plan, against the expected volume
   (a daily summary per person, up to ~130).

## 10. Codebase

1. **R10.1** A public repository, managed by devkit. **(owner, 2026-11-20)**
2. **R10.2** We own and can modify the foundation's source, with our own packaging and pipeline.
   **(owner, 2026-11-20)**
3. **R10.3** Code in languages the owner knows (Python or Rust) and that Claude is well trained in; JavaScript or
   TypeScript for the browser side is fine. **(owner, 2026-11-20)**
4. **R10.4** Python 3.15, for lazy imports. **(owner interested, 2026-11-20; not now)**
5. **R10.5** Running under Python's optimize mode. **(owner interested, 2026-11-20; not decided)**
6. **R10.6** Start minimal: only what is relevant to task tracking. **(owner, 2026-11-23)**
7. **R10.7** What ships is stripped down to only what is used: it isn't a CRM. Nothing is installed into the system
   while live. **(owner, 2026-11-23: "NEVER … Period.")**

## 11. People

1. **R11.1** Roughly 20 people to start, possibly as many as 130. **(owner, 2026-11-20)** For now mostly the
   corporate office. **(owner, 2026-11-23)**
2. **R11.2** Possibly used for the stores, either as one generic task tracker per store or with each store as a team
   and every store employee a user. **(owner, 2026-11-20: "maybe")** Which model, if any, is open.
3. **R11.3** Roles **(owner, 2026-11-23)**:
   1. administrators and managers create and assign tasks;
   2. a regular account completes or updates existing tasks and never creates one;
   3. being assigned a task grants no right to edit it beyond reporting progress; any other edit right comes from
      the account's role.
4. **R11.4** Deleting a task **(owner, 2026-11-23)**:
   1. Deleting archives the task by default. An administrator can restore an archived task or delete it for good,
      and can also delete a task for good straight away.
   2. Only the task's creator or an administrator can delete it.
   3. The creator can delete it only while no progress has been posted on it and while still within a grace period
      after creating it. Progress is anything someone other than the creator posts on the task: a ticked step or
      checklist item, a status change, a comment, a photo, or logged time. The aim: a restriction once others' work
      is on the task, without hindering someone who made a mistake creating it.

## 12. Learn from use

Usage specifics to settle once the system is running and pain points show. **(owner, 2026-11-20)**

1. What a reminder offset is measured from (only deadlines, or other dates and events), and where timings are set
   (per task, per project, company-wide defaults).
2. Whether the mobile website is enough on phones.
3. Whether replies to reminder emails should post onto the task.
4. How much data loss is tolerable, and how long records are kept.
5. How long the grace period for deleting a task lasts (R11.4).
6. Which members of a team get reminders for a task assigned to the team. As assignees (R2.12) all of them would,
   which may prove noisy.
