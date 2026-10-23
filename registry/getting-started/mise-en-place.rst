.. DRAFT (Oct 2026): Lesson 0. Click paths confirmed in workshop testing on
   the 5.2.0 kit. Remaining items to confirm are marked VERIFY.

.. _gs-before-you-begin:

Mise en Place: Getting Ready
============================

*Mise en place* is the cook's habit of getting everything in place before
starting. This lesson does the same for Registry.

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 0, Mise en place · **Learning paths:** all ·
**Registry:** v5.2.0 or later

The scenario
------------

You're about to learn Registry by using it. Before the first lesson, make
sure you have a place to work, the access you'll need, and a way to see the
email that Registry sends. Then meet the three organizations you'll be
working with.

What you'll learn
-----------------

- What a Platform Administrator can do, and why the lessons need one.
  See :ref:`struct-co`.
- Why some features have to be activated as plugins before you can use
  them. See :ref:`extend-plugins`.

Ingredients
-----------

- **A Registry environment.** This can be a test instance, or a sandbox
  environment if one is available to you. Installing Registry isn't covered
  here; the lessons assume it's already running.
- **A Platform Administrator account** on that environment. Platform
  Administrators can create COs and activate plugins, and the early lessons
  need both.
- **A web browser, plus a way to be someone else.** Later lessons have you
  log in as other people. Use a browser window that isn't logged in yet: a
  private window or a second browser. In Chrome, all incognito windows share
  one login, so for a third person use a different browser or browser
  profile.

.. warning::

   Use a test or sandbox environment, not production. The lessons create
   COs, people, and configuration that you won't want in a live registry.

Steps at a glance
-----------------

#. Prepare: sign in and check your Registry version
#. Configure: know where to activate plugins
#. Enable: set up a way to read test email
#. Check your work: meet the sample organizations

Step details
------------

1. Sign in and check your version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sign in with your Platform Administrator account. Every Registry
environment has at least one CO: the **COmanage** CO, which is where
platform-wide administration happens. On a brand-new installation you land
there directly. Once other COs exist, you land on the **Available
Collaborations** page instead, listing the COs you can manage; select
**COmanage** to get back to the platform settings.

.. figure:: /comanage-files/registry_v5.2/orgStructure/Available_Collaborations.png
   :alt: The Available Collaborations page, listing the COmanage CO and several other COs
   :width: 100%

   The Available Collaborations page. Your list will be shorter; you'll add
   COs for the sample organizations in the next lesson.

In the COmanage CO, open **Configuration** in the menu on the left. The
Registry version appears at the bottom of the Configuration panel, for
example "COmanage Registry v5.2.0". These lessons are written for **v5.2.0**;
if your version is different, some screens may not match.

.. figure:: /comanage-files/registry_v5.2/configuration/Platform_Configuration_Menu.png
   :alt: The Configuration panel in the COmanage CO, showing Platform-Wide Configuration, CO Configuration, and Personalization
   :width: 100%

   The Configuration panel in the COmanage CO. Platform-Wide Configuration
   appears only here.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`struct-co`

2. Know where to activate plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nearly everything in Registry is a plugin. Some plugins are **core** and
always on. Others are **available**: they start out Suspended, and a Platform
Administrator activates them once, for every CO on the platform.

You don't need to activate anything yet. Each lesson lists the plugins it
needs under *Ingredients*. When a lesson asks you to activate one:

#. In the **COmanage** CO, open **Configuration**. Under
   **Platform-Wide Configuration**, select **Plugins**.
#. Find the plugin (package) by name, open the gear menu on its row, and
   choose **Activate**. The page confirms "Plugin Activated".

The lessons in this series use these available plugins:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Plugin (package)
     - Used for
   * - FileConnector
     - Reading people from a CSV file; writing people to a file
   * - SqlConnector
     - Provisioning people to a SQL database
   * - PipelineToolkit
     - Optional Pipeline extras, such as mapping source values to your
       CO's terms

.. REVIEW: update this list as lessons are written.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`extend-plugins`

3. Set up a way to read test email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several lessons send email: invitations, verification messages, and
notifications. You'll want to read those messages without filling up your
own inbox or creating real accounts for pretend people.

A disposable-email service such as `Mailinator <https://www.mailinator.com>`_
works well. Its public inboxes need no sign-up: send mail to any
``name@mailinator.com`` address, then look up ``name`` on the Mailinator
site to read it.

.. warning::

   Public disposable inboxes can be read by anyone. Use them only for test
   data, never for real personal information.

For Registry to send email at all, your environment needs an outgoing mail
(SMTP) server. A Platform Administrator sets it up in the COmanage CO: add it
under **Configuration > Servers**, then select it in **CO Settings**. If
messages never arrive, check with whoever runs your environment.

.. VERIFY: whether Mailinator's public inboxes still work as described.
   (The workshop kit uses a local Mailpit instead.)

4. Meet the sample organizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The lessons follow three organizations. Each one shows a different way
people use Registry, and you're encouraged to try all three.

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Organization
     - Use case
     - What it needs
   * - **Redcurrant University**
     - Enterprise
     - A primary person registry for students, faculty, and staff, fed by
       institutional systems such as HR and the registrar.
   * - **Guests**
     - Guest management
     - Time-limited access for people who aren't in enterprise systems:
       parents, vendors, and short-term visitors.
   * - **MESS** (Medium Energy Synchrotron Source)
     - Research collaboration
     - Members from many institutions, organized into project teams, who
       sign in with their home accounts.

Check your work
---------------

You're ready when:

- You can sign in as a Platform Administrator and open the **COmanage** CO.
- You can find **Configuration > Plugins** in the COmanage CO.
- You know how you'll read test email.

Troubleshoot
------------

**You don't see the COmanage CO, or Platform-Wide Configuration is
missing.** Your account probably isn't a Platform Administrator. Ask
whoever manages your environment to add you to the COmanage CO's
administrators group.

**A plugin a lesson needs isn't on the Plugins page.** Available plugins
ship with Registry, so they should all be listed. If one is missing, your
environment may be on a different version, or the plugin may have been
removed by your deployment. Check with whoever runs it.

What you learned
----------------

- The COmanage CO is where platform-wide administration happens.
- Some features are plugins that need activating first.
- Test email needs both a working mail server and somewhere safe to read it.

Where to go next
----------------

- Next: :ref:`gs-module-1`
