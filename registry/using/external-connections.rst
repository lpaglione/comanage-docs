.. _using-external-connections:

External Connections
====================

Registry is a hub, not a silo. It connects to the systems around it — pulling
authoritative identity data in from your sources of record, issuing and managing
credentials, assigning identifiers, and pushing the resulting data out to the
applications and services that need it. This area of Registry covers everything
that crosses that boundary.

Understanding External Connections means understanding the data flow Registry is
designed to support:

**Inbound** — external systems of record (your HR database, student information
system, LDAP directory, ORCID, flat files, REST APIs) provide source data about
people. Registry connects to these systems through **External Identity Sources**
and processes the incoming data through **Pipelines** that match records, resolve
conflicts, and map attributes onto Person records.

**Outbound** — once data is in Registry and People are active, Registry can push
it to the downstream applications that depend on it: LDAP directories,
collaboration platforms, access management systems, and more. **Provisioning**
handles this, running automatically when relevant data changes and supporting a
range of delivery modes.

**Collaboration-managed credentials** — some credentials belong to the CO itself,
not to any external source. **Authenticators** let Registry store and manage
passwords, SSH keys, and other credential types for People, then pass them
outbound through the provisioning infrastructure.

**Identifier management** — external data rarely arrives with the identifiers your
systems need. **Identifier Assignment** automatically generates stable identifiers
and email addresses for People, Groups, and other entities, using pluggable
algorithms that enforce uniqueness across the CO.

**Server registry** — many External Connections configurations reference specific
external servers (an LDAP directory, an OAuth2 endpoint, an SMTP relay). The
**Servers** registry gives you a central place to define and maintain these
endpoints, so plugins and connectors can reference them by name rather than
repeating connection details.

.. TODO: Add data flow diagram showing inbound (External Identity Sources +
   Pipelines) → Registry Person record → outbound (Provisioning) flow, with
   Authenticators and Identifier Assignment shown alongside.

----

.. contents:: On this page
   :local:
   :depth: 1

----

Inbound: External Identity Sources
------------------------------------

An **External Identity Source** defines the connection between Registry and one
external system of record. It tells Registry where to look for person data, which
plugin to use to talk to that system, and how syncing should be handled.

Supported source types include SQL databases, LDAP directories, flat files, REST
APIs, and ORCID — and custom plugins can be written for any source. Each source
operates in one of four sync modes:

- **Full** — all records in the source are synced to Registry on each run
- **Update** — only records already in Registry are refreshed; new records in
  the source are not added
- **Manual** — records can only be synced individually by an administrator
- **Disabled** — no syncing occurs

Registry stores a local cache of the source data (the External Identity Source
Record) so it can detect changes without querying the source every time. For
privacy-sensitive deployments, Registry can store a hash of the source record
rather than the full copy.

Individual records can be managed once synced — an administrator can relink a
record to a different Person, resync a record from its source, or delete an
External Identity. Records can also be *adopted*, converting them from
source-authoritative to Registry-authoritative (useful in data migration
scenarios).

For the full reference, see
`Registry PE External Identity Sources <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743514/Registry+PE+External+Identity+Sources>`_
in the Technical Manual.

Inbound: Pipelines
-------------------

A **Pipeline** controls how data from an External Identity Source flows into
Registry. Every External Identity Source requires a Pipeline. The Pipeline
determines:

- how incoming source records are matched to existing Person records in Registry
- how attributes from the source are mapped onto External Identity and Person
  record fields
- how multiple Person Roles can be conveyed within a single External Identity
  record (v5 feature)

Pipelines are shared configuration objects — a single Pipeline can serve multiple
External Identity Sources that follow the same processing rules.

For the full reference, see
`Registry PE Pipelines <https://spaces.at.internet2.edu/spaces/COmanage/pages/275743515/Registry+PE+Pipelines>`_
in the Technical Manual.

Outbound: Provisioning
------------------------

**Provisioning** is the process of exporting Registry data to downstream
applications, typically to grant or remove access. Registry provisioning is
implemented through **Provisioner Plugins**, each of which connects to a specific
type of target system.

You configure one or more **Provisioning Targets**, each being an instantiation
of a Provisioner Plugin pointed at a specific endpoint. Key configuration options
include:

**Provisioning Mode** — controls when provisioning runs:

- *Immediate* — Registry provisions as soon as a change is made
- *Queue* — changes are queued and processed on the next job run
- *Queue on Error* — tries immediately, falls back to queue if it fails
- *Enrollment Only* — only provisions at the time of enrollment, not on later
  changes
- *Manual* — provisioning only runs when explicitly triggered
- *Disabled*

**Provisioning Group** — if configured, only People who are members of a
specified Group are sent to this Provisioning Target. People removed from the
group are reprovisioned with "deleted" eligibility, which generally triggers
removal from the target system.

**Provisioning Order** — Provisioning Targets can be ordered so that dependent
downstream systems are populated in the right sequence.

