.. DRAFT — April 2026
.. Terminology status (confirmed from PE Technical Manual, Mar 2026):
..   "Person record"     ✓ v5 term
..   "External identity" ✓ v5 term
..   "Enrollment flow"   ✓ unchanged
..   CO                  ✓ still used in v5
..   COU                 ✓ still used in v5
.. TODO: Replace "sub-unit" with "COU" and "your organization in Registry"
..       with "CO" throughout this page

.. _planning:

Planning Your Implementation
=============================

The best time to think carefully about your Registry configuration is before you
start building it. The decisions you make early — about your population, your
organizational structure, your connections to other systems, and who manages what
— shape everything that comes after. Getting them right the first time saves a
lot of reconfiguration later.

This page walks you through the key planning questions in roughly the order you
should think about them. You do not need to have every answer before you begin,
but you should at least have thought about each area. If you are still new to
Registry's concepts, read :doc:`concepts-overview` first.

----

.. contents:: On this page
   :local:
   :depth: 1

----

1. Describe Your Population
----------------------------

Start with your people: who will have Person records in Registry, and what do
their relationships with your organization look like?

**Who are they?**
   Think broadly. Your population might include employees, students, guests,
   visiting researchers, alumni, collaborators at other institutions, vendors,
   or any combination of these. Each category may have different attributes,
   different join and leave processes, and different access to systems.

**Do they share a single set of policies, or do different groups have
different rules?**
   If everyone in your Registry follows the same process to join, the same
   policies for how long they stay active, and the same provisioning rules,
   your configuration will be simpler. If different sub-populations have
   meaningfully different policies — different approval requirements, different
   systems they are provisioned to, different validity periods — you will need
   to plan for that variation.

**How do they get in, and how do they leave?**
   Some populations are imported automatically from an authoritative system.
   Some are invited by an administrator. Some self-register. Most real-world
   deployments use several of these approaches for different groups of people.
   You will design an enrollment flow for each pattern you need.

**How many organizations do you need?**
   Registry supports multiple organizations within a single installation. Most
   deployers start with one. You might need more than one if you are operating
   a shared Registry service for genuinely distinct organizations that should
   have no visibility into each other's data, or if you need to sandbox a
   test environment alongside a production one.

2. Model Your Organizational Structure
----------------------------------------

Once you know who is in your Registry, think about how they should be organized
within it. Registry gives you two tools — sub-units and groups — with different
purposes.

**Do you need sub-units?**
   Sub-units are for situations where different parts of your population have
   different administrative or policy requirements: different people managing
   them, different enrollment processes, different provisioning rules, or
   different validity and expiration policies. If those differences exist across
   meaningful sub-populations, you need sub-units.

   If your whole population is managed under a single set of policies, you
   probably do not need sub-units — groups will be sufficient for organizing
   people and driving access.

**If you need sub-units, how should they be structured?**
   Sub-units can be flat (all at the same level under your organization) or
   hierarchical (sub-units nested under other sub-units). Hierarchy is most
   useful when administrative authority should flow down — an administrator of
   a parent sub-unit automatically has authority over its children.

   Keep your sub-unit structure as simple as it needs to be. Over-engineering
   it creates configuration and maintenance overhead. A common pitfall is
   mirroring your complete org chart in Registry even when most of those
   divisions do not need different policies.

**What groups do you need?**
   Groups are more flexible than sub-units and can cut across your
   organizational structure. Think about what groups will drive access
   provisioning to other systems, what groups might have mailing lists attached,
   and what groups users might self-manage or self-join. You do not need to
   design every group before you start — groups are easy to add later — but you
   should have a sense of the patterns you will need.

3. Identify Your Identity Sources
-----------------------------------

Person records in Registry are built from external identities — connections to
data about that person held in other systems. Think through what those sources
are for your population.

**What are your authoritative sources?**
   For each major population in your Registry, identify where the authoritative
   data about that person lives. Common sources include HR systems, student
   information systems, LDAP directories, ORCID, and file-based imports. Some
   populations (guests, external collaborators) may have no authoritative source
   — their data is collected at enrollment and managed manually.

**How will you connect to each source?**
   Registry connects to identity sources through plugins. Check which plugins
   are available for your systems and whether any configuration or
   infrastructure work will be needed before you can make those connections.
   If you are importing initial data from a file (CSV or similar), plan for
   that as a distinct step before ongoing synchronization is in place.

**How will you handle matching?**
   When a new record arrives from a source, Registry needs to determine whether
   that person already exists in your Registry. Think about what data will be
   available for matching and how confident you need to be before linking records
   automatically. If identity de-duplication across multiple authoritative
   sources is a significant concern for your deployment, look at
   :doc:`About COmanage Match </about/about-match>`.

