.. _transitioning-feature-status:

Feature Status in v5
=====================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

The COmanage Project tracks feature completion on a six-point maturity scale.
The tables below show the current status of each v4 feature area and when
full feature equivalency is expected. Features already complete as of v5.0.0
are not listed here.

.. note::

   Status data is sourced from the COmanage Project's feature equivalency
   tracker, last updated May 2026. Items marked with a ✓ in the v5.2.0
   column were completed in that release. Planned release targets are
   subject to change based on community priorities and funding.

1. Maturity Scale
------------------

.. list-table::
   :widths: 8 20 55
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
     - Core behavior works; some v4 capabilities still in progress
   * - 2
     - In Progress
     - Under active development; usable but incomplete
   * - 1
     - Design Review
     - Scoped and planned; implementation not yet started
   * - 0
     - Not Started
     - On the roadmap; not yet scoped for a specific release

2. People and Identities
-------------------------

.. list-table::
   :widths: 35 20 20 25
   :header-rows: 1

   * - Feature
     - Maturity
     - Completed in
     - FE Target
   * - Person Records
     - 5 — Complete
     - v5.2.0 ✓
     -
   * - Person Roles
     - 3 — Functional
     -
     - v5.5.0
   * - External Identity Records
     - 3 — Functional
     -
     - v5.4.0
   * - External Identity Sources
     - 3 — Functional
     -
     - v5.5.0
   * - Pipelines
     - 3 — Functional
     -
     - v5.6.0
   * - Authenticators
     - 2 — In Progress
     -
     - v5.6.0
   * - Identifier Assignment
     - 3 — Functional
     -
     - v5.6.0
   * - Identifier Validation
     - 0 — Not Started
     -
     - v5.6.0
   * - Data Filter Plugins
     - 0 — Not Started
     -
     - v5.6.0
   * - LDAP Source Plugin
     - 0 — Not Started
     -
     - v5.6.0
   * - ORCID Source Plugin
     - 0 — Not Started
     -
     - v5.3.0
   * - Additional EIS Plugins
     - 0 — Not Started
     -
     - v5.7.0
   * - Vetting
     - 0 — Not Started
     -
     -
   * - Person Expunge
     - 3 — Functional
     -
     - v5.3.0

3. Organization and Structure
------------------------------

.. list-table::
   :widths: 35 20 20 25
   :header-rows: 1

   * - Feature
     - Maturity
     - Completed in
     - FE Target
   * - Collaborative Organizations (COs)
     - 5 — Complete
     - v5.2.0 ✓
     -
   * - COUs
     - 4 — Feature Equivalent
     -
     -
   * - Groups
     - 3 — Functional
     -
     - v5.5.0
   * - CO Duplication / Cloning
     - 3 — Functional
     -
     - v5.4.0
   * - Departments
     - 0 — Not Started
     -
     - v5.6.0
   * - Organizations
     - 0 — Not Started
     -
     - v5.6.0

4. Lifecycle Management
------------------------

.. list-table::
   :widths: 35 20 20 25
   :header-rows: 1

   * - Feature
     - Maturity
     - Completed in
     - FE Target
   * - Enrollment Flows
     - 3 — Functional
     -
     - v5.7.0
   * - Terms and Conditions
     - 3 — Functional
     -
     - v5.3.0
   * - Notifications
     - 2 — In Progress
     -
     - v5.5.0
   * - Message Templates
     - 3 — Functional
     -
     -
   * - Expiration Policies
     - 0 — Not Started
     -
     - v5.3.0
   * - Attribute Election
     - 1 — Design Review
     -
     - v5.5.0
   * - Sponsor Manager Plugin
     - 0 — Not Started
     -
     - v5.7.0

5. Provisioning
----------------

.. list-table::
   :widths: 35 20 20 25
   :header-rows: 1

   * - Feature
     - Maturity
     - Completed in
     - FE Target
   * - Provisioning Core
     - 4 — Feature Equivalent
     - v5.2.0 ✓
     -
   * - Provisioning Plugins (general)
     - 2 — In Progress
     -
     - v5.6.0
   * - SQL Provisioner Plugin
     - 3 — Functional
     -
     - v5.7.0
   * - LDAP Provisioner Plugin
     - 1 — Design Review
     -
     - v5.5.0
   * - Kerberos Provisioner Plugin
     - 5 — Complete
     -
     -
   * - Clusters
     - 1 — Design Review
     -
     - v5.6.0
   * - Email List
     - 0 — Not Started
     -
     - v5.7.0

