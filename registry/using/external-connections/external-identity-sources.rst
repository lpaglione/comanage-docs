.. _ec-external-identity-sources:

External Identity Sources
==========================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


Most organizations already have authoritative records about their people in one
or more external systems — an HR database, a student information system, an LDAP
directory, an ORCID registry, or a flat file export. Rather than asking
administrators to re-enter that data manually, Registry connects directly to
those systems through **External Identity Sources (EIS)** and pulls the records
in automatically.

When Registry syncs a record from an External Identity Source, it stores a local
representation — an **External Identity** — attached to the matching Person
record. The External Identity tracks what that source knows about the person, and
keeps Registry in sync as the source data changes over time. If a person appears
in multiple source systems, they will have multiple External Identities, all
attached to the same Person record.

External Identity data flowing in from a source is **read-only** in Registry —
it belongs to the source, not to Registry. Administrators cannot directly edit an
External Identity that was created from a source. Instead, changes flow through
the source and are synced back to Registry.

A **Pipeline** governs how incoming data is processed: how source records are
matched to existing Person records, how attributes are mapped, and how Person
Roles are created. Every External Identity Source requires a Pipeline. This means
you set up a Pipeline first, then configure the External Identity Source to use
it.

For the full technical reference, see
`Registry PE External Identity Sources <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743514/Registry+PE+External+Identity+Sources>`_
in the Technical Manual.

Configuring an External Identity Source
-----------------------------------------

Before adding an External Identity Source, create a suitable Pipeline if one
does not already exist. See :ref:`ec-pipelines` for guidance.

Once a Pipeline is in place:

1. Navigate to **Configuration > External Identity Sources > Add a New External
   Identity Source**.
2. Set the **Status** (sync mode) as described below.
3. Select the desired **Plugin** for your source type.
4. Select the **Pipeline** to use for processing incoming records.
5. If using the API Source Plugin, enter a **System of Record Label** — this
   identifier is passed to the plugin to distinguish between source systems.
6. Click **Save**, then configure the plugin-specific settings that appear.

Sync Modes
-----------

Each External Identity Source has a Status that controls how records are synced
from the source into Registry. Choose the sync mode that matches how you want
records to flow.

**Full**
   When a Sync Job runs, all records currently in the source are synced to
   Registry. Records that have been added to the source since the last sync will
   be added to Registry; records that have changed will be updated; records that
   have been removed may be set to a deactivated status.

   Use Full mode when Registry should mirror the contents of the source
   completely.

**Update**
   When a Sync Job runs, only records that already exist in Registry as External
   Identities from this source will be updated. New records in the source that
   have not yet been synced to Registry will be ignored.

   Use Update mode when you want to control which records come into Registry
   (for example, via manual sync or Enrollment Flow) but want those existing
   records kept current automatically.

**Manual**
   Records may only be synced one at a time, by an administrator searching the
   source and selecting records to sync. No automatic syncing via Sync Jobs.

   Use Manual mode during initial setup, or when importing is an administrative
   action that should be deliberate and controlled.

**Disabled**
   No syncing of any kind — manual or automated — is available. The source
   configuration is preserved but inactive.

   Disable a source when it is being reconfigured, during maintenance, or before
   running the Adopter Job (see Adoption, below).

Syncing Records
----------------

**Via Sync Job**

The `Sync Job Plugin <https://spaces.at.internet2.edu/spaces/COmanage/pages/305856987/Sync+Job+Plugin>`_
runs syncing automatically on a schedule. It processes all External Identity
Sources in Full or Update mode within the CO. Sync jobs can be triggered
manually by an administrator or scheduled to run periodically.

.. note::

   Not all External Identity Source Plugins support all sync modes. Consult the
   plugin documentation to confirm which modes are supported.

**Manually (one record at a time)**

Administrators can manually search a source and sync individual records:

1. Navigate to **ALL > Configuration > External Identity Sources**.
2. From the gear menu for the desired source, select **Search Source**.
3. Search for the record (by source key, email address, name, or other supported
   criteria depending on the plugin).
4. Select the appropriate result and click **Sync Record to CO**.

.. note::

   Not all plugins support direct record retrieval and therefore manual syncing.

Managing Synced Records
------------------------

Once a record is synced into Registry, several administrative actions are
available from the External Identity's gear menu on the Person record.

**Resync**
   Fetches the latest data from the source and updates the External Identity and
   its pipelined attributes. Use this when you know a source record has changed
   and you don't want to wait for the next scheduled sync.

**Relink**
   Moves an External Identity from one Person record to another. Use this when a
   record was inadvertently synced to the wrong Person.

   To relink: if the correct Person doesn't exist yet, create them first. Then
   navigate to the External Identity's gear menu and select Relink. Find the
   target Person record. Note that relink does not resync — it only moves the
   External Identity and its pipelined attributes.

   .. note::

      An External Identity cannot be relinked if any of its pipelined attributes
      are frozen on the source Person record.

