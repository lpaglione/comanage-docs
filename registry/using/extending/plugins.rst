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

**Plugin packages and the plugins inside them**

What you activate on the **Plugins** page is a *package*. A package
provides one or more plugins, and each of those plugins is of a particular
Plugin Type (see Section 3). For example:

- the **FileConnector** package provides **File Source** (an External
  Identity Source) and **File Provisioner** (a Provisioner);
- the **EnvSource** package provides **Env Source** (an External Identity
  Source), **Env Source Collector** (an Enrollment Flow Step) and **Env
  Source Detour** (a Traffic plugin).

Packages that connect Registry to an outside system in both directions are
often named "Connectors", but the name isn't a reliable guide to what a
package contains. The `4. Plugin Catalog`_ below lists every package that
ships with Registry and what it provides.

Three places use different names for the same thing, which can be
confusing at first:

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - Where
     - What it shows
     - Example
   * - The **Plugins** page (activation)
     - Package name only
     - FileConnector
   * - The **Plugin** menu when configuring something
     - ``Package.Plugin``
     - ``FileConnector.FileSources``
   * - The Technical Manual
     - Plugin name
     - File Source Plugin

The ``Package.Plugin`` form in configuration menus tells you exactly which
package a plugin comes from. That matters when two packages provide plugins
with similar names. For example, a locally installed package called
``MyCampusPlugins`` could also provide a file-based source, which would
appear as ``MyCampusPlugins.FileSources``.

.. note::

   The **Plugins** page currently shows Core or Available in a column
   labeled *Location*.

.. REVIEW: update or remove the note above once the UI label changes.

2. Installing and Activating Plugins
--------------------------------------

**Installing a Local Plugin**

To make a Local Plugin available to Registry, place the Plugin directory
under ``local/plugins/`` in your Registry installation. The appropriate method
depends on your deployment (containers, direct filesystem install, etc.). Once
the files are in place, Registry will automatically discover the Plugin when
the Plugin registry is next refreshed.

**Activating an Available or Local Plugin**

Activating a Plugin is done through the Registry administrative interface:

.. figure:: /comanage-files/registry_v5.2/configuration/Platform_Configuration_Menu.png
   :alt: The Platform-Wide Configuration menu from the Platform CO (COmanage)
   :width: 100%

1. Log in as a Platform Administrator.
2. Navigate to **COmanage CO > Configuration > Plugins**.
   Loading this page refreshes the Plugin registry, and any newly installed
   Local Plugins will appear in the list.
3. Find the Plugin you want to activate and select **Activate**.
   This applies the Plugin's database schema automatically.

.. tip::

   The Plugins list shows package names, not the plugins inside them. To
   find which package provides the plugin you need, see the
   `4. Plugin Catalog`_ below, or the page for that kind of plugin (for
   example, :ref:`ec-external-identity-sources`).

.. figure:: /comanage-files/registry_v5.2/configuration/Platform_Plugin_Configuration.png
   :alt: The Plugin configuration list. Available plugins can be activated by clicking on the "Gear" icon and selecting "activate".
   :width: 100%

A Plugin that is in use cannot be suspended. Before deactivating a Plugin,
remove any configurations that reference it.

**Activating Plugins from the command line** :bdg-secondary:`Available: v5.2.0`

Plugins can also be managed from the command line using the Plugin Command,
which is useful for scripted deployments or container initialization:

.. code-block:: bash

   cd $APP
   ./bin/cake Plugin -a activate -p PluginName
   ./bin/cake Plugin -a deactivate -p PluginName
   ./bin/cake Plugin -a applySchema -p PluginName

