.. _extend-plugins:

Plugins
=======

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry Plugins are modular extensions that add new capabilities to the
application. A Plugin implements one or more **Plugin Types** (described in
Section 3), and an administrator **instantiates** the Plugin within a CO to
create a working configuration.

For the full technical reference, see
`About Registry PE Plugins <https://spaces.at.internet2.edu/spaces/COmanage/pages/256939401/About+Registry+PE+Plugins>`_
in the Technical Manual.

1. Plugin Architecture
-----------------------

Registry organizes Plugins into three tiers based on how they are distributed
and managed:

**Core Plugins**
   Shipped with Registry and always active. Core Plugins provide foundational
   functionality and cannot be disabled. They require no installation or
   activation steps.

**Available Plugins**
   Shipped with Registry but not active by default, because they are less
   widely needed or have external dependencies that not all deployments require.
   A Platform Administrator must explicitly activate an Available Plugin before
   it can be used.

**Local Plugins**
   Plugins obtained from other sources — community-contributed plugins,
   vendor-supplied plugins, or plugins you write yourself. Local Plugins must
   be installed on the Registry filesystem before they can be activated.

A single Plugin can implement multiple Plugin Types. For example, a Plugin
that connects Registry to a specific downstream application might implement
both the Provisioner type and the External Identity Source type, making it a
"Connector."

2. Installing and Activating Plugins
--------------------------------------

**Installing a Local Plugin**

To make a Local Plugin available to Registry, place the Plugin directory
under ``local/plugins/`` in your Registry installation. The appropriate method
depends on your deployment (containers, direct filesystem install, etc.). Once
the files are in place, Registry will automatically discover the Plugin when
the Plugin registry is next refreshed.

**Activating an Available or Local Plugin**

Activating a Plugin is done through the Registry administrative interface —
no command-line steps are required:

1. Log in as a Platform Administrator.
2. Navigate to **COmanage CO > Configuration > Plugins**.
   Loading this page refreshes the Plugin registry, and any newly installed
   Local Plugins will appear in the list.
3. Find the Plugin you want to activate and select **Activate**.
   This applies the Plugin's database schema automatically.

A Plugin that is in use cannot be suspended. Before deactivating a Plugin,
remove any configurations that reference it.

.. note::

   For developer guidance on writing Registry Plugins, see
   `Writing Registry PE Plugins <https://spaces.at.internet2.edu/spaces/COmanage/pages/250251876/Writing+Registry+PE+Plugins>`_
   in the Technical Manual.

3. Plugin Types
----------------

Registry supports the following Plugin Types. Several types are covered in
detail in other sections of this guide — this table provides an overview and
links to where each is documented.

.. list-table::
   :header-rows: 1

   * - Plugin Type
     - What it does
     - Where documented
   * - :bdg-secondary:`Available: v5.2.0`
       **API**
     - Implements domain-specific REST APIs on top of Registry's standard
       model-specific API, enabling higher-level, function-oriented endpoints
       for external integration.
     - :ref:`extend-api`
   * - :bdg-secondary:`Available: v5.2.0`
       **Authenticator**
     - Manages credentials issued by the CO, such as passwords and SSH keys.
       Combined with an Identifier, an Authenticator forms a credential that
       can prove a person's identity to an application or service.
     - :ref:`ec-authenticators`
   * - :bdg-secondary:`Available: v5.1.0`
       **Enrollment Flow Step**
     - Implements steps within an Enrollment Flow, such as collecting
       attributes, verifying email addresses, presenting terms and conditions,
       or managing approval decisions.
     - :ref:`lifecycle-enrollment-flows`
   * - :bdg-secondary:`Available: v5.0.0`
       **External Identity Source**
     - Connects Registry to external systems of record — LDAP directories,
       SQL databases, REST APIs, flat files, ORCID, and others — that provide
       authoritative data about people.
     - :ref:`ec-external-identity-sources`
   * - :bdg-secondary:`Available: v5.0.0`
       **Identifier Assignment**
     - Automatically generates and assigns identifiers (usernames, email
       addresses, and other identifier types) according to configurable rules
       and algorithms.
     - :ref:`ec-identifier-assignment`
   * - :bdg-secondary:`Available: v5.0.0`
       **Job**
     - Implements background tasks that run on a schedule or can be triggered
       on demand — syncing records, reconciling group memberships, processing
       deletions, and similar operational tasks.
     - Operations section *(in development)*
   * - :bdg-secondary:`Available: v5.0.0`
       **Pipeline Plugin (Flange)**
     - Transforms or processes data as it flows through a Pipeline —
       remapping attribute values, filtering records, or applying custom
       logic before data is written to Registry records.
     - :ref:`ec-pipelines`
   * - :bdg-secondary:`Available: v5.0.0`
       **Provisioner**
     - Pushes Registry data to downstream applications and services — LDAP
       directories, SQL databases, collaboration platforms, Kerberos KDCs,
       and other targets.
     - :ref:`ec-provisioning`
   * - :bdg-secondary:`Available: v5.0.0`
       **Server**
     - Adds support for additional server endpoint types beyond those provided
       by the Core Server Plugin (HTTP, LDAP, OAuth2, SMTP, SQL).
     - :ref:`ec-servers`
   * - :bdg-secondary:`Available: v5.1.0`
       **Traffic**
     - Intercepts the platform's authentication flow at specific points —
       before, during, or after login — enabling custom handling such as
       redirecting authentication events to external systems.
     - *(Not yet separately documented)*

4. Changes from v4
-------------------

- **Plugin activation is now entirely UI-based.** In v4, enabling a non-core
  Plugin required creating a symlink and running command-line tools to clear
  caches and update the database schema. In v5, Available and Local Plugins
  are activated through the Registry administrative interface
  (COmanage CO > Configuration > Plugins), which also applies the database
  schema automatically.

- **A single Plugin can implement multiple Plugin Types** (polymorphic
  plugins), which was not supported in v4.

- **Several v4 plugin types have changed or been replaced.** The Cluster
  plugin type (for managing accounts on Unix-style systems) is not present
  in v5 — this use case is now handled through Provisioner Plugins. Dashboard
  Widgets are not currently listed as a supported plugin type in v5.

- **Plugin-implemented APIs are available as of v5.2.0**, extending the REST
  API with domain-specific endpoints via API Plugins.
