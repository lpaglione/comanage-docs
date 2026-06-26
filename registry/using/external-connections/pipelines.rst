.. _ec-pipelines:

Pipelines
==========

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


When data arrives from an External Identity Source, it doesn't flow directly
into a Person record. Instead, it passes through a **Pipeline** — a set of
rules that determine what happens to that data: who it belongs to, how it maps
to Registry's attributes, and what Registry should do if no matching Person
record exists yet.

A Pipeline is a required configuration object for every External Identity
Source. Think of the Pipeline as the "brains" of the inbound connection: the
External Identity Source tells Registry *where to get data*, while the Pipeline
tells Registry *what to do with it*.

Pipelines are shared objects. A single Pipeline can serve multiple External
Identity Sources that process data the same way — for instance, if you have two
LDAP directories with identical attribute schemas and matching rules, you can
point both External Identity Sources at the same Pipeline.

For the full technical reference, see
`Registry PE Pipelines <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743515/Registry+PE+Pipelines>`_
in the Technical Manual.

How Data Flows Through a Pipeline
------------------------------------

Data moves through the Pipeline in a specific sequence:

1. The **System of Record** (your HR database, SIS, LDAP, flat file, etc.)
   holds the authoritative data about a person.

2. The **External Identity Source Plugin** connects to the System of Record and
   converts its data into Registry's internal format.

3. The normalized data is stored as an **External Identity**. Registry also
   stores an **External Identity Source Record** — an artifact containing
   metadata about the source data and a copy of the original (unnormalized)
   record, used to detect changes on future syncs.

4. The Pipeline then creates or updates **Person** and **Person Role** records
   based on the External Identity attributes, following the match and sync
   configuration described below.

An important distinction runs through this entire flow: External Identity
attributes belong to the System of Record and are not directly editable by
administrators. Person-level attributes — the operational copy that Registry
manages — are owned by Registry and can be updated both from source syncs and
by administrator action. For more on this ownership model, see Frozen Attributes
below.

Match Strategy
---------------

Before the Pipeline can do anything else, it must determine whether the incoming
record represents a new person or an existing Person record. This is controlled
by the **Match Strategy**.

**Email Address**
   Registry searches for an existing Person who has a verified Email Address of
   the configured type that matches the email in the incoming record. The search
   is case-insensitive.

   Use this when the source provides an email address you can trust as a
   per-person unique identifier, and that email is likely to already exist in
   Registry for anyone who might be re-enrolled.

**Identifier**
   Registry searches for an existing Person who has an active Identifier of the
   configured type that matches the identifier in the incoming record. The search
   is case-sensitive.

   Use this when the source provides a stable, unique ID (such as an employee
   number or student ID) that you expect to be already attached to Person records
   from previous enrollments or imports.

**External** :bdg-secondary:`Available: v5.2.0`
   Registry calls an external matching service (such as Internet2 Match) to
   determine if the incoming record corresponds to an existing Person. See
   `Identity Match Integration <https://spaces.at.internet2.edu/spaces/COmanage/pages/338788374/Identity+Match+Integration>`_
   in the Technical Manual.

   Use this for complex identity resolution scenarios where local matching
   criteria are insufficient.

**No Matching**
   Every incoming record is treated as a new person and creates a new Person
   record, with no attempt to link to an existing one.

   Use this only when you are certain the source records are unique and there is
   no risk of duplicate Person records being created.

.. note::

   For Email Address and Identifier matching, if more than one existing Person
   matches the incoming record, the result is non-deterministic — Registry will
   pick one but cannot guarantee which. Use these strategies only when the
   matching attribute is reliably unique across your CO.

   When matching, the Pipeline ignores the overall Person status — it may match
   and attach to a Person in any status, including Suspended or Archived.

Sync Configuration
-------------------

Once a match is found (or a new Person created), the Pipeline applies the
following sync settings to control how data is written to Registry.

**Person Status on Create** :bdg-secondary:`Available: v5.2.0`
   When the Pipeline creates a new Person record, this is its initial status.
   Status will typically be recalculated quickly once Person Roles are created,
   but this setting controls the brief window before that happens.

**Role Status on Delete**
   When an External Identity Role is removed from the source, the corresponding
   Person Role will be set to this status. Common choices are Expired or
   Archived, depending on your offboarding policies.

**Sync to COU**
   If set, any new Person Role created through this Pipeline will be placed in
   the configured COU. If multiple External Identity Roles create multiple Person
   Roles, all will be placed in the same COU.

