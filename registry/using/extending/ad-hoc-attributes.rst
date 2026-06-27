.. _extend-ad-hoc-attributes:

Ad Hoc Attributes
=================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Ad Hoc Attributes** are simple key/value pairs that can be attached to
person records when the standard data model does not capture all the information
your organization needs, but the overhead of a full structured data extension is
not warranted.

.. note::

   Ad Hoc Attributes are neither namespaced nor typed. They should not be used
   as a replacement for solutions leveraging properly designed structured data.
   Ad Hoc Attributes are most suitable for simple, local data extensions where
   the value of structured data is not worth the complexity.

For the full technical reference, see
`Registry Ad Hoc Attributes <https://spaces.at.internet2.edu/spaces/COmanage/pages/219918825/Registry+Ad+Hoc+Attributes>`_
in the Technical Manual.

1. Where Ad Hoc Attributes Can Be Attached
-------------------------------------------

Ad Hoc Attributes can be attached to:

- **People** — attached directly to the Person record
- **Person Roles** — attached to a specific Person Role within a CO
- **External Identities** — attached to an External Identity record
- **External Identity Roles** — attached to a role within an External Identity

2. Integration with Registry Features
--------------------------------------

Ad Hoc Attributes are available through several Registry integration points:

- **REST API** — Ad Hoc Attributes can be read and written via the Registry
  REST API, allowing external systems to set or retrieve custom data.
- **External Identity Source Plugins** — EIS Plugins can populate Ad Hoc
  Attributes when syncing data from an authoritative source.
- **Pipelines** — Pipelines can process and route Ad Hoc Attribute data as
  part of their data flow.
- **Provisioner Plugins** — Ad Hoc Attribute values are made available to
  Provisioner Plugins, so custom data can be exported to downstream systems.

3. Limitations
--------------

Ad Hoc Attributes are not currently validated in any way — Registry does not
enforce value formats, allowed values, or required fields for Ad Hoc Attributes.
Ad Hoc Attributes also do not support Enrollment Flows.

Given these limitations, Ad Hoc Attributes work best for:

- Storing temporary or transitional data during migrations
- Passing custom flags or metadata between an EIS Plugin and a Provisioner Plugin
- Capturing organization-specific notes or identifiers that have no equivalent
  in the standard data model

4. Changes from v4
------------------

- **People attachment** :bdg-secondary:`Available: v5.0.0` — As of Registry
  v5.0.0, Ad Hoc Attributes can be attached directly to a Person record. In
  earlier versions, Ad Hoc Attributes could only be attached to Person Roles
  and External Identity records.
