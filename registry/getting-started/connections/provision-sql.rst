.. DRAFT (Oct 2026): Lesson 6b. Unpublished (listed in UNVERIFIED in conf.py).
   Procedure follows the kit's instructor guide ("Provisioning: SQL
   Provisioner"), verified on 5.2.0 against the kit's PostgreSQL target
   database.

.. _gs-provision-sql:

Send Changes to a Database
==========================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 6, Provisioning · **Learning paths:** Enterprise (Redcurrant
University) · **Features section:** :ref:`ec-provisioning` ·
**Registry:** v5.2.0

The scenario
------------

Redcurrant's campus applications read user information from a shared
database. You want Registry to keep that database up to date, so the
applications always see current people, roles and groups.

What you'll learn
-----------------

- How a **Server** record lets Registry connect to another system. See
  :ref:`ec-servers`.
- What the **SQL Provisioner** creates in the target database, and what it
  writes there.

Ingredients
-----------

- Completed: :ref:`gs-provision-file` (you know how provisioning targets and
  modes work)
- **SqlConnector** activated (see :ref:`gs-before-you-begin`)
- A database Registry can reach and write to, for example PostgreSQL, with
  its host name, database name, username and password. The provisioner
  creates its own tables there.
- A way to query that database (for example ``psql``)

Steps at a glance
-----------------

#. Configure: describe the database as a Server
#. Configure: create the target, Disabled
#. Enable: switch it to Immediate
#. Use: change Ruth, and look in the database
#. Check your work

Step details
------------

1. Describe the database as a Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open **Connections**, then **Servers** under Related Configurations (it's
also under **Configuration > Servers**), and select **Add a New Server**:
Description ``Target Database``, Status Active, Plugin
``CoreServer.SqlServers``. Save, then fill in the SQL server's form:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Field
     - Example
     - Notes
   * - RDBMS Type
     - Postgres
     - The kind of database.
   * - Hostname
     - your database's host name
     - As Registry sees it.
   * - Port
     - leave empty for the default
     -
   * - Database Name
     - your database's name
     -
   * - Username / Password
     - an account that can create tables
     - The provisioner creates its tables when you save it.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ec-servers` (SQL Servers)

2. Create the target, Disabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open **Connections > Provisioning Targets** and select **Add a New
Provisioning Target**: Description ``SQL Export``, Provisioning Mode
**Disabled**, Plugin ``SqlConnector.SqlProvisioners``. Save. In the SQL
Provisioner's form, choose Server **Target Database**, keep the Table Name
Prefix ``sp_``, and save.

Saving creates the provisioner's tables in the target database (such as
``sp_people``, ``sp_names``, ``sp_identifiers``, ``sp_person_roles``,
``sp_groups`` and ``sp_group_members``) and copies reference data such as
Types, COUs and Groups. The **Configure Plugin** tab also has **Reapply
Target Database Schema** and **Resync Reference Data**, for later.

3. Switch it to Immediate
~~~~~~~~~~~~~~~~~~~~~~~~~

On the target's **Properties** tab, set **Provisioning Mode** to
**Immediate** and save.

4. Change Ruth, and look in the database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Change one of Ruth Spence's role titles, as in :ref:`gs-provision-file`.
Then query the target database. For example, in PostgreSQL:

.. code-block:: sql

   select p.id, p.status, n.given, n.family, i.identifier as login, r.title
   from sp_people p
   join sp_names n on n.person_id = p.id and n.primary_name
   left join sp_identifiers i on i.person_id = p.id and i.login
   left join sp_person_roles r on r.person_id = p.id
   order by n.family, n.given limit 5;

The ``sp_`` IDs are Registry's own IDs. People from the HR file have two
names in ``sp_names``, just as in Registry: their primary name, and the copy
attached to their HR record.

As with the file, people who were already there go out when they change,
or with **Provision Now** or **Reprovision All** (see
:ref:`gs-provision-file`, step 5). Provision Now shows Last Comment "New
record published".

Check your work
---------------

- **Connections > Provisioning Targets** lists SQL Export, Immediate.
- The target database has the ``sp_`` tables, and Ruth's latest title
  appears in ``sp_person_roles``.

Troubleshoot
------------

**Saving the SQL Provisioner fails.** Registry can't reach or write to the
database. Check the Server's host name, database name and credentials, and
that the account can create tables.

**Every save of a person fails with an error page.** The target was switched
on before its plugin form was saved. See :ref:`gs-provision-file`,
Troubleshoot.

**A person has two names in the database.** That's expected for people from
a source: their primary name, and the copy attached to their source record.

What you learned
----------------

- A Server record holds the connection details another plugin uses.
- The SQL Provisioner creates its own tables and keeps them current.

Where to go next
----------------

- Next: :ref:`gs-module-8`, to run and monitor jobs
- Try on your own: expire one of Ruth's roles and look at how
  ``sp_person_roles`` changes.
