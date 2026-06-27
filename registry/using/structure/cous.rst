.. _struct-cous:

Collaborative Organizational Units (COUs)
==========================================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

A **Collaborative Organizational Unit (COU)** is a named policy context within a
CO for a group of people who have meaningfully different needs. Those differences
might be in how people join (different enrollment flows), who has administrative
authority over them, how their identifiers are assigned, or which downstream
systems receive their data.

COU membership works through **Person Roles**: a Person Role can optionally be
assigned to a COU, or it can exist at the CO level with no COU assignment at all.
Because one person can hold multiple Person Roles, a person can be a member of
several COUs simultaneously — or of none, if their only role is at the CO level.
COUs are not mutually exclusive slots that a person falls into; they are policy
containers that roles are associated with.

It's important to understand what COUs are *not*: they are not an org chart, and
they are not about expressing hierarchy for its own sake. If two groups of people
join and leave the same way, are managed by the same people, and provision to the
same systems, they probably don't need separate COUs — Groups or a simple naming
convention may be sufficient. A COU is the right tool when policy genuinely
differs between populations.

.. TODO: Add a case study or decision guide — "COUs vs Groups: which should I
   use to model a sub-population?" — to help administrators navigate this common
   design question. Key distinction: COUs carry policy (enrollment flows, admin
   delegation, identifier assignment, provisioning scope); Groups carry actions
   (access control, mailing lists, provisioning filters). A person can be in a
   Group without having a Role in a COU. Real-world scenarios (e.g., a
   department that needs its own enrollment process vs. a project team that just
   needs an LDAP group) would make this concrete. Candidate for Recipes or Case
   Studies section.

For the full technical reference, see
`Collaborative Organizational Units (COUs) <https://spaces.at.internet2.edu/spaces/COmanage/pages/392724546/Collaborative+Organizational+Units+COUs>`_
in the Technical Manual.

1. Creating COUs
-----------------

COUs are created via **CO > ALL > COUs > Add a New COU** within the CO's
administrative interface.

When a COU is created, Registry automatically creates a set of special Groups
associated with the COU: an admins group (``CO:COU:<COU Name>:admins``), an
active members group (``CO:COU:<COU Name>:members:active``), an all-members group
(``CO:COU:<COU Name>:members:all``), and an approvers group
(``CO:COU:<COU Name>:approvers``).

2. Naming COUs
---------------

COU names must be unique across the entire platform (enforced case-insensitively
as of v5.2.0). Short, descriptive names are recommended.

.. important::

   When a COU is renamed, its special Groups are also automatically renamed to
   match. If any downstream systems reference those Groups by name — for example,
   an LDAP provisioner that provisions the COU members group — renaming the COU
   will change those names in downstream systems as well. If this is a concern,
   consider using Group Nestings (to expose a stable Group name that doesn't
   incorporate the COU name) or using an Identifier assigned to the Group rather
   than the Group name itself.

3. COU Hierarchy
-----------------

COUs can be arranged in a parent/child hierarchy by setting a **Parent COU** in
the COU's configuration. COU hierarchy is an administrative tool, not a
membership tool:

- A **COU Administrator** for a parent COU is automatically a COU Administrator
  for all of that COU's child COUs.
- A **CO Person with a Person Role** in a COU is not automatically a member of
  any parent or child COU. Cross-COU membership must be established by creating
  an additional Person Role, or by using Group Nestings to cascade access.

This design keeps the hierarchy focused on delegating administrative authority
rather than implying anything about membership or provisioning scope.

4. Deleting COUs
-----------------

A COU cannot be deleted if it has current members (People with a Person Role
assigned to that COU) or if it has child COUs. Both conditions must be resolved
before deletion. Deleting a COU also deletes its associated special Groups.

5. COU Administrators
----------------------

A **COU Administrator** is a person with administrative authority over a specific
COU. COU Administrators can perform lifecycle management operations on Person
Roles within their COU, and their authority cascades to any child COUs in the
hierarchy.

COU Administrators must be Active members of the CO and members of the COU's
``CO:COU:<COU Name>:admins`` group. Being a CO member (but not necessarily a
member of the COU itself) is sufficient — a COU Administrator does not need a
Person Role within the COU they administer.

6. Changes from v4
-------------------

- **COU name uniqueness is now enforced case-insensitively as of v5.2.0.**
  Previously, "Research" and "research" could coexist as separate COU names.
