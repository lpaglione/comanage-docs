.. DRAFT (Oct 2026): Lesson 2. Unpublished (listed in UNVERIFIED in conf.py).
   Procedure follows the workshop deck's Section 2 and the kit's instructor
   guide, both tested on 5.2.0. Screenshots for the flange pages and the
   source's Search tab are still TODO (the deck's images aren't in
   comanage-files).

.. _gs-source-hr-file:

Bring People In from an HR File
===============================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 2, Bring People In · **Sample org:** Redcurrant University ·
**Features section:** :ref:`using-external-connections` · **Registry:** v5.2.0

The scenario
------------

Redcurrant University's HR office can export its staff list as a file. You
want Registry to read that file, create a Person for everyone in it, and let
those people log in with the username HR assigned them. Your first test
subject is Ruth Spence, who will help you administer Redcurrant in later
lessons.

What you'll learn
-----------------

- How data gets from a source into Registry: an **External Identity Source**
  reads the source, and a **Pipeline** turns each record into a Person. See
  :ref:`ec-external-identity-sources` and :ref:`ec-pipelines`.
- What a **flange** is, and why this one is needed for people to log in.
- How to test a source with one person before syncing everyone.

Ingredients
-----------

- Completed: :ref:`gs-module-1` (Redcurrant University exists, and you know
  its CO ID)
- Activated plugins (see :ref:`gs-before-you-begin`): **FileConnector** and
  **PipelineToolkit**
- The HR file, ``hr.csv``, placed **on the Registry server** where Registry
  can read it. Its first rows look like this:

  .. code-block:: text

     SORID,names.given.official,names.family.official,identifiers.identifier.uid
     f6735933-81cf-4b71-b335-cb659c09eb4a,Ruth,Spence,ruth.spence
     045c03e1-c76c-4638-9151-52c26e23bda5,Rachel,Payne,rachel.payne
     88f9f30f-82ae-4f99-a295-4f5b86281bcd,Vera,Montoya,vera.montoya

  .. REVIEW: link the full 45-person hr.csv once its public home is settled
     (it's in the workshop kit, filesource/hr.csv).

- To sync the whole file at once: command-line access to the Registry
  server. (You can do everything else, including syncing one person at a
  time, in the browser.)

.. note::

   **Coming from v4?** External Identities were Organizational Identities,
   External Identity Sources were Organizational Identity Sources, and a
   Person was a CO Person.

Steps at a glance
-----------------

#. Prepare: look at the file, and how data will flow
#. Configure: build the pipeline
#. Configure: add a flange that turns each uid into a login
#. Enable: connect the HR file as an External Identity Source
#. Use: find Ruth in the source and sync her
#. Use: sync everyone
#. Check your work

Step details
------------

1. Look at the file, and how data will flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each row of ``hr.csv`` is one person. The columns are:

- **SORID**: the HR system's own key for the person (its *system of record
  ID*). Registry uses it to recognize the same record on the next sync.
- **Given and family name**
- **uid**: the username HR assigned, such as ``ruth.spence``

The headers aren't arbitrary: they follow the **CSV v3** format the File
Source expects.

Data flows in this order:

#. The **External Identity Source** reads the file. Each row becomes an
   **External Identity**.
#. The **Pipeline** matches each External Identity to an existing Person, or
   creates a new one.
#. A **flange** on the pipeline adds a login identifier, so the person can
   sign in.

Because the source has to name the pipeline that handles its records, you
build it right to left: the pipeline first, then the source.

2. Build the pipeline
~~~~~~~~~~~~~~~~~~~~~

In Redcurrant University, open **Connections > Pipelines** and select
**Add**. Fill in the form, then save.

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Field
     - Value
     - Why
   * - Description
     - ``Process HR File Inputs``
     - Names the pipeline in lists and in the source's settings.
   * - Match Strategy
     - Identifier
     - Matches incoming records to existing People by an identifier.
   * - Identifier Type
     - UID
     - The identifier to match on. This field appears only after you choose
       the Identifier match strategy.
   * - Person Status On Create
     - Active
     - The status a new Person gets. **Don't leave this blank**: if it's
       empty, every record the pipeline syncs fails, and the interface
       doesn't show an error.
   * - Role Status On Delete
     - Expired
     - What happens to a person's role when their source record is no
       longer valid.

