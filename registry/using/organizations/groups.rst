.. _org-groups:

Groups
======

Registry Groups are a way to organize People within your CO — for controlling
who has access to what, for driving enrollment approvals, for scoping
provisioning, and for enabling self-organized membership. Groups are defined
at the CO level and memberships attach at the Person level.

Because Groups integrate with so many other Registry features, understanding
how they work is important for COmanage administrators: Groups control who
can approve enrollment petitions, who gets provisioned to which downstream
systems, and how organizational structure can be reflected in Registry.

For the full technical reference, see
`Registry Groups <https://spaces.at.internet2.edu/spaces/COmanage/pages/232358046/Registry+Groups>`_
in the Technical Manual. For v4-era background, see also
`CO Groups and Group Memberships <https://spaces.at.internet2.edu/spaces/COmanage/pages/102304360/CO+Groups+and+Group+Memberships>`_
in the v4 Technical Manual.

----

.. contents:: On this page
   :local:
   :depth: 1

----

Standard Groups vs System Groups
----------------------------------

There are two broad categories of Groups in Registry:

**Standard Groups**
   Groups created by administrators (or, if permitted, by CO members) for
   general organizational purposes. Standard Groups can be configured as open
   or closed, can have identifiers assigned, can be provisioned to downstream
   systems, and can be placed in a hierarchy.

   Standard Group names may not begin with the prefix ``CO:`` (reserved for
   System Groups) and may not contain colons.

**System Groups**
   Registry-managed groups with special characteristics. System Groups
   include Automatic Groups, Admin Groups, Approvers Groups, Members Groups,
   MFA Exemption Groups, and Owners Groups (each described below).

Open vs Closed Groups
----------------------

**Open Groups** allow any CO member to self-join. No administrator action is
required for a person to become a member.

**Closed Groups** restrict membership management to the group's owners and CO
administrators. Members must be added explicitly.

Automatic Groups
-----------------

Automatic Groups are managed entirely by Registry — memberships are updated
automatically as people's statuses change. Administrators cannot manually
add or remove members from Automatic Groups.

Registry creates and maintains the following Automatic Groups for each CO:

- ``CO:members:active`` — all People in Active or Grace Period status
- ``CO:members:all`` — all People (except those in Archived status)

For each COU, Registry also creates:

- ``CO:COU:<COU Name>:members:active`` — all People with an Active or Grace
  Period role in that COU
- ``CO:COU:<COU Name>:members:all`` — all People with any non-Archived role
  in that COU

These Automatic Groups are particularly useful as Provisioning Groups — for
example, you can configure a Provisioning Target to send only
``CO:members:active`` to a downstream system, ensuring that inactive members
are automatically deprovisioned.

.. note::

   Identifiers cannot be assigned to Automatic CO Groups.

Special Groups
---------------

In addition to Automatic Groups, Registry creates and maintains several other
System Groups with specific purposes.

**Admin Groups**
   Admin Groups determine who has Registry administrator privileges. One Admin
   Group is automatically created when the CO is created (``CO:admins``), and
   one is created for each COU (``CO:COU:<COU Name>:admins``). The Platform
   Administrator sets the initial CO Administrator by adding them to
   ``CO:admins``.

**Approvers Groups** *(available as of Registry v5.2.0)*
   Approvers Groups are used during Enrollment Flows to determine who may
   approve a petition. The CO-level Approvers Group (``CO:approvers``) is
   created automatically with the CO, and COU-level approvers groups are
   created for each COU. Other Groups can also be designated as approvers
   for specific Enrollment Flow Steps — see :ref:`lifecycle-enrollment-flows`.

**Members Groups**
   Members Groups are the Automatic Groups described above: ``CO:members:active``,
   ``CO:members:all``, and their COU-specific equivalents. They cannot be
   manually manipulated.

