.. DRAFT (Oct 2026): Lesson 6a. Unpublished (listed in UNVERIFIED in conf.py).
   Procedure follows the kit's instructor guide ("Provisioning: File
   Provisioner"), verified on 5.2.0 in Redcurrant University.

.. _gs-provision-file:

Send Changes to a File
======================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 6, Provisioning · **Learning paths:** Enterprise (Redcurrant
University) · **Features section:** :ref:`ec-provisioning` ·
**Registry:** v5.2.0

The scenario
------------

Several of Redcurrant's services want to know when someone joins, changes
jobs or leaves. Before connecting a real system, you'd like to see exactly
what Registry sends, and when. A **File Provisioner** writes each change to
a file on the server, so you can watch it happen.

What you'll learn
-----------------

- What a **Provisioning Target** is, and how its **Provisioning Mode**
  decides when changes go out. See :ref:`ec-provisioning`.
- What Registry sends about a person, and when.
- How to send people who were already in Registry before the target existed.

Ingredients
-----------

- Completed: :ref:`gs-module-2` (people in Redcurrant University, including
  Ruth Spence). :ref:`gs-module-3` makes the role changes more interesting,
  but it's optional.
- **FileConnector** activated (you did this for Module 2)
- A file on the Registry server that the web server's user can write to, for
  example ``/srv/provisioned/output.jsonl``. Registry won't create it: a
  file that doesn't exist is refused as "not writable".
- A way to look at that file as it changes (for example ``tail -f`` on the
  server)
- For sending everyone at once (step 5): command-line access to the Registry
  server

Steps at a glance
-----------------

Select a card to jump to that step.

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: 1. Create the target
      :link: gs-pfile-step-create
      :link-type: ref

      Create the provisioning target, Disabled.

   .. grid-item-card:: 2. Set the file
      :link: gs-pfile-step-file
      :link-type: ref

      Tell it which file to write to.

   .. grid-item-card:: 3. Switch it on
      :link: gs-pfile-step-on
      :link-type: ref

      Set the target to Immediate.

   .. grid-item-card:: 4. Change Ruth
      :link: gs-pfile-step-ruth
      :link-type: ref

      Make a change, and watch the file.

   .. grid-item-card:: 5. Send everyone
      :link: gs-pfile-step-all
      :link-type: ref

      Send people who were already there.

Then :ref:`check your work <getting-started/connections/provision-file:Check your work>`.

Step details
------------

Each step shows what to do. Select a heading marked ▸ to see why, or what to
do if something looks different.

.. _gs-pfile-step-create:

1. Create the target, Disabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open **Connections > Provisioning Targets** and select **Add a New
Provisioning Target**.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Field
     - Value
   * - Description
     - ``File Export``
   * - Provisioning Mode
     - **Disabled**
   * - Plugin
     - ``FileConnector.FileProvisioners``

.. dropdown:: Why these settings?
   :icon: info

   - **Description**: Names the target.
   - **Provisioning Mode**: Start disabled and switch on once it's
     configured (see the warning below).
   - **Plugin**: Writes changes to a file.

Leave the rest as it is and save.

.. warning::

   Always create a target as **Disabled** and configure its plugin before
   switching it on. The default mode is Queue on Error. In 5.2.0, a target in
   any mode except Disabled whose plugin form was never saved makes **every
   save of a person in the CO fail** with an error page, until the target is
   fixed or deleted.

.. SCREENSHOT: the Add a New Provisioning Target form (not yet in
   comanage-files).

.. _gs-pfile-step-file:

2. Set the file
~~~~~~~~~~~~~~~

Saving opens the File Provisioner's form. It has one field, **File Name**:
enter the full path of the file on the Registry server, for example
``/srv/provisioned/output.jsonl``, and save.

.. _gs-pfile-step-on:

3. Switch the target to Immediate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the target's **Properties** tab, set **Provisioning Mode** to
**Immediate** and save. Immediate sends each change as it happens.
Switching it on doesn't write anything by itself.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ec-provisioning` (Provisioning Modes)

.. _gs-pfile-step-ruth:

4. Change Ruth, and watch the file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Watch the file on the server, then make a change in Registry:

#. Open Ruth Spence's record and her **Person Roles** tab.
#. Change the **Title** of one of her roles (for example to ``Professor``)
   and save.

One new line appears in the file: Ruth's whole record as JSON, including her
names, identifiers, roles and group memberships. Every change to a person
adds another line.

Try one more: if Ruth has only one role, set it to **Expired**. She's no
longer eligible to be provisioned, and the new line holds just her ID, such
as ``{"id":45}``, which tells the receiving system to remove her.

.. _gs-pfile-step-all:

5. Send people who were already there
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

People who were in Registry before the target existed aren't sent until
something about them changes. Two ways to send them now:

- **One person:** on their record, open the gear menu by their name and
  choose **Provisioning Status**. On the File Export row, open its gear menu
  and choose **Provision Now**, then confirm. There's no message, but Last
  Status becomes "Provisioned".
- **Everyone:** in **Connections > Provisioning Targets**, open the target's
  gear menu and choose **Reprovision All**. This only *queues* the work, as
  jobs under **Operations > Jobs**. In 5.2.0 a queue runner has to run them.
  If your environment doesn't run one on a schedule, run it from Registry's
  ``app`` folder on the server, as the web server's user:

  .. code-block:: bash

     ./bin/cake job -r -c <CO ID>

  The People job writes one line per person.

  .. dropdown:: The Groups job reports 0 entities?
     :icon: question

     That's a known 5.2.0 issue. Groups are still sent when they or their
     members change.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ec-provisioning` (Reprovisioning All Entities) ·
   :ref:`ops-jobs`

Check your work
---------------

- **Connections > Provisioning Targets** lists File Export, Immediate.
- The file has a new line each time you change Ruth.
- Ruth's **Provisioning Status** shows File Export as Provisioned.

Troubleshoot
------------

.. dropdown:: Every save of a person fails with an error page

   A provisioning target was switched on before its plugin form was saved.
   Open the target, fill in and save the plugin form, or set it to Disabled.
   To remove it, open it and use **Delete** on its Properties tab.

.. dropdown:: Saving the File Provisioner says the file is "not writable"

   The file must already exist, and the web server's user must be able to
   write to it.

.. dropdown:: Nothing is written when you switch the target on

   That's expected: switching it on sends nothing. Make a change to a
   person, or use Provision Now.

.. dropdown:: Reprovision All didn't write anything

   It only queues jobs. Run the queue (step 5), then check **Operations >
   Jobs**.

What you learned
----------------

- A Provisioning Target sends changes about people to another system; its
  mode decides when.
- Create targets Disabled, configure them, then switch them on.
- Changes go out as they happen; people who were already there need
  Provision Now or Reprovision All.

Where to go next
----------------

- Next: :ref:`gs-provision-sql`, to send the same changes to a database
- Try on your own: add Ruth to a group you created in :ref:`gs-module-3`, and
  look at what the new line says about groups.
