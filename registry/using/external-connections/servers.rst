.. _ec-servers:

Servers
========

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


Many Registry features need to communicate with external server endpoints —
an LDAP directory for provisioning, a database for identity source data, an
OAuth2 provider for API authentication, an SMTP relay for sending notifications.
Rather than embedding connection details into each individual plugin
configuration, Registry maintains a **Server Registry** where you define these
endpoints once and reference them by name everywhere else.

This has a practical benefit: when a server hostname, port, or credential
changes, you update it in one place and every configuration that references
it picks up the change automatically.

For the full technical reference, see
`Registry Servers <https://spaces.at.internet2.edu/spaces/COmanage/pages/256938867/Registry+Servers>`_
in the Technical Manual.

Adding a Server
----------------

Servers are managed via **ALL > Servers > Add a New Server**.

When adding a server:

1. Select **CoreServer** as the Plugin (unless using a server type provided by
   a third-party plugin such as Kerberos).
2. Select the **Server Type** from the list (HTTP, Match, OAuth2, SMTP, SQL).
3. Provide a name and the type-specific configuration.

The sections below describe the configuration for each server type.

HTTP Servers
-------------

:bdg-secondary:`Available: v5.1.0` HTTP Servers define connections to resources accessed via HTTP or HTTPS. They
are used by any plugin or feature that needs to make web requests to a
configured endpoint — including the API Source External Identity Source Plugin
and, as a foundation, Match Servers (see below).

**Configuration:**

- **URL** — the endpoint URL (required; the format depends on what the Server
  is used for)
- **Username / Password** — authentication credentials (optional; some
  resources do not require authentication)
- **Authentication Type** — how to authenticate to the server
- **Disable SSL Certificate Verification** — useful for test environments where
  valid certificates are not in place; not recommended for production

Match Servers
--------------

:bdg-secondary:`Available: v5.1.0` Match Servers configure connections to servers implementing the
`TAP Identity Match Protocol <https://github.internet2.edu/api-schema/id-match-api/blob/draft/id-match-api.adoc>`_.
They are used when the Pipeline External Match Strategy is configured to call
out to an external identity matching service (such as Internet2 Match) to
determine whether an incoming record corresponds to an existing Person.

Because the Match API is built on HTTP, Match Server configuration builds on
HTTP Server configuration — all the HTTP Server fields apply, plus additional
**Match Server Attributes** that define how attributes are mapped for matching
queries. See
`Identity Match Integration <https://spaces.at.internet2.edu/spaces/COmanage/pages/338788374/Identity+Match+Integration>`_
in the Technical Manual for details on attribute configuration.

**Plugin:** ``CoreServer.MatchServers``

.. note::

   Match Server Attributes configuration (mapping attributes for matching queries) is available as of v5.2.0.

OAuth2 Servers
---------------

:bdg-secondary:`Available: v5.2.0` OAuth2 Servers configure connections to OAuth 2.0 authorization servers. They
are used by plugins that authenticate to external APIs via OAuth2 — for example,
the ORCID Source Plugin uses OAuth2 to authenticate to the ORCID Member API.

**Configuration:**

- **Server URL** — the OAuth2 provider or API endpoint URL (required)
- **Access Token Grant Type** — Authorization Code or Client Credentials
- **Client ID / Client Secret** — the application credentials registered with
  the OAuth2 provider (required; keep the Client Secret secure)
- **Scopes** — the OAuth2 scopes required (comma- or space-separated if
  multiple)
- **Redirect URI** — system-defined; cannot be changed; must be registered with
  your OAuth2 provider before obtaining tokens

After saving the configuration, use the **Obtain New Token** link to
authenticate and retrieve an access token. Always save the configuration before
attempting to obtain a token.

.. note::

   Register the Redirect URI shown in Registry with your OAuth2 service provider
   before your users attempt to authenticate. Failure to do this will result in
   authentication errors.

**Plugin:** ``CoreServer.Oauth2Servers``

SMTP Servers
-------------

SMTP Servers configure Registry's outgoing email relay. Registry sends
notifications, enrollment confirmations, and other messages through this
server. Every Registry deployment that sends outgoing email needs at least one
SMTP Server configured.

**Configuration:**

- **Hostname** — the mail relay server hostname (required)
- **Port** — the SMTP port; 587 is generally recommended; may vary by provider
- **TLS** — use of TLS is strongly recommended
- **Username / Password** — relay authentication credentials (optional; some
  servers permit sending by IP address without authentication)
- **Default From Address** — the sender address for outgoing Registry mail
  (required; many relay services will overwrite this if it doesn't match the
  relay account)
- **Default Reply-To Address** — where replies should go (required; can be
  overridden in specific Message Templates)
- **Delivery Override** — redirect all outgoing mail to a specific address
  during testing, rather than sending to actual recipients; see
  `Configuring Registry Outgoing Email <https://spaces.at.internet2.edu/spaces/COmanage/pages/297862066/Configuring+Registry+Outgoing+Email>`_
  in the Technical Manual

**Plugin:** ``CoreServer.SmtpServers``

SQL Servers
------------

SQL Servers configure connections to external SQL databases. They are used by
plugins that read from or write to a database — including the SQL Source
External Identity Source Plugin, SQL Provisioner Plugin, and SQL Identifier
Assignment Plugin.

.. note::

   SQL Server configuration applies only to external database integrations —
   sources you are connecting to for identity data or provisioning targets. It
   does not apply to Registry's own application database, which is configured
   separately during installation.

**Configuration:**

- **RDBMS Type** — the database type (Postgres, MySQL/MariaDB, Oracle, others)
- **Hostname, port, database name, credentials** — standard connection parameters

Postgres and MySQL/MariaDB are the best-supported database types. Oracle is
listed as an option but requires additional steps to enable — see
`Registry SQL Servers - Enabling Oracle Support <https://spaces.at.internet2.edu/spaces/COmanage/pages/305856600/Registry+SQL+Servers+-+Enabling+Oracle+Support>`_
in the Technical Manual. Support for other database types depends on community
contributions.

**Plugin:** ``CoreServer.SqlServers``

Kerberos Servers
-----------------

Kerberos Servers are provided by the **Kerberos Provisioner Plugin** (not the
CoreServer plugin) and configure connections to Kerberos Key Distribution
Centers. They are used when provisioning Authenticator data to a Kerberos
infrastructure.

Kerberos Servers are available when the Kerberos Provisioner Plugin is
installed. See the plugin documentation for configuration details.

Changes from v4
----------------

If you are migrating from Registry v4, the following changes apply:

- **Servers are now implemented as Plugins** rather than as core models. This
  means the Server Registry is extensible — new server types can be added by
  installing additional Server Plugins.

- **HTTP, Match, and OAuth2 Servers** all existed in v4. They are available
  in v5 via the CoreServer Plugin — HTTP and Match as of v5.1.0, OAuth2 as of
  v5.2.0. Match Server Attributes configuration was added in v5.2.0.

- **SQL and SMTP Servers** also existed in v4 and are available in v5. In v5,
  all server types are managed centrally through the Server Registry at
  ALL > Servers.

- **KDC (Kerberos) Servers** existed in v4 as of v4.4.0. In v5, Kerberos
  server configuration is handled via the Kerberos Provisioner Plugin rather
  than as a CoreServer type.

- **Kafka Servers** existed in v4 but are not currently included in v5.
