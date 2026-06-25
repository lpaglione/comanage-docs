.. DRAFT — April 2026
.. Terminology status (all confirmed from PE Technical Manual, Mar 2026):
..   "Person record"        ✓ v5 term (was "CO Person record")
..   "External identity"    ✓ v5 term (was "Organizational Identity")
..   "Enrollment flow"      ✓ unchanged
..   CO (Collaborative Organization) ✓ still used in v5
..   COU (Collaborative Organizational Unit) ✓ still used in v5
..   Groups                 ✓ unchanged
.. TODO: Replace "your organization in Registry" with "CO" and update
..       "sub-units (sometimes called COUs)" to use COU as primary term

.. _concepts-overview:

Registry Concepts Overview
==========================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


Before you configure Registry, it helps to have a mental model of how it thinks
about people and organizations. Registry is structured around a
deceptively simple idea: every person who has a relationship with your
organization should have exactly one record in your registry, no matter how many
systems they appear in or how many roles they hold. Everything else in Registry
is built to support that idea.

This page introduces the core concepts and how they relate to each other. None
of it requires deep technical knowledge — the goal is to give you the vocabulary
and mental model you need to make good decisions when you start configuring
Registry for your organization.

1. Your Organization in Registry
---------------------------------

Registry is a multi-tenant system, meaning it can support multiple organizations
within a single installation. Each organization gets its own distinct space — its
own people, its own groups, its own configuration, and its own enrollment
workflows. When you deploy Registry, the first thing you do is define the
organization (or organizations) that will use it.

Within your organization, Registry gives you a set of tools to model your
population's structure: you can define sub-units for departments, programs, or
teams; create groups to drive roles and access; and configure policies that
govern how people move through their relationship with your organization.

Think of your organization in Registry as the frame. Everything else —
people, groups, connections to external systems — lives within that frame.

2. Person Records
-----------------

The **person record** is the heart of Registry. It represents a single individual
and their relationship with your organization.

A person record is not just a copy of data from one system — it is an aggregated
view, assembled from every source that knows about that person. Someone who
appears in your HR system, your student information system, and a collaboration
platform they joined last year has one person record in Registry, with data drawn
from all three sources. Registry holds these together as a unified, consistent
view of who that person is to your organization.

Person records are enriched over time. Registry can assign identifiers to a
person record — stable IDs that can be relied upon across systems even if the
person's name or email changes. Registry can also store attributes about a person
that don't come from any external system, such as internal notes, custom
categorizations, or manually assigned values.

The person record is also where group memberships, roles, and entitlements live.
When a person's role changes, their person record reflects it — and Registry can
automatically update the systems that depend on that information.

3. External Identities
----------------------

A person record is built from **external identities** — connections to data about
that person held in external systems. Each external identity represents what one
system of record knows about a person.

When Registry connects to your HR system, for example, and imports a record for
an employee, that HR record becomes an external identity attached to the
employee's person record. If that same employee also has a record in your student
information system from an earlier degree, that becomes a second external identity
on the same person record. Registry holds both, maintains the link back to the
source, and lets you configure how the data from each source is used.

This separation — between the unified person record and the individual external
identities that feed into it — is what allows Registry to accommodate the
complexity of real-world organizational data: the same person seen differently by
different systems, brought together in one place.

.. note::

   External identities can be linked automatically through pipelines (when
   Registry connects to a live system of record) or manually by an administrator.
   See :doc:`Managing People in Registry </using/people/managing-people>` for
   more detail on how person records and external identities are created and
   maintained.

4. Organizational Structure: Groups and Sub-units
--------------------------------------------------

Registry gives you two main tools for organizing your population: **sub-units**
and **groups**.

**Sub-units** (sometimes called COUs — CO Organizational Units) model the
hierarchical structure of your organization: departments, colleges, programs,
teams, or any other subdivision that matters for how you manage people.
Sub-units can be nested, so you can represent complex organizational hierarchies.
Administrators can be delegated responsibility for specific sub-units, allowing
the people who know a population best to manage it directly.

**Groups** are more flexible. A group can contain any set of person records,
regardless of their sub-unit membership, and groups can be used to drive roles,
access provisioning, mailing list membership, and more. Groups can be managed
automatically (based on rules and attributes) or manually by administrators or
even by end users, depending on how you configure them.

In practice, sub-units and groups work together: sub-units reflect your org
chart, while groups reflect the functional units that cut across it.

5. Connecting to External Systems
----------------------------------

Registry is designed to connect — both inbound (pulling data in from your
authoritative sources) and outbound (pushing data out to the systems that need
it).

**Inbound connections** bring person data into Registry from your systems of
record. These connections are managed through pipelines, which define how
incoming data is matched to existing person records, how conflicts are resolved,
and how attributes are mapped into Registry's object structure.

**Outbound connections** push data from Registry to the systems that depend on
it: LDAP directories, collaboration platforms, mailing lists, access management
systems, and more. These are handled through provisioning plugins, which run
automatically based on rules you define — so when a person's status changes in
Registry, the right systems are updated without manual intervention.

The plugin architecture on both sides is designed to be extensible. Registry
ships with plugins for common systems, and the open-source community has
contributed others. If you need to connect to a system that isn't covered, you
can build your own plugin.

6. Lifecycle: From Enrollment to Offboarding
---------------------------------------------

Registry manages the full lifecycle of a person's relationship with your
organization, from their first record to their departure.

**Enrollment** is how people enter Registry. An enrollment flow defines the steps
a new person goes through to get a person record: who initiates the enrollment,
what information is collected, what approvals are required, and what happens when
the enrollment is complete. Registry supports self-service, invitation, and
automatic enrollment from external systems.

**Ongoing management** is handled through group memberships, attribute updates,
and provisioning rules. As a person's role changes — moving between departments,
taking on new responsibilities, joining or leaving projects — their person record
and their access to connected systems can be updated automatically.

**Offboarding** is as important as enrollment. Registry's expiration policies
allow you to define what happens when a person's relationship with your
organization ends: which group memberships are removed, which systems are
deprovisioned, and who is notified. A well-configured offboarding policy means
departures are handled consistently and completely, without relying on manual
checklists.

----

Putting It Together
--------------------

These concepts fit together as a coherent system:

- Your **organization in Registry** is the frame within which everything operates.
- **Person records** represent individuals — one per person, aggregating data
  from all sources.
- **External identities** are the connections to those sources, each holding what
  one system knows about a person.
- **Sub-units and groups** organize your population and drive roles and access.
- **Pipelines and provisioning** connect Registry to the systems around it,
  inbound and outbound.
- **Enrollment flows and expiration policies** govern how people enter and exit.

With this model in mind, the configuration decisions you'll make in Registry —
what sources to connect, how to structure your population, what enrollment
workflows to build — start to have a clear logic.

.. seealso::

   :doc:`What is COmanage Registry? </about/what-is-registry>`
      If you haven't read the overview yet.

   :doc:`Roles and Permissions </understanding/roles>`
      Who can do what in Registry.

   :doc:`Planning Your Implementation </understanding/planning>`
      Working through your organization's needs before you start configuring.

   :doc:`Managing People in Registry </using/people/managing-people>`
      How person records and external identities work in practice.

   `COmanage Registry Technical Manual <https://spaces.at.internet2.edu/display/COmanage/Technical+Manual>`_
      Detailed reference documentation.
