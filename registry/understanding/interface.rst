.. _understanding-interface:

The v5 Interface
================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

:bdg-success:`New in v5`

The v5 release introduced a **completely redesigned user interface**, one of
the most significant changes for day-to-day Registry users. The redesign
affects where features are found, how navigation is structured, and how the
interface behaves for users who are new to Registry or who access it
infrequently.

This page describes the key changes from the v4 interface and what to expect
when you first encounter v5.

.. TODO: Add annotated screenshots throughout this page once v5 UI screenshots
   are available (see screenshot repository).

1. Navigation Structure
------------------------

.. TODO: Document the new navigation structure, including where the major
   functional areas are accessed from, how CO-level vs platform-level
   navigation is organized, and any significant changes from where things
   lived in v4.

2. Global Search
-----------------

Global Search has been redesigned in v5. Search results are now **grouped by
object type**, making it easier to identify the kind of record that matched
your search and act on it directly from the results page.

**Type-ahead search** is also available in many individual search fields
throughout the interface and has been improved in v5.

For full details, see :ref:`ops-searching`.

3. The Person Canvas
---------------------

.. TODO: Document the Person Canvas layout once it is finalized and
   screenshots are available. This is the central view of a Person's record
   and is significantly redesigned from v4. See also person-records.rst.

4. Filtering vs. Searching
---------------------------

v5 distinguishes clearly between **filtering** (narrowing the index view of a
single object type) and **searching** (Global Search across the entire
Registry). The same distinction existed in v4 but is more explicitly
represented in the v5 interface.

.. TODO: Add screenshots and explicit callouts showing where filtering is used
   versus where search is applied — the interface distinction is still being
   refined and should be documented with screenshots once stable.

5. Usability Improvements for New and Infrequent Users
-------------------------------------------------------

A key goal of the v5 interface redesign was to make Registry more accessible
to users who log in infrequently or who are encountering it for the first
time. This includes improvements to:

- Labels and terminology that are more self-explanatory without prior training
- Clearer indication of where to go for common tasks
- More consistent placement of actions and configuration options

.. TODO: Document specific usability improvements with examples and screenshots
   once the v5 UI is finalized and feedback from early adopters is incorporated.

6. User Display Preferences
----------------------------

:bdg-secondary:`Available: v5.1.0`

Registry v5 stores individual user display preferences across sessions. Users
can adjust settings such as **display density** (compact vs. normal view for
list and canvas views) and **dark mode**, independently of operating system
settings. Pagination state is also remembered per user.

.. TODO: Add screenshots of the user preferences panel and document how to
   access it once v5 UI screenshots are available.

7. Changes from v4
-------------------

The v5 interface is a ground-up redesign; many things have moved. Where
specific features have changed location, this is noted in the relevant
feature documentation pages throughout this guide.

.. TODO: Build out a more explicit comparison here — "In v4, X was at... In
   v5, you can find it at..." — once the v5 interface is stable and screenshots
   are available.