**Person Role Affiliation**
   If set, all Person Roles created by this Pipeline will be given this
   affiliation, overriding whatever the source provided. If not set, the
   Pipeline uses the affiliation from the source data.

   Person Roles require a valid affiliation — make sure this is configured
   either here or in the source data.

**Sync Identifier Type**
   When source records include Manager or Sponsor relationships expressed as
   identifiers, this setting tells the Pipeline which Identifier Type to use
   when looking up the corresponding Person records in Registry. If this setting
   is not configured, Manager and Sponsor relationships will not be synced.

**Flag All Email Addresses Verified** :bdg-secondary:`Available: v5.1.0`
   By default, email address verification status passes through from the source.
   Enabling this flag marks all Email Addresses from this source as verified on
   the Person record, regardless of what the source asserts.

Frozen Attributes
------------------

By default, every time the Pipeline syncs a record from the source, it
overwrites the corresponding Person-level attribute with the source value. This
keeps Registry in sync with the System of Record.

But there are cases where you want to keep Registry in sync with the source for
most attributes, while overriding a specific value locally. For example, a
person's official title in the HR system might be "Research Consultant IV" while
the organization uses "Principal Investigator" in practice.

To handle this, Registry supports **Frozen Attributes**. An administrator can
edit a Person attribute and then mark it as Frozen. A frozen attribute will not
be overwritten by subsequent Pipeline syncs, even though the External Identity
continues to update normally. Unfreezing the attribute allows future syncs to
overwrite it again.

.. note::

   Freezing a Person Role only freezes the Role-level attributes (such as
   title). Related secondary attributes (such as Telephone Numbers) must be
   frozen separately on each attribute record.

   Attributes can be set as Frozen via the Registry REST API. Unfreezing
   currently requires the user interface.

Person Roles and External Identity Roles
-----------------------------------------

The Pipeline automatically creates a **Person Role** for each **External
Identity Role** present in the incoming source record. If the source later
removes an External Identity Role, the corresponding Person Role will be set to
the status configured by Role Status on Delete.

Some Systems of Record are not designed to convey multiple roles for the same
person within a single record. If your source assigns a separate record to each
role (with different source IDs per role), Registry will treat each one as a
different External Identity and may create multiple Person records by default.

Approaches to handling this include: preprocessing the source data before it
reaches the plugin; using Identifier-based matching so all roles resolve to the
same Person; or using the External Match Strategy with an external matching
service. The right approach depends on your specific integration.

Extending Pipelines with Plugins
----------------------------------

Data flowing through a Pipeline can be modified using **Pipeline Plugins**,
which are attached to the Pipeline via **Flanges**. A Flange connects a Plugin
to a specific **Integration Point** — a defined location within the Pipeline
flow where the Plugin is called.

Multiple Flanges can be defined for the same Integration Point. They will all
run, in the specified order, and later Flanges may override the results of
earlier ones.

Available Pipeline Plugins and their supported Integration Points are listed in
`Available Pipeline Plugins <https://spaces.at.internet2.edu/spaces/COmanage/pages/310247815/Available+Pipeline+Plugins>`_
in the Technical Manual.

Manually Rerunning a Pipeline
------------------------------

To rerun a Pipeline for a specific record, retrieve the current record from the
External Identity Source (either by searching in the source or navigating from
the Person record) and select **Sync Record to CO**. This reprocesses the record
from the source and reruns the Pipeline, even if the source data has not changed.

Changes from v4
----------------

If you are migrating from Registry v4, the following Pipeline changes apply:

- **Pipelines now connect External Identity Sources to Person records**, not
  Organizational Identities to CO Person records. The underlying concepts are
  the same, but the terminology has changed throughout.

- **Sync on Add/Update/Delete** is no longer configurable per-Pipeline. Syncing
  behavior is now controlled by the Sync Mode on the External Identity Source
  itself.

- **Person Roles are created automatically** from External Identity Roles. The
  v4 "Create CO Person Role Record" option is no longer needed.

- **Match Strategy with multiple results is non-deterministic.** In v4, an
  error was thrown if more than one Person matched. In v5, Registry will pick
  one record non-deterministically — design your match strategies to avoid
  this situation.

- **Sync Identifier Type must be set to a specific type** to enable syncing
  Manager and Sponsor relationships. A blank value no longer matches any
  Identifier type.

- **Pipeline Plugins (Flanges) are supported** as of v5.0.0.

- **External Match Strategy** is supported as of v5.2.0.

- **External Identities cannot flag Identifiers for login.** Use the Identifier
  Mapper Pipeline Plugin (available as of v5.1.0) if you need to set the login
  flag on identifiers arriving through a Pipeline.
