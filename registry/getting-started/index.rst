.. _gs-index:

Getting Started with Registry
=============================

The recipes elsewhere in this guide are for when you know what you want to
make: a specific dish, for a specific occasion. This series is about
**learning to cook.** Each lesson is a hands-on exercise that builds on the
one before it, so that by the end you have a working feel for how Registry's
pieces fit together.

The lessons follow three sample organizations throughout:

- **Redcurrant University**, an enterprise registry for students, faculty,
  and staff
- **Guests**, a guest management system for campus visitors
- **MESS** (the Medium Energy Synchrotron Source), a multi-institution
  research collaboration

You don't need to adopt any of them. They're there so that each step has a
concrete reason behind it.

.. note::

   This series is under development. Lessons are published as they are
   verified against Registry v5.2.0.

Before you begin
----------------

Start with :ref:`gs-before-you-begin`. It covers what you need in place (a
running Registry environment where you can create COs) and a few tools that
make the lessons easier.

.. toctree::
   :hidden:
   :maxdepth: 2

   mise-en-place

Modules
-------

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: 1 · Your First CO
      :link: gs-module-1
      :link-type: ref

      Create the CO you'll work in, and take a tour of the v5 interface.

   .. grid-item-card:: 2 · Bring People In
      :link: gs-module-2
      :link-type: ref

      Connect External Identity Sources and Pipelines to create Person records.

   .. grid-item-card:: 3 · Model Your Structure
      :link: gs-module-3
      :link-type: ref

      Use COUs and Groups to reflect how your population is organized.

   .. grid-item-card:: 4 · Identifiers and Authenticators
      :link: gs-module-4
      :link-type: ref

      Assign identifiers automatically and collect credentials such as SSH keys.

   .. grid-item-card:: 5 · Enrollment
      :link: gs-module-5
      :link-type: ref

      Build Enrollment Flows for invitations and self sign-up.

   .. grid-item-card:: 6 · Provisioning
      :link: gs-module-6
      :link-type: ref

      Send Registry data to the systems that rely on it.

   .. grid-item-card:: 7 · Offboarding
      :link: gs-module-7
      :link-type: ref

      Manage how people leave a role, or your organization.

   .. grid-item-card:: 8 · Automate with Jobs
      :link: gs-module-8
      :link-type: ref

      Run and monitor background work from the Registry interface.

.. toctree::
   :hidden:
   :maxdepth: 2

   module-1
   module-2
   module-3
   module-4
   module-5
   module-6
   module-7
   module-8

Learning paths
--------------

If one of the sample organizations looks like yours, its learning path
sequences the lessons that matter most for that use case.

- :ref:`gs-path-enterprise`
- :ref:`gs-path-guest`
- :ref:`gs-path-vo`

.. toctree::
   :hidden:
   :maxdepth: 2

   path-enterprise
   path-guest
   path-vo
