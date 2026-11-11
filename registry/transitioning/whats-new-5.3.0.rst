.. _transitioning-whats-new-5.3.0:

What's New in Registry v5.3.0
================================

*Released 30 October 2026*

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry v5.3.0 is a feature release that completes the second phase of
feature equivalency work between Registry v4 and v5. Most of this release
brings back capabilities that v4 administrators will recognize, including
Departments and Organizations, LDAP provisioning, Person deletion,
normalization and Themes. Full release notes and the complete changelog are
available in the
`Release History <https://spaces.at.internet2.edu/display/COmanage/Release+History>`_.

.. important::

   **This release includes a security advisory.** The COmanage Project
   expects its impact to be very low, but encourages deployers to review it
   and act according to their own risk profile. See the
   `security advisory <https://spaces.at.internet2.edu/x/I4AsGg>`_.

   **Mostly Static Page URLs have changed.** Pages are now served at
   ``$REGISTRY/<coid>/pages/<slug>`` instead of ``$REGISTRY/<coid>/<slug>``.
   Update any links to these pages from outside Registry. See
   :ref:`transitioning-upgrading`.

1. New Capabilities
--------------------

**Mostly Static Resources**

Mostly Static Resources are a media library for your CO. You can upload
images and other files, then reference them from Mostly Static Pages and
Themes. Each resource is served at a stable URL within your CO. File uploads
must first be enabled at the platform level, which also sets the maximum
upload size. See :ref:`personalization-mostly-static-pages`.

**Connecting Enrollment Flows**

An Enrollment Flow can now start another Flow automatically. Two new Flow
settings let you choose the next Flow to run: **Next Flow on Finalize**
starts it when a Petition is finalized, and **Next Flow on Duplicate**
starts it when a Petition is flagged as a duplicate. Each takes the place of
the matching Redirect setting.

When the next Flow starts, the Petitioner and Enrollee carry over to its new
Petition, so the person doesn't start from scratch. The COU is not carried
over, which makes it possible, for example, to follow one enrollment with a
second Flow that enrolls the person in another COU. This makes it easier to
build enrollment processes out of smaller Flows. See
:ref:`lifecycle-enrollment-flows` and
`Registry PE Enrollment Flows <https://spaces.at.internet2.edu/spaces/COmanage/pages/289113561/Registry+PE+Enrollment+Flows>`_
in the Technical Manual.

2. Capabilities Restored from v4
----------------------------------

The following capabilities existed in Registry v4 and are now available
in Registry v5.3.0.

**Departments and Organizations**

.. REVIEW: point these links to the Departments and Organizations pages
   once they are written. The Structure page currently lists them under
   "Coming to v5".

**Departments** store structured information about departments, institutes
or other units within your CO. A Department can belong to the CO or to a
COU, and can be linked to Groups for its leadership, administrative staff
and support staff. **Organizations** store similar information about
outside institutions, companies and funders that your members work with.

Both can hold addresses, email addresses, identifiers, telephone numbers,
URLs and **Contacts** (named administrative, billing, support or technical
contacts). Both appear in the **Structure** menu and are included in Global
Search. Transmogrification now migrates v4 CO Departments and CO
Organizations.

**Organization Sources**

.. REVIEW: confirm current status and how sync is run (on demand only,
   or also by Job) against the Organization Sources page in the Technical
   Manual.

Organization Sources from Registry v4 are being restored, so that
Organizations can be loaded and kept up to date from an outside source
instead of being entered by hand. This work is not yet complete. The first
Organization Source plugin, **Federation Source**, must be activated before
use. It reads organizations from SAML federation metadata, either from a
metadata file or through an MDQ service.

**Person Deletion, including hard delete**

Deleting a Person now opens a confirmation page that lists everything the
deletion will affect, such as Person Roles, External Identities, Petitions,
Notifications and history records. Platform and CO Administrators can choose
a **hard delete**, which permanently removes the Person and related records
from the database, including changelog entries. A hard delete can only be
reversed by restoring from a backup. See :ref:`ops-record-management`.

**Terms and Conditions at Login**

Terms and Conditions were restored in v5.2.0. In v5.3.0, a CO can require
people to agree (or agree again, after a document changes) when they log in
to Registry. This is set in CO Settings. Agreements are now included in
provisioning data, and a REST API endpoint is available for recording them.
See :ref:`lifecycle-terms-and-conditions`.

**LDAP Provisioner and LDAP Servers**

