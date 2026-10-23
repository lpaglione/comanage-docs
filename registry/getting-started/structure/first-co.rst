.. DRAFT (Oct 2026): Lesson 1. Published on the Module 1 page (Oct 23).
   Click paths confirmed in workshop testing on the 5.2.0 kit (deck Section 1).
   Screenshots are 5.2.0 captures; some show the Discovery TNG demo CO and
   should be retaken with the sample orgs.

.. _gs-first-co:

Your First CO
=============

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 1, Your First CO · **Learning paths:** all ·
**Features section:** :ref:`using-structure` · **Registry:** v5.2.0

The scenario
------------

You have to start somewhere, and with Registry everything starts with a
**CO** (Collaborative Organization). People, groups, enrollment flows, and
connections to other systems all live inside a CO.

In this lesson you create **Redcurrant University**, the CO the next
lessons build on. You can create the other two sample organizations now or
when you reach a lesson that uses them. Then you'll take a short tour of the
v5 interface, so you know where things are before the work begins.

What you'll learn
-----------------

- What a CO is, and how the COmanage CO differs from the others.
  See :ref:`struct-co`.
- How the v5 interface is organized: the five menu areas, the All Features
  page, and search. See :ref:`understanding-interface`.

Ingredients
-----------

- Completed: :ref:`gs-before-you-begin`
- A Platform Administrator account in your Registry environment
- No plugins to activate

Steps at a glance
-----------------

#. Prepare: open the COmanage CO
#. Configure: create Redcurrant University (and, optionally, Guests and MESS)
#. Enable: switch into your new CO
#. Use: take a tour of the v5 interface
#. Check your work

Step details
------------

1. Open the COmanage CO
~~~~~~~~~~~~~~~~~~~~~~~

Sign in as a Platform Administrator. On a new installation you land in the
**COmanage** CO directly; if other COs already exist, select **COmanage** on
the **Available Collaborations** page. A banner tells you that this is the
CO used for platform-wide configuration.

COs are created from here because creating a CO is a platform-level action,
not something an administrator of an individual CO can do.

.. figure:: /comanage-files/registry_v5.2/orgStructure/Available_Collaborations.png
   :alt: The Available Collaborations page
   :width: 100%

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`struct-co`

2. Create Redcurrant University
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Which COs you create depends on the path you're following. Every path
needs a CO for the next lessons; Redcurrant University is the one the
lessons use as their example.

.. list-table::
   :header-rows: 1
   :widths: 30 25 45

   * - CO
     - Create it?
     - For
   * - **Redcurrant University**
     - Yes
     - Every path, and all the lessons that follow. If you're not following
       a particular path, this is the only CO you need.
   * - **Guests**
     - Optional
     - The :ref:`gs-path-guest` path. Create it now or when that path asks
       for it.
   * - **MESS**
     - Optional
     - The :ref:`gs-path-vo` path. Create it now or when that path asks for
       it.

To create a CO:

#. Open **Configuration** in the menu on the left. Under
   **Platform-Wide Configuration**, select **COs**.
#. Select **Add a New CO**.
#. Fill in the form using the values in the tab for that CO, then save.

.. figure:: /comanage-files/registry_v5.2/configuration/Platform_Configuration_Menu.png
   :alt: The Configuration panel in the COmanage CO, with COs listed under Platform-Wide Configuration
   :width: 100%

   **COs** is under Platform-Wide Configuration, which appears only in the
   COmanage CO.

.. TODO screenshot: the Add a New CO form.

