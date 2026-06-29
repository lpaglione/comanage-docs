.. _transitioning-whats-new-5.1.0:

What's New in Registry v5.1.0
================================

*Released 27 May 2025*

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry v5.1.0 is a feature release focused on bringing Enrollment Flows
to v5 and introducing several new capabilities for managing identity records.
This release was intended for early adopters with compatible use cases —
Registry v5 was not yet at feature parity with Registry v4 at the time of
this release. Full release notes and the complete changelog are available in
the
`Release History <https://spaces.at.internet2.edu/display/COmanage/Release+History>`_.

1. New Capabilities
--------------------

**Identifier Mapper Pipeline Plugin**

A new Pipeline Plugin is available for deployments that need to set the
Registry login identifier for a person based on data arriving through a
Pipeline. The Identifier Mapper Plugin maps a source attribute value to
a specific Identifier type in Registry, allowing the login identifier to
be derived from source data rather than assigned separately. See
:ref:`ec-pipelines`.

**Record Adoption**

Administrators can now convert an External Identity record into a
Registry-native record via **Adoption**. When a record is adopted, it is
unlinked from its External Identity Source and the person's attributes
become directly managed within Registry — the source can no longer sync
that record. Adoption is useful for data migration scenarios, such as
moving people from a source-driven population into a directly managed one.
Adoption can be reversed via Annulment. See :ref:`ec-external-identity-sources`.

**Relinking**

An External Identity record can now be relinked to a different Person record
when it has been matched to the wrong person. To relink, navigate to the
External Identity's gear menu and select Relink, then find the correct target
Person. Relink moves the External Identity but does not resync — the Pipeline
must be run afterward to apply the source data to the new person. See
:ref:`ec-external-identity-sources`.

**Traffic Plugins**

Traffic Plugins are a new plugin type that can intercept the platform's
authentication flow at specific points — before, during, or after login —
enabling custom handling such as redirecting authentication events to external
systems. See :ref:`extend-plugins` for the plugin type overview; individual
Traffic Plugins are documented in the Technical Manual.

2. Capabilities Restored from v4
----------------------------------

**Enrollment Flows** *(redesigned)*

Enrollment Flows are back in v5.1.0, rebuilt from the ground up. An
Enrollment Flow defines a sequence of Steps that participants move through
to join a CO. When someone begins a Flow, they create a **Petition** —
the artifact that tracks their progress through the process. At the end of a
successful Flow, the Petition is finalized and a Person record is created or
updated.

Several Enrollment Flow Step Plugins are available at this release:
the **Identifier Collector**, **Basic Attribute Collector** and **Attribute
Collector** for gathering information from the enrollee; the **Identifier
Assignment Enroller** for assigning identifiers during enrollment; and the
**Invitation Accepter** for invitation-based flows. The Enrollment Flow
implementation in v5.1.0 is focused on initial use cases; some v4 Enrollment
Flow capabilities are planned for future releases. See
:ref:`lifecycle-enrollment-flows`.

**Env Source Plugin**

The Env Source Plugin reads identity attributes from environment variables —
the variables set by a web server or identity provider at authentication time.
This makes it straightforward to bring attributes like name, email, and
affiliation directly from a SAML assertion or OIDC token into Registry without
an intermediate directory or database. Env Source also restores Sync on Login
behavior that was not available in v5.0.x — the plugin can be configured to
sync a person's record each time they log in. See
:ref:`ec-external-identity-sources`.

**HTTP Servers and Match Servers**

**HTTP Servers** define connections to resources accessed via HTTP or HTTPS,
including authentication credentials and TLS configuration. **Match Servers**
build on HTTP Servers to configure connections to servers implementing the
COmanage Match API — used when a Pipeline's External Match Strategy calls out
to an external matching service to resolve identity matches. See
:ref:`ec-servers`.

**Mostly Static Pages**

Mostly Static Pages — Registry's mechanism for publishing simple HTML content
pages within the Registry application — are now available as standard data
model elements in v5.1.0. In v5.0.x, Mostly Static Pages required filesystem
access to configure; in v5.1.0 they are managed entirely through the Registry
administrative interface. See :ref:`personalization-mostly-static-pages`.

3. Interface and Usability Improvements
-----------------------------------------

**Identifier Assignment: transliteration and minimum length**

The Format Identifier Assignment Plugin has two new configuration options.
**Transliteration** converts non-ASCII characters to their ASCII equivalents
before generating the identifier — useful when identifiers must be ASCII-only
but source name data may include accented or non-Latin characters.
**Minimum length** sets a floor on the generated identifier length, with the
plugin iterating until the candidate meets the minimum. See
:ref:`ec-identifier-assignment`.

**Person status badge**

A person's status is now shown as a badge in the supertitle bar across all
Person canvas tabs, making it immediately visible without navigating to the
Person record itself.

**User display preferences**

Registry v5.1.0 introduces persistent user display preferences: **display
density** (compact vs. normal view) and a **dark mode toggle** independent
of operating system settings. Preferences are stored per user and remembered
across sessions. See :ref:`understanding-interface`.

**Accessibility improvements**

A range of accessibility improvements to forms and data input fields were
included in this release, including better handling of required field
indicators, keyboard navigation, and label associations.

4. Looking Ahead
-----------------

Registry v5.1.0 was the first feature release of Registry v5, intended for
early adopters. Feature equivalency work continued in
:ref:`transitioning-whats-new-5.2.0`.

The COmanage Project's monthly **Open Office Hours** is an open call where
you can ask questions, share feedback, and hear how other organizations are
using Registry. Subscribe to the
`COmanage Project calendar <https://www.addevent.com/calendar/Nr648428>`_
for dates and connection links.
