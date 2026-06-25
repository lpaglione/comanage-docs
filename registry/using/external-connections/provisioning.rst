.. _ec-provisioning:

Provisioning
=============

Provisioning is how Registry pushes identity data out to the applications and
services that depend on it. When a person's status changes, when they join or
leave a group, when their name or email address is updated — provisioning
ensures that the downstream systems that need to know about those changes are
updated, automatically and consistently.

Each downstream system is configured as a **Provisioning Target**, an
instantiation of a **Provisioner Plugin** that knows how to communicate with
that specific type of system (an LDAP directory, a collaboration platform, a
Kerberos KDC, etc.). You can have as many Provisioning Targets as you have
downstream systems to feed.

For the full technical reference, see
`Registry PE Provisioning <https://spaces.at.internet2.edu/spaces/COmanage/pages/256939260/Registry+PE+Provisioning>`_
in the Technical Manual.

----

.. contents:: On this page
   :local:
   :depth: 1

----

What Gets Provisioned
----------------------

Registry supports provisioning the following types of objects:

**People**
   The most common provisioning target. When a Person record is provisioned,
   Registry sends the Person's attributes along with associated data: names,
   identifiers, email addresses, addresses, telephone numbers, pronouns,
   ad hoc attributes, group memberships (valid memberships only, for eligible
   People), Person Roles (valid roles only, for eligible People), Authenticators,
   and URLs.

   What a Person is eligible to receive depends on their status:

   - **Active or Grace Period** — the full record is sent. (Grace Period people
     receive the same provisioning as Active people — they are not yet
     deprovisioned.)
   - **Suspended, Expired, Pending, Pending Activation** — only the "core"
     record is sent: person data and All Members group memberships, but no role
     data or active group memberships.
   - **Archived or Deleted** — triggers deletion behavior in the target system,
     not deactivation.

**Groups**
   Sent with their member list (eligible members only) and active identifiers.
   Eligibility for Group provisioning follows status rules similar to People.

**COUs**
   Sent when created or deleted.

**Types**
   Registry Type definitions (custom attribute enumerations) can be provisioned
   to targets that need them, following Active/Inactive eligibility rules.

Configuring Provisioning Targets
----------------------------------

Provisioning Targets are managed via **Configuration > Provisioning Targets**.

When adding a new Provisioning Target:

1. Select the desired **Plugin** for your target system type.
2. Configure **Provisioning Mode**, **Provisioning Group** (if applicable), and
   **Provisioning Order** (if multiple targets exist).
3. Save. Plugin-specific configuration will become available after saving.

.. note::

   Once set, the Plugin associated with a Provisioning Target cannot be changed.
   If you need to change plugins, delete the Provisioning Target and create a
   new one.

Provisioning Modes
-------------------

The Provisioning Mode controls when and how Registry sends data to a target.

**Immediate**
   As soon as a change is made to a provisionable object or a related object,
   Registry immediately tries to run the Provisioning Target. If provisioning
   fails, it will not automatically be retried.

   Use for targets where near-real-time updates are important and you can tolerate
   occasional missed updates on failure.

**Queue** *(available as of v5.2.0)*
   Changes are queued, and the Provisioner Job processes the queue on the next
   scheduled run. Supports retry with configurable Retry Interval and Max
   Retries.

   Use for targets where eventual consistency is acceptable and resilience to
   transient failures matters.

**Queue on Error** *(available as of v5.2.0)*
   Registry tries immediately, like Immediate mode. If provisioning fails, the
   failed attempt is queued for retry by the Provisioner Job.

   Use as a best-of-both-worlds option: fast when things work, resilient when
   they don't.

**Enrollment Only**
   The object is provisioned only during the Enrollment Flow. Changes made after
   enrollment do not trigger automatic reprovisioning, though an administrator
   can manually trigger it.

   Use for systems that only need to know about initial enrollment events, not
   ongoing changes.

**Manual**
   Provisioning only runs when explicitly triggered by an administrator or via
   the API. No automatic provisioning occurs.

   Use during initial setup, testing, or for systems that should only be updated
   on deliberate administrative action.

**Disabled**
   The Provisioning Target is configured but inactive. No provisioning occurs.

**Retry Interval and Max Retries** (Queue and Queue on Error modes)
   These settings control how often Registry retries failed provisioning jobs
   and how many attempts are made before giving up. Setting Retry Interval to 0
   disables retries (one attempt only). Setting Max Retries to 0 causes Registry
   to retry indefinitely until the job succeeds or is manually cancelled.

