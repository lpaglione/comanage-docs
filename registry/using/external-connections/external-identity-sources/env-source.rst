.. _eis-env-source:

Env Source
==========

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Env Source creates an External Identity from the **attributes a person's
identity provider releases when they log in**. The web server's
authentication module (for example, the Shibboleth SP or
``mod_auth_openidc``) puts those attributes into environment variables, and
Env Source reads them. It is mainly used **during enrollment**: a person
signs up or accepts an invitation, logs in with their home organization's
credentials, and Registry records who they are from what the identity
provider asserted, rather than from what they typed. Optionally, Registry
can refresh that identity each time the person logs in again.

.. list-table:: Env Source at a glance
   :widths: 35 65
   :stub-columns: 1

   * - Provided by
     - The **EnvSource** plugin
   * - Plugin location
     - **Core**: always available; nothing to activate
   * - The EnvSource package also includes
     - **Env Source Collector** (an Enrollment Flow Step that collects the
       identity during enrollment) and **Env Source Detour** (a Traffic
       plugin that refreshes identities at login)
   * - Appears in the Plugin menu as
     - ``EnvSource.EnvSources`` (External Identity Source),
       ``EnvSource.EnvSourceCollectors`` (Enrollment Flow Step) and
       ``EnvSource.EnvSourceDetours`` (Traffic Detour)
   * - How data flows
     - Captured from the web server's environment at the moment the person
       authenticates. Registry doesn't contact the identity provider itself.
   * - Sync modes (the **Status** field)
     - None: there is no source to sync from between logins. Set the Status
       to **Manual**.
   * - Manual search
     - Yes, by exact Source Key, among identities already collected
   * - Available since
     - v5.1.0

.. REVIEW: confirm the dropdown labels above match the UI, and confirm with
   developers what "Manual" means for Env Source (fact sheet open question 1).

1. When to Use Env Source
-------------------------

Env Source suits situations where:

- people enroll themselves (self-signup) or accept an invitation, and log in
  through SAML or OIDC federation, for example via InCommon or eduGAIN;
- you want their name, email address, affiliation and identifiers to come
  from their identity provider rather than from a form;
- you'd like those details kept current each time they log in.

Env Source can only learn about people when they log in, so it isn't a way
to load a population in advance. For that, use
:ref:`File Source <eis-file-source>` or :ref:`SQL Source <eis-sql-source>`.

2. Enabling Env Source
----------------------

Env Source is a **Core** plugin, so there is nothing to activate. Its
behavior is set up in up to three places, depending on what you need:

.. list-table::
   :header-rows: 1
   :widths: 30 25 45

   * - Part
     - Configured by
     - Needed for
   * - **Env Source** (External Identity Source)
     - CO Administrator
     - Always: defines which environment variables to read
   * - **Env Source Collector** (Enrollment Flow Step)
     - CO Administrator
     - Collecting the identity during an Enrollment Flow
   * - **Env Source Detour** (Traffic Detour)
     - Platform Administrator, once per platform
     - Sync on Login

3. How Data Flows
-----------------

.. code-block:: text

   Person logs in ──▶ Identity provider (SAML / OIDC)
                              │  releases attributes
                              ▼
            Web server authentication module (e.g. Shibboleth SP)
                              │  sets environment variables
                              ▼
     Env Source Collector (in an Enrollment Flow)  or  Env Source Detour (at login)
                              │
                              ▼
              External Identity Source (Env Source)
                              │
                           Pipeline
                              ▼
                Person record and Person Roles

- **Getting attributes into the environment is the web server's job.**
  Configuring the authentication module, and arranging attribute release
  with identity providers, happens outside Registry. Deployments using
  ``mod_auth_openidc`` will need to adjust the expected variable names.
- **Each login identity becomes one External Identity with one role.**
  Affiliation, department, organization and title attach to the role;
  everything else attaches to the External Identity.
- **The Source Key is the person's authenticated identifier** (the
  equivalent of ``REMOTE_USER``). It must be mapped, and a given Source Key
  can belong to only one External Identity.
- **Types can't be carried in environment variables**, so Env Source
  applies default types that you choose.
- **Affiliation values must match** the *Database Value* of an Affiliation
  Type in the CO, for example ``member`` or ``student``.
- **The Pipeline does the rest**: matching to existing people, mapping
  attributes and creating Person Roles. See :ref:`ec-pipelines`.

4. Configuring Env Source
-------------------------

Before you start, make sure a suitable Pipeline exists
(:ref:`ec-pipelines`), and that your web server is already authenticating
users and setting environment variables.

1. Add a new External Identity Source as described in
   :ref:`ec-external-identity-sources`, selecting ``EnvSource.EnvSources``
   as the Plugin, and set the **Status** to **Manual**.
