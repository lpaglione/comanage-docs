.. _transitioning-whats-new-5.2.0:

What's New in Registry v5.2.0
================================

*Released 4 June 2026*

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry v5.2.0 is a feature release and the next step in feature
equivalency work between Registry v4 and v5. Alongside several
capabilities that are genuinely new to Registry, this release restores a
substantial set of features that v4 administrators will recognize — making
v5 a viable primary registry for a significantly broader range of
deployments. Full release notes and the complete changelog are available in
the
`Release History <https://spaces.at.internet2.edu/display/COmanage/Release+History>`_.

1. New Capabilities
--------------------

**Requiring MFA for Registry Access**

Deployments with strict security requirements can now require Multi-Factor
Authentication for access to Registry administrative functions. MFA
enforcement is configured at the platform level and relies on the web
server or operating system to signal whether MFA was asserted at login.
Individual COs can be configured to exempt specific people via MFA
Exemption Groups — useful when some administrators have roles that don't
support MFA. See :ref:`ops-security`.

**Group Hierarchies**

Standard Groups can now be organized into a parent/child hierarchy, giving
administrators a way to reflect organizational structure within their group
namespace. A Group placed in a hierarchy inherits a Fully Qualified Group
Name that reflects its position in the tree, and its name uniqueness is
scoped to its siblings rather than the entire CO. Group Hierarchies are
independent from Group Nestings — hierarchy is about structure and naming,
while nestings remain the mechanism for propagating membership. See
:ref:`org-groups`.

**Cloning Records** *(experimental)*

Registry can now clone configuration and data objects from one CO to
another — including COs on different Registry platforms. Clonable objects
are assigned UUIDs that allow them to be tracked across environments, and
administrators can attach Change Request Identifiers to group related
objects for batch cloning. This is the foundation for promoting
configuration from a test environment to production without rebuilding
it by hand. Cloning is experimental in v5.2.0 and may change in future
releases. See :ref:`ops-record-management`.

**SQL Assigner Job Plugin**

A new Job Plugin is available for deployments that assign identifiers by
looking them up in an external SQL database. The SQL Assigner Job Plugin
works with a configured SQL Assigner Identifier Assignment and can be
scheduled to run on a recurring basis via the Registry Jobs interface.
See the Technical Manual's
`SQL Assigner Job Plugin <https://spaces.at.internet2.edu/spaces/COmanage/pages/346129582/SQL+Assigner+Job+Plugin>`_
for configuration details.

2. Capabilities Restored from v4
----------------------------------

The following capabilities existed in Registry v4 and are now available
in Registry v5.2.0.

**Terms and Conditions**

CO Administrators can define Terms and Conditions documents that must be
agreed to before a person gains access to CO resources. Agreement can be
required as a step in an Enrollment Flow, or applied directly to existing
CO Persons. Registry tracks agreement history, and administrators can agree
to a Terms and Conditions document on behalf of a person when needed.
See :ref:`lm-terms-and-conditions`.

**Authenticators: Password and SSH Key**

Registry can now manage credentials directly. The **Password Authenticator**
stores hashed passwords for CO Persons, supporting multiple encoding formats
and integration with the Kerberos Provisioner via Pass Through Provisioning
(see below). The **SSH Key Authenticator** collects and stores public SSH
keys, ready for provisioning to research computing resources. Both
authenticators are available as plugins that must be activated before use.
See :ref:`ec-authenticators`.

**Pass Through Provisioning**

When credentials change in an Authenticator — for example, when a person
sets or updates their password — a Provisioner can now receive the raw
credential value at the moment of the change and push it downstream
immediately, without it being stored in Registry. This allows Registry to
act as the point of credential management for systems like Kerberos KDCs
without Registry itself becoming a credential store.

**Kerberos Provisioner**

A new Provisioner Plugin is available for pushing credentials to a Kerberos
Key Distribution Center. It is designed to work with the Password
Authenticator and Pass Through Provisioning, enabling Registry to
manage Kerberos passwords as part of a person's overall identity lifecycle.
See the Technical Manual's Available Provisioner Plugins page for
configuration details.

**Provisioning Groups**

