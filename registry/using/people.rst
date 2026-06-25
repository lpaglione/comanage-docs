.. _using-people:

People
======

At its core, Registry is a registry for people. Every identity, every
affiliation, every group membership, every provisioned account ultimately
traces back to a Person record — a representation of one human being within
your collaborative organization.

Understanding how Registry models people is the foundation for everything else:
how enrollment works, how provisioning is scoped, how status is calculated, and
how your organizational structure maps onto your membership.

----

.. contents:: On this page
   :local:
   :depth: 1

----

How Registry Represents People
--------------------------------

Registry uses a layered model to represent a person and their relationships.

**The Person Record**
   The top-level object representing one physical human within the CO.
   A Person record holds the attributes shared across all of a person's
   roles: their names, identifiers, email addresses, addresses, telephone
   numbers, URLs, and a small number of personal attributes (date of birth,
   pronouns, time zone). A Person's status is calculated from the statuses
   of their Person Roles.

**Person Roles**
   Roles capture a person's relationship to the organizational structure —
   their affiliation, their COU, their title, their manager. A person can
   hold more than one Role, representing different affiliations or positions
   within the same CO.

**External Identities**
   An External Identity links a Person to a representation of that same
   person in another system — an HR database, a SAML assertion, an ORCID
   record, a CSV file. External Identities are where identity data comes
   *from*, while the Person record and Person Roles are where Registry
   *manages* that data.

These three layers work together: External Identities (typically created by
Organizational Identity Sources and Pipelines) feed data into Person records,
which carry the attributes that drive downstream provisioning.

.. note::

   **External Identities, Identity Sources, and Pipelines** are covered in
   the :ref:`ec-external-identity-sources` and :ref:`ec-pipelines` pages
   under :ref:`using-external-connections`. This section focuses on managing
   Person records and Person Roles once people are in the system.

   **Groups** are covered under :ref:`using-organizations`, where they sit
   alongside COs and COUs as part of the organizational structure.

The Person Canvas
------------------

When you view a Person in the Registry administrative interface, you see the
**Person Canvas** — a comprehensive view of all the information associated with
a Person: their roles, group memberships, identifiers, email addresses, External
Identities, authenticators, and provisioning status.

The Person Canvas is the primary point of interaction for administrators working
with individual People. From it, you can edit attributes, manage identifiers,
view status, and trigger provisioning operations.

How People Get Into Registry
------------------------------

People can enter Registry through any of three paths:

**Enrollment Flows**
   A person (or a petitioner acting on their behalf) completes an Enrollment
   Flow. Registry creates the Person record when the flow is finalized. See
   :ref:`lifecycle-enrollment-flows`.

**Pipelines**
   An Organizational Identity Source (such as an HR feed or LDAP directory)
   creates or updates an Org Identity, and a Pipeline either links it to an
   existing Person or creates a new Person record. See :ref:`ec-pipelines`.

**Manual creation**
   An administrator creates a Person record directly. This is common for
   small-scale administration or when migrating records from another system.

Multiple paths can be active simultaneously. A person might first appear via
enrollment and later have their record updated via an identity source pipeline.

Notifications
--------------

Registry includes a notification facility for delivering short messages to
People and Groups — for example, prompts for approvers to act on a pending
enrollment petition. Notifications appear in the bell (🔔) menu in the
Registry administrative interface and are also sent via email when an SMTP
Server is configured.

For the full technical reference, see
`Registry PE Notifications <https://spaces.at.internet2.edu/spaces/COmanage/pages/297862255/Registry+PE+Notifications>`_
in the Technical Manual.

----

In This Section
----------------

.. toctree::
   :maxdepth: 1

   people/person-records
   people/person-roles