**MFA Exemption Groups** *(available as of Registry v5.2.0)*
   MFA Exemption Groups (``CO:mfaexempt``) control access to the Registry
   application itself, specifically to exempt certain People from multi-factor
   authentication requirements when accessing Registry. These Groups exist only
   at the CO level. While COU-specific MFA Exemption Groups are not
   automatically created, you can create them as Standard Groups and nest them
   into the CO-level Group.

**Owners Groups**
   Every Standard Group has a corresponding Owners Group, created automatically
   when the Standard Group is created. Group Owners (the people who can manage
   group membership) are managed by adding them to the Owners Group.

   Owners Groups have several restrictions: their name, description, and status
   are kept in sync with the primary Group automatically; additional attributes
   (like identifiers) cannot be attached to them; they cannot be provisioned;
   and when the primary Group is deleted, the Owners Group is also deleted.

   Owners Groups are effectively "black box" infrastructure — they should not
   be provisioned to or integrated with external systems directly. If you need
   a Group that serves double duty as both a Standard Group (provisionable) and
   as Owners, use a Group Nesting to populate the Owners Group from a Standard
   Group.

Group Memberships
------------------

Group Memberships attach at the Person level and can be managed in several
ways:

- **Manually by a Group owner or administrator** — directly from the Group's
  membership list or from the Person Canvas
- **Via an Enrollment Flow** — Enrollment Flows can add a Group membership
  as part of the enrollment result
- **Via a Pipeline** — Pipelines connected to Organizational Identity Sources
  can add Group memberships
- **Via Group Nestings** — automatic population of one Group from another

**Validity Dates on Memberships**
   Group Memberships can have **Valid From** and **Valid Through** dates,
   restricting the membership to a specific time window. Validity date
   changes are processed by the ``ValidateGroupMember`` job. When a membership
   validity date takes effect, nested Group memberships will not automatically
   propagate — the ``ValidateGroupMember`` job must run first.

Group Nestings
---------------

A **Group Nesting** causes the members of one Group (the *source* Group) to
be automatically included as members of another Group (the *target* Group).
Only CO administrators can create or remove Group Nestings.

Group Nestings are useful for building composite Groups from smaller ones —
for example, nesting several COU-level Groups into a single provisioning Group.

Nestings honor validity dates: if a membership in the source Group is not
yet valid or has expired, it will not propagate to the target Group.

Memberships created via nesting cannot be manually deleted. To remove a
nested member, the nesting itself must be removed.

**Boolean Logic for Nestings**
   Registry supports AND/OR/NOT logic on Group Nestings, enabling you to
   construct Group memberships based on set operations:

   - **OR (default)** — a Person is a member of the target Group if they are
     a member of *any* nested source Group (excluding any negated Groups).
     Configured by leaving "Require All For Nested Memberships" unchecked on
     the target Group.

   - **AND** — a Person must be a member of *all* nested source Groups in
     order to become a member of the target Group. Configured by checking
     "Require All For Nested Memberships" on the target Group.

   - **NOT** — a particular nesting can be negated (check "Negate Nesting" on
     the nesting record), meaning members of that source Group are *excluded*
     from the target Group. This can be used to construct "exclusion" groups.

   .. note::

      Changing the "Require All For Nested Memberships" or "Negate Nesting"
      settings does not automatically recalculate existing memberships.

**Processing Large Nestings**
   Adding or removing a Group Nesting can trigger significant processing,
   depending on the size of the Groups and any configured provisioners.
   For large Groups, it is recommended to queue the nesting operation as a
   background job rather than processing it immediately:

   - Via the UI, check **Queue Job to Add Group Nesting** when adding a new
     nesting
   - Via the UI, select **Queue for Deletion** when removing a nesting
   - Via the command line using the Nester Job Plugin or Deletion Job Plugin

**Reconciling Group Memberships**
   If an Automatic Group or a Group with Nestings appears to have incorrect
   memberships, you can manually reconcile it from the Group's detail page by
   clicking **Reconcile**. Note that reconciling a Group does not automatically
   reconcile related Groups — if Group A nests Group B which nests Group C,
   reconciling C does not cascade to B or A.

