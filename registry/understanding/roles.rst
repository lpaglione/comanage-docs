.. DRAFT — April 2026
.. Terminology status (confirmed from PE Technical Manual, Mar 2026):
..   "Person record"     ✓ v5 term
..   "External identity" ✓ v5 term
..   "Enrollment flow"   ✓ unchanged
..   CO                  ✓ still used in v5
..   COU                 ✓ still used in v5
..   CMP                 ✓ Collaboration Management Platform = the Registry installation
.. Sources: Registry PE Permissions (Sep 2025, draft), Registry User Roles (Feb 2026)
.. Note: Registry PE Permissions page is marked as draft — treat as directional.
..       Helpdesk Supervisor / Helpdesk / Manager / Sponsor roles need verification
..       when Permissions page is finalized.

.. _roles:

Roles and Permissions
=====================

Registry uses a layered permission model built primarily on group membership.
Different people in your organization will interact with Registry in different
ways — some configure and maintain it, some manage a specific population, some
participate in enrollment flows, and some simply appear in it as people with a
record. Understanding who has what access matters both for planning your
deployment and for day-to-day operation.

----

.. contents:: On this page
   :local:
   :depth: 1

----

1. Two Kinds of Access
-----------------------

It helps to start with a distinction: Registry separates **administrative roles**
from **membership**.

**Administrative roles** give someone the ability to configure, manage, or
operate some part of Registry. Administrators sign in to Registry and work with
its configuration and data.

**Membership** simply means that someone has a Person record in Registry. Most
people in your Registry are members — they have a record, group memberships,
and provisioned access to other systems, but they do not log in to Registry
itself to manage anything. By default, members do not have access to view or
edit their own records through the core application; end-user self-service is
provided through Dashboard Widgets, which administrators configure separately.

A person can be both: a COU Administrator who also has their own Person record
in the COU they manage, for example.

2. Administrative Roles
------------------------

Registry defines the following roles. Permissions are assigned primarily through
membership in specific Registry Groups.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Role
     - What it grants
   * - Platform (CMP) Administrator
     - Access to all parts of all COs, with certain exceptions related to
       Enrollment Flows.
   * - Collaboration (CO) Administrator
     - Full access to all parts of their CO.
   * - Collaboration Unit (COU) Administrator
     - Ability to view Person records within their CO and manage Person Role
       records within their COU.
   * - Support Desk
     - Full view access into all People records; no write access.
   * - Helpdesk Supervisor
     - View all of the Person record and manage parts.
   * - Helpdesk
     - View most parts of the Person record.
   * - Manager
     - View Person records and Person Roles for which they are a Manager.
   * - Sponsor
     - View Person records and Person Roles for which they are a Sponsor, and
       renew or expire those Person Roles.
   * - Approver
     - View Petitions up to the appropriate approval step for which they are an
       Approver.
   * - Petitioner
     - View the status of Petitions for which they are the Petitioner.

.. note::

   The Registry PE Permissions page in the Technical Manual is currently marked
   as a draft and some descriptions may not yet match the implementation. The
   role descriptions above should be treated as directional guidance; verify
   specifics in the Technical Manual before configuring production systems.

3. Platform (CMP) Administrators
----------------------------------

