.. DRAFT (Oct 2026): Lesson 4. Unpublished (listed in UNVERIFIED in conf.py).
   Values follow the workshop deck's Section 4 ("Give new people a
   username"), tested on 5.2.0. The "when it runs" statements come from
   Claude's reading of the 5.2.0 code (noted in the deck's speaker notes);
   confirm in a walk-through.

.. _gs-identifier-assignment:

Give Everyone a Username Automatically
======================================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 4, Identifiers and Authenticators · **Learning paths:** Enterprise
(Redcurrant University; any CO works) ·
**Features section:** :ref:`ec-identifier-assignment` · **Registry:** v5.2.0

The scenario
------------

People from Redcurrant's HR file arrive with a username, but not everyone
will come from a file. Someone you invite (in Module 5) has no username at
all until Registry gives them one. Redcurrant wants every person to get a
predictable username, such as ``casey.invitee``, that they can log in with.

In this lesson you set up an **Identifier Assignment** that creates that
username automatically.

What you'll learn
-----------------

- What an Identifier Assignment does, and when it runs. See
  :ref:`ec-identifier-assignment`.
- How a format such as ``(g).(f)`` turns a person's name into an identifier,
  and what happens when two people have the same name.
- Why the **Login** flag matters for an identifier.

Ingredients
-----------

- Completed: :ref:`gs-module-1` (you have a CO). People from
  :ref:`gs-module-2` make it easier to see the result, but they're optional.
- No plugins to activate (the Format Assigner is core)

Steps at a glance
-----------------

Select a card to jump to that step.

.. grid:: 1 2 4 4
   :gutter: 3

   .. grid-item-card:: 1. Prepare
      :link: gs-ia-step-how
      :link-type: ref

      How identifier assignment works.

   .. grid-item-card:: 2. Add the assignment
      :link: gs-ia-step-add
      :link-type: ref

      Create the Identifier Assignment.

   .. grid-item-card:: 3. Set the format
      :link: gs-ia-step-format
      :link-type: ref

      Tell it how to build each username.

   .. grid-item-card:: 4. See it work
      :link: gs-ia-step-see
      :link-type: ref

      Watch a username appear.

Then :ref:`check your work <getting-started/connections/identifier-assignment:Check your work>`.

Step details
------------

Each step shows what to do. Select a heading marked ▸ to see why, or what to
do if something looks different.

.. _gs-ia-step-how:

1. How identifier assignment works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An **Identifier Assignment** is a rule: "give each Person an identifier of
this type, built this way." Each assignment uses a plugin to build the
value. The **Format Assigner** builds it from a pattern, using parts of the
person's name and, when needed, a number.

An assignment only gives an identifier to people who don't already have one
of that type. It runs when an enrollment finishes, and when a pipeline
creates or updates someone.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ec-identifier-assignment`

.. _gs-ia-step-add:

2. Add the Identifier Assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In your CO, open **Configuration** and select **Identifier Assignments**,
then **Add**. Fill in the properties and save.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Field
     - Value
   * - Description
     - ``Username``
   * - Status
     - Active
   * - Plugin
     - ``CoreAssigner.FormatAssigners``
   * - Context
     - Person
   * - Identifier Type
     - Network, with **Login** ticked

.. important::

   **Tick Login.** Without it, the username exists but can't be used to log
   in.

.. dropdown:: Why these settings?
   :icon: info

   - **Description** names the assignment.
   - **Status: Active** means the assignment runs.
   - **Plugin:** ``CoreAssigner.FormatAssigners`` builds the identifier from
     a pattern.
   - **Context: Person** assigns the identifier to People (rather than, for
     example, Groups).
   - **Identifier Type** is the kind of identifier to create. **Login**
     means people can sign in with it.

.. SCREENSHOT: the Add a New Identifier Assignment form (not yet in
   comanage-files).

.. _gs-ia-step-format:

3. Set the format
~~~~~~~~~~~~~~~~~

Saving opens the Format Assigner's own form. Fill it in and save.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Field
     - Value
   * - Format
     - ``(g).(f)``
   * - Collision Mode
     - Sequential (required)
   * - Permitted Characters
     - Alphanumeric, dot, dash, underscore

.. dropdown:: Why these settings?
   :icon: info

   - **Format** ``(g).(f)`` is the given name, a dot, and the family name.
     Lowercase ``(g)`` and ``(f)`` give a lowercase username, such as
     ``casey.invitee``; ``(G)`` and ``(F)`` keep the capitals. Usernames are
     case-sensitive, so lowercase is the safest choice for something people
     type to log in.
   - **Collision Mode: Sequential**: if the username is already taken,
     Registry adds a number, so a second Casey Invitee gets a different
     username.
   - **Permitted Characters**: characters outside this set are left out of
     the username.

.. SCREENSHOT: the Format Assigner form (not yet in comanage-files).

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ec-identifier-assignment` (Constraints and Uniqueness)

.. _gs-ia-step-see:

4. See a username appear
~~~~~~~~~~~~~~~~~~~~~~~~

The assignment doesn't change anyone right away. It runs the next time
something happens to a person. Two ways to see it work:

- **Sync someone again.** If you brought people in from the HR file in
  :ref:`gs-module-2`, open the source, **Search Source** for ``rachel``, and
  **Sync Record to CO**. Open Rachel Payne's record: her identifiers now
  include a Network identifier, ``rachel.payne``, flagged for login.
- **Invite someone.** In :ref:`gs-module-5`, the person you invite gets a
  username when their enrollment finishes.

.. REVIEW: confirm in a walk-through that re-syncing an existing person runs
   the assignment (Claude's reading of the 5.2.0 code says assignments run
   when a pipeline runs, for people without one yet).

Check your work
---------------

- **Configuration > Identifier Assignments** lists **Username**, Active,
  using ``CoreAssigner.FormatAssigners``.
- After a re-sync (or an enrollment), the person's record has a Network
  identifier in the ``given.family`` format, flagged for login.

Troubleshoot
------------

.. dropdown:: Saving the Format Assigner fails

   Collision Mode is required; choose Sequential.

.. dropdown:: Nobody gets a username

   The assignment only runs when something happens to a person (an
   enrollment finishing, or a pipeline sync), and only for people who don't
   already have that type of identifier. Check its Status is Active, then
   sync someone again.

.. dropdown:: The username has capitals, or odd characters missing

   Check the Format: lowercase ``(g)`` and ``(f)`` give lowercase.
   Characters not in Permitted Characters are dropped.

.. dropdown:: Someone has the username but can't log in with it

   The identifier wasn't flagged for login. Check that **Login** is ticked
   on the assignment's Identifier Type.

What you learned
----------------

- An Identifier Assignment gives people an identifier automatically, built
  from a pattern, and only to people who don't have one yet.
- A **Login** identifier is what someone signs in with.
- Collision Mode decides what happens when two people would get the same
  value.

Where to go next
----------------

- Next: :ref:`gs-module-5`, where an invited person gets a username from this
  assignment
- Try on your own: compare formats. On a test CO, try ``(f)(g)`` or ``(G).(F)``
  and see what username a new person gets.
