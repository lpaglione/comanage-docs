.. DRAFT (Nov 2026): Lesson 0, rewritten around Graeme Varga's COmanage
   Registry PE workshop kit (agreed with Graeme). Commands and addresses come
   from the kit's README and participant guide.

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
**Registry:** v5.2.0

The scenario
------------

You're about to learn Registry by using it. Before the first lesson, you
need a Registry of your own to practice on, a way to read the email it
sends, and a way to act as different people. Then you'll meet the three
organizations the lessons follow.

The lessons use the **COmanage Registry PE workshop kit**: a complete
Registry 5.2.0 that runs on your own computer with one command, along with
a mail catcher and the sample files the lessons need.

.. admonition:: About the kit, and thanks
   :class: tip

   The kit was created by **Graeme Varga** (Southern Methodist University)
   for the hands-on COmanage Registry v5 workshop at TechEx 2026, and he has
   generously agreed to its use for this series. It's maintained in his
   repository: https://github.com/graemevarga/comanage-pe-workshop. Thank
   you, Graeme!

   Because it was built for that workshop, the kit's own documentation
   mentions the workshop, its slides and its organizers. Everything you need
   for these lessons is on this page; the kit's
   `participant guide <https://github.com/graemevarga/comanage-pe-workshop/blob/main/docs/participant-guide.md>`_
   has more detail, especially for troubleshooting.

   The sample people in the kit's files are adapted from the COmanage
   Registry v4 training materials by Shayna Atkinson.

What you'll learn
-----------------

- How to start, pause and reset your own Registry.
- What a Platform Administrator can do, and why the lessons need one. See
  :ref:`struct-co`.
- Why some features have to be activated as plugins before you can use
  them. See :ref:`extend-plugins`.

Ingredients
-----------

- **A computer** running macOS (Apple Silicon or Intel), Windows 10 or 11,
  or Linux, with at least 8 GB of memory and 5 GB of free disk space, and
  permission to install software
