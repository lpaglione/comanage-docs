.. DRAFT — April 2026
.. Terminology status:
..   "Person record"       ✓ confirmed v5 term (was "CO Person record")
..   "External identity"   ✓ confirmed v5 term (was "Organizational Identity" / "system of record")
..   "Enrollment workflow" ✓ unchanged
..   CO / COmanage CO      ⚠ OPEN QUESTION — v5 term not yet confirmed; avoiding in this page for now
..
.. This page does not yet use "external identity" (that term will appear in the
.. Concepts and External Connections pages). No CO-container terminology appears
.. on this page. Both can be addressed when the terminology resource is located.

.. _what-is-registry:

What is COmanage Registry?
==========================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


COmanage Registry is an identity registry with flexible enrollment and lifecycle
management capabilities that help you meet your identity management objectives
using standardized tools and approaches. It can be used as a central person
registry, a guest management system, or a membership management platform for
virtual organizations — groups of colleagues from different institutions who
come together to work toward shared research or educational goals.

Registry is part of the `InCommon Trusted Access Platform
<https://incommon.org/software/comanage/>`_, an open-source project used and
shaped by the research and education community.

1. Why a Registry?
------------------

People in your organization don't fit neatly into one box. A person might arrive
as a graduate student, stay on as a postdoc, join a research collaboration, and
later become a faculty member — all while appearing as separate, disconnected
records in your HR system, student information system, and collaboration
platforms. Managing access, entitlements, and transitions across those silos is
manual, error-prone work.

Registry gives you **one authoritative record per person**, aggregated from your
existing systems of record. Once that central record exists, you can manage group
memberships, configure access entitlements, automate lifecycle transitions, and
provision data to the systems that need it — all from one place, without writing
code.

2. What Registry Does
---------------------

Registry's capabilities map directly to the lifecycle of a person's relationship
with your organization:

**Bring people in** through enrollment workflows you design — invitation,
self-service, or automatic import from an authoritative source. You choose the
steps, the approval stages, and the end-user experience, without writing a line
of code or XML.

**Know who they are** by aggregating identity data from your existing systems
into a single **Person record**. Registry connects to HR systems, student
information systems, LDAP directories, and more, giving you a composite view
that stays accurate even as roles and personal data change.

**Identify them across all of your systems** using a stable identifier that
remains reliable even when names or email addresses change over time.

**Organize them into groups** that drive roles and access. Distribute population
management to the people who know the population best — department
administrators, project leads, collaboration coordinators — without routing every
request through central IT.

**Provision their data to other systems** — LDAP directories, collaboration
platforms, mailing lists, and more — automatically, in real time or in batches,
based on rules you define.

**Manage the end of the relationship** through offboarding policies that automate
membership transitions and notify the right people when someone's status changes.

3. Common Uses of Registry
--------------------------

Registry is flexible enough to serve very different organizational needs. A few
common patterns:

**Central person registry**
   Your institution maintains one registry that aggregates person data from HR,
   your student information system, and other sources. Every person who has a
   relationship with your institution has a single record that downstream systems
   can rely on — even someone who is simultaneously an alumnus, a staff member,
   and a parent.

**Guest and external collaborator management**
   You have populations that don't belong in your enterprise systems: visiting
   researchers, guest lecturers, library users, vendors, student families,
   conference attendees. Registry gives them a home — a record you control, with
   access you can grant and revoke on your own timeline.

**Virtual organization management**
   A research group or virtual organization spanning multiple institutions uses
   Registry to manage its own membership, group structure, and resource access —
   giving members from different home institutions a shared identity and
   centrally managed access to the tools they need, independent of any single
   institution's central IT.

4. Registry and the COmanage Project
-------------------------------------

Registry is one of two tools in the COmanage Project. **COmanage Match**
complements Registry by preventing duplicate records: it provides a
heuristic-based system for matching incoming person data against existing records
across multiple authoritative systems. Match can be used alongside Registry or as
a standalone tool.

Because COmanage is an open-source project, the community is central to how it
evolves. Registry is shaped by the organizations that use it, and the project
team actively invites participation — through the monthly newsletter, Open Office
Hours, Slack, and community contributions. See
:doc:`The COmanage Community </community/about>` for ways to get involved.

The COmanage Project is stewarded by **SCG Collaboration Group** (also known
as Spherical Cow Group) and has been made possible through the sustained support
of **Internet2** via the TIER Initiative and the InCommon Trusted Access Platform
Program, as well as funding from the **National Science Foundation**. The project
also reflects significant contributions — in funding, development, and community
engagement — from universities, national labs, and research organizations across
the US and internationally. The full acknowledgements list is available on the
`COmanage wiki <https://spaces.at.internet2.edu/spaces/COmanage/pages/10732/Home>`_.

.. seealso::

   :doc:`How and Why to Use Registry </about/how-and-why>`
      User stories and use cases in more depth.

   :doc:`Registry Concepts Overview </understanding/concepts-overview>`
      The core mental model: Person records, external identities, and how
      Registry structures your data.

   :doc:`What's New in v5 </about/whats-new>`
      What has changed and improved in this version.

   :doc:`About COmanage Match </about/about-match>`
      A brief orientation to the companion tool.

   `COmanage Registry Technical Manual <https://spaces.at.internet2.edu/display/COmanage/Technical+Manual>`_
      Detailed reference documentation for Registry administrators and developers.