.. figure:: /comanage-files/registry_v5.2/connections/Add_New_PipelineNEW.png
   :alt: The Add a New Pipeline form in Redcurrant University
   :width: 100%

   The Add a New Pipeline form.

Saving returns you to the Pipelines list.

.. seealso::

   User guide: :ref:`ec-pipelines`

3. Add a flange that turns each uid into a login
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:bdg-success:`New in v5`

A **flange** plugs an extra step into a pipeline. You need one here because
the CSV v3 format can't mark an identifier as a login. Without a flange,
people from the file sync fine but can't log in.

The **Identifier Mapper** flange (from PipelineToolkit) copies each person's
uid onto their Person record and marks it as a **Login** identifier, so Ruth
can sign in as ``ruth.spence``.

**Add the flange**

#. In the Pipelines list, select **Process HR File Inputs** to reopen it.
#. Select **Flanges** at the upper right of its edit page, then **Add**.
#. Fill in the form, then save.

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Field
     - Value
     - Why
   * - Description
     - ``Map the UID``
     - Names the flange.
   * - Status
     - Build Related Attributes
     - A flange's Status says *where* in the pipeline it acts: Build Person
       Role, Build Related Attributes, or Retrieve External Identity (or
       Disabled). Identifiers are related attributes.
   * - Plugin
     - ``PipelineToolkit.IdentifierMappers``
     - The plugin that does the work.

.. TODO screenshot: the pipeline's edit page with the Flanges link at the
   upper right, and the Add a New Flange form with the Status list open.

