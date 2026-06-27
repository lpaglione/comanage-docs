.. _extend-api:

REST API
========

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry provides a REST API for programmatic access to Registry data and
operations, enabling integration with external systems, automation scripts,
and custom tooling.

For the full reference, including endpoint documentation for each model, see
`Registry PE REST API <https://spaces.at.internet2.edu/spaces/COmanage/pages/338788391/Registry+PE+REST+API>`_
and `Model Specific REST API v2 <https://spaces.at.internet2.edu/spaces/COmanage/pages/141821501/Model+Specific+REST+API+v2>`_
in the Technical Manual.

1. API Layers
--------------

The Registry REST API is made up of two layers:

**Model-Specific API**
   The standard API, available at ``/api/v2/``, that provides fine-grained
   read and write access to Registry's data models — People, Groups, COUs,
   Identifiers, Person Roles, External Identities, Types, and more. Each
   model has its own set of endpoints following a consistent URL pattern with
   standard CRUD operations (Add, Edit, Delete, View one, View all).

   The Model-Specific API is designed for granular, per-object access. It is
   not optimized for bulk transactions — for large-scale data operations, an
   External Identity Source is a better approach.

**Plugin-Implemented APIs** :bdg-success:`New in v5` :bdg-secondary:`Available: v5.2.0`
   Higher-level APIs implemented by API Plugins, providing domain-specific or
   function-oriented endpoints beyond what the model-specific API exposes. This
   includes the ability to expose custom data and operations introduced by
   specific plugins — for example, a plugin that manages a custom data model can
   also provide its own API endpoints for that data. Each Plugin-implemented API
   must be instantiated within a CO before use.

.. TODO: Confirm with development team: do Plugin-Implemented APIs specifically
   cover custom data models created by plugins (e.g., provisioner or connector
   plugins that store their own data)? Or are they more narrowly scoped to
   "functional" endpoints? Clarify scope and update this description accordingly.

2. Authentication and API Users
---------------------------------

API authentication uses HTTP Basic Auth over HTTPS — a username and generated
API Key (not a self-selected password) transmitted with each request. API Keys
are displayed once at generation time and hashed for storage; a new key can be
regenerated if needed.

There are three types of API Users, each with different scope:

- **Platform API Users** — created within the COmanage CO; have full access
  to the API across all COs on the platform.
- **Privileged CO API Users** — created within a specific CO and designated
  as Privileged; have full API access within their CO.
- **Unprivileged CO API Users** — created within a CO but not designated as
  Privileged; have no default API access, but can be granted specific access
  by individual plugins.

API Users are managed by a CO Administrator via **ALL > API Users**. Usernames
must be prefixed with the CO number and a dot (e.g., ``co_2.apiuser``). Validity
dates and IP address constraints can be applied to API Users.

3. Instantiating a Plugin-Implemented API
------------------------------------------

Plugin-Implemented APIs (available as of v5.2.0) must be instantiated before
they can be used:

1. Create an API User as described above.
2. Navigate to **ALL > APIs > Add a New API**.
3. Select the appropriate API Plugin, per the Plugin-specific documentation.
4. Select the API User.
5. Once saved, complete any Plugin-specific configuration.

4. Changes from v4
-------------------

- **REST API v1 → Model Specific API v2.** The v4 REST API v1, which provided
  table-level access to Registry data, is the predecessor of the v5 Model
  Specific API v2. The v2 API is JSON-only (XML is no longer supported) and
  adds pagination, changelog/archived record access, and several new models.

- **The v4 Core API** provided higher-level, object-oriented access (for
  example, retrieving all data related to a Person record in one call). An
  equivalent object-level API is planned for v5 but is not yet available.

.. TODO: Confirm with development team: what is the current status of the v5
   Core API equivalent? Which version is it targeted for? Add a
   "Coming to v5" note with version badge once confirmed.

- **The VOOT API is no longer supported** in v5.

- **The API is now extensible via Plugin-Implemented APIs** (v5.2.0). Plugins
  can implement their own API endpoints for custom data and domain-specific
  operations, allowing the Registry API to grow with the plugins you deploy.
  This is new in v5 — the v4 API did not support plugin-level extension.
