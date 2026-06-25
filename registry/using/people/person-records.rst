.. _people-person-records:

Person Records
==============

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


A **Person record** (also called a Registry Person, or simply a Person)
represents one physical human being within your CO. It is the central object
in Registry — enrollment flows create it, pipelines populate it, provisioning
targets consume it, and status calculations are derived from it.

For the full technical reference, see
`Registry People <https://spaces.at.internet2.edu/spaces/COmanage/pages/219918161/Registry+People>`_
in the Technical Manual.

What a Person Record Contains
-------------------------------

The Person record itself carries relatively few top-level attributes — its
role is to serve as the anchor for a collection of related objects. Most
person-level data is stored in multi-valued related records so that, for
example, a single person can have more than one name, more than one identifier,
or more than one email address.

**Names**
   Every Person must have at least one name, and exactly one name must be
   designated as the **primary name**. Names can be encoded in any language
   or character set. The primary name is the one used by Registry in
   display, provisioning, and identifier generation contexts.

   Names can also be typed — for example, to distinguish an official name from
   a preferred name. Each name type can be configured to reflect how your
   organization handles naming.

**Identifiers**
   Identifiers are the values used to identify a Person in external systems
   and to facilitate application integration. A Person can have any number of
   identifiers of any number of types.

   Registry can assign identifiers automatically (via Identifier Assignment)
   or they can be entered manually. It is strongly recommended to configure
   at least one automatically assigned identifier to serve as the person's
   primary Registry identifier. See :ref:`ec-identifier-assignment` for
   configuration details.

   Identifiers of a given type must be unique within the CO. An identifier
   can be suspended rather than deleted to prevent it from being reassigned.

**Email Addresses**
   Registry tracks email addresses and allows multiple addresses per person,
   each with a type. Common types include:

   - **Official** — the address to use in directory entries and for sending
     Registry-generated messages to the person
   - **Personal** — alternate addresses for delivery or forwarding
   - **Delivery** — the delivery mailbox location
   - **Forwarding** — an address to forward mail to
   - **Mailing List** — the priority address used by mailing list plugins

   Email addresses can be verified from within Registry using an Enrollment
   Flow with an Email Verifier step.

**Addresses**
   Physical mailing addresses can be attached to a Person record, each with
   a type (official, home, postal, etc.).

**Telephone Numbers**
   One or more telephone numbers can be attached, each with a type (office,
   mobile, fax, etc.).

**URLs**
   One or more URLs can be attached, with types such as official or personal
   homepage.

**Ad Hoc Attributes**
   Registry supports storing arbitrary key-value attributes on Person records
   via the Ad Hoc Attribute feature. These can be used to capture information
   that does not fit the standard data model.

**Date of Birth**
   An optional field on the Person object itself.

**Pronouns**
   An optional field for preferred pronouns.

Person Status
--------------

A Person's status is a **calculated value** derived from the statuses of the
Person's Roles. Registry takes the most favorable active status across all of
the person's roles to determine the overall Person status.

This means that changing a Role's status — whether manually, via an expiration
policy, or via a pipeline — can change the Person's status. A person with one
Active role and one Expired role will have an overall Person status of Active.

The one exception is **Locked** status, which overrides all role statuses and
applies directly to the Person record.

For the full explanation of status values and how they interact, see
:ref:`lifecycle-status-and-validity`.

Managing Person Records
------------------------

**Viewing a Person**
   From the People listing, select a person to open the Person Canvas. The
   canvas shows all attributes, roles, group memberships, External Identities,
   authenticators, and provisioning status in a single view.

**Editing Attributes**
   Most person-level attributes can be edited from the Person Canvas. Click
   the edit control next to the attribute type you wish to modify (names,
   identifiers, email addresses, etc.).

**Adding and Removing Values**
   Because most attributes are multi-valued, you can add additional names,
   identifiers, email addresses, etc. from the Person Canvas without replacing
   existing values.

**Assigning Identifiers on Demand**
   If Identifier Assignment is configured, an **Assign Identifiers** button is
   available on the Person Canvas to trigger identifier generation for the
   person immediately. See :ref:`ec-identifier-assignment`.

**Viewing History**
   Each modification to a Person record generates a History Record. The full
   history of changes to a person's record is viewable from the Person Canvas
   and provides an audit trail of who changed what and when.

**Reprovisioning**
   An administrator can manually trigger reprovisioning of a Person to any
   or all configured Provisioning Targets from the Person Canvas.

Searching and Listing People
------------------------------

The People listing provides search and filter tools for finding people within
the CO. You can search by name, identifier, or email address, and filter by
status or COU.

For large COs, searching is strongly preferred over browsing the full list,
which can become very long.

Changes from v4
----------------

- **CoPerson was renamed to Person** in Registry v5.0.0. The underlying
  concept is the same; only the terminology changed.

- **Enrollment-state statuses** (Approved, Confirmed, Declined, Denied,
  Duplicate, Invited, Pending, PendingApproval, PendingConfirmation,
  PendingVetting) **are no longer tracked on Person records** as of v5.2.0.
  In v5.2.0 and later, these states are tracked at the Enrollment Flow
  petition level, not on the Person object. Person status values are limited
  to the operational statuses: Active, Grace Period, Suspended, Expired,
  Pending Activation, Archived, and Locked.

- **Pronouns** are a new attribute on the Person record in v5.

- The v4 **Deleted** status is now **Archived** in v5.0.0.
