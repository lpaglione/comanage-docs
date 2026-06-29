.. _ops-searching:

Searching and Filtering
=======================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry offers two ways to find records: **Filtering** within a specific
object type's index view, and **Global Search** across the entire Registry.

For the full technical reference, see
`Searching and Filtering (PE) <https://spaces.at.internet2.edu/spaces/COmanage/pages/243078053/Searching+and+Filtering+PE>`_
in the Technical Manual.

1. Filtering
-------------

Filtering is available on most object index pages (People, Groups, COUs,
Enrollment Flows, and others). From the index page, use the filter form to
narrow the displayed list by specifying attribute values.

Filtering is scoped to a single object type and operates on the records
currently visible to the logged-in user.

2. Global Search
-----------------

:bdg-warning:`Redesigned in v5`

**Global Search** operates across the entire Registry, looking for matches
across multiple object types at once. It is accessible from the main Registry
navigation.

If an exact match is found, the matching record is displayed directly.
Otherwise, results are returned **grouped by object type** — a significant
improvement over earlier versions that makes it easier to identify what kind
of record matched and act on it accordingly.

Any CO Person may perform a Global Search within their CO. Results are
limited to records the searcher has permission to see.

.. TODO: Add screenshots showing Global Search results grouped by object type.

.. TODO: Once the interface distinction between filtering and searching is
   clearer, add an explicit section (with screenshots) showing where search
   is applied vs where filtering is used — for now this distinction is not
   always obvious in the UI.

The following object types are searched by Global Search:

- **Name** — given, middle, and family name (tokenized)
- **Email Address** — exact match only
- **Identifier** — exact, case-sensitive match only
- **Address** — street address (tokenized)
- **Group** — group name (tokenized)
- **Person Role** — title, organization, and organizational unit (tokenized)
- **Person** — via associated models
- **Enrollment Flow** — name (tokenized)
- **Department** — name (tokenized)
- **Service** — name (tokenized)
- **Telephone Number** — exact, case-sensitive match only

.. note::

   Searching currently only returns results associated with People or Person
   Roles. Searching records associated with External Identities is not yet
   supported.

Registry Plugins may also implement custom search backends that extend the
objects searchable via Global Search.

3. Searching by UUID and Change Request Identifier
---------------------------------------------------

:bdg-secondary:`Available: v5.2.0`

Global Search also supports finding **Clonable Objects** — configuration and
data objects that can be cloned across COs — by:

- **UUID** — the unique identifier assigned to each clonable object. A UUID
  search returns at most one result.
- **Change Request Identifier (CRI)** — an arbitrary string attached to
  clonable objects to group them by change request or ticket number. CRI
  searches are not subject to the search result limit described below.

See :ref:`ops-record-management` for more on Cloning and Change Request
Identifiers.

4. Search Result Limits
------------------------

To avoid performance issues with large datasets, Global Search limits the
number of results returned per object type. The default limit is **500 records
per model**, though a given search may return more or fewer depending on how
results are distributed across types.

The limit can be adjusted via **CO > Configuration > CO Settings > Global
Search Limit**.

5. Limiting Searched Models
----------------------------

For large deployments where Global Search performance is a concern, it is
possible to restrict the scope of Global Search to a narrower set of models.
When enabled via **CO > Configuration > Limit Global Search Scope**, only the
following models are searched:

- Email Address
- Identifier
- Name

This can significantly improve search performance at the cost of reduced
coverage.

6. Changes from v4
-------------------

- **Global Search has been significantly redesigned in v5.** Search results
  are now grouped by object type, making it much easier to identify what kind
  of record matched and act on it accordingly.

- **Type-ahead search** in individual search boxes throughout the interface
  has been improved in v5. This is distinct from Global Search and appears
  inline in the fields where it is available.

  .. TODO: Add screenshots documenting type-ahead search locations once the
     interface stabilizes.

- **UUID and Change Request Identifier searching** were added in v5.2.0,
  supporting workflows that use Cloning to manage configuration across COs.
