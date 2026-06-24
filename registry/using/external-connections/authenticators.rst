.. _ec-authenticators:

Authenticators
===============

An **Authenticator** is a credential that your collaboration manages directly —
a password, an SSH key, or another credential type — that Registry stores and
provisions to downstream systems. Unlike identity attributes that flow in from
external sources, Authenticators belong to the collaboration itself: they are
issued, managed, and revoked by the CO, and attached to Person records (not
External Identities).

Registry does not use Authenticators to validate logins to Registry itself. Its
role is to *store* Authenticators (or route them through to a downstream system)
and to *provision* them outward via the Provisioning infrastructure, so that
target systems — an LDAP directory, a Kerberos KDC, a unix server — have the
credential data they need. This means Authenticators and Provisioning work
together: you configure an Authenticator type, and a Provisioner Plugin writes
it to the appropriate target.

Authenticators were introduced in Registry v5.2.0. For the full technical
reference, see
`Registry Authenticators <https://spaces.at.internet2.edu/spaces/COmanage/pages/350160332/Registry+Authenticators>`_
in the Technical Manual.

----

.. contents:: On this page
   :local:
   :depth: 1

----

Terminology
------------

Registry uses several related terms when discussing Authenticators:

**Authenticator Plugin**
   A Registry Plugin implementing the interfaces for a specific credential type
   (Password, SSH Key, etc.).

**Authenticator Backend**
   An instantiated Authenticator Plugin — the Plugin with a specific
   configuration applied. For example, a Password Authenticator Backend might
   be configured for domain A, and a second one for domain B.

**Authenticator**
   A specific credential instance attached to a Person. For example, a given
   person's password in domain A.

**Credential**
   An Authenticator combined with an Identifier — the package of "who you are"
   plus "how you prove it."

Single-Valued vs. Multi-Valued Authenticators
----------------------------------------------

Authenticator Backends can be single-valued or multi-valued, depending on the
Plugin.

A **single-valued** Backend allows only one credential per Person. The Password
Authenticator Plugin is single-valued: each Backend supports one password per
Person. If you need passwords for multiple domains, instantiate the Plugin
multiple times — once per domain.

A **multi-valued** Backend allows a Person to have multiple credentials of the
same type. The SSH Key Authenticator Plugin is multi-valued: a single Backend
can hold as many SSH keys as a Person needs. In general, there is no reason to
instantiate a multi-valued Plugin more than once, though it is technically
possible.

Administrative Operations
--------------------------

Registry supports the following operations on a Person's Authenticators:

**Manage**
   Set or change the Authenticator (for example, assign a new password). Can
   be performed by an administrator or, where self-service is enabled, by the
   Person themselves.

**Lock**
   Prevent the Authenticator from being changed or used. When locked, the
   Authenticator is excluded from provisioning — downstream systems will not
   receive the credential data. For multi-valued Backends, locking applies to
   the entire Backend for that Person (all credentials, including the ability
   to add new ones).

   Only administrators can lock an Authenticator.

**Unlock**
   Re-enable the Authenticator. If a value was previously set, it is restored.
   For multi-valued Backends, unlocking applies to the entire Backend.

   Only administrators can unlock an Authenticator.

**Reset**
   Clear the current Authenticator. Once reset, the Person can set a new value
   (if the Authenticator is not also locked). This operation is not available
   for multi-valued Backends, though individual values can be edited or deleted.

   Only administrators can reset an Authenticator. Note that a locked
   Authenticator can be reset, but will remain locked after the reset.

After any of these operations, the provisioning infrastructure runs so that
Provisioner Plugins can take appropriate action in the downstream systems.
Authenticators can also be manually reprovisioned using the standard
reprovisioning process.

Configuration
--------------

Authenticators are configured via **Configuration > Authenticators**, where you
instantiate one or more Authenticator Backends by selecting a Plugin and
providing the configuration that Plugin requires.

**Pass Through Provisioning** *(experimental)*
   When supported by the Plugin, an Authenticator can be configured to pass
   credentials directly to a downstream system without storing them in the
   Registry database. This allows, for example, a Password Authenticator to
   collect a password and send it to a Kerberos KDC without the password ever
   being persisted in Registry.

   Pass Through Provisioning involves tradeoffs: the Authenticator cannot be
   directly reprovisioned from Registry, though metadata (such as lock status)
   can still be reprovisioned. This feature also requires the use of
   Provisioner Plugins that support it.

.. note::

   The Message Template notification option (to notify a Person when their
   Authenticator is updated) is not yet available.

Self-Service and Enrollment
----------------------------

Depending on Plugin and configuration, Authenticators can be managed by People
themselves — setting their own password or uploading their own SSH keys — rather
than requiring administrator intervention for each credential. Configuration for
self-service is Plugin-specific.

Authenticators can also be collected during Enrollment Flows, allowing a Person
to set a credential as part of joining the CO.

.. note::

   Documentation for Authenticator self-service configuration and Enrollment
   Flow integration is under development.

Using Authenticators to Enable Registry Login
----------------------------------------------

Because Registry does not validate Authenticators itself, additional
infrastructure is needed if you want People to use Authenticators to log into
Registry. The general approach is:

1. Configure a Provisioning Target that writes the Authenticator to a suitable
   target system (such as LDAP or a KDC).
2. Set up an authentication service (Shibboleth, CAS, mod_authnz_ldap, etc.)
   that validates credentials against that target system and provides web-based
   authentication.
3. Configure Apache (or your web server) to use that authentication service for
   Registry.
4. Ensure the identifier returned by the authentication service matches an
   Identifier flagged for login on the Person record (not the External Identity
   record).

Available Authenticator Types
-------------------------------

.. note::

   **About this section**

   The current set of available Authenticator Plugins is listed in the Technical
   Manual. See
   `Available Authenticator Plugins <https://spaces.at.internet2.edu/spaces/COmanage/pages/350160334/Available+Authenticator+Plugins>`_
   for the current list.

   Available types in v5 include Password and SSH Key.

Custom Authenticator Plugins can be written to support additional credential
types. See
`Writing Registry PE Plugins <https://spaces.at.internet2.edu/spaces/COmanage/pages/250251876/Writing+Registry+PE+Plugins>`_
in the Technical Manual for the technical specification.

Changes from v4
----------------

Authenticators are a new feature in Registry v5. They do not have a direct
equivalent in Registry v4.

The use cases they address — provisioning passwords and SSH keys to downstream
systems — were previously handled by other mechanisms outside Registry, or
required custom integrations. In v5, these credential types can be managed
and provisioned directly within Registry's standard configuration model.