.. tab-set::

   .. tab-item:: Redcurrant University (every path)

      .. list-table::
         :header-rows: 1
         :widths: 20 30 50

         * - Field
           - Value
           - Why
         * - Name
           - ``Redcurrant University``
           - Shown in lists and at the top of every page. Keep it short and
             recognizable.
         * - Description
           - ``Redcurrant University Person Registry``
           - Helps people who don't know the CO's name tell what it's for.
         * - Status
           - Active
           - The CO is usable as soon as it's saved.

   .. tab-item:: Guests (optional, Guest path)

      .. list-table::
         :header-rows: 1
         :widths: 20 30 50

         * - Field
           - Value
           - Why
         * - Name
           - ``Guests``
           - Shown in lists and at the top of every page. Keep it short and
             recognizable.
         * - Description
           - ``Guest Registry``
           - Helps people who don't know the CO's name tell what it's for.
         * - Status
           - Active
           - The CO is usable as soon as it's saved.

   .. tab-item:: MESS (optional, Research path)

      .. list-table::
         :header-rows: 1
         :widths: 20 30 50

         * - Field
           - Value
           - Why
         * - Name
           - ``MESS``
           - Shown in lists and at the top of every page. Keep it short and
             recognizable.
         * - Description
           - ``Medium Energy Synchrotron Source``
           - Helps people who don't know the CO's name tell what it's for.
         * - Status
           - Active
           - The CO is usable as soon as it's saved.

**About Status.** A CO can be **Active**, **Suspended**, or **Template**.
Suspending a CO immediately shuts off access to it, including the web
interface, the API, and scheduled jobs. Template is for a CO you intend to
use as a starting point for others. For these lessons, always choose Active.

.. tip::

   CO names must be unique, and as of v5.2.0 that check ignores case: you
   can't have both ``MESS`` and ``mess``. If someone else is working in the
   same environment (in a workshop, for example), add your initials, such as
   ``MESS-LP``.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`struct-co`

3. Switch into your new CO
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your COs exist, you need to be *in* one to work on it.

#. Open the **My Identity** menu: your name, at the top right.
#. Choose **Switch CO**.
#. Select **Redcurrant University**.

.. figure:: /comanage-files/registry_v5.2/people/My_Identity_Menu.png
   :alt: The My Identity menu open at the upper right, with Switch CO, the link to your own record, display settings and Log Out
   :width: 100%

   The My Identity menu. You'll come back to it to switch COs, open your own
   record, change display settings, or log out.

.. SCREENSHOT: My_Identity_Menu.png isn't in the local comanage-files
   checkout yet (update the submodule). Check the alt text against it.

.. note::

   After you save a new CO, the COs list shows it with a link. Clicking the
   CO's name there opens its **edit page** in the COmanage CO; it doesn't
   take you into the CO. Use **Switch CO** instead.

The CO's name now appears in the banner at the top of every page. Get in
the habit of checking it: working in the wrong CO is one of the easiest
mistakes to make in Registry.

.. figure:: /comanage-files/registry_v5.2/orgStructure/MESS_Home.png
   :alt: The home page of a new CO, with the CO name in the banner and the five menu areas on the left
   :width: 100%

   The home page of a new CO. The CO's name is in the banner.

.. SCREENSHOT: shows the MESS CO; the step describes Redcurrant University.
   Retake as Redcurrant University's home page.

**Note the CO's ID number.** Every CO has a numeric ID. You'll need it in
the next lesson, and whenever you use the API or command-line tools. It
appears in your browser's address bar while you're working in the CO, as
``co_id=`` followed by the number (for example ``co_id=2``).

.. figure:: /comanage-files/registry_v5.2/configuration/co_id.png
   :alt: The browser address bar while working in a CO, with co_id and the CO's number highlighted
   :width: 100%

   Where to find the CO's ID: ``co_id=`` in the address bar.

.. SCREENSHOT: co_id.png isn't in the local comanage-files checkout yet
   (update the submodule). Check the alt text against it.

.. note::

   On the Available Collaborations page, your new CO is marked **(Not a
   Member)**. That means your account doesn't have a Person record in that
   CO. As a Platform Administrator you can still open and manage it. Some
   actions, such as sending invitations, need someone who is a Person in the
   CO; a later lesson covers that.

.. REVIEW: the Features page (using/structure/collaborative-organizations.rst,
   section 2) says the creating Platform Administrator becomes the first CO
   Administrator. Workshop testing on 5.2.0 suggests otherwise; reconcile.

4. Take a tour of the v5 interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:bdg-success:`Redesigned in v5`

