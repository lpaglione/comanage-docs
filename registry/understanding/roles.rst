.. DRAFT — April 2026
.. Terminology status:
..   "Person record"     ✓ confirmed v5 term
..   "External identity" ✓ confirmed v5 term
..   "Enrollment flow"   ✓ confirmed v5 term
..   CO / organization container ⚠ OPEN QUESTION — using "your organization in Registry"
..   COU / sub-unit      ⚠ using "sub-unit" as working term; COU abbreviation flagged for v5 verification
..   CMP Administrator   ⚠ check whether this label is unchanged in v5
..   CO Administrator    ⚠ check whether this label is unchanged in v5

.. _roles:

Roles and Permissions
=====================

Registry uses a layered permission model. Different people in your organization
will interact with Registry in different ways — some configure and maintain it,
some manage a specific population, some just appear in it as people with a
record. Understanding who has what access is important both for planning your
deployment and for day-to-day operation.

This page describes the main administrator roles, what each can do, and how they
fit together.

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
operate some part of Registry. Admins sign in to Registry and work with its
configuration and data.

**Membership** simply means that someone has a Person record in Registry. Most
people in your Registry are members — they have a record, they may have group
memberships and provisioned access to other systems, but they do not log in to
Registry itself to manage anything.

A person can be both: an administrator who also has their own Person record in
the system, like a department administrator who is also a member of the
department they manage.

2. The Administrator Role Hierarchy
-------------------------------------

Registry defines administrative roles at three levels: the installation, the
organization, and sub-units and groups within the organization.

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - **Installation Admin**
     - Manages the Registry application and platform itself.
   * - **Platform Admin** (CMP Admin)
     - Configures the platform, creates organizations, and has broad access
       across the entire Registry installation.
   * - **Organization Admin**
     - Manages everything within a specific organization: its people,
       configuration, groups, and connections to external systems.
   * - **Sub-unit Admin**
     - Manages people and policies within a specific sub-unit, with delegated
       authority from the organization.
   * - **Group Owner**
     - Manages membership in a specific group.

Each level can do everything its level permits, plus it inherits nothing
automatically from the level above — an Organization Admin, for example, cannot
reconfigure the platform, and a Sub-unit Admin cannot modify organization-level
settings.

3. Installation and Platform Administrators
--------------------------------------------

**Installation Administrators** (sometimes called System Administrators) operate
the infrastructure that Registry runs on. Their work is largely outside Registry
itself: provisioning servers or containers, managing upgrades, handling backups,
and maintaining the operating environment. This role is typically held by
technical staff at your institution or hosting provider.

**Platform Administrators** (also called CMP Administrators — COmanage Platform
Administrators) are super users within Registry. They can:

- Create and configure organizations within Registry
- Access and manage data in any organization in the installation
- Configure platform-level settings
- Do everything an Organization Admin can do within any organization, with
  one exception: Platform Admins cannot initiate an enrollment flow petition
  on behalf of another person unless they are explicitly granted that
  permission in the workflow.

Because Platform Admins have broad access across the entire installation, this
role should typically be held by a small number of trusted staff — often the
same people who manage the technical infrastructure, or a designated Registry
service owner.

4. Organization Administrators
--------------------------------

**Organization Administrators** are super users within a specific organization.
They can:

- Configure the organization's settings and features
- Add and manage Person records, including initiating enrollment flows
- Create and configure sub-units, groups, and organizational structure
- Manage connections to external identity sources and provisioning targets
- Assign and revoke administrative roles for other people within the
  organization

This is the role most people think of as "the Registry admin." In a typical
deployment, one or a small number of Organization Admins handle the configuration
work and have authority over the full population.

.. note::

   An Organization Admin who is also a Platform Admin has platform-wide access.
   An Organization Admin who is *not* a Platform Admin can only manage their
   specific organization.

5. Sub-unit Administrators
---------------------------

**Sub-unit Administrators** have delegated management authority over a specific
sub-unit within the organization. They can manage the people who have roles in
their sub-unit: reviewing enrollment petitions, updating Person records,
adjusting membership status, and handling day-to-day population management
within their area.

Sub-unit Admins cannot change the organization's overall configuration — they
work within the structure that an Organization Admin has set up for them. This
is by design: the delegation model lets the people who know a population best
(a department coordinator, a project lead, a collaboration manager) manage that
population directly, without requiring Organization Admin access.

Sub-unit Admins of a parent sub-unit also have admin access to any child
sub-units. This means you can model your organizational hierarchy in Registry's
sub-unit structure and let administrative authority flow accordingly.

6. Group Owners
----------------

**Group Owners** can manage membership in a specific group: adding and removing
members, and in some cases allowing self-enrollment (for open groups). A group
owner does not need to hold any other administrative role — any person with a
Person record in the organization can be a group owner.

In v5, group ownership is assigned to a **group of people** rather than to
named individuals. This is consistent with how administrative roles work for
organizations and sub-units, where the "admins" group determines who has
management authority. Practical benefits include: group ownership survives
personnel changes without requiring updates to individual assignments, and
management responsibility can be distributed among a team rather than held by
a single person.

When Registry creates a group automatically — for example, when you create a
new sub-unit, Registry creates corresponding "admins," "all members," and "active
members" groups — ownership follows the administrative roles for that object.

7. Automatic Groups and Administrative Roles
---------------------------------------------

Registry uses groups to implement administrative roles internally. When you
assign someone as an Organization Admin or Sub-unit Admin, Registry adds them to
the corresponding administrative group for that object. This group-based
implementation means that:

- Every organization and sub-unit automatically has "admins," "all members,"
  and "active members" groups.
- Administrative access can be managed the same way as any other group
  membership.
- Provisioning rules can use these groups to control access to other systems —
  for example, to grant Registry admins access to an admin dashboard
  provisioned elsewhere.

8. How Administrative Roles Are Assigned
-----------------------------------------

Administrative roles are assigned by an existing administrator with authority at
or above the level being assigned:

- Platform Admins are assigned by other Platform Admins (or Installation Admins
  during initial setup).
- Organization Admins are assigned by Platform Admins.
- Sub-unit Admins are assigned by Organization Admins (or Sub-unit Admins of a
  parent sub-unit).
- Group Owners are assigned by the group's existing owners or by Organization
  Admins.

You do not need to create an enrollment flow to assign administrative roles —
they can be assigned directly through the Registry interface. However, if your
organization uses enrollment flows for onboarding, the flow can be configured to
assign roles automatically as part of the enrollment process.

----

Where to go for more information
----------------------------------

- :doc:`Registry Concepts Overview </understanding/concepts-overview>` — the
  mental model for people, groups, and organizational structure in Registry
- :doc:`Planning Your Implementation </understanding/planning>` — working through
  your organization's structure and admin model before you start configuring
- :doc:`Managing People in Registry </using/people/managing-people>` — how
  Person records are created and managed in practice
- `COmanage Registry Technical Manual <https://spaces.at.internet2.edu/display/COmanage/Technical+Manual>`_
  — detailed reference documentation for role configuration
