.. DRAFT (Oct 2026): Lesson 2. Published on the Module 2 page (Oct 23).
   Procedure follows the workshop deck's Section 2 and the kit's instructor
   guide, both tested on 5.2.0.
   FORMAT TRIAL (Nov 3): "Steps at a glance" as linked cards, and the "why"
   and edge-case detail in each step folded into dropdowns. If it works,
   carry the pattern to the other lessons.

.. _gs-source-hr-file:

Bring People In from an HR File
===============================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 2, Bring People In · **Learning paths:** Enterprise (Redcurrant
University; any CO from Module 1 works) ·
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
  reads the source, and a **Pipeline** turns each source record into a Person record. See
  :ref:`ec-external-identity-sources` and :ref:`ec-pipelines`.
- What a **flange** is, and why one is needed in this case for people to log in.
- How to test a source with one person before syncing everyone.

Ingredients
-----------

- Completed: :ref:`gs-module-1` (you have created a CO and know its ID)
- Activated plugins (see :ref:`gs-before-you-begin`): **FileConnector** and
  **PipelineToolkit**
- The HR file, ``hr.csv``. It comes with the workshop kit (see
  :ref:`gs-before-you-begin`): it's ``filesource/hr.csv`` in the kit's folder
  on your computer, and Registry sees it as ``/srv/filesource/hr.csv``.
- A terminal in the kit's folder, to sync the whole file at once in step 6.
  (Everything else, including syncing one person at a time, is in the
  browser.)

.. note::

   **Coming from v4?** External Identities were Organizational Identities,
   External Identity Sources were Organizational Identity Sources, and a
   Person was a CO Person.

Steps at a glance
-----------------

Select a card to jump to that step.

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: 1. Prepare
      :link: gs-hr-step-look
      :link-type: ref

      Look at the HR file, and how its data will flow into Registry.

   .. grid-item-card:: 2. Build the pipeline
      :link: gs-hr-step-pipeline
      :link-type: ref
      :img-top: /comanage-files/registry_v5.2/connections/Add_New_PipelineNEW.png
      :img-alt: The Add a New Pipeline form

      Create the pipeline that turns each record into a Person.

   .. grid-item-card:: 3. Add a flange
      :link: gs-hr-step-flange
      :link-type: ref
      :img-top: /comanage-files/registry_v5.2/connections/Pipeline_Flange_Configure_Plugin.png
      :img-alt: A flange's Configure page

      Turn each uid into a login ID.

   .. grid-item-card:: 4. Connect the HR file
      :link: gs-hr-step-source
      :link-type: ref
      :img-top: /comanage-files/registry_v5.2/people/Add_New_External_Identity_SourceNEW.png
      :img-alt: The Add a New External Identity Source form

      Add the file as an External Identity Source.

   .. grid-item-card:: 5. Sync Ruth
      :link: gs-hr-step-ruth
      :link-type: ref
      :img-top: /comanage-files/registry_v5.2/connections/External_Identity_Source_Search.png
      :img-alt: Searching the source for ruth

      Find Ruth in the source, sync her, and log in as her.

   .. grid-item-card:: 6. Sync everyone
      :link: gs-hr-step-sync
      :link-type: ref
      :img-top: /comanage-files/registry_v5.2/connections/FileSource_ID.png
      :img-alt: The source's ID in the address bar

      Run one command to bring in the rest of the file.

Then :ref:`check your work <getting-started/connections/source-hr-file:Check your work>`.

Step details
------------

Each step shows what to do. Select a heading marked ▸ to see why, or what to
do if something looks different.

.. _gs-hr-step-look:

1. Look at the file, and how data will flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each row of ``hr.csv`` represents one person. Its first rows look like this:

.. code-block:: text

   SORID,names.given.official,names.family.official,identifiers.identifier.uid
   f6735933-81cf-4b71-b335-cb659c09eb4a,Ruth,Spence,ruth.spence
   045c03e1-c76c-4638-9151-52c26e23bda5,Rachel,Payne,rachel.payne
   88f9f30f-82ae-4f99-a295-4f5b86281bcd,Vera,Montoya,vera.montoya

The columns are:

- **SORID**: the HR system's own key for the person (its *system of record
  ID*). Registry uses it to recognize the same record on the next sync.
- **Given and family name**
- **uid**: the username HR assigned, such as ``ruth.spence``