6. User Interface
------------------

.. list-table::
   :widths: 35 20 20 25
   :header-rows: 1

   * - Feature
     - Maturity
     - Completed in
     - FE Target
   * - Breadcrumb Navigation
     - 4 — Feature Equivalent
     - v5.2.0 ✓
     -
   * - Global Search
     - 3 — Functional
     -
     - v5.5.0
   * - Search and Filtering
     - 3 — Functional
     -
     - v5.5.0
   * - Mostly Static Pages
     - 3 — Functional
     -
     - v5.6.0
   * - Dashboards
     - 2 — In Progress
     -
     - v5.4.0
   * - Themes
     - 2 — In Progress
     -
     - v5.3.0
   * - Navigation Links
     - 0 — Not Started
     -
     - v5.6.0
   * - Services
     - 0 — Not Started
     -
     - v5.6.0

7. Developer and API
---------------------

.. list-table::
   :widths: 35 20 20 25
   :header-rows: 1

   * - Feature
     - Maturity
     - Completed in
     - FE Target
   * - Model-Specific REST API v2
     - 4 — Feature Equivalent
     -
     - v5.6.0
   * - REST API (Core)
     - 0 — Not Started
     -
     - v5.6.0

8. General Platform
--------------------

.. list-table::
   :widths: 35 20 20 25
   :header-rows: 1

   * - Feature
     - Maturity
     - Completed in
     - FE Target
   * - Multi-Value Entity Attributes
     - 3 — Functional
     -
     - v5.3.0
   * - History Records
     - 3 — Functional
     -
     -
   * - CO Settings
     - 3 — Functional
     -
     -
   * - Type MVC
     - 4 — Feature Equivalent
     -
     - v5.6.0
   * - Servers
     - 3 — Functional
     -
     -
   * - Plugin Infrastructure
     - 3 — Functional
     -
     - v5.6.0
   * - Changelog Behavior
     - 4 — Feature Equivalent
     - v5.2.0 ✓
     -
   * - Normalization Behavior
     - 0 — Not Started
     -
     - v5.3.0
   * - Localization
     - 0 — Not Started
     -
     - v5.4.0
   * - Dictionaries and Enumerations
     - 0 — Not Started
     -
     - v5.6.0
   * - Configuration Labels
     - 0 — Not Started
     -
     - v5.7.0
   * - Standardize Logging
     - 2 — In Progress
     -
     - v5.3.0

9. Tools and Commands
----------------------

.. list-table::
   :widths: 35 20 20 25
   :header-rows: 1

   * - Feature
     - Maturity
     - Completed in
     - FE Target
   * - Job Command
     - 5 — Complete
     - v5.2.0 ✓
     -
   * - Jobs (UI management)
     - 3 — Functional
     -
     - v5.4.0
   * - Background CO Deletion
     - 5 — Complete
     - v5.2.0 ✓
     -
   * - Transmogrify Command
     - 4 — Feature Equivalent
     - v5.2.0 ✓
     -
   * - UpgradeVersion Command
     - 5 — Complete
     -
     -
   * - Setup Command
     - 5 — Complete
     -
     -
   * - Database Command
     - 4 — Feature Equivalent
     -
     -
   * - BulkLoad Command
     - 0 — Not Started
     -
     - v5.4.0
   * - Configuration Handler Plugin
     - 0 — Not Started
     -
     -

10. v4 End-of-Life Timeline
----------------------------

Registry v4 will not receive new features; only critical security issues may
be considered for correction. The COmanage Project plans to announce a firm
v4 end-of-life date in late 2026, once v5 has reached feature equivalency
for most deployers.

Key milestones:

- **December 2025** — v4 EOL announced; no new features; critical fixes only
- **2026** — Development continues toward feature parity (new v5 features
  generally deferred in favor of equivalency work)
- **Late 2026** — Expected announcement of v4 end-of-life date and final
  transmogrification support window

For the latest information, subscribe to the
`COmanage Project calendar <https://www.addevent.com/calendar/Nr648428>`_
and follow the community mailing list.

.. seealso::

   :ref:`transitioning-whats-new-5.2.0`
      New capabilities, restored v4 features, and improvements in the
      most recent release.

   :ref:`transitioning-whats-new-5.1.0`
      New capabilities introduced in Registry v5.1.0.

   :ref:`transitioning-upgrading`
      Step-by-step guidance for organizations moving from v4 to v5.
