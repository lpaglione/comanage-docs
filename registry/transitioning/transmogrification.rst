.. _transitioning-transmogrification:

Transmogrification
==================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


Transmogrification is the process by which data is migrated from a Registry v4
instance to Registry v5. It is a command-line tool that reads your existing v4
database and writes a converted version into a new v5 database — leaving the
original v4 data untouched.

.. note::

   This page is under development. For current Transmogrification documentation,
   see `Registry Transmogrification
   <https://spaces.at.internet2.edu/display/COmanage/Registry+Transmogrification>`_
   in the Technical Manual.

.. TODO: Expand this page using content from Technical_Reference/Upgrading/
..       Registry Transmogrification. Key sections to cover:
..       - Prerequisites and what to do before running Transmogrification
..         (unpool Org Identities, instantiate Extended Types, migrate salt
..         file, check Group names, consider archival requirements)
..       - Setting up the source and target databases
..       - Running the transmogrify command and its parameters
..       - What gets migrated and what doesn't (the supported tables list)
..       - Common warnings and errors and what to do about them

.. seealso::

   :doc:`Upgrading to v5 </transitioning/upgrading>`
      The overall upgrade process, of which Transmogrification is one step.

   `Registry Transmogrification <https://spaces.at.internet2.edu/display/COmanage/Registry+Transmogrification>`_
      Full technical reference in the COmanage Technical Manual.