.. dropdown:: Where does this file come from?
   :icon: info

   In this lesson the file is ready-made: it stands in for an export from
   Redcurrant's HR system. In your own deployment you would produce this
   file from your system of record and put it where Registry can read it.

   The headers aren't arbitrary: they follow the **CSV v3** format the File
   Source expects. See :ref:`eis-file-source` and the Technical Manual's
   `CSV v3 format <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743557/File+Source+Plugin#FileSourcePlugin-CSVv3>`_.

Data flows in this order:

.. include:: /_snippets/file-source-data-flow.rst

#. The **External Identity Source** reads the file. Each row becomes an
   **External Identity**.
#. The **Pipeline** matches each External Identity to an existing Person, or
   creates a new one.
#. A **flange** on the pipeline adds a login identifier, so the person can
   sign in.

Because the source has to name the pipeline that handles its records, you
build it right to left: the pipeline first, then the source.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`using/external-connections/external-identity-sources/file-source:3. How Data Flows`

.. _gs-hr-step-pipeline:

2. Build the pipeline
~~~~~~~~~~~~~~~~~~~~~

In Redcurrant University, open **Connections > Pipelines** and select
**Add**. Fill in the form, then save.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Field
     - Value
   * - Description
     - ``Process HR File Inputs``
   * - Match Strategy
     - Identifier
   * - Identifier Type
     - UID (appears after you choose the Identifier match strategy)
   * - Person Status On Create
     - Active
   * - Role Status On Delete
     - Expired

.. important::

   **Don't leave Person Status On Create blank.** If it's empty, every
   record the pipeline syncs fails, and the interface doesn't show an error.

.. figure:: /comanage-files/registry_v5.2/connections/Add_New_PipelineNEW.png
   :alt: The Add a New Pipeline form in Redcurrant University
   :width: 100%

   The Add a New Pipeline form.

Saving returns you to the Pipelines list.

.. dropdown:: Why these settings?
   :icon: info

   - **Description** names the pipeline in lists and in the source's
     settings.
   - **Match Strategy: Identifier** matches incoming records to existing
     People by an identifier.
   - **Identifier Type: UID** is the identifier to match on.
   - **Person Status On Create** is the status a new Person gets.
   - **Role Status On Delete** is what happens to a person's role when their
     source record is no longer valid.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ec-pipelines`

.. _gs-hr-step-flange:

3. Add a pipeline flange that turns each uid into a login ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:bdg-success:`New in v5`

A **flange** adds a capability to a pipeline. The **Identifier Mapper**
flange (from PipelineToolkit) copies each person's uid onto their Person
record as a **Login** identifier, so Ruth can sign in as ``ruth.spence``.

.. dropdown:: Why is a flange needed here?
   :icon: info

   The CSV v3 format can't mark an identifier as a login. Without this
   configuration, people from the file sync fine but can't log in.

**Add the flange**

#. In the Pipelines list, select **Process HR File Inputs** to reopen it.
#. Select **Flanges** at the upper right of its edit page, then **Add**.
#. Fill in the form, then save.

.. figure:: /comanage-files/registry_v5.2/connections/Pipeline_Add_a_Flange.png
   :alt: The Edit Process HR File Inputs page, with an arrow pointing to the Flanges link at the upper right
   :width: 100%

   The Flanges link is at the upper right of the saved pipeline's edit page.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Field
     - Value
   * - Description
     - ``Map the UID``
   * - Status
     - Build Related Attributes
   * - Plugin
     - ``PipelineToolkit.IdentifierMappers``

.. dropdown:: Why "Build Related Attributes"?
   :icon: info

   A flange's Status says *where* in the pipeline it acts: Build Person
   Role, Build Related Attributes, or Retrieve External Identity (or
   Disabled). Identifiers are related attributes.

   .. figure:: /comanage-files/registry_v5.2/connections/Pipeline_Flange_Status.png
      :alt: The Add a New Flange form with the Status list open: Disabled, Build Person Role, Build Related Attributes, Retrieve External Identity
      :width: 100%

      The flange's Status list: where in the pipeline the flange acts.

.. dropdown:: Can't find PipelineToolkit.IdentifierMappers in the Plugin list?
   :icon: question

   The PipelineToolkit plugin isn't activated yet. Check this lesson's
   *Ingredients* and activate the plugins it needs (see
   :ref:`gs-before-you-begin`).

**Configure it** (don't skip this part)

Saving the flange opens a page titled **Configure** followed by a number.
It looks empty: the Identifier Mapper has no fields of its own. Its
settings are one click away.

#. Select the small **Login Identifier Types** text at the upper right. It's
   a link.
#. Select **Add**. Choose Type **UID**, tick **Login**, and save.
#. Check that the list shows UID with Login set.

.. figure:: /comanage-files/registry_v5.2/connections/Pipeline_Flange_Configure_Plugin.png
   :alt: A flange's Configure page after saving: a Saved message, the ID and creation date, a collapsible Changelog, and an arrow pointing to the Login Identifier Types link at the upper right
   :width: 100%

   The flange's Configure page. Its settings are behind **Login Identifier
   Types**, at the upper right.

.. dropdown:: Lost this page?
   :icon: question

   You can get back to it: **Connections > Pipelines > Process HR File
   Inputs > Flanges >** your flange **> Configure Plugin**.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ec-pipelines` (Extending Pipelines with Plugins)

