.. _eis-sql-source:

SQL Source
==========

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

SQL Source loads people into Registry from a **table or view in an external
SQL database**. It is typically used as an ongoing feed: the team that owns a
system of record (such as HR or a student information system) maintains a
table or view in the agreed shape, and Registry queries it on each sync to
create or update an External Identity for each person.

.. list-table:: SQL Source at a glance
   :widths: 35 65
   :stub-columns: 1

   * - Provided by
     - The **SqlConnector** plugin
   * - Plugin location
     - **Available**: a Platform Administrator must activate SqlConnector
       before SQL Source can be used
   * - Activating SqlConnector also enables
     - **SQL Provisioner** (a Provisioner plugin that writes Registry data to
       SQL tables)
   * - Appears in the Plugin menu as
     - ``SqlConnector.SqlSources``
   * - How data flows
     - Registry **queries** the source database through a SQL Server
       definition. It only reads from the source tables.
   * - Also requires
     - A **SQL Server** in Registry's Server list (see :ref:`ec-servers`)
   * - Sync modes (the **Status** field)
     - Full, Update, Manual (and Disabled)
   * - Manual search
     - Yes (see :ref:`Searching and Syncing <eis-sql-source-search>`, below)
   * - Available since
     - v5.0.0

.. REVIEW: confirm the dropdown label above matches the UI.

1. When to Use SQL Source
-------------------------

SQL Source suits situations where:

- your system of record can expose a table or view (or a copy of one) that
  Registry is allowed to read;
- you want Registry to stay in step with that system on a regular schedule;
- you'd rather not manage exports and file transfers.

For a one-time initial load, or where database access isn't possible,
:ref:`File Source <eis-file-source>` may be simpler. If the source needs to
send changes as they happen, consider :ref:`API Source <eis-api-source>`.

2. Enabling SQL Source
----------------------

SQL Source is not available until its plugin package is activated.

1. As a Platform Administrator, go to **COmanage CO > Configuration > Plugins**
   (see :ref:`extend-plugins`).
2. Find **SqlConnector** and activate it.

.. REVIEW: screenshot of the SqlConnector row in the Plugins list
   (for example, configuration/plugin_activate_SqlConnector.png).

**ABOUT SqlConnector**: SqlConnector is a package containing two plugins.
Activating it makes both **SQL Source** and **SQL Provisioner** available.
Activation creates no configuration of either one; nothing reads from or
writes to a database until an administrator sets up a source or a
provisioning target.

.. note::

   The Plugins list shows package names (SqlConnector), not the plugins
   inside them (SQL Source). This page and the plugin catalog on
   :ref:`extend-plugins` map one to the other.

3. How Data Flows
-----------------

.. code-block:: text

   System of record ──maintains──▶ Source table or view (external database)
                                        │
                           SQL Server definition (connection)
                                        │
                              Sync Job or manual sync
                                        ▼
                     External Identity Source (SQL Source)
                                        │
                                     Pipeline
                                        ▼
                         Person record and Person Roles

- **Registry connects with its own database account.** The account defined
  in the SQL Server needs read access to the source tables or views.
- **The data can be shaped two ways** (the *Table Mode*):

  - **Flat**: one table, one row per person (or per role), with at most one
    value for each attribute, such as one email address. Simpler to set up.
  - **Relational**: a primary table plus related tables
    (``<table>_names``, ``<table>_roles``, ``<table>_email_addresses`` and
    so on) that allow several values per attribute. Use this when people
    have more than one name, email address or identifier to bring in.

- **Each person is identified by a unique** ``source_key`` (the Source Key).
- **Types come from the configuration in Flat mode** (one default type for
  each attribute) and **from the data in Relational mode** (each related
  row has its own ``type`` column).
- **Change detection matters.** If the source table has a ``modified``
  timestamp column, each sync only processes rows that changed since the
  last one. Without it, Registry compares every record on every sync, which
  is slower but may be fine for small populations.
- **The Pipeline does the rest**: matching records to existing people,
  mapping attributes and creating Person Roles. See :ref:`ec-pipelines`.

4. Configuring SQL Source
-------------------------

Before you start:

- make sure a suitable Pipeline exists (:ref:`ec-pipelines`);
- add a **SQL Server** for the source database if there isn't one already
  (:ref:`ec-servers`). PostgreSQL, MariaDB and MySQL are fully supported;
  other database types may work but are not regularly tested;
- make sure the source table or view exists and the database account can
  read it.

Then:

1. Add a new External Identity Source as described in
   :ref:`ec-external-identity-sources`, selecting ``SqlConnector.SqlSources``
   as the Plugin.
