.. _using-extending:

Extending Registry
==================

Part of the power of COmanage Registry is its ability to be extended beyond
the features and functionality built into the core software. Extensions allow
you to connect Registry to the systems your organization uses, adapt it to your
data model, integrate it with downstream services, and automate tasks specific
to your environment.

1. Plugins
----------

Registry's primary extension mechanism is **Plugins** — self-contained modules
that add new capabilities. Plugins follow a consistent pattern: each Plugin
implements one or more **Plugin Types**, and an administrator instantiates the
Plugin within a CO to create a working configuration.

Registry ships with Core Plugins (always active) and Available Plugins (activated
as needed). Local Plugins — community-contributed, vendor-supplied, or plugins
written specifically for your organization — can be installed on the filesystem
and activated through the same administrative interface.

.. button-ref:: extend-plugins
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Plugins →

2. Data Model Customization
----------------------------

Registry's default data model fits many organizations well, but you may need
to customize or extend it to capture the specifics of your community.

**Types** control how Registry categorizes multi-valued attributes — names,
email addresses, identifiers, addresses, telephone numbers, URLs, and
affiliations. Types are defined per-CO, so your organization controls both the
category options that appear in the interface and the values used in data exports
and provisioning. (In v4, these were called Extended Types.)

.. button-ref:: extend-types
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Types →

**Ad Hoc Attributes** are simple key/value pairs that can be attached to People,
Person Roles, and External Identities when the standard data model is
insufficient but the overhead of a full structured extension is not warranted.
Ad Hoc Attributes are available via the REST API and can be handled in Pipeline
processing and Provisioner Plugins.

.. button-ref:: extend-ad-hoc-attributes
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Ad Hoc Attributes →

3. Data Filters
---------------

Data filtering in Registry means transforming or conditionally processing
attribute values as data flows through a Pipeline — remapping identifier values,
normalizing formats, or selectively acting on records based on attribute content.
In Registry v5, this is implemented through Pipeline Plugins (Flanges).

.. button-ref:: extend-data-filters
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Data Filters →

4. REST API
-----------

Registry provides a REST API for programmatic access to identity data, enabling
integration with external systems, automation scripts, and custom tooling. The
API includes a standard Model-Specific API covering all of Registry's core data
objects, and Plugin-Implemented APIs (available as of v5.2.0) that provide
higher-level, domain-specific endpoints.

.. button-ref:: extend-api
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about the REST API →

----

Pages in This Section
----------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   extending/plugins
   extending/types
   extending/ad-hoc-attributes
   extending/data-filters
   extending/api
