.. _lifecycle-expiration-policies:

Expiration Policies
====================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


Over time, people's relationships with your organization end or change. Some
departures are managed manually — an administrator updates a Role's status when
notified. But for organizations managing large populations, automating these
transitions is essential. **Expiration Policies** are rules that automatically
manage Person Role status over time, triggering transitions like Grace Period,
Expired, Suspended, or Archived based on time-based conditions such as
approaching or passed validity dates.

Expiration Policies run as a background job on a schedule (typically via cron),
rather than in response to individual events. This makes them the right tool for
population-scale lifecycle management.

.. note::

   Expiration Policies are referenced in the Registry PE Technical Reference as
   a mechanism for changing Person status, but a dedicated v5 configuration guide
   is not yet available in the Technical Manual. For current configuration
   guidance, see
   `Expiration Policies <https://spaces.at.internet2.edu/spaces/COmanage/pages/49840329/Expiration+Policies>`_
   in the v4 Technical Manual, and check the
   `Registry community resources <https://spaces.at.internet2.edu/spaces/COmanage>`_
   for v5 updates.

1. What Expiration Policies Do
------------------------------

An Expiration Policy defines a rule of the form: when a Person Role meets
condition X, change its status to Y. Conditions typically involve the Role's
current status combined with validity dates — for example, a Role whose valid
through date has passed and is still Active. Actions include changing the Role
status, sending notifications, and triggering provisioning updates downstream.

The practical effect is to automate the offboarding workflow. Rather than
requiring administrators to manually update status for everyone whose relationship
has ended, Policies can:

- Move people from Active to Grace Period when their end date approaches
- Move them from Grace Period to Expired when the grace period ends
- Eventually move them to Archived when no further action is expected

Each of these transitions triggers reprovisioning, so downstream systems
automatically reflect the changing access at each stage.

2. Running Expiration Policies
------------------------------

Expiration Policies are triggered by a scheduled background job. The job
processes all configured Policies for a CO and applies any resulting status
changes. This job should be run periodically via cron — typically once per day,
often scheduled to run shortly after midnight so that transitions take effect at
the start of a new day.

For job configuration and scheduling details, see the Registry PE Technical
Manual (Jobs section) and :ref:`using-operations`.

3. Relationship to Validity Dates
---------------------------------

Expiration Policies and validity dates work together but serve different
purposes. See :ref:`lifecycle-status-and-validity` for the full status model.

Validity date rules (built into the status recalculation logic) handle simple,
specific cases automatically — a Role with a valid through date in the past
becomes Expired. These transitions happen as part of normal Registry processing.

Expiration Policies handle more complex, configurable workflows that require
multiple stages, notification, or custom conditions. For example, a simple
validity date transition moves a Role directly to Expired when the date passes.
An Expiration Policy can instead first move the Role to Grace Period a few days
before the date, then to Expired on the actual date, with notifications at each
stage.

Both mechanisms can coexist in the same deployment. Many deployments use validity
dates for straightforward cases and Expiration Policies for workflows that need
more control.

4. Changes from v4
------------------

- **Expiration Policies exist in Registry v5** and are referenced in the v5
  Technical Reference as a mechanism for changing Person status. However, the
  v5 configuration documentation was not yet available in the Technical Manual
  at the time this guide was written. The v4 Expiration Policies page remains the
  best available reference; verify v5 behavior with the Registry community.

- **Status terminology changes in v5 affect Policy configurations.** In
  particular, the v4 status "Deleted" is now "Archived" in v5, and the new
  "Pending Activation" status exists in v5 but not in v4. When translating v4
  Expiration Policy configurations to v5, account for these renamed and new
  statuses.

- **Locked status cannot be reset by Expiration Policies** (or by Enrollment
  Flows or Pipelines). Only a CO or COU administrator can unlock a Person.