4. Design Your Enrollment Flows
---------------------------------

An enrollment flow is the process by which a new person gets a Person record
in Registry. You will need at least one, and most organizations need several —
one for each distinct pattern of how people join.

**Who initiates the enrollment?**
   Three patterns are most common. In an *administrator-initiated* flow, an
   admin creates or invites the person. In a *self-service* flow, the person
   signs up on their own using a shared link. In an *automated import* flow,
   Registry creates records automatically from a connected source. You may use
   all three for different sub-populations.

**Does the flow require approval?**
   For some populations you want an approval step — a human review before the
   Person record is finalized and provisioning begins. For others (employees
   imported from HR, for example), approval would just be friction. Plan
   approval requirements per flow, not globally.

**What information is collected at enrollment?**
   Think about which attributes you need to collect from the person being
   enrolled (versus pulling from an identity source), and who should provide
   them. For guest or affiliate populations, enrollment may be where you collect
   most of their data.

**How many flows do you need?**
   It is common for organizations to have between three and ten enrollment flows
   covering different populations and scenarios. Some complex deployments have
   many more. Start by listing your distinct population types and join patterns
   — each distinct combination typically becomes its own flow.

5. Plan Your Provisioning
--------------------------

Provisioning is how Registry pushes data out to the systems that need it.
Think through what needs to happen downstream when someone is added, changed,
or removed in Registry.

**Which systems need to receive data from Registry?**
   Common provisioning targets include LDAP directories, SQL databases,
   collaboration platforms, mailing list managers, and access management
   systems. List the systems you want Registry to provision and what data each
   needs.

**What triggers provisioning?**
   Provisioning typically runs automatically when a person's record changes —
   when they are enrolled, when their group membership changes, when their
   status expires. Think about which events should trigger updates to which
   systems, and whether any systems need near-real-time updates versus batch
   processing.

**What happens at offboarding?**
   Provisioning is not just about access grants — it also handles revocations.
   Registry's expiration policies define what happens when a Person record
   expires or is deactivated: which group memberships are removed, which systems
   are deprovisioned, and who is notified. Planning offboarding alongside
   onboarding is strongly recommended. Omitting it is one of the most common
   sources of orphaned access in deployed registries.

6. Assign Administrative Responsibility
-----------------------------------------

Think through who will manage Registry and at what level.

**Who will be your Organization Administrators?**
   These are the people who will configure and maintain your Registry. They
   have full authority within the organization, including the ability to add
   and remove people and change configuration. Start with a small number —
   usually one to three — and expand as needed.

**Will you delegate management to Sub-unit Administrators?**
   If you have sub-units, think about whether there are people outside your
   core admin team who should be able to manage the people in their sub-unit.
   Department coordinators, project leads, and collaboration managers are
   common candidates. Delegation reduces the burden on central admins and puts
   management in the hands of the people who best know each population.

**Who will own groups?**
   For groups that represent real teams or mailing lists, consider whether
   ownership should rest with a small admin group or whether it makes sense
   for a broader group of people (for example, the group's members themselves,
   for open groups) to manage membership.

----

Putting Your Plan Together
---------------------------

Before you start configuring, you should be able to sketch answers to these
questions:

- What populations will you manage, and what are the differences between them?
- Do you need sub-units? If so, what is their structure?
- What identity sources will you connect, and how?
- What enrollment flows do you need — one per population join pattern?
- What systems will you provision, and what triggers those updates?
- What are your offboarding and expiration rules?
- Who are your administrators, and at what level?

You do not need complete, final answers to all of these before you begin — and
you will certainly refine your configuration as you learn from experience. But
thinking them through before you start will save significant rework.

.. note::

   If you are moving from Registry v4 to v5, see :doc:`../transitioning/index`
   for migration-specific planning considerations. Many v4 concepts map directly
   to v5, though some configuration will need to be recreated.

.. seealso::

   :doc:`Registry Concepts Overview </understanding/concepts-overview>`
      The mental model for how Registry structures people and organizations.

   :doc:`Roles and Permissions </understanding/roles>`
      The administrator role hierarchy in detail.

   :doc:`How and Why to Use Registry </about/how-and-why>`
      Use cases that illustrate how different types of organizations deploy
      Registry.

   :doc:`../transitioning/index`
      Planning resources for organizations moving from v4 to v5.

   `COmanage Registry Technical Manual <https://spaces.at.internet2.edu/display/COmanage/Technical+Manual>`_
      Detailed configuration reference once you are ready to build.
