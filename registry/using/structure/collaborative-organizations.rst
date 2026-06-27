.. _struct-co:

Collaborative Organizations (COs)
==================================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

A **Collaborative Organization (CO)** is the top-level tenant in Registry. Every
person, group, enrollment flow, provisioning target, and configuration object
belongs to a CO. A CO can represent a real institution — a university, a
laboratory, a company — or a virtual organization like a research collaboration or
a project team. The name reflects this flexibility: what makes something a
"Collaborative Organization" in Registry is that it has a defined population and
needs to manage that population's identities and access.

Most deployments operate with a single CO for their primary population. A second
CO (or more) makes sense when populations are truly independent — when the people,
the policies, and the resources they access are distinct enough that there is no
meaningful cross-membership. If people might belong to both groups, COUs and
Groups within a single CO are generally the better approach.

.. TODO: Add a case study or decision guide — "Multiple COs vs a single CO with
   COUs: which should I use?" — to help administrators make this foundational
   design decision. Key factors: whether people might cross-participate (argues
   for one CO), whether administrative separation is needed (argues for COUs or
   separate COs), whether resource sharing (e.g. enrollment flows, pipelines) is
   desirable (argues for one CO). Real-world scenarios (e.g., multi-campus
   federation vs. departmental sub-populations) would make this concrete.
   Candidate for the Recipes or Case Studies section.

For the full technical reference, see
`Registry Collaborative Organizations (COs) <https://spaces.at.internet2.edu/spaces/COmanage/pages/392724540/Registry+Collaborative+Organizations+COs>`_
in the Technical Manual.

1. The COmanage CO
-------------------

:bdg-warning:`Redesigned in v5` :bdg-secondary:`Available: v5.0.0` Every Registry deployment includes a built-in CO called the **COmanage CO**,
created automatically when the platform is first installed. The COmanage CO
operates the same way as any other CO, but it has a special role: it is the home
for platform-level administration.

From the COmanage CO, Platform Administrators can:

- Create and manage other COs on the platform
- Configure the default outgoing SMTP server (used as a fallback for all COs)
- Manage platform-wide plugins
- Create API users with cross-CO access to the REST API
- Configure multi-factor authentication requirements for Registry itself

Members of the COmanage CO's ``CO:admins`` group are considered **Platform
Administrators** — they are superusers of the entire platform and can perform
almost any action across all COs. (There are limited exceptions where CO
membership is required for audit integrity, such as starting a CO-member-only
enrollment flow.)

In v5.0.0, the COmanage CO replaced the Platform configuration menu that existed
in v4, making platform administration consistent with regular CO administration.

2. Creating and Naming COs
---------------------------

COs are created via the COmanage CO administrative interface:
**COmanage CO > ALL > COs > Add a New CO**.

When a CO is created, Registry automatically creates the CO's initial set of
special Groups — including the ``CO:admins`` group — and assigns the creating
Platform Administrator as the first CO Administrator.

**Naming.** CO names must be unique across the platform (enforced
case-insensitively as of v5.2.0). Short, clear names are recommended. Registry
uses the CO's internal ID in most operations, so renaming a CO is generally safe
from Registry's perspective — though downstream systems that reference the CO by
name may need to be updated.

3. Duplicating a CO
--------------------

CO duplication is planned but not yet available (CFM-127). When implemented, it
will copy configuration objects (COUs, Groups, Enrollment Flows) but not data
objects (People, Group Memberships). A typical use case is creating a baseline
template CO and duplicating it to spin up new COs with a standard starting
configuration.

4. Suspending and Deleting a CO
---------------------------------

**Suspending** a CO immediately terminates all access to it: the web interface
becomes unavailable, API requests are rejected, and scheduled jobs will not run
within the CO. Suspending does not affect downstream systems — LDAP directories,
provisioning targets, and other services connected to the CO continue operating
as-is. Those must be managed separately if you want to cut off downstream access
as well.

**Deleting** a CO requires that it first be set to Suspended status — a safeguard
against accidentally deleting an active production CO. CO deletion is a hard
delete: all records are physically removed from the database. This is different
from most Registry delete operations, which soft-delete data (keeping it in the
database but hiding it from the interface). There is no undo for CO deletion;
recovery requires restoring from backup.

:bdg-secondary:`Available: v5.2.0` For large COs with substantial data, immediate deletion may time out. In that
case, use the **Deletion Job** to queue the deletion as a background operation.

5. CO Administrators
---------------------

A **CO Administrator** is a person who can perform lifecycle management operations
on Person Roles within a CO. CO Administrators must be Active members of the CO
and members of the ``CO:admins`` group.

CO Administrators are distinct from **COU Administrators**, who have
administrative authority over a specific COU (and any of its child COUs). COU
Administrators must also be Active CO members and members of the relevant
``CO:COU:<COU Name>:admins`` group.

6. Changes from v4
-------------------

- **The COmanage CO replaced the Platform configuration menu as of v5.0.0.**
  In v4, platform-level configuration lived in a separate "Platform" area of the
  Registry interface. In v5, that functionality moved into the COmanage CO, making
  platform administration consistent with regular CO administration.

- **CO name uniqueness is now enforced case-insensitively as of v5.2.0.**

- **CO deletion can be processed asynchronously as of v5.2.0**, using the
  Deletion Job Plugin to queue and run large CO deletions in the background.
