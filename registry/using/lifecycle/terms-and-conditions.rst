.. _lifecycle-terms-and-conditions:

Terms and Conditions
=====================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


:bdg-secondary:`Available: v5.2.0` When people enroll in your organization, they often need to agree to a policy —
acceptable use, data handling, research participation, membership terms.
**Terms and Conditions** let you present one or more policy documents to people
at appropriate points in their relationship with the CO, and track that they have
agreed.

Registry records the authenticated identifier used to agree to each Terms and
Conditions document, providing an audit trail. Agreements can be configured to
expire after a specified duration (requiring periodic re-agreement), and can be
automatically invalidated when the document content changes.

For the full technical reference, see
`Registry PE Terms and Conditions <https://spaces.at.internet2.edu/spaces/COmanage/pages/377389135/Registry+PE+Terms+and+Conditions>`_
in the Technical Manual.

1. Configuring Terms and Conditions
-----------------------------------

Terms and Conditions are defined via **Configuration > Terms and Conditions**.
The available settings are:

- **Description** — the label displayed to the person when the T&C is presented.
  This is what the person sees, not just an administrative label.
- **Status** — only Active Terms and Conditions require agreement. Setting a T&C
  to a non-Active status disables the requirement without deleting the record or
  its agreement history.
- **T&C via URL** — a link to an external, publicly accessible document. If both
  this and T&C via Mostly Static Page are specified, the URL takes precedence.
- **T&C via Mostly Static Page** — a :ref:`personalization-mostly-static-pages`
  within Registry that holds the T&C content.
- **COU** — if specified, this T&C applies only to people with a Person Role in
  the specified COU, or during an Enrollment Flow associated with that COU.
  Leave blank to apply the T&C CO-wide.
- **Agreement Duration** — if set, a new agreement is required after the
  specified duration has passed. Note that no expiration timestamp is stored with
  individual agreements — changing this setting takes effect immediately for all
  existing agreements.
- **Require Agreement on Updated T&C** — if enabled, any change to this T&C
  record (regardless of whether the actual content changed) immediately requires
  a new agreement from all relevant people.

2. Choosing How to Present T&C Content
--------------------------------------

Content can be provided either via an external URL or via a Mostly Static Page
within Registry. The two approaches have different trade-offs:

**Via URL** — useful when your T&C document is already maintained in an external
system (a SharePoint page, a public website, an official policy portal). Because
of browser security restrictions (CORS), the T&C opens in a new window rather
than inline, which creates a less seamless experience. Registry is also unable to
enforce that the person scroll to the end of the document before agreeing.

**Via Mostly Static Page** — because the content lives inside Registry, it can be
rendered inline on the same page as the agreement interface. Registry can also
enforce a scroll-to-end requirement before the agreement button becomes active.
The trade-off is that the content now exists as a copy within Registry, so if
the official document changes, the Mostly Static Page must be updated separately.

3. Agreement at Enrollment
--------------------------

Collecting T&C agreements as part of an Enrollment Flow requires adding an
**Agreement Collector** Step to the Flow. The Agreement Collector is an Enroller
Plugin that presents the configured Terms and Conditions to the current Actor and
records their agreement before allowing the Petition to proceed to the next Step.

See :ref:`lifecycle-enrollment-flows` for how to add Steps to an Enrollment Flow,
and
`Agreement Collector Enroller Plugin <https://spaces.at.internet2.edu/spaces/COmanage/pages/377389152/Agreement+Collector+Enroller+Plugin>`_
in the Technical Manual for plugin-specific configuration.

4. Agreement at Login
---------------------

Agreement at Login — requiring a person to agree (or re-agree) to T&C when
authenticating to Registry — is **not yet supported** in Registry v5.

5. Administrative Operations
----------------------------

**Agreeing on behalf of a person**

An administrator may agree to a Terms and Conditions document on behalf of a
person by navigating to the person's canvas and selecting **Terms and
Conditions**. For each T&C listed, use **Agree on Behalf** to record agreement.
This is useful for people who cannot complete the enrollment process themselves,
or for populations that need to be onboarded by an administrator.

**Revoking an agreement**

An administrator may revoke an existing agreement by navigating to the person's
canvas, selecting **Terms and Conditions**, finding the relevant agreement, and
selecting **Revoke**. The person will then be required to re-agree in the next
appropriate context.

Only CO Administrators may revoke agreements — not Platform Administrators. A
Platform Administrator who is not registered within the CO would not have a valid
Person ID for that CO, making it impossible to maintain a proper audit trail of
the revocation.

6. Changes from v4
------------------

- **Terms and Conditions are available as of Registry v5.2.0.** The feature
  existed in Registry v4 but was not included in v5.0.x or v5.1.x.

- **T&C Body is no longer configured directly** in the Terms and Conditions
  record. Content must be provided either via an external URL or via a Mostly
  Static Page.