.. _gs-hr-step-source:

4. Connect the HR file
~~~~~~~~~~~~~~~~~~~~~~

The source is saved in two parts: first its general properties, then the
File Source plugin's own settings.

Open **Connections > External Identity Sources** and select **Add**.

**Part 1: Properties** (then save)

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Field
     - Value
   * - Description
     - ``HR File``
   * - Status
     - Full
   * - Plugin
     - ``FileConnector.FileSources``
   * - Pipeline
     - Process HR File Inputs
   * - System of Record Label
     - ``hr``

.. important::

   **Set Status to Full.** The form starts at Disabled, and in 5.2.0,
   syncing a Disabled source gives an error.

.. figure:: /comanage-files/registry_v5.2/people/Add_New_External_Identity_SourceNEW.png
   :alt: The Add a New External Identity Source form: Description, Status, Plugin, Pipeline and System of Record Label
   :width: 100%

   Part 1 of the source: its properties. Status starts at Disabled.

**Part 2: Configure Plugin** (then save)

After you save Part 1, the **Configure Plugin** tab opens.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Field
     - Value
   * - File Name
     - ``/srv/filesource/hr.csv``
   * - File Format
     - CSV v3
   * - Archive Directory
     - Leave empty

.. figure:: /comanage-files/registry_v5.2/connections/FileSource_configuration.png
   :alt: The Configure Plugin tab of a File Source: File Name, File Format, Archive Directory, Warning Threshold and Warning Threshold Override
   :width: 100%

   Part 2: the File Source plugin's settings.

.. SCREENSHOT: this capture is of a source named "Test file source"; retake
   with "HR File" if it matters.

.. dropdown:: Why these settings?
   :icon: info

   - **Description** names the source.
   - **Status: Full** lets the source be synced.
   - **Plugin:** ``FileConnector.FileSources`` reads a source that is
     configured as a CSV file.
   - **Pipeline** is the pipeline that handles this source's records.
   - **System of Record Label** is a short label for where these records
     come from.
   - **File Name** is where Registry finds the kit's HR file. This is the
     path *inside* Registry, not on your computer. (In your own deployment,
     it's the file's full path on the Registry server.)
   - **File Format** is the format the file's headers follow.
   - **Archive Directory** lets later syncs compare the file with its
     previous copy, which matters for larger files. You don't need it yet.

