.. _using-structure:

Structure
=========

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry is built around the idea that different populations of people have
different needs — different ways of joining, different attributes, different
access rights, and different administrators. The Structure area is where you
define the containers and groupings that make those distinctions real.

Three objects form the structural core of every Registry deployment:

**Collaborative Organizations (COs)** are the top-level tenant containers.
Each CO is a distinct population with its own configuration, administrators,
enrollment flows, provisioning targets, and people. Most deployments operate
with a single CO for their organizational population, plus the built-in
COmanage CO used for platform administration.

**Collaborative Organizational Units (COUs)** are named policy contexts within a
CO. COUs are not an org chart — they exist where policies differ: where people
join differently, where different people have administrative authority, or where
downstream provisioning should be scoped separately. A person can hold roles in
multiple COUs at once, or none at all. A CO can have many COUs, and COUs can be
arranged in a hierarchy for administrative purposes.

**Groups** are flexible collections of people used to drive actions — controlling
who can approve an enrollment petition, which people get provisioned to a
downstream system, who receives a mailing list, and more. Some Groups are
managed automatically by Registry; others are managed by administrators or by
members themselves.

1. Collaborative Organizations (COs)
-------------------------------------

A Collaborative Organization is the fundamental unit of tenancy in Registry.
Everything else — COUs, Groups, People, enrollment flows, provisioning targets —
belongs to a CO. Even the platform itself is managed through a CO (the COmanage
CO).

CO structure is intentionally simple: a CO either exists and is active, or it
is suspended or deleted. The complexity lives in the configuration within the CO
— in its COUs, Groups, enrollment flows, and external connections — rather than
in the CO record itself.

For the full technical reference, see
`Registry Collaborative Organizations (COs) <https://spaces.at.internet2.edu/spaces/COmanage/pages/392724540/Registry+Collaborative+Organizations+COs>`_
in the Technical Manual.

.. button-ref:: struct-co
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about COs →

2. Collaborative Organizational Units (COUs)
---------------------------------------------

A COU is a named policy context within a CO for a group of people with
meaningfully different needs. Those differences might be in how people are
enrolled, who has administrative responsibility, how people's identifiers are
assigned, or which downstream systems receive their data. A person can hold
roles in multiple COUs at once, or none at all — COU membership is not
an either/or assignment.

COU hierarchy is administrative, not membership-based: being a member of a COU
does not automatically imply membership in a parent or child COU. COUs can be
arranged in a hierarchy for the purpose of delegating administrative authority
— a COU Administrator over a parent COU is automatically a COU Administrator
over all its children.

For the full technical reference, see
`Collaborative Organizational Units (COUs) <https://spaces.at.internet2.edu/spaces/COmanage/pages/392724546/Collaborative+Organizational+Units+COUs>`_
in the Technical Manual.

.. button-ref:: struct-cous
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about COUs →

3. Groups
----------

Groups are how Registry applies actions to a set of people at once. A Group
might determine who can approve a petition, which people are provisioned to an
LDAP directory, who receives email from a mailing list plugin, or who is exempt
from multi-factor authentication requirements.

Registry maintains several types of automatic Groups — for CO and COU membership,
for administration, and for enrollment approvals — and also supports
administrator-managed and self-service Standard Groups. Groups can be nested to
combine populations using AND, OR, and NOT logic.

For the full technical reference, see
`Registry Groups <https://spaces.at.internet2.edu/spaces/COmanage/pages/232358046/Registry+Groups>`_
in the Technical Manual.

.. button-ref:: org-groups
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Groups →

----

.. _struct-coming-to-v5:

4. Coming to v5
----------------

Two additional structural object types from Registry v4 are not yet available in
v5 but are planned for a future release.

**CO Departments** provide a place to store structured information about
departments or other internal units within your CO: contact information,
identifiers, URLs, and physical addresses. CO Departments are standalone records
— they are not attached to individual Person records — and can be associated with
a CO or a COU. They can be used as a source of metadata for provisioning.

**CO Organizations** provide a similar capability for external organizations —
institutions, companies, or other entities that your CO members may be affiliated
with. Like CO Departments, they are standalone records used to store contact and
identifier information, not linked directly to Person records.

Both features will be documented here when they are available in v5.

----

Pages in This Section
----------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   structure/collaborative-organizations
   structure/cous
   structure/groups