Multiple plugins can be specified as a comma-separated list with a single
``-p`` option. In v4, the command line was the only way to manage plugins;
in v5 the interface is the recommended approach for most administrators.

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
   :widths: auto

   * - Plugin Type
     - What it does
     - Where documented
   * - **API**

       :bdg-secondary:`Available: v5.2.0`
     - Implements domain-specific REST APIs on top of Registry's standard
       model-specific API, enabling higher-level, function-oriented endpoints
       for external integration.
     - :ref:`extend-api`
   * - **Authenticator**

       :bdg-secondary:`Available: v5.2.0`
     - Manages credentials issued by the CO, such as passwords and SSH keys.
       Combined with an Identifier, an Authenticator forms a credential that
       can prove a person's identity to an application or service.
     - :ref:`ec-authenticators`
   * - **Enrollment Flow Step**

       :bdg-secondary:`Available: v5.1.0`
     - Implements steps within an Enrollment Flow, such as collecting
       attributes, verifying email addresses, presenting terms and conditions,
       or managing approval decisions.
     - :ref:`lifecycle-enrollment-flows`
   * - **External Identity Source**

       :bdg-secondary:`Available: v5.0.0`
     - Connects Registry to external systems of record — LDAP directories,
       SQL databases, REST APIs, flat files, ORCID, and others — that provide
       authoritative data about people.
     - :ref:`ec-external-identity-sources`
   * - **Identifier Assignment**

       :bdg-secondary:`Available: v5.0.0`
     - Automatically generates and assigns identifiers (usernames, email
       addresses, and other identifier types) according to configurable rules
       and algorithms.
     - :ref:`ec-identifier-assignment`
   * - **Job**

       :bdg-secondary:`Available: v5.0.0`
     - Implements background tasks that run on a schedule or can be triggered
       on demand — syncing records, reconciling group memberships, processing
       deletions, and similar operational tasks.
     - Operations section *(in development)*
   * - **Pipeline Plugin (Flange)**

       :bdg-secondary:`Available: v5.0.0`
     - Transforms or processes data as it flows through a Pipeline —
       remapping attribute values, filtering records, or applying custom
       logic before data is written to Registry records.
     - :ref:`ec-pipelines`
   * - **Provisioner**

       :bdg-secondary:`Available: v5.0.0`
     - Pushes Registry data to downstream applications and services — LDAP
       directories, SQL databases, collaboration platforms, Kerberos KDCs,
       and other targets.
     - :ref:`ec-provisioning`
   * - **Server**

       :bdg-secondary:`Available: v5.0.0`
     - Adds support for additional server endpoint types beyond those provided
       by the Core Server Plugin (HTTP, LDAP, OAuth2, SMTP, SQL).
     - :ref:`ec-servers`
   * - **Traffic**

       :bdg-secondary:`Available: v5.1.0`
     - Intercepts the platform's authentication flow at specific points —
       before, during, or after login — enabling custom handling such as
       redirecting authentication events to external systems.
     - *(Not yet separately documented)*

4. Plugin Catalog
-----------------

These are the plugin packages that ship with Registry v5.2.0. Core packages
are always active; Available packages must be activated before their
plugins can be used.

.. list-table::
   :header-rows: 1
   :widths: 24 14 62

   * - Package (as on the Plugins page)
     - Core / Available
     - Plugins it provides (Plugin Type)
   * - **ApiConnector**
     - Available
     - :ref:`API Source <eis-api-source>` (External Identity Source);
       API Source Endpoint (API)
   * - **CoreApi**
     - Core
     - Match Callback (API)
   * - **CoreAssigner**
     - Core
     - Format Assigner, SQL Assigner (Identifier Assignment)
   * - **CoreEnroller**
     - Core
     - Approval Collector, Attribute Collector, Basic Attribute Collector,
       Email Verifier, Identifier Collector, Invitation Accepter
       (Enrollment Flow Step)
   * - **CoreJob**
     - Core
     - Adopter, Assigner, Deletion, Nester, Provisioner and Sync Jobs (Job)
   * - **CoreServer**
     - Core
     - HTTP, Match, OAuth2, SMTP and SQL Servers (Server)
   * - **EnvSource**
     - Core
     - :ref:`Env Source <eis-env-source>` (External Identity Source);
       Env Source Collector (Enrollment Flow Step);
       Env Source Detour (Traffic)
   * - **FileConnector**
     - Available
     - :ref:`File Source <eis-file-source>` (External Identity Source);
       File Provisioner (Provisioner)
   * - **HistoricPetitionViewer**
     - Available
     - No plugin types; a utility for viewing petitions migrated from v4
   * - **KerberosConnector**
     - Available
     - Kerberos Provisioner (Provisioner); Kerberos Server (Server)
   * - **OrcidSource**
     - Core
     - :ref:`ORCID Source <eis-orcid-source>` (External Identity Source);
       ORCID Source Collector (Enrollment Flow Step)
   * - **PasswordAuthenticator**
     - Available
     - Password Authenticator (Authenticator)
   * - **PipelineToolkit**
     - Available
     - Identifier Mapper, Person Role Mapper (Pipeline Plugin)
   * - **SqlConnector**
     - Available
     - :ref:`SQL Source <eis-sql-source>` (External Identity Source);
       SQL Provisioner (Provisioner)
   * - **SshKeyAuthenticator**
     - Core
     - SSH Key Authenticator (Authenticator)
   * - **TermsAgreer**
     - Core
     - T&C Agreement Collector (Enrollment Flow Step)
   * - **Transmogrify**
     - Available
     - No plugin types; the v4-to-v5 data migration tool (see
       :ref:`transitioning-transmogrification`)

.. REVIEW: this list was compiled from the v5.2.0 source code (each
   package's plugin.json). Check it against the Plugins page in a running
   instance, and confirm the descriptions of HistoricPetitionViewer and
   Transmogrify with the developers.

5. Changes from v4
------------------

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