- **Docker:** `Docker Desktop <https://docs.docker.com/desktop/>`_ on macOS
  and Windows (on Windows, keep the installer's WSL 2 default), or
  `Docker Engine <https://docs.docker.com/engine/install/>`_ with the Compose
  plugin on Linux. Docker Desktop is free for personal use, education and
  small businesses; larger organizations need a paid subscription.
- **Git**, to download the kit (or download it as a ZIP file instead)
- **A web browser**, and ideally a second one (see step 4)

.. warning::

   The kit is for learning only. Anyone who can reach it can log in as its
   administrator, so it's only reachable from your own computer. Keep it that
   way, and use only fictional data.

.. dropdown:: Using your own Registry instead?
   :icon: server

   You can follow the lessons on any Registry 5.2.0 test environment where
   you're a Platform Administrator. You'll need to provide what the kit
   provides: an outgoing mail server and a way to read the mail, the sample
   files on the Registry server, and a way to sign in as several different
   people.

Steps at a glance
-----------------

Select a card to jump to that step.

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: 1. Start the kit
      :link: gs-mise-step-start
      :link-type: ref

      Download the kit and start your own Registry.

   .. grid-item-card:: 2. Sign in
      :link: gs-mise-step-signin
      :link-type: ref

      Sign in as the administrator, and find the mail catcher.

   .. grid-item-card:: 3. Plugins
      :link: gs-mise-step-plugins
      :link-type: ref

      Know where to activate the plugins a lesson needs.

   .. grid-item-card:: 4. Be someone else
      :link: gs-other-people
      :link-type: ref

      Sign in as different people, in different windows.

   .. grid-item-card:: 5. Sample organizations
      :link: gs-mise-step-orgs
      :link-type: ref

      Meet the three organizations the lessons follow.

Then :ref:`check your work <getting-started/mise-en-place:Check your work>`.

Step details
------------

Each step shows what to do. Select a heading marked ▸ to see why, or what to
do if something looks different.

.. _gs-mise-step-start:

1. Download and start the kit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start Docker and wait until it says it's running. Then open a terminal
(Terminal on macOS, PowerShell on Windows) and run:

.. code-block:: bash

   git clone https://github.com/graemevarga/comanage-pe-workshop.git
   cd comanage-pe-workshop
   docker compose up --wait

.. dropdown:: No Git?
   :icon: question

   On the repository's page, select **Code > Download ZIP**, unzip it, and
   run only the last command, from inside the unzipped folder.

The first start downloads about 500 MB and takes a few minutes (longer on
Apple Silicon Macs, which run Registry under emulation). It's ready when your
prompt comes back and the last lines say ``Healthy``.

**Everyday commands**, run in the ``comanage-pe-workshop`` folder:

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - To
     - Run
   * - Start, or resume after a pause
     - ``docker compose up --wait``
   * - Pause (your work is kept)
     - ``docker compose stop``
   * - Start over from a fresh install
     - ``docker compose down -v``, then ``docker compose up --wait``

.. _gs-mise-step-signin:

2. Sign in, and find the mail catcher
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 45 35

   * - What
     - Where
     - How
   * - Registry
     - https://localhost:8443/registry/
     - Log in as ``admin``, with an empty password
   * - Mail
     - http://localhost:8025/
     - Every email Registry sends lands here (Mailpit)

#. Open **https://localhost:8443/registry/**. Your browser warns that the
   connection isn't private, because the kit uses a self-signed
   certificate. Continue anyway (in Chrome or Edge: **Advanced**, then
   **Proceed to localhost**).
#. Select **Login**. When the browser asks for a username and password,
   type ``admin`` and leave the password empty.
#. You land in the **COmanage** CO, which is where platform-wide
   administration happens.
#. Open **http://localhost:8025/** in another tab: the mailbox where
   invitations, verification codes and other messages will arrive. The kit
   has already connected Registry's outgoing mail to it.

In the COmanage CO, open **Configuration** in the menu on the left. The
Registry version appears at the bottom of the Configuration panel:
"COmanage Registry v5.2.0".

.. figure:: /comanage-files/registry_v5.2/configuration/Platform_Configuration_Menu.png
   :alt: The Configuration panel in the COmanage CO, showing Platform-Wide Configuration, CO Configuration, and Personalization
   :width: 100%

   The Configuration panel in the COmanage CO. Platform-Wide Configuration
   appears only here.

.. dropdown:: Why sign in as admin?
   :icon: info

   ``admin`` is the kit's **Platform Administrator**: it can create COs and
   activate plugins, which the early lessons need.

.. dropdown:: Landed on Available Collaborations instead?
   :icon: question

   Once you've created other COs, signing in takes you to the **Available
   Collaborations** page instead; select **COmanage** there to get back to
   the platform settings.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`struct-co`

.. _gs-mise-step-plugins:

3. Know where to activate plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some features are plugins that a Platform Administrator activates once, for
every CO on the platform. You don't need to activate anything yet. Each lesson lists the plugins it
needs under *Ingredients*. When a lesson asks you to activate one:

#. In the **COmanage** CO, open **Configuration**. Under
   **Platform-Wide Configuration**, select **Plugins**.
#. Find the plugin (package) by name, open the gear menu on its row, and
   choose **Activate**. The page confirms "Plugin Activated".

.. dropdown:: Why do some features need activating?
   :icon: info

   Nearly everything in Registry is a plugin. Some plugins are **core** and
   always on. Others are **available**: they start out Suspended, and a
   Platform Administrator activates them once, for every CO on the platform.
   In the kit, the available plugins are installed but not active.

The lessons in this series use these available plugins:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Plugin (package)
     - Used for
   * - FileConnector
     - Reading people from a CSV file; writing people to a file
   * - PipelineToolkit
     - Pipeline extras, such as turning a source's uid into a login
   * - SqlConnector
     - Provisioning people to a SQL database

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`extend-plugins`

.. _gs-other-people:

4. Learn how to be someone else
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several lessons have you act as more than one person: the administrator,
someone who sends an invitation, and someone who accepts it. The kit makes
this easy: **any username works with an empty password**, and you become
whoever that username belongs to.

- ``admin`` is the Platform Administrator.
- A username Registry already knows, such as ``ruth.spence`` once she's been
  brought in, makes you that person.
- A username Registry doesn't know yet makes you a new person, with no COs.
  That's who accepts an invitation or signs up.
- Use lowercase: usernames are case-sensitive.

Your browser remembers who you logged in as until you close it. To be
someone else at the same time, use a browser window that isn't logged in
yet:

- **A private (incognito) window**
- **A second browser**, or a second browser profile
- **A second address:** https://127.0.0.1:8443/registry/ reaches the same
  Registry, but the browser treats it as a different site.

To switch who you are in the same window, log out from the **My Identity**
menu (your name, at the top right), or close the browser.

.. dropdown:: Need more than one extra person in Chrome?
   :icon: question

   In Chrome, all private windows share one login, so you get one extra
   person that way, not several. Add a second browser, a second browser
   profile, or the 127.0.0.1 address.

.. _gs-mise-step-orgs:

5. Meet the sample organizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The lessons follow three organizations. Each one shows a different way
people use Registry.

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

The kit also includes the files the lessons use, in folders you can open on
your computer:

- ``filesource/hr.csv`` and ``filesource/registrar.csv``: fictional people
  from Redcurrant's HR and registrar systems. Registry sees them as
  ``/srv/filesource/hr.csv`` and ``/srv/filesource/registrar.csv``.
- ``provisioned/output.jsonl``: where Registry writes people's records in the
  provisioning lesson. Registry sees it as ``/srv/provisioned/output.jsonl``.

Check your work
---------------

You're ready when:

- You can sign in to https://localhost:8443/registry/ as ``admin`` and see
  the COmanage CO.
- You can find **Configuration > Plugins** in the COmanage CO.
- Mailpit opens at http://localhost:8025/.

Troubleshoot
------------

.. dropdown:: "Cannot connect to the Docker daemon" or "error during connect"

   Docker isn't running. Start Docker Desktop, wait until it says it's
   running, and try again.

.. dropdown:: "Port is already allocated"

   Another program uses port 8443, 8080 or 8025. In the kit's folder, copy
   ``.env.example`` to ``.env``, change ``HTTPS_PORT``, ``HTTP_PORT`` or
   ``MAILPIT_PORT``, run ``docker compose up --wait`` again, and use your
   port in the addresses.

.. dropdown:: The login box keeps coming back

   Type a username: the password can be empty, but the username can't.

.. dropdown:: "Too many redirects"

   You're logged in as someone who can't see that page. Go back to
   https://localhost:8443/registry/, or log out and in as ``admin``.

.. dropdown:: Something else

   The kit's
   `participant guide <https://github.com/graemevarga/comanage-pe-workshop/blob/main/docs/participant-guide.md>`_
   has a longer troubleshooting list, including Apple Silicon, Linux
   firewall and VPN issues. ``docker compose logs registry`` shows
   Registry's log.

What you learned
----------------

- How to start, pause and reset your own Registry with the kit.
- The COmanage CO is where platform-wide administration happens, and some
  features are plugins that need activating first.
- Any username logs you in to the kit, so you can act as several people, one
  per browser window.

Where to go next
----------------

- Next: :ref:`gs-module-1`
