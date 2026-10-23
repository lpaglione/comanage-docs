.. _eis-orcid-source:

ORCID Source
============

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

ORCID Source attaches a person's **ORCID iD** to their Registry record.
During enrollment, the person signs in to ORCID and authorizes Registry;
Registry then reads their ORCID record and creates an External Identity
from it, with the ORCID iD as an identifier. Because the person proves
control of the iD by signing in, you know it really is theirs, rather than
one they typed in.

.. list-table:: ORCID Source at a glance
   :widths: 35 65
   :stub-columns: 1

   * - Provided by
     - The **OrcidSource** plugin
   * - Plugin location
     - **Core**: always available; nothing to activate
   * - The OrcidSource package also includes
     - **ORCID Source Collector** (an Enrollment Flow Step that runs the
       ORCID sign-in during enrollment)
   * - Appears in the Plugin menu as
     - ``OrcidSource.OrcidSources`` (External Identity Source) and
       ``OrcidSource.OrcidSourceCollectors`` (Enrollment Flow Step)
   * - How data flows
     - The person signs in to ORCID (OAuth 2.0); Registry then **reads**
       their ORCID record through the ORCID API
   * - Also requires
     - An **OAuth2 Server** holding your ORCID API client credentials (see
       :ref:`ec-servers`)
   * - Sync modes (the **Status** field)
     - None on a schedule. Set the Status to **Manual**.
   * - Manual search
     - Yes: searches the ORCID registry itself (see
       :ref:`Searching <eis-orcid-source-search>`, below)
   * - Available since
     - v5.2.0

.. REVIEW: confirm the dropdown labels above match the UI, and confirm with
   developers what "Manual" means for ORCID Source (fact sheet open question 1).

1. When to Use ORCID Source
---------------------------

ORCID Source suits situations where:

- your collaboration serves researchers, and services downstream need a
  trustworthy ORCID iD for each person (for example, for publication
  systems or research information systems);
- you want the iD linked by the person themselves, in a sign-in step, as
  part of enrollment.

It adds an identity alongside one from the person's home organization; it
isn't a way to load a population. For that, use
:ref:`File Source <eis-file-source>` or :ref:`SQL Source <eis-sql-source>`.

2. Enabling ORCID Source
------------------------

ORCID Source is a **Core** plugin, so there is nothing to activate in
Registry. Before configuring it, though, you need **ORCID API client
credentials**:

1. Register Registry as an application with ORCID. The free *Public API*
   credentials are enough for most deployments; ORCID member organizations
   can use *Member API* credentials instead. Use ORCID's **Sandbox** for
   testing and **Production** for live use.
2. Add an **OAuth2 Server** in Registry holding the client ID and secret
   (:ref:`ec-servers`).

The OrcidSource package has two parts: **ORCID Source** (the External
Identity Source, which defines how to talk to ORCID) and **ORCID Source
Collector** (the Enrollment Flow Step that runs the sign-in).

.. REVIEW: confirm with developers the recommended order: does the ORCID
   application registration need the Redirect URI that Registry only shows
   after the ORCID Source is saved?

3. How Data Flows
-----------------

.. code-block:: text

   Enrollee ──▶ ORCID Source Collector (Enrollment Flow Step)
                        │  redirects to ORCID sign-in (OAuth 2.0)
                        ▼
                   ORCID ──▶ person authorizes Registry
                        │
                        ▼
   ORCID Source reads the person's ORCID record via the ORCID API
                        │
                        ▼
          External Identity Source (ORCID Source)
                        │
                     Pipeline
                        ▼
            Person record and Person Roles

- **What comes in**: the person's name, their email addresses (with ORCID's
  verified flag), country, and the **ORCID iD** as an identifier of type
  ``orcid``, plus one role with the default affiliation you choose. What
  ORCID returns depends on the person's privacy settings and your API
  type.
- **The ORCID iD is the Source Key.**
- **Types and affiliation come from your configuration**, since ORCID
  doesn't supply them. Affiliation values must match the *Database Value*
  of an Affiliation Type in the CO.
- **The Pipeline does the rest**: matching to existing people, mapping
  attributes and creating Person Roles. See :ref:`ec-pipelines`.

4. Configuring ORCID Source
---------------------------

Before you start, make sure a suitable Pipeline exists
(:ref:`ec-pipelines`) and the OAuth2 Server is in place.

1. Add a new External Identity Source as described in
   :ref:`ec-external-identity-sources`, selecting
   ``OrcidSource.OrcidSources`` as the Plugin, and set the **Status** to
   **Manual**.
2. Save. The ORCID Source settings appear next.

.. REVIEW: screenshot of the ORCID Source configuration form
   (for example, connections/OrcidSource_configuration.png).

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - What to decide
   * - **Server**
     - The OAuth2 Server holding your ORCID client credentials.
   * - **API Type**
     - **Public** (most deployments), **Members** (ORCID member
       organizations, with access to more of each record) or
       **Authorize**.
   * - **API Tier**
     - **Production** for live use, or **Sandbox** for testing.
   * - **Redirect URI**
     - Generated by Registry; you can't edit it. Register this URI with
       ORCID as part of your application's settings.
   * - **Scope** / **Inherit Scope**
     - The OAuth scope Registry requests from ORCID. By default this is
       ``/authenticate``; leave **Inherit Scope** on unless you have a
       reason to change it.
   * - **Default types** (Name, Address, Email Address, Telephone Number,
       Default Affiliation)
     - The type given to each value brought in, and the affiliation given
       to the role.

.. REVIEW: confirm required fields (red asterisks) in the UI; the code
   doesn't mark any of these as required. Also confirm the on-screen label
   for the Redirect URI (the code's label text is "Additional ORCID
   Redirect URI"), and when an admin should choose the "Authorize" API
   Type (fact sheet open question 7).

5. Using ORCID Source in an Enrollment Flow
-------------------------------------------

To collect an ORCID identity during enrollment, add an Enrollment Flow Step
(see :ref:`lifecycle-enrollment-flows`):

1. Set the **Plugin** to ``OrcidSource.OrcidSourceCollectors``.
2. Set the **Actor Type** to **Petitioner** for self-signup flows, or
   **Enrollee** for other flows.
3. On the plugin configuration page, select the ORCID Source configured
   above.

When the enrollee reaches this step, they are sent to ORCID to sign in and
authorize Registry, then returned to the flow.

.. _eis-orcid-source-search:

6. Searching
------------

**Search Source** for ORCID Source sends your search to ORCID's public
search service, so results can include anyone with an ORCID record, not
just people already in Registry. Results show each matching person's ORCID
record details.

.. REVIEW: confirm with developers whether syncing a record found this way
   is supported and recommended, given that it skips the person's own
   sign-in (fact sheet open question 1).

7. Technical Reference
----------------------

See
`Orcid Source Plugin <https://spaces.at.internet2.edu/spaces/COmanage/pages/337444876/Orcid+Source+Plugin>`_
in the Technical Manual.

8. Changes from v4
------------------

- **ORCID Source is available from v5.2.0.**
- **The ORCID Identifier is now called the Source Key.**