The **Collaboration Management Platform (CMP)** is the Registry installation
itself. **Platform Administrators** are super users across the entire
installation. They are determined by membership in the ``CO:admins`` Group
within the COmanage CO (the platform's own internal CO).

Platform Administrators can:

- Create and configure any CO within the installation
- Access and manage data in any CO
- Do everything a CO Administrator can do within any CO

One important limitation: if a Platform Administrator does not also have a
Person record within a specific CO, there are a small number of actions they
cannot perform in that CO. This is because certain operations — such as revoking
Terms and Conditions — require a CO-specific Person ID to maintain a complete
audit trail. For this reason, Platform Administrators who actively manage a CO
are typically also registered as a Person within it.

4. CO Administrators
---------------------

**CO Administrators** have full access to their CO. They are determined by
membership in the ``CO:admins`` Group within their CO.

CO Administrators can configure the CO's settings, manage Person records,
design enrollment flows, create and configure COUs and Groups, manage
connections to external identity sources and provisioning targets, and assign
administrative roles to others within the CO.

This is the role most people think of as "the Registry admin." In a typical
deployment, a small number of CO Administrators handle configuration and have
authority over the full population.

5. COU Administrators
----------------------

**COU Administrators** can view Person records within their CO and manage
Person Role records within their COU. They are determined by membership in
the ``CO:COU:COU_Name:admin`` Group within the CO.

This delegation model lets the people who know a population best — a department
coordinator, a project lead, a collaboration manager — manage that population
directly, within the structure that a CO Administrator has established.
COU Administrators of a parent COU also have admin access to any child COUs.

6. Support Desk and Helpdesk Roles
------------------------------------

Registry v5 introduces dedicated roles for staff who need to look up person
information without having full administrative authority.

**Support Desk** personnel have full view access into all People records across
the CO, but no write access. This role is well suited for IT help desk staff
who need to look up a person's record to answer questions or troubleshoot
access issues without being able to modify anything.

**Helpdesk Supervisor** can view all parts of a Person record and manage
certain parts. **Helpdesk** can view most parts of a Person record. These
roles provide graduated access for support staff with different levels of
responsibility.

7. Enrollment-Related Roles
-----------------------------

Several roles are scoped to specific enrollment flows and people rather than
to the CO or COU as a whole.

**Managers** can view Person records and Person Roles for the people they
manage. This is useful for giving supervisors or project leads limited
visibility into the records of those they are responsible for, without
granting broader administrative access.

**Sponsors** can view Person records and Person Roles for the people they have
sponsored, and can renew or expire those Person Roles. Sponsorship is commonly
used in guest or affiliate populations, where a staff member takes responsibility
for a visitor or external collaborator.

**Approvers** can view Petitions up to the approval step for which they are an
Approver. This is sufficient to review and act on the petition without exposing
the full administrative interface.

**Petitioners** can view the status of Petitions they have initiated. This
allows someone who has started an enrollment on someone else's behalf to follow
its progress.

8. Group Access and Dashboard Widgets
---------------------------------------

Group managers — people who own or manage a Registry Group — do not have default
access to Person records or other Registry data by virtue of their group role
alone. By default, no access is granted to users outside the administrative
roles described above.

Additional permissions, including end-user self-service capabilities, are
provided through **Dashboard Widgets**, which CO Administrators configure to
expose specific actions to specific audiences. This means that what a regular
member of your CO can see or do in Registry is determined entirely by the
Dashboard Widgets you set up for them — not by any automatic permission tied
to group membership.

9. How Roles Are Assigned
--------------------------

Administrative roles are primarily determined by group membership:

- **Platform Administrators** are members of the ``CO:admins`` Group in the
  COmanage CO.
- **CO Administrators** are members of the ``CO:admins`` Group within their CO.
- **COU Administrators** are members of the ``CO:COU:COU_Name:admin`` Group
  within their CO.

Enrollment-related roles (Manager, Sponsor, Approver, Petitioner) are assigned
in the context of specific enrollment flows and Person Role relationships, not
through group membership.

Administrative group membership can be managed directly in the Registry
interface by an existing admin with sufficient authority. It can also be
assigned automatically as part of an enrollment flow — for example, a flow
that gives a department coordinator COU Administrator access as part of their
onboarding.

----

Where to go for more information
----------------------------------

- :doc:`Registry Concepts Overview </understanding/concepts-overview>` — the
  mental model for people, groups, and organizational structure in Registry
- :doc:`Planning Your Implementation </understanding/planning>` — working through
  your organization's needs and admin model before you start configuring
- `Registry PE Permissions <https://spaces.at.internet2.edu/display/COmanage/Registry+PE+Permissions>`_
  — the Technical Manual reference for permissions (currently a draft)
- `Registry User Roles <https://spaces.at.internet2.edu/display/COmanage/Registry+User+Roles>`_
  — concise summary of roles and their scope in the Technical Manual
- `Registry Groups <https://spaces.at.internet2.edu/display/COmanage/Registry+Groups>`_
  — how the groups that underpin role assignment work