Group Hierarchy
----------------

*(Available as of Registry v5.2.0)*

Standard Groups can be organized into a parent/child hierarchy by assigning a
**Parent Group** to a Standard Group. Hierarchy can be used to reflect
organizational structure within your Groups namespace, but it operates
independently of Group Nestings — being a child of a Group does not
automatically make you a member of the parent Group.

**Fully Qualified Group Names**
   When a Group is placed in a hierarchy, its Fully Qualified Group Name is
   constructed by concatenating all ancestor Group names with colons, starting
   from the top. For example, if the Group ``Pizza Aficionados`` is assigned
   to the Parent Group ``Lunch Societies``, its Fully Qualified Group Name is
   ``Lunch Societies:Pizza Aficionados``.

   Fully Qualified Group Names are used when provisioning and when constructing
   Owners Group names.

**Hierarchy and Permissions**
   Group owners have permissions over all child Groups in the direct path
   below their Group, regardless of the number of intermediary Groups. Only
   Standard Groups can have Parent Groups, and only Standard Groups can be
   assigned as Parent Groups.

**Hierarchy and Group Nestings**
   Group Hierarchy and Group Nestings are independent mechanisms. Hierarchy
   defines organizational structure without affecting memberships; Nestings
   manage membership propagation without implying hierarchy.

Identifiers for Groups
-----------------------

Identifiers can be attached to Standard Groups, either manually or via
Identifier Assignment. This is useful when provisioning Groups to downstream
systems that require a stable external identifier. Identifiers cannot be
assigned to Automatic CO Groups.

Group Permissions Summary
--------------------------

The following table summarizes who can perform key Group-related actions:

.. list-table::
   :header-rows: 1
   :widths: 40 15 15 15 15

   * - Action
     - CO Admin
     - Group Owner
     - Group Member
     - CO Member
   * - Create a new top-level Group
     - Yes
     - —
     - —
     - If enabled
   * - Create a Group with a Parent
     - Yes
     - If owner of an Ancestor Group
     - —
     - —
   * - Edit Group Metadata
     - Yes
     - Yes
     - —
     - —
   * - Delete Group
     - Yes
     - Yes
     - —
     - —
   * - Manage Group Members
     - Yes
     - Yes
     - —
     - —
   * - View Group Members
     - Yes
     - Yes
     - Yes
     - If public
   * - Join open Group
     - Yes
     - Yes
     - —
     - Yes
   * - Leave open Group
     - Yes
     - Yes
     - Yes
     - —

.. note::

   COU Administrators do not receive any special Group management permissions
   beyond those granted by CO administrator status.

Changes from v4
----------------

- **Group Ownership is now managed via Owners Groups** *(as of v5.0.0)*.
  In v4, Group owners were tracked as a flag on the Group Membership record
  (the "member vs owner" distinction). In v5, ownership is managed by adding
  the Person to the Group's corresponding Owners Group, a separate System
  Group created automatically alongside every Standard Group.

- **Approvers Groups are available as of v5.2.0.** These are automatically
  created for the CO and for each COU, and are used for Enrollment Flow
  approval. They existed in v4 as a concept but were not implemented as
  formal System Groups.

- **MFA Exemption Groups are available as of v5.2.0.** These Groups control
  access to the Registry application itself and are new in v5.

- **Groups can be placed in a hierarchy as of v5.2.0.** Standard Groups can
  now be assigned Parent Groups, and Fully Qualified Group Names are
  constructed from the hierarchy.

- **Group name uniqueness is scoped to the parent Group (or CO, for top-level
  Groups) as of v5.2.0**, rather than requiring uniqueness across the entire
  CO. This allows child Groups to reuse names that exist in other branches of
  the hierarchy.

- **Group Nestings can be managed by the Nester Job Plugin and Deletion Job
  Plugin as of v5.2.0**, enabling background processing of large nesting
  operations.