.. dropdown:: Can't find FileConnector.FileSources in the Plugin list?
   :icon: question

   The FileConnector plugin isn't activated yet. Check this lesson's
   *Ingredients* and activate the plugins it needs (see
   :ref:`gs-before-you-begin`).

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ec-external-identity-sources`

.. _gs-hr-step-ruth:

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

.. figure:: /comanage-files/registry_v5.2/connections/External_Identity_Source_Search.png
   :alt: The HR File source's Search Source tab, with a search for ruth returning Ruth Spence's Source Key
   :width: 100%

   Searching the source for ruth.

.. figure:: /comanage-files/registry_v5.2/connections/View_External_Identity_Source.png
   :alt: View External Identity Source Record for Ruth Spence: her name, uid ruth.spence and sorid, with an arrow pointing to Sync Record to CO at the upper right
   :width: 100%

   Ruth's record as the file has it. **Sync Record to CO** is at the upper
   right.

Now check that Ruth can log in:

#. Open a browser window that isn't logged in yet: a private window, or a
   second browser (see :ref:`gs-other-people`).
#. Go to https://localhost:8443/registry/ and select **Login**.
#. Type ``ruth.spence`` as the username, and leave the password empty.

Ruth lands in Redcurrant University as herself.

.. dropdown:: Why does this work?
   :icon: info

   Registry lets someone in when the username they sign in with matches one
   of their **Login** identifiers, which is what the flange in step 3 set
   up. (The kit accepts any username; in your own deployment, people sign
   in through your identity provider.)

.. _gs-hr-step-sync:

6. Sync everyone
~~~~~~~~~~~~~~~~

In 5.2.0, syncing a whole file is done from the command line; there's no
button for it in the interface. The command runs a **Sync job** for one
source in one CO. You need two numbers:

- ``<CO ID>``: Redcurrant's number, from ``co_id=`` in the address bar
  (``2`` if Redcurrant was the first CO you created).
- ``<source ID>``: the HR File source's number, which appears in the address
  when you edit it (``external-identity-sources/edit/1``).

.. figure:: /comanage-files/registry_v5.2/connections/FileSource_ID.png
   :alt: Editing the HR File source, with the source's ID highlighted in the browser address bar
   :width: 100%

   Where to find the External Identity Source's ID.

In a terminal, in the kit's ``comanage-pe-workshop`` folder, run **one** of
these. They do the same thing.

.. tab-set::

   .. tab-item:: macOS, Linux, WSL or Git Bash

      The kit's shortcut:

      .. code-block:: bash

         ./workshop sync <CO ID> <source ID>

      For example, ``./workshop sync 2 1``. It prints the full command it
      runs, then runs it.

   .. tab-item:: Windows PowerShell

      The full command (the shortcut isn't available in PowerShell):

      .. code-block:: powershell

         docker compose exec -u www-data -w /srv/comanage-registry/app registry ./bin/cake job -c <CO ID> -j CoreJob.SyncJob -s external_identity_source_id=<source ID>

When it finishes, it reports something like:

.. code-block:: text

   Job 3: OK - Sync Finished (44 new, 0 updated, 0 errors, 45 total)

"44 new" because Ruth is already there. The job number varies. The same
result is in the CO under **Operations > Jobs**.

.. dropdown:: In your own deployment
   :icon: server

   You run the same job on the Registry server, from Registry's ``app``
   folder, as the web server's user:
   ``./bin/cake job -c <CO ID> -j CoreJob.SyncJob -s external_identity_source_id=<source ID>``.
   In production, you'd schedule it (for example with cron).

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ops-jobs`

Check your work
---------------

- **People > My Population** lists 45 people, with Ruth Spence there once.
- Ruth's record has an **External Identities** tab showing her HR record.
- You can sign in as ``ruth.spence`` and land in Redcurrant University. Use
  a private window or a second browser, or log out as the administrator
  first (**My Identity** menu, top right).

Troubleshoot
------------

.. dropdown:: The plugin you need isn't in the Plugin list

   For example ``FileConnector.FileSources`` or
   ``PipelineToolkit.IdentifierMappers``. Its plugin isn't activated. In the
   COmanage CO, open **Configuration > Plugins** and activate the plugins
   listed under *Ingredients*.

.. dropdown:: Every record fails to sync, with no error in the interface

   Check the pipeline's **Person Status On Create**. If it's blank, choose
   Active and sync again.

.. dropdown:: Syncing gives an error about the source

   Check the source's Status. A Disabled source can't be synced in 5.2.0;
   set it to Full.

.. dropdown:: Searching the source finds nothing

   Registry can't read the file. Check the File Name (the full path on the
   Registry server, not your computer) and that the web server's user can
   read the file.

.. dropdown:: Ruth syncs, but logs in to an empty list of COs

   The flange isn't configured. Open its **Login Identifier Types** and add
   UID with Login ticked. Changing the flange doesn't update people who were
   already synced, so sync Ruth again afterward (**Search Source > Sync
   Record to CO**).

.. dropdown:: You removed a row from the file and nothing happened to that person

   In 5.2.0, rows removed from a file aren't processed; the sync logs an
   error for each missing record instead. To show someone leaving, change
   their role's status rather than deleting their row.

What you learned
----------------

- An External Identity Source reads people from a system of record, and a
  Pipeline turns each record into a Person. When you set them up, create the
  pipeline first, because the source has to name it.
- Flanges, new in v5, add capabilities to a pipeline. The Identifier Mapper
  flange makes it possible for the pipeline to turn a source's uid into a
  login identifier.
- Test a source with one record before syncing everyone.

Where to go next
----------------

- Next: :ref:`gs-module-3`, to give Redcurrant University its structure
- Try on your own: add a second source for the registrar file, with File
  Name ``/srv/filesource/registrar.csv``, the same pipeline and the System of
  Record Label ``registrar``, and sync it (for example
  ``./workshop sync 2 2``).