If you've used Registry v4, this is where you'll notice the biggest change.
Take a few minutes to look around your new CO before moving on.

**The five menu areas.** The menu on the left groups everything into five
areas. Select each one to open its panel:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Area
     - What you'll find there
   * - **People**
     - My Population (the people in your CO), Petitions (enrollments in
       progress), and Enrollment Flows
   * - **Structure**
     - COUs and Groups, the ways you organize your population
   * - **Connections**
     - Pipelines, External Identity Sources, and Provisioning Targets: data
       coming in from other systems, and going out to them
   * - **Operations**
     - Jobs and Notifications: background work, and messages that need
       attention
   * - **Configuration**
     - Settings for this CO, and Personalization (message templates and
       static pages)

.. figure:: /comanage-files/registry_v5.2/people/People_Menu.png
   :alt: The People panel, showing My Population, Petitions, and Enrollment Flows, with Authenticators and Types under Related Configurations
   :width: 100%

   The People panel. **Related Configurations** on the right links to
   settings that affect this area but live under Configuration.

**Related Configurations.** Some panels include a short list on the right
called Related Configurations. These are shortcuts to settings that live
under Configuration but matter for that area. For example, the People panel
links to Authenticators and Types.

**All Features.** The **ALL** button at the bottom of the menu opens a
single page listing every feature in the CO, grouped as Registries,
Artifacts, and Configuration. It's a good fallback when you can't remember
which area something is in.

.. figure:: /comanage-files/registry_v5.2/configuration/All_Features_Configuration_Menu.png
   :alt: The All Features page, listing Registries, Artifacts, and Configuration items
   :width: 100%

   The All Features page.

**Search.** The search box at the top searches the whole CO. Results are
grouped by type (people, groups, and so on), so you can go straight to the
record you want. Lists such as My Population also have their own
**Filter**, which narrows just that list.

**Your display settings.** The **My Identity** menu (top right, shown in
step 3) has a **Settings** section where you choose a display **density**
and **dark mode**. Registry remembers these choices for you.

.. note::

   **Coming from v4?** Platform configuration now lives in the COmanage CO
   (it was a separate Platform menu in v4), and the CO menu is organized
   into the five areas above instead of a single long configuration page.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`understanding-interface`

Check your work
---------------

- The **Available Collaborations** page lists **Redcurrant University**
  (and Guests and MESS, if you created them), each with the description you
  entered.
- When you open one of them, its name appears in the banner.
- You can open each of the five menu areas and the **ALL** page.
- **People > My Population** is empty for now. You'll add people in the
  next module.

.. figure:: /comanage-files/registry_v5.2/people/My_Population.png
   :alt: The My Population list for a CO
   :width: 100%

   My Population lists the people in the CO. (This example already has one
   person; yours will be empty.)

Troubleshoot
------------

**You can't find COs under Configuration.** Platform-Wide Configuration
appears only in the COmanage CO. Check the banner: if it shows another CO's
name, switch to COmanage first.

**Saving the CO fails with a message about the name.** Another CO already
uses that name, possibly with different capitalization. Choose a different
name, for example by adding your initials.

**Clicking your new CO's name opens a form instead of the CO.** That's the
CO's edit page in the COmanage CO. Use **Switch CO** in the My Identity menu to go
into the CO.

**Your new CO doesn't appear in the list, or you can't open it.** Check that
its Status is Active. A Suspended CO can't be used, and a Template CO is
meant as a pattern rather than a working CO.

**Changes seem to land in the wrong place.** You may be working in a
different CO than you think. Check the banner at the top of the page.

What you learned
----------------

- A CO is the container for everything else in Registry. The COmanage CO is
  special: it's where platform-wide configuration lives, including creating
  COs.
- The v5 menu groups features into five areas: People, Structure,
  Connections, Operations, and Configuration. The **ALL** page lists
  everything in one place.
- Always check which CO you're in.

Where to go next
----------------

- Next: :ref:`gs-module-2`, to bring people into Redcurrant University from
  an HR file
- Or jump to :ref:`gs-module-3` to start modeling your organization's
  structure