Registry provisions People (with their associated names, identifiers, email
addresses, group memberships, Person Roles, Authenticators, and addresses),
Groups, COUs, and Types. Eligibility rules determine what data is sent depending
on a Person's status — Active and Grace Period People receive the full record;
others receive a reduced "core" record; Archived and deleted People trigger
deletion behavior in the target.

**Provisioning Keys** — when a Provisioner Plugin assigns or generates an
identifier in the target system (such as a database row ID or LDAP distinguishing
name), Registry can store that back as a Provisioning Key on the Person or Group
record.

Provisioning history is tracked for all events. Current provisioning status can
be reviewed per-entity, including a live query against the target system (where
the plugin supports it) and the most recent history record.

For the full reference, see
`Registry PE Provisioning <https://spaces.at.internet2.edu/spaces/COmanage/pages/256939260/Registry+PE+Provisioning>`_
in the Technical Manual.

Authenticators
---------------

**Authenticators** are credentials that the CO issues and manages directly —
passwords, SSH keys, and other credential types. Unlike External Identity data,
Authenticators belong to the Person record (not the External Identity) because
they represent what your collaboration has issued, not what an external source
knows about the person.

Registry does not validate Authenticators for login directly. Instead, it stores
them (or passes them through to a downstream system) and makes them available to
the provisioning infrastructure so Provisioner Plugins can write them to target
systems such as LDAP or a KDC.

Administrators can manage Authenticators for People — setting, locking,
unlocking, and resetting credentials. Depending on the plugin, Authenticators
may be self-service as well (a Person can set their own password or upload their
SSH keys). Locking an Authenticator prevents it from being changed or used and
excludes it from provisioning.

**Pass Through Provisioning** (experimental) allows a credential to be collected
and sent to a downstream system (such as a Kerberos KDC) without being stored in
the Registry database.

Available Authenticator types in v5 include Password and SSH Key. Each type is
implemented as an Authenticator Plugin. Authenticators were introduced in
Registry v5.2.0.

For the full reference, see
`Registry Authenticators <https://spaces.at.internet2.edu/spaces/COmanage/pages/350160332/Registry+Authenticators>`_
in the Technical Manual.

Identifier Assignment
----------------------

**Identifier Assignment** automatically generates and assigns identifiers and
email addresses to entities within a CO. Rather than manually assigning IDs,
administrators configure assignment rules — using pluggable algorithms — and let
Registry assign identifiers when people are enrolled, when pipelines run, or on
demand.

Identifier Assignment can be applied to People, Groups, and (in future versions)
Departments. Multiple assignment configurations can be ordered so that
identifiers generated by one rule can be used as inputs to another — for example,
generating a username first, then generating an email address derived from it.

Key behaviors:

- Identifiers of a given type must be unique within a CO (uniqueness checks are
  case-insensitive and include Suspended identifiers)
- If an entity already has an identifier of a given type, no additional identifier
  will be created
- Assignment can generate either Identifiers or Email Addresses (using separate
  configurations)
- Email Addresses generated by assignment are considered verified

Available plugins include the Format Identifier Assignment Plugin and the SQL
Identifier Assignment Plugin. The Assigner Job Plugin can run assignment for all
entities within a CO.

For the full reference, see
`Registry PE Identifier Assignment <https://spaces.at.internet2.edu/spaces/COmanage/pages/269746372/Registry+PE+Identifier+Assignment>`_
in the Technical Manual.

Configuration: Servers
-----------------------

A **Server** in Registry represents a physical or logical endpoint referenced by
the CO — a backend system that External Identity Sources, Provisioners, or other
configuration objects connect to. The Servers registry gives administrators a
central place to define and maintain these endpoints.

Server types available by default (via the CoreServer plugin):

- **HTTP** — general HTTP/HTTPS endpoints
- **Match** — Internet2 Match Server endpoints, used by the Match Algorithm
  for record matching
- **OAuth2** — OAuth2 authorization servers
- **SMTP** — outgoing mail servers, used for Registry notifications
- **SQL** — SQL database servers, referenced by External Identity Sources and
  Provisioners that work with databases

Additional server types are available via plugins — for example, Kerberos servers
are supported via the Kerberos Provisioner Plugin.

Server objects are referenced by other configuration objects rather than
duplicating connection details. This makes it easier to update a server endpoint
in one place when it changes.

For the full reference, see
`Registry Servers <https://spaces.at.internet2.edu/spaces/COmanage/pages/256938867/Registry+Servers>`_
in the Technical Manual.

----

In This Section
----------------

.. note::

   Detailed configuration pages for each area below are under development.

Detailed pages within this section will cover:

- **External Identity Sources** — connecting to systems of record, sync modes,
  managing synced records
- **Pipelines** — matching, attribute mapping, and processing rules for inbound
  data
- **Provisioning** — configuring provisioning targets, modes, and groups;
  monitoring provisioning status
- **Authenticators** — setting up collaboration-issued credential types and
  self-service options
- **Identifier Assignment** — configuring assignment rules and running bulk
  assignment
- **Servers** — maintaining the registry of external server endpoints