**Delete**
   Removes the External Identity from the Person record. The pipelined attributes
   and any associated Person Roles will also be removed or set to the configured
   deletion status.

   Deleting an External Identity does not prevent the source from resyncing the
   record. Whether it reattaches to the same Person depends on the Pipeline's
   Match Strategy.

**Adopt** :bdg-success:`New in v5` :bdg-secondary:`Available: v5.1.0`
   Converts an External Identity to a Registry-native record. Adoption unlinks
   the Person's attributes from the source — they become read/write rather than
   read-only, and Registry becomes the authoritative system for those records.
   After adoption, the source can no longer sync this record.

   Adoption is useful for data migration scenarios, such as transitioning records
   from an external system to Registry as the authoritative system of record.

   Adoption can be reversed via **Annulment**, which reruns the Pipeline to
   reestablish the External Identity from the source. Because adopted attributes
   may have been edited, annulment may leave some records in a state that requires
   manual cleanup.

   To adopt all records from a source at once, use the Adopter Job Plugin. Before
   running it, set the source Status to Disabled to prevent unintentional data
   transformations.

Configuration Options
----------------------

**Hashing Source Records**

When Registry syncs a record, it stores a copy of the source data locally in the
External Identity Source Record. This cache is useful for detecting changes
between syncs and for tracing problems.

If your deployment has privacy or data retention concerns about storing full
source record copies, you can enable **Hash Source Records**. When enabled,
Registry stores a hash of the source data rather than the full copy. This
confirms whether data has changed without preserving the original values.

Tradeoffs: the cached copy is no longer human-readable for debugging, and all
records will be treated as out-of-date the next time a sync runs after enabling
this option. Additionally, previous copies of source records may remain in
Registry's changelog and require manual SQL intervention to remove.

Determine the appropriate value for this setting before you have significant
production data.

**Suppressing No-op Logs**

For large datasets where most records don't change between syncs, the Sync Job
can generate a large number of history records for records it processed but found
unchanged. Enabling **Suppress No-op Logs** prevents Job History Records from
being created for entries that have not changed. This reduces noise in Operations
views for high-volume sources.

Available Plugins
------------------

.. note::

   **About this section**

   In the original v4 documentation, this list was generated automatically from
   a content-by-label macro in Confluence, pulling all pages tagged as External
   Identity Source plugins. We are evaluating the best way to surface this list
   dynamically — or to maintain it — within this Read The Docs site.

   For now, the canonical list of available External Identity Source Plugins is:

   `Available External Identity Source Plugins <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743510/Available+External+Identity+Source+Plugins>`_
   in the Technical Manual.

   The plugins available in Registry v5 are: API Source, Env Source, File Source,
   ORCID Source, and SQL Source.

If none of the available plugins meets your needs, custom plugins can be written.
See
`External Identity Source Plugins (PE) <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743750/External+Identity+Source+Plugins+PE>`_
in the Technical Manual for the technical specification.

Technical Reference
--------------------

.. note::

   **About this section**

   The database tables associated with External Identity Sources were listed in
   the v4 documentation using an automatically generated Confluence macro. We are
   discussing the best approach for surfacing these links in this documentation —
   whether as a manually maintained list, a generated index, or a link to the
   Technical Manual's own reference pages.

   For now, see
   `Registry PE External Identity Sources <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743514/Registry+PE+External+Identity+Sources>`_
   in the Technical Manual for links to the relevant database table documentation.

Changes from v4
----------------

If you are migrating from Registry v4, the following changes apply:

- **Renamed.** Organizational Identity Sources are now called External Identity
  Sources. Organizational Identities are now External Identities.

- **Pipelines are required.** In v4, it was possible to create an Organizational
  Identity without a Pipeline. In v5, every External Identity Source must be
  attached to a Pipeline — it is no longer possible to sync a record without one.

- **Multiple Roles per record.** v5 Pipelines support External Identity Roles,
  meaning a single External Identity record from a source can convey multiple
  Person Roles. See the Pipeline documentation for details.

- **Sync modes changed.** The v4 **Query** mode (matching against verified email
  addresses) and **Sync on Login** are not available in v5. The sync modes in v5
  are Full, Update, Manual, and Disabled.

- **Record Adoption added (v5.1.0).** Administrators can now convert External
  Identities to Registry-native records via adoption.

- **Plugins changed.** Several v4 plugins (LDAP Source, netFORUM Source, Novi
  Source, Salesforce Source) are not available in the v5 plugin library. The v5
  plugins are: API Source, Env Source, File Source, ORCID Source, SQL Source.

- **ePPN generation removed.** The v4 configuration option for automatically
  generating ePPN identifiers from source data is not present in v5. This
  functionality should now be handled via Pipeline attribute mapping or Identifier
  Assignment.

- **CO Group Mappings removed.** The v4 Group Mapping configuration on
  Organizational Identity Sources is not present in v5. Group membership
  assignment from source attributes is now handled through Pipeline configuration.

- **Data Filters.** Registry v4 supported Data Filters on Organizational Identity
  Sources. Check the current Technical Manual for the v5 status of this feature.
