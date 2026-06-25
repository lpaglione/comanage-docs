.. _lifecycle-status-and-validity:

Status and Validity
====================

Status is how Registry expresses where a person stands in their lifecycle
relationship with the CO. It drives what data gets provisioned to downstream
systems, what access is granted, and what operations are available for that
person. Understanding the status model is fundamental to understanding how
Registry manages the lifecycle — particularly as people transition from active
to expiring to archived states.

For the full technical reference, see
`Person and External Identity Status <https://spaces.at.internet2.edu/spaces/COmanage/pages/281018939/Person+and+External+Identity+Status>`_
in the Technical Manual.

----

.. contents:: On this page
   :local:
   :depth: 1

----

Person and Person Role Status
-------------------------------

Registry maintains status at two levels:

**Person Role status** — each Person Role has its own status, assigned directly.
A person may have multiple Roles (for example, a role in the CO and a role in
a specific COU), each with its own status.

**Person status** — each Person has an overall status, calculated automatically
as the "most preferred" of all their Person Role statuses. A person with one
Active role and one Expired role has an overall Person status of Active, because
Active is more preferred than Expired.

Status can change through several mechanisms:

- As part of an Enrollment Flow (the Petition process assigns an initial status)
- Via a Pipeline sync from an External Identity Source
- Automatically, when valid from or valid through dates on a Person Role take effect
- Due to an Expiration Policy
- Manually by an administrator — though manual changes may be overwritten when
  an automatic update would produce a different status, unless the Person is
  Locked or the Role is Frozen

Status Values
--------------

**Active** — the person or role is currently active within the organization.
Full person, role, and group membership data is provisioned to downstream
systems.

**Grace Period** — the person's primary association has ended, but services have
not yet been deprovisioned. Full data continues to be provisioned, exactly the
same as Active. Grace Period is typically the first automated step in an
offboarding workflow: the person retains access while the transition is managed.

**Suspended** — the association has been temporarily suspended. Only person-level
data and All Members group memberships are provisioned (role data and other group
memberships are not).

**Expired** — a valid through date for the Role has been reached. Same
provisioning scope as Suspended: person-level data and All Members groups only.

**Pending Activation** — the valid from date for a Role has not yet been reached.
No data is provisioned. A Role in this status will automatically transition to
Active when the valid from date passes.

**Archived** — the record is not expected to be reactivated. No data is
provisioned. (This status was called "Deleted" in Registry v4.)

**Locked** — a special Person-level status (not available on Roles) that
immediately overrides all Role statuses. The entire Person record is disabled.
Only person-level data and All Members group memberships are provisioned. Locked
status can only be reset by a CO or COU administrator — Enrollment Flows,
Pipelines, and Expiration Policies cannot reset it.

Several additional statuses exist to represent states within Enrollment Flows
(PendingApproval, Approved, PendingConfirmation, Confirmed, Denied, Declined,
Pending, Duplicate). In Registry v5.2.0 and later, these do not appear on Person
records because Person records are not created until Petition finalization.

Validity Dates and Automatic Status Transitions
-------------------------------------------------

Each Person Role can have a **Valid From** and **Valid Through** date. These
dates drive automatic status transitions, reducing the need for manual updates
across large populations:

- A Role with a future valid from date and a current status of Active, Expired,
  or Grace Period is automatically set to **Pending Activation** (unless the
  Role is Frozen).
- A Role in Pending Activation with a valid from date now in the past is
  automatically set to **Active**.
- A Role with a past valid through date and a current status of Active, Grace
  Period, or Pending Activation is automatically set to **Expired** (unless the
  Role is Frozen).
- A Role in Expired status with a valid from date now in the future is
  automatically set to **Active**.

If both dates are provided, the valid from date must be earlier than the valid
through date.

Validity dates can be collected during an Enrollment Flow, synced from an
External Identity Source through a Pipeline, or set manually by an administrator
on the Person Role record.

Locking a Person
-----------------

Locking provides an immediate way to disable a person's entire record when
needed — for example, when an account is under review or when temporary access
needs to be revoked while the situation is assessed. To lock a Person, set their
status to Locked from the Person canvas.

A Locked Person continues to provision the same data as Suspended: person-level
data and All Members group memberships. All other provisioned data — role
attributes, other group memberships — is withheld while the Person is Locked.

A critical distinction: **Locking a Person does not lock their Authenticators.**
Applications should check authorization information (which is deprovisioned when
the record is Locked) rather than relying on Authenticator state to determine
whether a Person should have access.

Only a CO or COU administrator can unlock a Person. Enrollment Flows, Pipelines,
and Expiration Policies cannot override the Locked status.

External Identity Status
-------------------------

External Identity Sources can assign statuses to External Identity Roles, which
then flow into Person Roles via the Pipeline. The statuses available for External
Identity Roles are a subset of those available for People: Active, Grace Period,
Suspended, Archived, and Deleted (Deleted here meaning the backend removed the
record, and is a state that backends cannot directly assert).

External Identity Roles use validity dates to convey Pending Activation or
Expired status — those statuses cannot be directly asserted by an EIS backend.
The status field should reflect the practical current state (Active, Suspended,
etc.), while validity dates indicate future or past effectiveness.

The overall External Identity status is the most preferred status among its
Roles. Person Roles created from External Identity Roles via the Pipeline inherit
the status of the corresponding External Identity Role, with one exception: if
the backend deletes an External Identity Role entirely, the resulting Person Role
status is determined by the Pipeline's Role Status on Delete configuration. See
:ref:`ec-pipelines` for details.

How Status Affects Provisioning
---------------------------------

Status determines what data is sent to downstream systems on the next
provisioning cycle:

- **Active and Grace Period** — full provisioning: person data, role data, and
  all group memberships
- **Suspended, Expired, and Locked** — partial provisioning: person data and
  All Members group memberships only
- **Pending Activation, Archived, Duplicate, and enrollment-state statuses**
  — no data provisioned

The Grace Period behavior is intentional: a person in Grace Period continues to
receive exactly the same provisioning as an Active person. Their access is fully
maintained while the offboarding process is being managed. Only when status
transitions to Expired or Suspended does provisioning reduce — triggering access
removal in downstream systems.

Changes from v4
----------------

- **"Deleted" was renamed "Archived"** in Registry v5.0.0. Person and Role
  records that were in Deleted status in v4 will appear as Archived in v5. If
  your Expiration Policies or downstream integrations referenced the Deleted
  status, update them to use Archived.

- **"Pending Activation" is a new status in v5.** In v4, a Role with a future
  valid from date would appear as Active but provisioners would check dates
  before processing. In v5, the pre-active state is now explicit and carries its
  own provisioning behavior (no data provisioned).

- **Several enrollment-state statuses no longer appear on Person records** in
  v5.2.0 (Approved, PendingApproval, Confirmed, PendingConfirmation, and others).
  Because Person records are not created until Petition finalization, these
  in-progress states only appear on Petitions, not on operational Person records.

- **Person Roles cannot be set to Locked.** Locked is a Person-level status
  only. Individual Roles can be set to Suspended, Expired, or Archived, but not
  Locked.

- **"Invited" status** — available in v4 for the Default Enrollment process —
  is no longer used in v5, as Default Enrollment has been removed.
