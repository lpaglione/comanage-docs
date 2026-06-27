.. _extend-data-filters:

Data Filters
============

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Data filtering refers to transforming, remapping, or conditionally processing
attribute values as data flows through Registry — for example, normalizing
identifier formats, remapping affiliation values from an authoritative source
to your CO's terminology, or selectively acting on records based on attribute
content.

In Registry v5, data filtering is implemented through **Pipeline Plugins
(Flanges)** — the Pipeline Plugin type that executes within a Pipeline to
transform data before it is written to Registry records.

For full documentation on how to configure and use Pipeline Plugins for data
filtering, see :ref:`ec-pipelines`.

1. How Data Filtering Works in v5
----------------------------------

Data filtering happens within the Pipeline processing flow:

1. Data enters Registry from an External Identity Source (or another Pipeline
   trigger event).
2. The Pipeline applies any configured Pipeline Plugins (Flanges), which can
   transform attribute values, filter records, or apply custom logic.
3. The transformed data is then written to the Registry data model (People,
   Person Roles, Identifiers, etc.) according to the Pipeline's rules.

This means the configuration for data filtering lives in the Pipeline
configuration, not in a separate filter management interface.

2. Available Pipeline Plugins
------------------------------

The following Pipeline Plugins (Flanges) ship with Registry for data
transformation purposes:

- **Identifier Mapper Plugin** — Remaps identifier values from one Identifier
  Type to another, or transforms identifier formats.
- **Person Role Mapper Plugin** — Maps Person Role attributes such as affiliation
  values from the source's terminology to your CO's configured Types.

Additional Pipeline Plugins may be available from the community or can be
written as Local Plugins. See :ref:`extend-plugins` for more on Plugin types
and activation.

3. Changes from v4
-------------------

In v4, Data Filters were a distinct feature that could be configured outside
of Pipelines. In v5, this capability is integrated into the Pipeline framework
as Pipeline Plugins (Flanges). If you are migrating from v4, review your
existing Data Filter configurations and identify the equivalent Pipeline Plugin
configuration in v5.