**Configure it** (don't skip this part)

Saving the flange opens a page titled **Configure** followed by a number.
It looks empty: the Identifier Mapper has no fields of its own. Its
settings are one click away.

#. Select the small **Login Identifier Types** text at the upper right. It's
   a link.
#. Select **Add**. Choose Type **UID**, tick **Login**, and save.
#. Check that the list shows UID with Login set.

If you lose this page, you can get back to it: **Connections > Pipelines >
Process HR File Inputs > Flanges >** your flange **> Configure Plugin**.

.. TODO screenshot: the flange's Configure page, with the Login Identifier
   Types link at the upper right.

.. note::

   The number after "Configure" is the flange's record ID, not its name, so
   yours may differ.

.. seealso::

   User guide: :ref:`ec-pipelines` (Extending Pipelines with Plugins)

4. Connect the HR file
~~~~~~~~~~~~~~~~~~~~~~

The source is saved in two parts: first its general properties, then the
File Source plugin's own settings.

Open **Connections > External Identity Sources** and select **Add**.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Field
     - Value
     - Why
   * - **Part 1: Properties**
     - *then save*
     -
   * - Description
     - ``HR File``
     - Names the source.
   * - Status
     - Full
     - Lets the source be synced. The form starts at Disabled; in 5.2.0,
       syncing a Disabled source gives an error.
   * - Plugin
     - ``FileConnector.FileSources``
     - Reads a CSV file.
   * - Pipeline
     - Process HR File Inputs
     - The pipeline that handles this source's records.
   * - System of Record Label
     - ``hr``
     - A short label for where these records come from.
   * - **Part 2: Configure Plugin**
     - *then save*
     -
   * - File Name
     - The file's full path **on the Registry server**, for example
       ``/srv/filesource/hr.csv``
     - Registry reads the file where it runs, not from your computer.
   * - File Format
     - CSV v3
     - The format the file's headers follow.

Leave Archive Directory empty for now. (It lets later syncs compare the file
with its previous copy, which matters for larger files.)

.. figure:: /comanage-files/registry_v5.2/people/Add_New_External_Identity_SourceNEW.png
   :alt: The Add a New External Identity Source form: Description, Status, Plugin, Pipeline and System of Record Label
   :width: 100%

   Part 1 of the source: its properties. Status starts at Disabled.

After you save Part 1, the **Configure Plugin** tab opens for Part 2.

.. seealso::

   User guide: :ref:`ec-external-identity-sources`

5. Find Ruth in the source and sync her
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test the connection with one person before bringing in everyone.

#. Open the **HR File** source and its **Search Source** tab.
#. Search for ``ruth``. Searching reads the file directly, so a result means
   Registry can read it.
#. Select Ruth's Source Key to see her record exactly as the file has it,
   including the identifiers the pipeline will use (her uid and SORID).
#. Select **Sync Record to CO** at the upper right. Registry runs Ruth's
   record through the pipeline and confirms that the sync is complete.

.. TODO screenshot: the Search Source tab with a result for ruth, and Ruth's
   source record with Sync Record to CO at the upper right.

Now check that Ruth can log in. In a browser window that isn't logged in
yet (see :ref:`gs-before-you-begin`), sign in as ``ruth.spence``. She should
land in Redcurrant University as herself.

.. note::

   How "sign in as ruth.spence" works depends on how your environment
   authenticates people. Registry lets someone in when the username they
   sign in with matches one of their **Login** identifiers. In a test
   environment that accepts any username, typing ``ruth.spence`` is enough.

6. Sync everyone
~~~~~~~~~~~~~~~~

In 5.2.0, syncing a whole file is done from the command line on the Registry
server; there's no button for it in the interface. The command runs a **Sync
job** for one source in one CO. Run it from Registry's ``app`` folder, as
the web server's user:

.. code-block:: bash

   ./bin/cake job -c <CO ID> -j CoreJob.SyncJob -s external_identity_source_id=<source ID>

- ``<CO ID>`` is Redcurrant's number, from ``co_id=`` in the address bar.
- ``<source ID>`` is the HR File source's number, which appears in the
  address when you edit it (``external-identity-sources/edit/1``).

If Registry runs in a container, you run the same command inside it, for
example with ``docker compose exec``.

.. REVIEW: confirm the web server user (www-data in the official images) and
   whether to show the full docker compose form here or link to an
   installation page.

When it finishes, it reports something like:

.. code-block:: text

   Job 3: OK - Sync Finished (44 new, 0 updated, 0 errors, 45 total)

"44 new" because Ruth is already there. The job number varies. The same
result is in the CO under **Operations > Jobs**.

.. seealso::

   User guide: :ref:`ops-jobs`

Check your work
---------------

- **People > My Population** lists 45 people, with Ruth Spence there once.
- Ruth's record has an **External Identities** tab showing her HR record.
- You can sign in as ``ruth.spence`` and land in Redcurrant University.

Troubleshoot
------------

**Every record fails to sync, with no error in the interface.** Check the
pipeline's **Person Status On Create**. If it's blank, choose Active and
sync again.

**Syncing gives an error about the source.** Check the source's Status. A
Disabled source can't be synced in 5.2.0; set it to Full.

**Searching the source finds nothing.** Registry can't read the file. Check
the File Name (the full path on the Registry server, not your computer) and
that the web server's user can read the file.

**Ruth syncs, but logs in to an empty list of COs.** The flange isn't
configured. Open its **Login Identifier Types** and add UID with Login
ticked. Changing the flange doesn't update people who were already synced,
so sync Ruth again afterward (**Search Source > Sync Record to CO**).

**You removed a row from the file and nothing happened to that person.** In
5.2.0, rows removed from a file aren't processed; the sync logs an error for
each missing record instead. To show someone leaving, change their role's
status rather than deleting their row.

What you learned
----------------

- An External Identity Source reads people from a system of record, and a
  Pipeline turns each record into a Person. The pipeline comes first.
- Flanges, new in v5, add steps to a pipeline. The Identifier Mapper turns a
  source's uid into a login identifier.
- Test a source with one record before syncing everyone.

Where to go next
----------------

- Next: :ref:`gs-module-3`, to give Redcurrant University its structure
- Try on your own: add a second source for a registrar file, with the same
  pipeline and the System of Record Label ``registrar``, and sync it.