2. Save. The SQL Source settings appear next.

.. REVIEW: screenshot of the SQL Source configuration form
   (for example, connections/SqlSource_configuration.png).

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Setting
     - What to decide
   * - **Server** \*
     - The SQL Server that connects to the source database.
   * - **Table Mode** \*
     - **Flat** or **Relational** (see above).
   * - **Source Table** \*
     - The exact name of the table or view to query. In Relational mode,
       this is the primary table; the related tables must be named after
       it (``<table>_names`` and so on).
   * - **Address Type**, **Email Address Type**, **Identifier Type**,
       **Name Type**, **Pronouns Type**, **Telephone Number Type**,
       **URL Type**
     - The type given to each value brought in, for example whether an email
       address is *Official* or *Personal*. Required in Flat mode, where the
       data has no type columns; not used in Relational mode.
   * - **Check Threshold**
     - Optional safety check, entered as a percentage. If this percentage
       of records (or more) has changed since the last sync, a Full sync stops
       with an error instead of processing them. This protects against a
       truncated or wrong data set. Only works when the source table has a
       ``modified`` column; otherwise the check is skipped.
   * - **Threshold Override**
     - Lets the next sync go ahead despite the threshold, for example after
       a planned bulk change. It clears itself afterwards.

\* *Required*

.. REVIEW: confirm in the UI which fields show the red required asterisk.
   (The code requires Server, Table Mode and Source Table, and the type
   fields in Flat mode only.)

**Things to plan for**

- **Removing a row isn't detected by timestamps.** If ``modified`` is used
  for change detection, a deleted row has no timestamp to notice. Either
  mark loss of eligibility with ``valid_through`` instead of deleting the
  row, or periodically run a full sync that processes every record (the
  Sync Job's force option).
- **In Relational mode, the threshold counts each changed row in each
  table**, so the percentage can exceed 100. Choose the value with that in
  mind.
- **Index the source tables** on ``source_key``, names, email address,
  identifier and ``modified`` for larger populations. This keeps syncs and
  searches fast.
- **A "Table not found" error usually means a permissions problem**: the
  database account can't see the table.

.. REVIEW: confirm with developers what Registry does in Full mode when a
   source_key disappears from the source table (same question as File Source).

5. Preparing the Source Data
----------------------------

The source tables can be physical tables, views or materialized views, as
long as they match the column layout Registry expects. In outline:

- every row has a unique integer ``id`` and a ``source_key``;
- in Flat mode, several rows can share a ``source_key`` to describe several
  roles for one person;
- any Flat-mode column whose name starts with ``a_`` (for example,
  ``a_favorite_color``) becomes an Ad Hoc Attribute;
- in Relational mode, only the ``_names`` and ``_roles`` tables are
  required; other related tables are used if present.

If you're preparing the tables or views, work from the
`table definitions <https://spaces.at.internet2.edu/spaces/COmanage/pages/305856976/SQL+Source+Plugin>`_
in the Technical Manual. They list every column, its type, which values are
required, and how multiple roles are handled.

.. _eis-sql-source-search:

6. Searching and Syncing
------------------------

All of the sync modes on :ref:`ec-external-identity-sources` apply to SQL
Source.

When you use **Search Source**, SQL Source looks for what you typed in
several columns at once:

- **Source Key and identifiers**: exact match only;
- **email address**: exact match, ignoring case;
- **names** (and, in Flat mode, other text columns): partial matches are
  returned.

7. Related: SQL Provisioner
---------------------------

The same SqlConnector package provides **SQL Provisioner**, which writes
Registry records out to tables in a SQL database. It's configured
separately, as a provisioning target. See :ref:`ec-provisioning`.

8. Technical Reference
----------------------

For the full table definitions, change-detection details and
troubleshooting, see
`SQL Source Plugin <https://spaces.at.internet2.edu/spaces/COmanage/pages/305856976/SQL+Source+Plugin>`_
in the Technical Manual.

9. Changes from v4
------------------

- **Several columns were renamed**: ``sorid`` is now ``source_key``, ``o``
  is now ``organization`` and ``ou`` is now ``department``.
- **Multiple roles per person** are supported in both Flat and Relational
  modes. In Relational mode, many attributes moved from the primary table
  to the new ``_roles`` table.
- **Ad Hoc Attributes in Flat mode** must now be prefixed ``a_``.
  Previously, any extra column was treated as one.
- **Preferred pronouns** can be brought in.
- **Check Threshold** is new.
- **Primary names and login identifiers can no longer be set in the source
  data.** Both still exist in v5, but they are now attributes of the Person
  record rather than of External Identities.
