.. _eis-file-source:

File Source
===========

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

File Source loads people into Registry from a **CSV file** on the Registry
server. It is most often used for an **initial load**: bringing an existing
population into Registry in one pass when a deployment starts. It can also
serve as an ongoing feed, where another system (such as an HR or student
information system) exports the file on a schedule and Registry reads it
during each sync. Either way, Registry creates or updates an External
Identity for each row.

.. list-table:: File Source at a glance
   :widths: 35 65
   :stub-columns: 1

   * - Provided by
     - The **FileConnector** plugin
   * - Plugin location
     - **Available**: a Platform Administrator must activate FileConnector
       before File Source can be used
   * - Activating FileConnector also enables
     - **File Provisioner** (a Provisioner plugin that writes Registry data to
       a file)
   * - Appears in the Plugin menu as
     - ``FileConnector.FileSources``
   * - How data flows
     - Registry **reads** a file from its own filesystem. Nothing is sent to
       the source system.
   * - Sync modes (the **Status** field)
     - Full, Update, Manual (and Disabled)
   * - Manual search
     - Yes, by exact value (see :ref:`Searching and Syncing <eis-file-source-search>`, below)
   * - Available since
     - v5.0.0. Archive Directory and Warning Threshold were added in v5.2.0.

1. When to Use File Source
--------------------------

File Source suits situations where:

- you're loading an initial population into Registry, and the data is easiest
  to assemble as a spreadsheet or a one-time export;
- your system of record can produce a regular export (nightly, hourly), but
  you can't or don't want to give Registry direct database or API access to it;
- you want a simple, inspectable hand-off: the file *is* the record of what
  was sent.

For an ongoing feed, other sources may fit better. If the source can expose a
database table or view, :ref:`SQL Source <eis-sql-source>` avoids the
file-transfer step. If the source needs to send changes as they happen,
consider :ref:`API Source <eis-api-source>`.

2. Enabling File Source
-----------------------

File Source is not available until its plugin package is activated.

1. As a Platform Administrator, go to **COmanage CO > Configuration > Plugins**
   (see :ref:`extend-plugins`).
2. Find **FileConnector** and activate it.

    .. figure:: /comanage-files/registry_v5.2/configuration/plugin_activate_FileConnector.png
       :alt: Screen shot of selecting the activation for the FileConnector plugin
             Click "Activate" from the gear menu for the FileConnector Plugin.
       :width: 100%

**ABOUT FileConnector**: FileConnector is a package containing two plugins. Activating it makes both
**File Source** and **File Provisioner** available. Activation creates no
configuration of either one; nothing reads or writes files until an
administrator sets up a source or a provisioning target.

.. note::

   The Plugins list shows package names (FileConnector), not the plugins
   inside them (File Source). This page and the plugin catalog on
   :ref:`extend-plugins` map one to the other.

3. How Data Flows
-----------------

.. code-block:: text

   System of record ──export──▶ CSV file on the Registry server
                                        │
                              Sync Job or manual sync
                                        ▼
                     External Identity Source (File Source)
                                        │
                                     Pipeline
                                        ▼
                         Person record and Person Roles

- **Getting the file onto the server is up to you.** Registry reads a path on
  its own filesystem; it doesn't fetch files from elsewhere. Most deployments
  use a scheduled export plus a file transfer (for example, SFTP) or a shared
  volume.
- **Each row is one person** from the source, identified by a unique
  **SORID** (the Source Key) in the first column.
- **A row can carry** names, email addresses, identifiers, telephone numbers,
  addresses, URLs, date of birth, ad hoc attributes and one or more roles
  (affiliation, title, department, organization, validity dates and so on).
- **Types travel in the file.** Unlike some other sources, File Source has no
  default-type settings. Each column header names the type (for example,
  ``email_addresses.mail.official``), using the type's *Database Value*.
- **The Pipeline does the rest**: matching rows to existing people, mapping
  attributes and creating Person Roles. See :ref:`ec-pipelines`.

.. REVIEW: confirm what happens in Full mode when a SORID disappears from the file
   (open question 5 in the fact sheet) and describe it here.

