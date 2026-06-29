.. _ops-history:

History and Audit Trail
=======================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry maintains two parallel systems for tracking what has happened to
records over time: **History Records** and **Changelogs**. Together they
provide the audit trail needed for troubleshooting, accountability, and
understanding the state of your data.

For the full technical reference, see
`History Records and Changelogs <https://spaces.at.internet2.edu/spaces/COmanage/pages/350161263/History+Records+and+Changelogs>`_
in the Technical Manual.

1. History Records
-------------------

History Records are created at logical points during Registry operations and
are intended to be human-readable explanations of transactions — a Name was
updated, a Group Membership was added, an Enrollment Flow was completed.

Registry maintains three types of History Records:

**Regular History Records**
   Apply to People, Person Roles, External Identities, and Groups. Most
   Registry activity is recorded here. These records can be viewed from the
   relevant Person or Group canvas in the Registry interface.

**Petition History Records**
   Apply to transactions specific to Enrollment Flows. Because Petitions are
   generally created before a Person record exists, Petition History cannot be
   recorded in regular History Records until the Petition is finalized.

**Job History Records**
   Apply to Registry Jobs. Jobs may need to record History that is not
   specific to any one Person or object — for example, a sync job that
   processed thousands of records.

.. note::

   It may be necessary to review multiple types of History Records to get a
   complete picture of a complex transaction.

2. Supplementing History Records
---------------------------------

Administrators can manually add History Records to supplement the
automatically-generated entries. This is useful for recording the reason
behind a manual change, noting an out-of-band action, or adding context that
would not otherwise appear in the automated record.

.. TODO: Add instructions and screenshots for supplementing History Records
   once v5 UI screenshots are available.

3. Changelogs
--------------

In addition to human-readable History Records, Registry maintains
**Changelogs** — database-level transaction logs that record every change to
tracked fields. A Changelog Entry is created on any change to a tracked record
and stored in the active table itself.

Basic Changelog information is visible at the bottom of each record page in
the Registry interface, with links to Archive Records showing previous values.
Not all information is currently visible in the UI; enhancements to this
interface are expected in future releases.

For technical details about how Changelog behavior works under the hood, see
`Changelog Behavior <https://spaces.at.internet2.edu/spaces/COmanage/pages/350161235/Registry+PE+TID+Changelog+Behavior>`_
in the Technical Manual.

4. Changes from v4
-------------------

- **Changelogs** are now stored in the active table itself (as of v5.0.0),
  rather than in a separate changelog table as in earlier versions. This
  change makes changelog access more straightforward.

- **Job History Records** are a new record type in v5, providing structured
  history for asynchronous Job processing.
