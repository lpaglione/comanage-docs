.. _eis-api-source:

API Source
==========

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

API Source lets an external system **send** person records to Registry
through a REST API, as changes happen. It works the other way round from the
other sources. Registry doesn't fetch data on a schedule; the source system
(or integration middleware) calls Registry each time a record is added,
changed or removed, and Registry creates or updates the matching External
Identity straight away.

.. list-table:: API Source at a glance
   :widths: 35 65
   :stub-columns: 1

   * - Provided by
     - The **ApiConnector** plugin
   * - Plugin location
     - **Available**: a Platform Administrator must activate ApiConnector
       before API Source can be used
   * - Activating ApiConnector also enables
     - **API Source Endpoint** (an API plugin that provides the REST endpoint
       the source system calls). You need both to use API Source.
   * - Appears in the Plugin menu as
     - ``ApiConnector.ApiSources`` (External Identity Source) and
       ``ApiConnector.ApiSourceEndpoints`` (API)
   * - How data flows
     - The source system **pushes** records to Registry over HTTPS.
       Registry doesn't contact the source system.
   * - Also requires
     - An **API User** for the source system to authenticate as (see
       :ref:`extend-api`)
   * - Sync modes (the **Status** field)
     - Not applicable: records arrive when the source system sends them,
       so Sync Jobs have nothing to fetch
   * - Manual search
     - Yes, by exact Source Key, among records already received
   * - Available since
     - v5.0.0. The endpoint has been configured through an API plugin since
       v5.2.0.

.. REVIEW: confirm both dropdown labels above match the UI.

1. When to Use API Source
-------------------------

API Source suits situations where:

- changes in the source system should reach Registry within moments, not
  at the next scheduled sync;
- you already have integration middleware (an ESB, iPaaS or event
  pipeline) that can call a REST API;
- someone on the source side can build and maintain the integration.

If a scheduled feed is good enough, :ref:`SQL Source <eis-sql-source>` or
:ref:`File Source <eis-file-source>` needs no development work on the source
side.

2. Enabling API Source
----------------------

API Source is not available until its plugin package is activated.

1. As a Platform Administrator, go to **COmanage CO > Configuration > Plugins**
   (see :ref:`extend-plugins`).
2. Find **ApiConnector** and activate it.

.. REVIEW: screenshot of the ApiConnector row in the Plugins list
   (for example, configuration/plugin_activate_ApiConnector.png).

**ABOUT ApiConnector**: ApiConnector is a package containing two plugins
that work as a pair. **API Source** is the External Identity Source that
receives records and passes them to a Pipeline. **API Source Endpoint** is
the API that the source system actually calls. Unlike the other "Connector"
packages, you configure *both* parts to use API Source.

.. note::

   The Plugins list shows package names (ApiConnector), not the plugins
   inside them (API Source). This page and the plugin catalog on
   :ref:`extend-plugins` map one to the other.

3. How Data Flows
-----------------

.. code-block:: text

   Source system or middleware
            │  HTTPS PUT / DELETE, authenticated as an API User
            ▼
   API Source Endpoint (API) ──▶ External Identity Source (API Source)
                                        │
                                     Pipeline
                                        ▼
                         Person record and Person Roles

- **Each call is about one person**, identified by the source system's own
  ID for that record (the *SORID*, which Registry calls the Source Key).
  The SORID is part of the URL.
- **PUT adds or updates** a record, **DELETE removes** it, and **GET**
  returns what Registry currently holds for it.
- **Records are sent as JSON**, in a format based on the TAP Attribute
  Dictionary. Because of that, the Technical Manual uses the TAP term
  *System of Record* (SoR) alongside *External Identity Source*; the two
  mean the same thing here.
- **Registry keeps a copy of each record it receives.** That copy is what
  Search Source looks through, and what GET returns.
- **The Pipeline does the rest**: matching records to existing people,
  mapping attributes and creating Person Roles. See :ref:`ec-pipelines`.

4. Configuring API Source
-------------------------

Before you start, make sure a suitable Pipeline exists
(:ref:`ec-pipelines`), and create (or choose) the **API User** the source
system will authenticate as (:ref:`extend-api`).

Setting up API Source has two parts.

**Part 1: the External Identity Source**

1. Add a new External Identity Source as described in
   :ref:`ec-external-identity-sources`, selecting ``ApiConnector.ApiSources``
   as the Plugin.
2. Enter a **System of Record Label**: a short name for the source system,
   such as ``hr``. It becomes part of the endpoint URL, and identifies
   which source a pushed record belongs to.
3. Save. There are no further API Source settings to choose; the page
   shows that it operates in **Push Mode**.

**Part 2: the API endpoint**

1. Go to **ALL > APIs > Add a New API**.
2. Select ``ApiConnector.ApiSourceEndpoints`` as the Plugin, and the API
   User from above.
3. Save, then select the API Source you created in Part 1.
4. The page now shows the **exact endpoint URL**. Give it, together with
   the API User's credentials, to the people building the integration.

.. REVIEW: screenshots of the API Source configuration page and the API
   Source Endpoint configuration page showing the endpoint URL.

The endpoint URL has this form:

.. code-block:: text

   https://<registry-host>/registry-pe/api/apisource/<apisourceid>/v2/sorPeople/<sorlabel>/<sorid>

where ``<apisourceid>`` identifies the External Identity Source (not the
API), ``<sorlabel>`` is the System of Record Label, and ``<sorid>`` is the
source system's ID for the record.

**Things to plan for**

- **Share the Technical Manual pages with the integration developers.** The
  message format, HTTP response codes and formatting rules (for example,
  how to clear a single-valued attribute, and the codes used for role
  status) are all specified there.
- **A 202 response** means Registry accepted the record but it needs
  further processing, possibly by an administrator. The integration should
  log these so they can be followed up.

.. REVIEW: confirm with developers whether the External Identity Source
   Status (for example, Disabled) affects records pushed through the API
   (fact sheet open question 2).

5. Searching
------------

Because there's nothing to fetch, Sync Jobs and the sync modes on
:ref:`ec-external-identity-sources` don't drive API Source; records are
created and updated as they arrive.

When you use **Search Source**, enter a Source Key (SORID) exactly. The
search only covers records Registry has already received; it doesn't query
the source system.

6. Related
----------

- The **API Source Endpoint** API plugin, configured in Part 2 above, is
  part of the same package. For APIs in Registry generally, see
  :ref:`extend-api`.

.. REVIEW: the old HR API Source recipe draft was removed (Oct 2026). A Getting
   Started lesson (connections/source-hr-api) is planned but unpublished until
   API Source works in 5.2.0. Add a link here when it publishes.

7. Technical Reference
----------------------

See, in the Technical Manual:

- `API Source Plugin <https://spaces.at.internet2.edu/spaces/COmanage/pages/283967884/API+Source+Plugin>`_
  for the modes and data format;
- `API Source Endpoint API Plugin <https://spaces.at.internet2.edu/spaces/COmanage/pages/338788442/API+Source+Endpoint+API+Plugin>`_
  for the endpoint, actions, response codes and message format.

8. Changes from v4
------------------

- **The endpoint is now an API plugin** (v5.2.0). Push Mode is set up by
  adding an API with ``ApiConnector.ApiSourceEndpoints``, rather than as
  part of the source itself.
- **Only Push Mode is available.** The Technical Manual lists Pull and Poll
  modes as not yet implemented.
- **Message Meiosis is no longer supported**, because one External Identity
  can now carry several roles directly.
- **Timestamps no longer use the** ``Z`` **notation.** Strictly speaking,
  this departs from the TAP API and may change in a future release.
