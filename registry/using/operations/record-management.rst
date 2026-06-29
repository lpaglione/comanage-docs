.. _ops-record-management:

Record Management
=================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry provides several tools for managing the data stored within it:
controlling record statuses, removing data at varying levels of permanence,
normalizing attribute values for consistency, and cloning configuration or
person records across COs.

1. Record Statuses
-------------------

Most Registry records can be in one of the following statuses:

- **Active** — the record is in normal use.
- **Suspended** — the record is not currently in use but is retained and
  can be reactivated. Configuration objects that are Suspended cannot be
  referenced by new configurations.
- **Archived** — the record is no longer in use and is not expected to be
  reactivated. Archived is the v5 replacement for the v4 "Deleted" status.
  Archived records remain visible in the Registry interface.

These statuses apply to most types of objects — People, Person Roles,
Groups, configuration objects, and others. Specific objects may have
additional or different status values; refer to the relevant section for
details.

2. Deleting Records
--------------------

When a record is **deleted** in Registry, it is a **soft delete** by default:
the record is removed from normal view but remains in the database with an
internal deleted flag. Deleted records are not visible in normal interface
views but are retained for audit and changelog purposes.

Registry performs dependency checking before allowing deletion — a
configuration object that is still referenced by another object cannot
be deleted until those references are resolved.

**Expunge (hard delete)**

If your CO requires the ability to permanently remove records from the
database — for example, for data minimization or privacy compliance purposes
— a CO Administrator can enable **Expunge** in CO Settings. When enabled,
an Expunge operation appears alongside the standard Delete option for
supported objects.

Expunging a record performs a hard delete: the record and all of its archived
(changelog) copies are permanently removed from the database. Expunging a
record with dependent records will also expunge those dependent records.

**CO removal**

COs cannot be deleted with an ordinary Delete operation — they can only be
Expunged. When a CO Expunge is requested, the CO enters **Pending Removal**
status. The CO can be reactivated from this status before the deletion is
finalized. The physical removal is then handled by the Garbage Collector Job,
which processes the deletion asynchronously.

For the full technical reference on deletion behavior, see
`Record Deletion <https://spaces.at.internet2.edu/spaces/COmanage/pages/250251271/Record+Deletion>`_
in the Technical Manual.

3. Normalizing Data
--------------------

Registry can automatically normalize attribute values as they are written to
the database, correcting common formatting inconsistencies before they are
stored. For example, a name entered as " los angeles " would be normalized to
"Los Angeles."

Normalization is enabled per-CO via **CO > Configuration > CO Settings**.
When enabled, normalization runs transparently after a supported form is
submitted, before data is written to the database.

The following normalizations are supported:

- **Trim Whitespace** — removes leading and trailing whitespace from values.
- **Mix Case** — capitalizes the first letter of each word and lowercases the
  remaining characters.
- **Punctuation to Space** — replaces non-alphanumeric characters with
  whitespace.

Normalizations are applied to specific fields on specific models (names,
addresses, email addresses, identifiers, telephone numbers, and others).
Additional normalizations can be added via custom plugins.

4. Cloning Records
-------------------

:bdg-success:`New in v5` :bdg-secondary:`Available: v5.2.0`

.. warning::

   Cloning is an experimental feature in v5.2.0 and may change in a
   backward-incompatible manner in future minor releases.

**Cloning** is the process of duplicating a record from one CO to another,
potentially on a different Registry platform. It is the mechanism for
migrating configuration between tiers (test to production), deploying a new
CO from a template, or promoting an individual configuration change — such
as an Enrollment Flow revision — from one environment to another.

Cloning is distinct from:

- **Copying** — duplicating a record within the same CO (not yet available;
  see :ref:`ops-coming-to-v5`)
- **Provisioning** — writing Registry data to downstream systems
- **Syncing** — bringing data in from external identity sources

**What can be cloned**

Not all objects are clonable. In general, primary Registry objects (such as
People) and top-level configuration objects (such as Enrollment Flows, COUs,
Groups, Pipelines, Servers, and Types) are clonable. Child objects (such as
individual Names or Enrollment Flow Steps) are cloned automatically as part
of their parent objects.

**UUIDs**

Clonable objects are identified by UUIDs, which allow the same object to be
uniquely identified in both source and target COs even if its other attributes
change. When a record is cloned, the Cloned Object in the Target CO receives
the same UUID as the Original Object in the Source CO.

Administrators can search for clonable objects by UUID via Global Search.
See :ref:`ops-searching`.

**Change Request Identifiers**

A **Change Request Identifier (CRI)** is an arbitrary string — typically a
ticket or change request number — that can be attached to clonable objects
to group them. CRIs make it possible to identify and batch-clone all objects
associated with a given change. Administrators can search for objects by CRI
via Global Search.

**How cloning works**

Cloning is performed via the Registry Clone Command (CLI). The Clone Command
retrieves the object from the Source CO, checks dependencies in the Target CO,
processes any required predecessors (objects that must be cloned first), and
writes the Cloned Object to the Target CO. Standard Registry application rules
apply — for example, uniqueness constraints are still enforced.

Cloning does not trigger provisioning. To push cloned records to downstream
systems, manually reprovision or schedule a Provisioner Job.

**Cloning to a remote platform**

To clone records to a Target CO on a different Registry platform, create an
SQL Server configuration in the Source CO pointing to the target database. See
`Cloning Records <https://spaces.at.internet2.edu/spaces/COmanage/pages/360644879/Cloning+Records>`_
in the Technical Manual for full details.

5. Duplicate Records
---------------------

Registry can detect and flag potential duplicate Person records within a CO
— cases where the same individual may have been enrolled more than once.
Duplicate detection can be integrated with COmanage Match for more
sophisticated identity matching across platforms.

.. TODO: Expand this section with specifics on how duplicate detection works
   in v5 (Duplicate Records Technical Reference page), and add a cross-reference
   to the Match Integration section once it is written.

See :ref:`using-match` for information on integrating Registry with COmanage
Match for identity deduplication.

6. Changes from v4
-------------------

- **"Deleted" status renamed to "Archived."** The v4 "Deleted" Person status
  (which indicated a record was no longer in use but remained visible) is now
  called **Archived** in v5. The underlying database value is unchanged.

- **Expunge** is now a general hard-delete operation, available on any
  supported model when enabled by a CO Administrator. In v4, "Expunge" referred
  specifically to removing a CO Person and related records. In v5, the same
  behavior is preserved, but the operation is generalized and must be explicitly
  enabled in CO Settings.

- **Cloning is new in v5.2.0.** Registry v4 did not support cross-CO record
  cloning.