Provisioning Targets can now be scoped to a specific Group, so that only
members of that Group are provisioned to that target. Non-members receive
deleted eligibility in the target system. This allows a single CO to feed
multiple downstream systems with different population scopes — for example,
provisioning faculty to one directory and staff to another — without
requiring separate COs. See :ref:`ec-provisioning`.

**Pipeline External Match Strategy**

Pipelines can use an External Match Strategy that calls out to an external
matching service — such as COmanage Match — to resolve identity matches,
rather than relying solely on Registry's internal matching logic. This
enables tighter integration with identity deduplication workflows for
deployments where Record Matching needs to draw on data or algorithms
outside of Registry. Available in v5 as of v5.2.0. See :ref:`ec-pipelines`
and :ref:`using-match`.

**Queue Provisioning Modes**

Two additional Provisioning Modes are now available in v5: **Queue** and
**Queue on Error**. Queue mode defers all provisioning to the Provisioner
Job, supporting retry with configurable intervals and maximum retry counts.
Queue on Error tries immediately and falls back to the queue only if
provisioning fails — a good default for resilient production deployments.
See :ref:`ec-provisioning`.

**OAuth2 Servers and ORCID Source Plugin**

Registry can now connect to OAuth2 authorization servers, enabling plugins
that authenticate to external APIs using OAuth2. The new **ORCID Source
Plugin** uses OAuth2 to connect to the ORCID Member API and pull identity
data — particularly useful for research collaborations where ORCID is an
authoritative source of researcher identity. See :ref:`ec-servers`.

**Enrollment Flow Improvements**

Several new Enrollment Flow Step Plugins are available: the **Email Verifier
Enroller** requires an enrollee to verify their email address before
proceeding, and the **Approval Enroller** adds an approval step to any
enrollment flow. Petition handling has also been improved, including a
revised Approval view that makes it easier for approvers to review and act
on pending Petitions.

**Platform-Wide SMTP Server**

The COmanage CO can now have a platform-wide outgoing SMTP server configured,
which individual COs inherit when they have not configured their own. This
simplifies email delivery for platforms that host many COs with the same
mail infrastructure.

**Deletion and Nester Job Plugins**

Two new Job Plugins handle time-consuming operations asynchronously. The
**Deletion Job Plugin** performs background deletion of COs — rather than
blocking during a potentially long CO removal, the CO enters Pending Removal
status and the Deletion Job handles cleanup. The **Nester Job Plugin**
processes Group Nesting calculations in the background, improving performance
for COs with complex nesting configurations.

**Local Plugins**

Registry now supports Local Plugins — plugins obtained from community
contributors, vendors, or written in-house — without requiring changes to
the core Registry installation. A Local Plugin placed in the ``local/plugins/``
directory is automatically discovered when the Plugin registry is next
refreshed. See :ref:`extend-plugins`.

3. Interface and Usability Improvements
-----------------------------------------

**Jobs can now be managed through the Registry interface**

In v4, all job management required logging into the server console or
updating container configuration. In v5.2.0, CO Administrators can queue,
monitor, and cancel Jobs entirely through the Registry web interface —
including filtering the Job list by status and type. This was one of the
most frequently requested capabilities from the v4 community. See
:ref:`ops-jobs`.

**Dark mode and accessibility**

The v5.2.0 interface includes substantially improved dark mode support,
a Bootstrap upgrade to support modern theming, and a range of accessibility
improvements including better handling of required fields, read-only form
views, and keyboard navigation. These changes benefit all users, and are
particularly meaningful for users who rely on assistive technologies or
high-contrast display settings.

**Transmogrification updates**

Significant updates to the Transmogrification tooling make migration from
Registry v4 to v5 more capable and reliable. The Transmogrify Plugin
handles migration of Org Identities and Group membership in addition to
CO Person records, and alignment with v5 group rules (including Group
Hierarchy) has been improved. See :ref:`transitioning-transmogrification`.

4. Looking Ahead
-----------------

Registry v5.2.0 marks the next phase of feature equivalency work.
For the current status of feature equivalency between v4 and v5, see
:ref:`transitioning-feature-status`.

The COmanage Project's monthly **Open Office Hours** is an open call where
you can ask questions, share feedback, and hear how other organizations are
using Registry. Subscribe to the
`COmanage Project calendar <https://www.addevent.com/calendar/Nr648428>`_
for dates and connection links.
