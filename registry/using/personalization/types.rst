.. _personalization-types:

Types
======

Many of Registry's data objects support multiple values, and those values need
to be distinguished from each other. A Person can have multiple email addresses
— but is a given address their official contact, their personal address, or
their preferred address for CO notifications? A Person can have multiple
identifiers — but which is their ePPN, which is their employee number, and which
is their ORCID? **Types** are how Registry makes these distinctions.

A Type is a category label attached to an attribute value. It has two parts: a
human-readable Name that appears in the Registry interface, and a database Value
that is used in data exports and provisioning. Types are defined per-CO, so your
organization controls exactly what category options exist for each attribute and
what they're called.

For the full technical reference, see
`Registry Types <https://spaces.at.internet2.edu/spaces/COmanage/pages/207650961/Registry+Types>`_
in the Technical Manual.

----

.. contents:: On this page
   :local:
   :depth: 1

----

Which Attributes Use Types
---------------------------

The following attribute categories support Types in Registry:

- **Address Type** — categories for physical addresses (e.g., official, home, work)
- **Department Type** — categories for departments or sub-units
- **Email Address Type** — categories for email addresses (e.g., official, personal, preferred)
- **Identifier Type** — categories for identifiers (e.g., ePPN, employee number, ORCID)
- **Name Type** — categories for names (e.g., official, preferred, alternate)
- **Organization Type** — categories for organizations or institutions
- **Person Role Affiliation** — the affiliation value for a Person Role (e.g., faculty, staff, student, affiliate)
- **Telephone Number Type** — categories for telephone numbers
- **URL Type** — categories for URLs

Types apply equally to Person-level and External Identity-level attributes.

Default Types
--------------

When a new CO is created, Registry automatically creates a default set of Types
for each supported attribute. This gives you a working starting point without
requiring manual setup for every attribute type before you can begin enrolling
people.

Default Types can be modified (renamed) or — if they have never been used —
deleted. However, deleting default Types is not generally recommended. Registry
may expect certain default Type values to exist in some circumstances, and
deleting them can have unexpected consequences in the current release or in
future releases as new functionality is added.

If Types are accidentally deleted, they can be restored using the **Add/Restore
Default Types** action, which applies to all available attribute types.

Managing Types
---------------

Types are managed via **CO Settings > Types** (or via the Identifier Type,
Email Address Type, etc. sub-menus, depending on your navigation).

When creating or editing a Type:

- **Name** — the label displayed in the Registry user interface when this Type
  is presented as an option
- **Value** — the database value used in exports, API responses, and Provisioner
  Plugin output. The Value must be unique for that Type within the CO. Choose
  values that will be stable over time, as changing them after data has been
  assigned to this Type may affect provisioning and integrations.
- **Status** — Active Types are available for new attribute assignments. A
  Suspended Type will not appear as an option for new values, but existing
  records that already use it are not affected.

Types can only be deleted if they have never been used. If a record using a
Type is subsequently deleted, the Type is still considered "in use" due to
Registry's changelog behavior, so it still cannot be deleted. Suspend a Type
rather than trying to delete it if it should no longer be available for new
assignments.

Type-Specific Options
----------------------

Some attribute Types have additional configuration:

**Identifier Types**
   Identifiers can be configured for case sensitivity. By default, identifiers
   are matched case-insensitively, but if your identifier values are
   case-sensitive (common for some external systems), you can enable case-
   sensitive matching for that Identifier Type.

**Person Role Affiliations**
   Affiliations can be mapped to standard **eduPersonAffiliation** values:
   faculty, student, staff, alum, member, affiliate, employee, and library-walk-
   in. This mapping is used by Provisioner Plugins that export affiliation data
   to LDAP or other systems following the eduPerson schema. If your affiliation
   terminology differs from the standard values, the mapping lets you use your
   own labels internally while still exporting standard values downstream.

Provisioning and Types
-----------------------

Types that are provisioned to downstream systems carry their database **Value**
(not their display Name). When configuring integrations, make sure the Values
you assign to your Types match what downstream systems expect to receive.
Changing a Type's Value after provisioning has already occurred may cause
inconsistencies between Registry and the provisioned systems.

Registry also provisions Type definitions as a first-class provisionable object
— alongside People, Groups, and COUs. This means some Provisioner Plugins can
receive the full list of your CO's Types and use them to configure the target
system accordingly.

Changes from v4
----------------

If you are migrating from Registry v4:

- **Renamed from Extended Types.** In v4, these were called "Extended Types."
  The feature is the same conceptually, but the name has changed.

- **The column name is now "value"** and supported models now use a foreign key
  to reference Types rather than storing the Type name as a string. This is an
  internal change that affects database structure and plugin development, not
  day-to-day administration.

- **Default types are no longer enumerations.** In v4, default Type values
  were implemented as enumerations (fixed lists). In v5, they are standard
  Type records that can be modified and managed through the standard interface.

- **Add/Restore Default Types** now applies to all available attribute types
  at once, rather than to individual attributes as in v4.

- **Types now apply to External Identities** in exactly the same way as they
  apply to People. (Previously there were some internal differences in how
  External Identity attribute types were handled.)

- **Identifier Types support case sensitivity configuration** (new in v5).
