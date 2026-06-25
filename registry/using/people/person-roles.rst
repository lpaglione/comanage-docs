.. _people-person-roles:

Person Roles
============

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


A **Person Role** represents a Person's relationship to the collaborative
organization — their affiliation, their position in the organizational
structure, and their validity within that context. One Person can hold
multiple Roles, each capturing a distinct relationship.

Roles are how Registry expresses *why* someone is a member of your CO and
*what kind* of member they are. A researcher might have one Role as a faculty
member of a university department (COU) and another as a visiting collaborator
in a separate COU. Both roles co-exist on the same Person record.

For the full technical reference, see
`Registry Person Roles <https://spaces.at.internet2.edu/spaces/COmanage/pages/219918164/Registry+Person+Roles>`_
in the Technical Manual.

Role Attributes
----------------

**Affiliation**
   Every Person Role must be assigned an Affiliation type. Affiliations are
   drawn from the eduPersonAffiliation vocabulary (Member, Faculty, Student,
   Staff, Alum, etc.) extended with additional types available in Registry.
   The specific affiliation types available are configured via your CO's Type
   settings.

   When External Identity roles are synced to a Person via a Pipeline, an
   affiliation must be set. See the Pipeline documentation for how to handle
   affiliation assignment in this context. See :ref:`ec-pipelines` for
   details.

**COU (Collaborative Organization Unit)**
   A Role can optionally be assigned to a COU — the Registry equivalent of
   an organizational subdivision (department, working group, project team,
   etc.). Roles without a COU are assigned at the CO level.

   COUs are configured in the Organizations section. See
   :ref:`using-organizations`.

**Department**
   An optional free-text field describing the department within the COU or
   organization. Formerly named ``ou`` in Registry v4.

**Organization**
   An optional field for the organization associated with the role. Formerly
   named ``o`` in Registry v4.

**Title**
   An optional free-text field for the person's title in this role.

**Manager**
   An optional link to another Person within the CO who serves as this
   person's manager in this role.

**Sponsor**
   An optional link to another Person within the CO who sponsored this
   person's enrollment or membership.

**Status**
   Each Role has its own status (Active, Suspended, Expired, etc.), which
   contributes to the Person's overall status calculation. See
   :ref:`lifecycle-status-and-validity` for the full status model.

**Validity Dates**
   A Role can have a **Valid From** date and a **Valid Through** date.
   Registry uses these dates to automatically transition Role status:

   - Before the Valid From date is reached, the Role is in
     **Pending Activation** status.
   - After the Valid Through date has passed, the Role transitions to
     **Expired** status.

   Validity dates are processed by the background Jobs framework. See
   :ref:`lifecycle-status-and-validity` for details on automatic status
   transitions.

Role Ordering
--------------

When a Person has multiple Roles, roles can be ordered within the same Person.
Role ordering can matter for downstream systems that consume the first or
"primary" role — for example, a provisioner that needs to select a single
affiliation for a directory entry.

To set the order, edit the Role and assign it an order number. Lower numbers
indicate higher priority.

Multi-valued Attributes on Roles
----------------------------------

In addition to the scalar attributes described above, several multi-valued
attributes can be attached to Person Roles:

- **Addresses** — physical mailing addresses scoped to this role
- **Telephone Numbers** — phone numbers scoped to this role
- **URLs** — web addresses scoped to this role
- **Ad Hoc Attributes** — arbitrary key-value attributes scoped to this role

These are analogous to the same attribute types on the Person record, but
scoped to a specific role rather than the person as a whole. This allows, for
example, storing a role-specific office phone number separately from the
person's general contact telephone number.

How Roles Are Created
-----------------------

Roles can be created:

- **Via an Enrollment Flow** — when a petition is finalized, Registry creates
  a Person Role as part of the enrollment result. Role attributes can be
  collected during the flow or assigned by configuration. See
  :ref:`lifecycle-enrollment-flows`.

- **Via a Pipeline** — when an Organizational Identity Source creates or
  updates a person's External Identity, a Pipeline can create or update a
  corresponding Role. See :ref:`ec-pipelines`.

- **Manually by an administrator** — an administrator can add a Role to an
  existing Person record from the Person Canvas.

Changes from v4
----------------

- **The** ``affiliation`` **field was replaced with** ``affiliation_type_id``
  in v5.0.0, reflecting the transition to extended types for affiliations.

- **The** ``o`` **field was renamed** ``organization`` in v5.0.0.

- **The** ``ou`` **field was renamed** ``department`` in v5.0.0.

- **Person Roles cannot be Locked in v5.** In v4, Locked status could be
  applied to either a Person or a CoPerson Role. In v5, Locked status applies
  only to the Person record itself, not to individual Roles. See
  :ref:`lifecycle-status-and-validity`.
