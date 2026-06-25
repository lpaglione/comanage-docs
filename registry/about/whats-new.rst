.. DRAFT — April 2026
.. Terminology status (confirmed from PE Technical Manual, Mar 2026):
..   "Person record"     ✓ v5 term
..   "External identity" ✓ v5 term
..   "Enrollment flow"   ✓ unchanged
..   CO                  ✓ still used in v5
..   COU                 ✓ still used in v5

.. _whats-new:

What's New in Registry v5
==========================

Registry v5 is a ground-up rebuild of the COmanage Registry you know — the same
capabilities and concepts, re-engineered to be more flexible, easier to use, and
better positioned for the next decade of identity management in research and
education. Where v4 evolved through years of incremental additions, v5 was
designed thoughtfully from the start, shaped by years of community feedback and
real-world deployment patterns.

v5 is currently an **Early Adopter Release**. Core functionality is in place and
working well, and feature parity with v4 is progressing release by release. See
:ref:`feature-status` below for the current picture, and
:doc:`../transitioning/index` if you are planning a migration from v4.

----

.. contents:: On this page
   :local:
   :depth: 1

----

1. A Redesigned Interface
--------------------------

The v5 interface has been rebuilt to make Registry faster and more intuitive to
use day to day.

**Enhanced global search** runs across all object types — people, groups,
sub-units, identifiers — from a single search bar at the top of every page.
In v4, finding a record often required knowing which section of Registry to look
in first. In v5, a search returns results across multiple object types at once,
so you spend less time navigating and more time doing the work.

**A redesigned Person record page** consolidates the information that was spread
across multiple tabs and screens in v4. Properties, attributes, and external
identities appear in one organized view, making it easier to understand a
person's complete record at a glance and to find what you need to edit.

**Improved navigation and labeling** throughout the interface means that features
are where you expect to find them, and named in ways that reflect how they are
used. The changes are particularly noticeable for administrators who work in
Registry regularly — the mental overhead of navigating the application has been
reduced.

2. More Flexible Enrollment Flows
----------------------------------

Enrollment flows in v5 have been redesigned around a modular step model, making
them significantly more powerful and easier to configure.

In v4, an enrollment flow was a relatively fixed sequence. In v5, an enrollment
flow is built from individual steps that you assemble — and can reuse across
flows. This means you can:

- **Add approvals at exactly the stages you need** — whether that is one
  approval step, two, or none at all.
- **Build simple flows without inheriting the complexity of advanced ones.** If
  your use case is straightforward, your enrollment flow can be too.
- **Follow a petition through its full lifecycle** in one view. The status of
  each step, and what happens next, is visible without digging through separate
  screens.

The attribute collector — the step where enrollees enter or confirm their
information — has also been redesigned for clarity and ease of use on both sides:
easier to configure for administrators, and cleaner to interact with for
end users.

3. Built on a Stronger Foundation
-----------------------------------

Because v5 was rebuilt from scratch rather than extended, the underlying
architecture is cleaner and more consistent throughout. A few implications that
will matter to deployers:

**Plugin architecture** has been extended throughout the tool. Plugins have
always been a core part of how Registry (and Match) connects to external systems,
but v5 brings plugin support to more parts of the tool — allowing you to
customize and extend nearly every aspect of Registry to suit your organization's
specific needs.

**Group management has been brought into line with the broader administrative
model.** In v4, group ownership was assigned to individuals. In v5, a group can
be owned and managed by a group of people — consistent with how administrator
roles work for organizations and sub-units. This makes it practical to distribute
group management responsibilities without relying on a single named owner.

**Multi-value entity attributes** are supported at the data model level, rather
than as a workaround. This makes it easier to represent the real-world
complexity of organizational data — a person with multiple roles, multiple
institutional affiliations, multiple identifiers of the same type — without
special-case configuration.

**Containerized deployment** is available for v5. Running Registry in containers
simplifies installation, updates, and operational maintenance compared to the
traditional server-based deployment model.

These architectural changes are not primarily things you will see in the UI —
they are the foundation that makes everything else more reliable and that will
support new capabilities as v5 continues to develop.

.. _feature-status:

4. Feature Status in v5
------------------------

v5 is an Early Adopter Release, and the project is transparent about where things
stand. Features are tracked on a six-point maturity scale:

.. list-table::
   :widths: 10 20 55
   :header-rows: 1

   * - Level
     - Label
     - What it means
   * - 5
     - Complete
     - Fully implemented; meets or exceeds v4 behavior
   * - 4
     - Feature Equivalent
     - Matches v4 functionality; refinements may continue
   * - 3
     - Functional
     - Core behavior works; some v4 capabilities may still be in progress
   * - 2
     - In Progress
     - Under active development; usable but incomplete
   * - 1
     - Design Review
     - Scoped and planned; implementation not yet started
   * - 0
     - Not Started
     - On the roadmap; not yet scoped for a specific release

The areas where v5 is already at or near feature parity with v4 include core
person management, enrollment flows, organizational structure, provisioning
infrastructure, and global search. Areas actively in progress include
authenticators, notifications, LDAP provisioning, and dashboards.

For the full feature-by-feature status, see
:doc:`../transitioning/feature-status`.

.. note::

   The COmanage Project team is committed to reaching full feature parity.
   Development priorities for each release are discussed in the community and
   tracked publicly. See :doc:`../community/about` for how to follow along and
   participate.

.. seealso::

   :doc:`What is COmanage Registry? </about/what-is-registry>`
      A concise overview of Registry and what it does.

   :doc:`Registry Concepts Overview </understanding/concepts-overview>`
      The core mental model for understanding how Registry works.

   :doc:`../transitioning/index`
      Resources for organizations moving from v4 to v5, including the full
      feature status table.

   `COmanage Registry Technical Manual <https://spaces.at.internet2.edu/display/COmanage/Technical+Manual>`_
      Detailed technical reference for the v5 release.
