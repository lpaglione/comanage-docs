.. _using-operations:

Operations
==========

Operations covers the tools and features that keep your Registry instance
running smoothly — scheduling background work, tracking what has happened and
why, finding records efficiently, managing the lifecycle of data, and securing
access to the platform.

1. Background Jobs
-------------------

Registry **Jobs** are processes designed to run asynchronously — usually via
cron — and are intended for two broad purposes: handling **large or time-consuming
operations** that are not suitable for a single web transaction, and **automating
recurring tasks** such as re-provisioning records in batch on a schedule. Jobs
can be queued from the Registry interface (where supported by the specific Job
Plugin) or run directly from the command line.

.. button-ref:: ops-jobs
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Jobs →

2. Notifications
-----------------

**Notifications** are short internal messages that Registry uses to alert
administrators and other participants to events that require their attention
— such as enrollment approvals pending, or actions taken on a Person record.
Notifications can be delivered through the Registry web interface and by email.

.. button-ref:: ops-notifications
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Notifications →

3. History and Audit Trail
---------------------------

Registry maintains two parallel systems for tracking what has happened:
**History Records** (human-readable logs of transactions) and **Changelogs**
(database-level records of every change to tracked fields). Together they
provide the audit trail needed for troubleshooting and accountability.

.. button-ref:: ops-history
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about History and Changelogs →

4. Searching and Filtering
---------------------------

Registry provides two ways to find records: **Filtering** within a specific
object type's index view, and **Global Search** across the entire Registry.
Global Search can locate people, groups, identifiers, email addresses, and
other objects, and supports searching by UUID and Change Request Identifier
as of v5.2.0.

.. button-ref:: ops-searching
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Searching and Filtering →

5. Record Management
---------------------

Registry provides tools for managing the data stored within it: controlling
record statuses, removing data, normalizing attribute values for consistency,
and cloning configuration or person records across COs.

.. button-ref:: ops-record-management
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Record Management →

6. Security Configuration
--------------------------

:bdg-success:`New in v5` :bdg-secondary:`Available: v5.2.0`

Registry supports requiring Multi-Factor Authentication (MFA) for access to
the platform. MFA enforcement is configured at the platform level, with the
option to allow individual COs to exempt specific people via MFA Exemption
Groups.

.. button-ref:: ops-security
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Security Configuration →

----

.. _ops-coming-to-v5:

Coming to v5
-------------

The following operational capabilities are planned for v5 and are in
development:

**Bulk Operations** — the ability to select a set of records and apply an
operation (such as a status change) to all of them at once. Bulk Operations
will be implemented via Job Plugins, allowing operations to be queued for
asynchronous processing.

**Copy within a CO** — copying a configuration or data object to a new object
within the same CO (for example, duplicating an Enrollment Flow as a starting
point for a new one). This is planned for a future release.

**CO Configuration Copy** — copying the full configuration of one CO to a new
CO, for example to promote a QA configuration to production without manually
recreating every setting. Individual configuration objects can already be
cloned across COs using Cloning Records (v5.2.0); whether a higher-level
"copy entire CO configuration" workflow has been implemented is to be confirmed
with the development team.

.. TODO: Confirm with dev team whether CO Configuration Copy (full CO-to-CO
   config promotion) is implemented in v5, in progress, or still planned. If
   implemented, document here and/or on the Collaborative Organizations page.
   Note: this is distinct from Cloning Records (v5.2.0), which copies
   individual objects across COs.

----

Pages in This Section
----------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   operations/jobs
   operations/notifications
   operations/history
   operations/searching
   operations/record-management
   operations/security