Provisioning Groups
--------------------

By default, all eligible People are sent to every Provisioning Target. If you
need to scope provisioning — sending some people to one system and others to
another — use a **Provisioning Group**.

When a Provisioning Group is configured on a Provisioning Target, only People
who are members of that Group will be provisioned to that target. If a Person
is later removed from the Group, they are reprovisioned with "deleted"
eligibility, which typically means removal from the target system (not just
deactivation).

The Provisioning Group configuration also applies to Group provisioning: if set,
only the configured Group itself will be sent to this Provisioning Target (not
all Groups in the CO).

Provisioning Order
-------------------

If your downstream systems have dependencies — for example, an LDAP directory
must be populated before a system that authenticates against it — you can
assign a **Provisioning Order** to your Provisioning Targets. Targets with
lower order numbers run first (e.g., Order 1 runs before Order 2).

Provisioning Keys
------------------

When a Provisioner Plugin assigns or generates an identifier for a Person or
Group in the target system (such as a unique row ID in a database or a
distinguished name in LDAP), the plugin can return that value to Registry as
a **Provisioning Key**. Registry stores it as an Identifier on the entity,
flagged as a Provisioning Key and linked to the Provisioning Target that
created it.

Provisioning Keys are available as of v5.2.0. While they can technically be
edited via the entity's Identifiers, doing so is not recommended — editing a
Provisioning Key may interfere with the plugin's ability to find the record on
subsequent provisioning runs.

Monitoring Provisioning Status
--------------------------------

Registry tracks a Provisioning History Record for every provisioning event,
for all object types. You can view provisioning status for any entity from
the appropriate gear menu.

The status view includes:

- **Live Status** (where supported by the plugin) — a real-time query against
  the target system showing the entity's current state there.
- **Last Status** — the result of the most recent Provisioning History Record.

The two can differ: for example, if a record was successfully provisioned
but the most recent attempt failed, Live Status might show "Provisioned" while
Last Status shows the failure.

.. note::

   There is currently no proactive notification mechanism for provisioning
   failures. Failures are only visible by reviewing Provisioning Status on
   individual entities or checking provisioning history records.

Reprovisioning All Entities
-----------------------------

To (re)provision all entities within a CO to a specific target, use the
**Provisioner Job Plugin**. This is useful after initial configuration, after
recovering from a failure that left many records out of sync, or when making
broad configuration changes that require all records to be re-sent.

Available Plugins
------------------

.. note::

   **About this section**

   The canonical list of available Provisioner Plugins is maintained in the
   Technical Manual. See
   `Available Provisioner Plugins <https://spaces.at.internet2.edu/spaces/COmanage/pages/256939405/Available+Provisioner+Plugins>`_
   for the current set.

   We are evaluating the best approach for surfacing this list within this
   documentation — whether as a manually maintained summary with context, or as
   a direct link to the Technical Manual.

Custom Provisioner Plugins can be written to provision to any target system.
See
`Provisioner Plugins (PE) <https://spaces.at.internet2.edu/spaces/COmanage/pages/256938864/Provisioner+Plugins+PE>`_
in the Technical Manual for the technical specification.

Changes from v4
----------------

If you are migrating from Registry v4, the following Provisioning changes apply:

- **Provisioning Plugins have been renamed Provisioner Plugins.**

- **Automatic Mode is now Immediate Mode.** The v4 "Automatic" provisioning
  mode corresponds to v5 "Immediate."

- **Queue and Queue on Error modes** existed in v4 since v4.0.0 and are
  available in v5 as of v5.2.0. Retry Interval and Max Retries carry over
  from v4 as well.

- **Provisioning Groups** have been part of Registry since v2.0.0 and are
  available in v5 as of v5.2.0.

- **Provisioning Keys** are available in v5 as of v5.2.0. This generalized
  mechanism for storing provisioner-assigned identifiers (such as LDAP DNs or
  database row IDs) back on Registry records did not exist as a formal feature
  in v4.

- **Authenticators are included in provisioning data** as of v5.2.0.

- **Pass Through Provisioning for Authenticators** is supported as of v5.2.0.

- **The Provisioning Status view now includes both live and last status**
  as of v5.2.0.

- **Skip If Associated With Org Identity Source is no longer supported.**

- **Notifications are no longer sent on provisioning failures.** Check
  provisioning history or live status to detect failures.