2. Save. The Env Source settings appear next.

.. REVIEW: screenshot of the Env Source configuration form
   (for example, connections/EnvSource_configuration.png).

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - What to decide
   * - **Environment Variable Map**
     - Which environment variable holds each attribute: name parts, email,
       telephone, address parts, affiliation, department, organization,
       title, and identifiers (ePPN, ePTID, ePUID, network, OIDC ``sub``,
       SAML pairwise-id, SAML subject-id). Most are optional, but a name
       and an affiliation should be mapped.
   * - **Identifier (Source Key)** \*
     - The variable holding the authenticated identifier. Required; Sync
       on Login depends on it.
   * - **Default types** (Name, Address, Email Address, Telephone Number,
       Default Affiliation)
     - The type given to each value collected, for example *Official* for
       names and email addresses.
   * - **Service Provider Multi Value Delimiter** \*
     - The character your authentication module uses to separate multiple
       values in one variable (for example, ``;`` for the Shibboleth SP).
   * - **Redirect on Duplicate**
     - Where to send someone who tries to enroll with an identity that is
       already in Registry. If blank, Registry shows its
       *duplicate-landing* page (see :ref:`personalization-mostly-static-pages`).
   * - **Sync on Login**
     - Whether to refresh this identity each time the person logs in. Also
       needs the Env Source Detour (see below).
   * - **Lookaside File**
     - For testing only: a file of variable values that Registry reads
       instead of the real environment. Not supported in production.

\* *Required*

.. REVIEW: confirm in the UI which fields show the red required asterisk.
   (The code requires the Source Key mapping and the delimiter.)

5. Using Env Source in an Enrollment Flow
-----------------------------------------

To collect an identity during enrollment, add an Enrollment Flow Step (see
:ref:`lifecycle-enrollment-flows`):

1. Set the **Plugin** to ``EnvSource.EnvSourceCollectors``.
2. Set the **Actor Type** to **Petitioner** for self-signup flows, or
   **Enrollee** for other flows.
3. Decide whether to **Enable Confirmation Page**, which shows the person
   the collected values to review before continuing.
4. On the plugin configuration page, select the Env Source configured
   above.

The step triggers a login if the person isn't already authenticated, so it
can help to tell enrollees beforehand that they'll be asked to log in.

**Duplicates.** If the identity is already attached to someone in Registry,
the enrollment is flagged as a duplicate and the person is redirected (see
*Redirect on Duplicate*, above). In rare cases where two enrollments for
the same person run at once, the duplicate is caught later, and the
Enrollment Flow's own redirect setting applies instead.

**Primary name.** If the person doesn't yet have a primary name in
Registry, the name collected by Env Source becomes their primary name.

6. Keeping Identities Current: Sync on Login
--------------------------------------------

Sync on Login refreshes an Env Source identity whenever its owner logs in.
It needs two steps, by two different administrators:

1. **Platform Administrator, once per platform**: from the COmanage CO, go
   to **ALL > Platform-Wide Configuration > Traffic Detours > Add a New
   Traffic Detour** and select ``EnvSource.EnvSourceDetours``. There are no
   further settings (an Edit page with a Save button appears; saving is
   optional).
2. **CO Administrator**: turn on **Sync on Login** in the Env Source
   configuration.

After that, when someone logs in, Registry finds their Env Source
identities in any CO, updates any attributes that changed, and reruns the
Pipeline.

.. note::

   This happens during the login redirect. If the Pipeline triggers slow
   work, such as provisioning to several targets, the person's browser may
   time out. In that case, Sync on Login may not be a good fit.

7. Searching
------------

Env Source can't search the identity provider. **Search Source** looks only
at identities Registry has already collected, by exact Source Key.

8. Technical Reference
----------------------

See
`Env Source Plugin <https://spaces.at.internet2.edu/spaces/COmanage/pages/327975001/Env+Source+Plugin>`_
in the Technical Manual. For setting up the web server side, see
`Managing Apache Web Server Environment Variables <https://spaces.at.internet2.edu/spaces/COmanage/pages/119930883/Managing+Apache+Web+Server+Environment+Variables>`_.

9. Changes from v4
------------------

- **Env Source returned in v5.1.0**; it wasn't available in v5.0.x.
- **Sync on Login** is now provided by a Traffic Detour that a Platform
  Administrator sets up once per platform.
- **The System of Record ID is now called the Source Key.**
- **Duplicate Handling Mode was removed.** A Source Key can now belong to
  only one active External Identity.
- **Login identifier flags were removed.** Login identifiers are now
  attributes of the Person record rather than of External Identities.
- **The Web Server Service Provider setting** was replaced in v5.2.0 by
  *Service Provider Multi Value Delimiter*, which lets you set the
  delimiter directly instead of choosing a Service Provider product.
