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

#. Prepare: how identifier assignment works
#. Configure: add the Identifier Assignment
#. Configure: set the format
#. Check your work: see a username appear

Step details
------------

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

2. Add the Identifier Assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In your CO, open **Configuration** and select **Identifier Assignments**,
then **Add**. Fill in the properties and save.

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Field
     - Value
     - Why
   * - Description
     - ``Username``
     - Names the assignment.
   * - Status
     - Active
     - The assignment runs.
   * - Plugin
     - ``CoreAssigner.FormatAssigners``
     - Builds the identifier from a pattern.
   * - Context
     - Person
     - Assign the identifier to People (rather than, for example, Groups).
   * - Identifier Type
     - Network, with **Login** ticked
     - The kind of identifier to create. **Login** means people can sign in
       with it; without it, the username exists but can't be used to log
       in.

.. SCREENSHOT: the Add a New Identifier Assignment form (not yet in
   comanage-files).

3. Set the format
~~~~~~~~~~~~~~~~~

Saving opens the Format Assigner's own form. Fill it in and save.

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Field
     - Value
     - Why
   * - Format
     - ``(g).(f)``
     - The given name, a dot, and the family name. Lowercase ``(g)`` and
       ``(f)`` give a lowercase username, such as ``casey.invitee``;
       ``(G)`` and ``(F)`` keep the capitals.
   * - Collision Mode
     - Sequential
     - Required. If the username is already taken, Registry adds a number,
       so a second Casey Invitee gets a different username.
   * - Permitted Characters
     - Alphanumeric, dot, dash, underscore
     - Characters outside this set are left out of the username.

.. tip::

   Usernames are case-sensitive. Lowercase is the safest choice for
   something people type to log in.

.. SCREENSHOT: the Format Assigner form (not yet in comanage-files).

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`ec-identifier-assignment` (Constraints and Uniqueness)

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

**Saving the Format Assigner fails.** Collision Mode is required; choose
Sequential.

**Nobody gets a username.** The assignment only runs when something happens
to a person (an enrollment finishing, or a pipeline sync), and only for
people who don't already have that type of identifier. Check its Status is
Active, then sync someone again.

**The username has capitals, or odd characters missing.** Check the Format:
lowercase ``(g)`` and ``(f)`` give lowercase. Characters not in Permitted
Characters are dropped.

**Someone has the username but can't log in with it.** The identifier
wasn't flagged for login. Check that **Login** is ticked on the assignment's
Identifier Type.

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