Registry can once again provision people and groups to an LDAP directory.
The **LDAP Provisioner** is a core plugin, so no activation is needed. It
supports common object classes and schemas, including inetOrgPerson,
eduPerson, eduMember, groupOfNames, ldapPublicKey and voPerson. Connection
details are kept on a new **LDAP Server** type. See :ref:`ec-provisioning`
and :ref:`ec-servers`.

**API Provisioner**

The **API Provisioner** sends Registry data to an outside HTTP endpoint
whenever a record changes. It can send the full record or a link to it.
It's part of the ApiConnector plugin package, which must be activated before
use. The SQL Provisioner now also publishes Terms and Conditions agreements
and External Identity Source data. See :ref:`ec-provisioning`.

**Normalization**

.. REVIEW: point to the rewritten Normalizing Data section once it reflects
   the plugin-based model.

Registry can tidy up attribute values as they are saved, for example by
trimming extra spaces or fixing capitalization. In v5, normalization is
plugin-based. The core **Case Mixer**, **Punctuation Remover** and
**Whitespace Trimmer** plugins are set up automatically for each CO, and
administrators choose which ones are active and in what order. Custom
normalization plugins can also be written.

**Themes**

.. REVIEW: point to the Themes page once it is written. The Personalization
   page currently lists Themes under "Coming to v5".

Themes let you change the look of the Registry interface to match your
organization. A Theme can include custom CSS, header and footer content, and
options to hide the title banner or footer logo. A Theme set for the
COmanage CO applies across the platform; a CO can use its own Theme instead,
and a Theme can also be set on an individual Enrollment Flow or Mostly
Static Page. Images used in a Theme can be stored as Mostly Static
Resources. If you maintain custom CSS, note that ``co-color.css`` has been
renamed ``co-variables.css``.

**Enrollment Flow Step Plugins**

.. REVIEW: confirm what the Information Renderer displays and where its
   content comes from.

Four new Enrollment Flow Step plugins are available:

- **Person Selector** attaches an existing Person to the Petition, either
  the person running the Flow or a Person chosen from a search.
- **COU Selector** attaches a COU to the Petition, chosen from all COUs, from
  the COUs the person belongs to, or set to a specific COU.
- **Information Renderer** shows information to the Enrollee during the Flow.
- **Password Collector** lets the Enrollee set a password during enrollment.
  It's part of the Password Authenticator plugin.

Two additional Petitioner Authorization levels are also supported: **CO or
COU Administrator** and **Person**. The Attribute Collector has also been
improved. Valid From dates now default
to the start of the day and Valid Through dates to the end of the day. See
:ref:`lifecycle-enrollment-flows`.

3. Interface and Usability Improvements
-----------------------------------------

**Global Search and the People Picker**

Global Search now covers Departments, Organizations and Servers, as well as
People, Groups and COs. The People Picker, used when choosing a group member
or the Person to relink an External Identity to, now uses Global Search. Two
new CO Settings control who can use the People Picker and how many results
it returns. See :ref:`ops-searching`.

**Group Nestings**

The form for adding a Group Nesting has been improved, and it now offers a
**Queue Job** option. The nesting is applied by a background Job instead of
right away, which helps when nesting large Groups. See :ref:`org-groups`.

**Menu updates**

Departments and Organizations now appear in the **Structure** menu. Mostly
Static Resources and Themes appear under **Configuration > Personalization**,
and the Platform-Wide Configuration section of the Configuration menu has
moved.

**Env Source ORCID mapping**

The Env Source plugin can now map an ORCID identifier from the web server
environment. See :ref:`eis-env-source`.

4. Looking Ahead
-----------------

Registry v5.3.0 completes the second phase of feature equivalency work under
the v4 end-of-life plan. Registry v5 is still intended for early adopters with
compatible use cases, and is not yet at full feature equivalency with v4. For
the current status, see :ref:`transitioning-feature-status`. For what the
COmanage Project is focusing on next, see the
`v4 end-of-life plan <https://spaces.at.internet2.edu/x/74ABFg>`_.

The COmanage Project's monthly **Open Office Hours** is an open call where
you can ask questions, share feedback, and hear how other organizations are
using Registry. Subscribe to the
`COmanage Project calendar <https://www.addevent.com/calendar/Nr648428>`_
for dates and connection links.

5. Acknowledgments
-------------------

Funding for Registry v5.3.0 has been provided by:

- The CILogon Project and the University of Illinois
- Internet2
- LIGO (Caltech)
- SCG Collaboration Group
- Southern Methodist University
- And an additional funder