4. Configuring File Source
--------------------------

Before you start, make sure a suitable Pipeline exists (:ref:`ec-pipelines`),
and that the file is already in place on the Registry server and readable by
the web server account Registry runs as.

1. Add a new External Identity Source as described in
   :ref:`ec-external-identity-sources`, selecting ``FileConnector.FileSources``
   as the Plugin.
2. Save. The File Source settings appear next.

    .. figure:: /comanage-files/registry_v5.2/connections/FileSource_configuration.png
       :alt: Screen shot of the FileSource plugin configuration page
             Configure the FileSources plugin.
       :width: 100%

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Setting
     - What to decide
   * - **File Name** \*
     - The full path to the CSV file (must start with ``/``). The file must
       already exist and be readable.
   * - **File Format** \*
     - CSV v3 is currently the only format.
   * - **Archive Directory**
     - Optional, but recommended for files with more than a few hundred
       records. Registry keeps the last two copies of the file here so it
       can work out which rows changed, which makes syncs much faster. The
       directory must be writable.
   * - **Warning Threshold**
     - Optional safety check, entered as a percentage (0–100). If more than
       this percentage of rows have changed since the last sync (counting
       new and removed rows), processing stops before any records are
       touched, and the job reports an error. This protects against a
       truncated or wrong file. Requires an Archive Directory: if a
       threshold is set without one, syncs fail with an error.
   * - **Warning Threshold Override**
     - Lets the next Full sync go ahead despite the threshold, for example
       after a planned bulk change. It clears itself afterwards.

\* *Required*

**Things to plan for**

- **The first sync after adding an Archive Directory reprocesses every
  record**, because there's no earlier copy to compare against. For large
  files, the Technical Manual describes how to seed the archive and avoid
  this.
- **Don't share an Archive Directory** between two File Sources that read
  files with the same name.
- **The Warning Threshold is skipped** the first time a file is processed.

5. Preparing the File
---------------------

The file must be in **CSV v3** format. In outline:

- The first line is a header row naming the columns; each following line is
  one person.
- The first column is always ``SORID``.
- Column names say where each value goes in Registry, including its type and,
  for role attributes, which role it belongs to.

If you're preparing a file, work from the
`CSV v3 specification <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743557/File+Source+Plugin#FileSourcePlugin-CSVv3>`_
in the Technical Manual. It covers the column-naming rules, role keys, date
formats, how CSV parsing edge cases are handled, and example files.

.. REVIEW: confirm the #FileSourcePlugin-CSVv3 anchor resolves on the wiki
   (it follows Confluence's usual heading-anchor pattern, but is unverified).

.. _eis-file-source-search:

6. Searching and Syncing
------------------------

All of the sync modes on :ref:`ec-external-identity-sources` apply to File
Source.

When you use **Search Source**, File Source returns rows where *any* column
exactly matches what you typed (ignoring case). Search for a complete value,
such as a SORID or a full email address; partial matches are not returned.

7. Related: File Provisioner
----------------------------

The same FileConnector package provides **File Provisioner**, which writes
Registry records out to a file. It's configured separately, as a provisioning
target. See :ref:`ec-provisioning`.

8. Technical Reference
----------------------

For field-level detail, the complete CSV v3 specification and example files,
see
`File Source Plugin <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743557/File+Source+Plugin>`_
in the Technical Manual.

9. Changes from v4
------------------

- **CSV v3 is the only supported format.** Files in CSV v1 or v2 need
  converting: model names are now plural with underscores
  (``email_addresses``, not ``EmailAddress``), most former Org Identity
  attributes now belong to roles, and types use Database Values. CSV v1 files
  also need a header row added.
- **Login identifiers and primary names can no longer be set in the file.**
  Both still exist in v5, but they are now attributes of the Person record
  rather than of External Identities, so a source can't assert them.
- **Duplicate SORIDs** no longer cause an error; the first matching row is
  used. (Each SORID should still appear only once.)
- **Search is free-form** rather than field by field.
