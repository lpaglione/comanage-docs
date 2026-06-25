.. _using-lifecycle:

Lifecycle Management
====================

Enrolling a new person is just the beginning. Over time, their relationship
with your organization will evolve — roles will change, affiliations will shift,
new responsibilities will be added, and eventually, at some point, their
connection to some or all of your systems will end. Registry supports your
organization through every stage of this journey.

Lifecycle management in Registry covers three broad phases:

**Bringing people in** — Enrollment Flows are Registry's mechanism for creating
new Person records through interactive, human-driven processes: applications,
invitations, approvals, self-signup, and multi-step onboarding workflows. Flows
are fully configurable and plugin-based, so they can reflect exactly how your
organization actually works. Terms and Conditions lets you present and track
policy agreement as part of that process.

**Managing relationships over time** — Once a person is in Registry, their status
reflects the current state of their relationship with your organization. Status
is calculated from Person Role statuses, which in turn can be set manually,
derived from valid from/valid through dates, updated by Pipelines, or changed
automatically by Expiration Policies. The status model drives what data gets
provisioned downstream, so it is the central mechanism for expressing who has
access to what.

**Offboarding and expiration** — When a person's role ends, Registry can manage
the transition automatically. Expiration Policies define rules for what happens as
validity periods approach and pass — moving people through Grace Period, Expired,
Suspended, or Archived states and triggering reprovisioning to downstream systems
at each stage.

Together, these mechanisms mean Registry doesn't just store identity data at a
point in time — it actively manages the lifecycle of that data as relationships
change.

----

.. contents:: On this page
   :local:
   :depth: 1

----

Enrollment Flows
-----------------

**Enrollment Flows** are Registry's mechanism for bringing new people into a CO
through interactive, human-driven processes. Every organization has its own
terminology for this — applications, invitations, intakes, signups — and its own
steps: collecting attributes, verifying email, obtaining approvals, requiring
policy agreement. Enrollment Flows let you model exactly that process.

A Flow consists of a series of **Steps**, each implemented by a plugin. The order
of Steps, the Actor types who complete them (Petitioner, Enrollee, Approver),
and the notifications sent at handoffs are all configurable. A single Registry
deployment can have as many Enrollment Flows as needed to represent the different
ways people join your COs and COUs.

Person records are not created until the Petition is successfully finalized —
only at the end of a completed Flow do operational records appear. This prevents
partial records from accumulating when Petitions are rejected or abandoned.

.. note::

   Enrollment Flows were completely redesigned in v5.1.0 and are **not available
   in Registry v5.0.x**.

See :ref:`lifecycle-enrollment-flows` for configuration details.

Terms and Conditions *(v5.2.0)*
---------------------------------

**Terms and Conditions** let you present policy documents to people and track
their agreement. Each T&C can be configured with an agreement duration (requiring
periodic re-agreement), scoped to a specific COU, and tied to content hosted
either in a Mostly Static Page within Registry or at an external URL.

Agreement at enrollment is collected through the Agreement Collector Enroller
Plugin as a Step within an Enrollment Flow. Administrators can also record
agreement on behalf of a person, or revoke an existing agreement.

See :ref:`lifecycle-terms-and-conditions` for configuration details.

Status and Validity
--------------------

**Status** is how Registry represents where a person stands in their lifecycle.
Each Person Role carries a status, and the overall Person status is calculated
as the "most preferred" of those Role statuses. Statuses range from Active and
Grace Period (full provisioning) through Suspended and Expired (reduced
provisioning) to Archived (no provisioning).

Person Role validity dates — valid from and valid through — drive automatic
status transitions without requiring manual updates. A Role with a future valid
from date enters Pending Activation; a Role that passes its valid through date
becomes Expired. When needed, an entire Person record can be Locked to
immediately disable access regardless of Role statuses.

See :ref:`lifecycle-status-and-validity` for details on the status model,
validity dates, and locking.

Expiration Policies
--------------------

**Expiration Policies** are rules that automatically manage person status over
time — for example, moving a person from Active to Grace Period when a Role
validity date approaches, or transitioning to Expired after the grace period ends.
They run as a scheduled background job rather than in response to individual
events, making them suitable for managing large populations.

.. note::

   Expiration Policies are referenced in the Registry PE Technical Reference as
   a mechanism for status change, but a dedicated v5 configuration page is not
   yet available in the Technical Manual. For current configuration guidance,
   see the
   `Expiration Policies <https://spaces.at.internet2.edu/spaces/COmanage/pages/49840329/Expiration+Policies>`_
   page in the v4 Technical Manual, and check the Registry community for v5
   updates.

See :ref:`lifecycle-expiration-policies` for what is available about v5.

----

If You Are Migrating from v4
------------------------------

Several significant changes affect lifecycle management when migrating from v4:

- **Enrollment Flows are completely redesigned** in v5.1.0. The v4 flow model
  (Enrollment Sources, Enrollment Wedges, and the Default Enrollment fallback)
  has been replaced by a fully plugin-based Step system. All Enrollment Flows
  must be rebuilt for v5.

- **Enrollment Flows are not available in v5.0.x.** Deployments on v5.0.x cannot
  use Enrollment Flows.

- **Operational records are now created only at finalization.** In v4, records
  could be created or updated during the Enrollment Flow even if the Petition was
  later rejected. In v5.1.0+, records are only committed when a Petition
  successfully finalizes.

- **Terms and Conditions are available as of v5.2.0.** The feature existed in v4 but was not yet included in v5.0.x or v5.1.x.

- **Status terminology has changed.** The v4 status "Deleted" is now "Archived"
  in v5. A new "Pending Activation" status exists in v5 for Roles whose valid
  from date has not yet been reached. Several enrollment-state statuses no longer
  appear on Person records in v5.2.0 because Person records are not created until
  Petition finalization.

----

In This Section
----------------

.. toctree::
   :maxdepth: 1

   lifecycle/enrollment-flows
   lifecycle/terms-and-conditions
   lifecycle/status-and-validity
   lifecycle/expiration-policies
