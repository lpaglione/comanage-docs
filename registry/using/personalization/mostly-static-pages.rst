.. _personalization-mostly-static-pages:

Mostly Static Pages and Resources
===================================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


Registry is an identity management platform, not a general-purpose web
publishing system. But every deployment has some content that needs to live
alongside the Registry interface — a policy your members must acknowledge before
completing enrollment, an error message that tells them what to do when something
goes wrong, a help page explaining what the enrollment process involves.

:bdg-secondary:`Available: v5.1.0` **Mostly Static Pages** solve this by letting you
publish simple content pages that display within Registry's own look and feel —
using the same navigation, header, footer, and CSS theme as the rest of the
interface. Administrators create and edit page content through the Registry
configuration interface, with no filesystem access required.

:bdg-success:`New in v5` :bdg-secondary:`Available: v5.3.0` **Mostly Static Resources** extend this with a media
library for uploading images and files that can be referenced from pages and
themes, served at stable URLs within your CO.

For the full technical reference, see
`Mostly Static Pages <https://spaces.at.internet2.edu/spaces/COmanage/pages/318570826/Mostly+Static+Pages>`_
and
`Mostly Static Resources <https://spaces.at.internet2.edu/spaces/COmanage/pages/409763999/Mostly+Static+Resources>`_
in the Technical Manual.

Mostly Static Pages
---------------------

**What they're for**

Mostly Static Pages are appropriate for:

- Policy documents and terms of use that appear before or during enrollment
- Custom error messages (with instructions specific to your organization)
- Enrollment handoff instructions (explaining what a self-enrolling user should
  do next)
- Help and FAQ content available at a stable URL within Registry
- Landing pages for completed enrollments

.. note::

   Mostly Static Pages present public content — no authentication is required
   to view them. Do not use them to display information from the Registry
   database or any content that should be access-controlled. If you need
   dynamic, authenticated content, you will need to write a Registry Plugin.

**Creating and editing pages**

Mostly Static Pages are managed via **ALL > Configuration > Mostly Static Pages
> Add a New Mostly Static Page**.

Each page has three required fields:

- **Title** — displayed at the top of the page and in the browser tab or title
  bar
- **Slug** — a URL-safe identifier used to construct the page's URL; must be
  unique within the CO and consist only of lowercase alphanumeric characters
  and dashes (e.g., ``enrollment-help``)
- **Body** — the page content; HTML tags are currently permitted

Once saved, Registry displays a **Page Display URL** directly below the
configuration fields. This is the stable URL at which the page is available
within your CO. The format is generally ``$REGISTRY/<coid>/<slug>``.

**Context** is an advisory field that helps organize pages in the configuration
interface. It has no functional effect currently but may be used in future
releases.

Default Mostly Static Pages
-----------------------------

When a new CO is created, Registry automatically creates the following Mostly
Static Pages with default content. These handle common error and workflow states
within the platform:

**default-handoff**
   Displayed when an Enrollment Flow transitions from one Actor type to another
   — for example, from the self-enrollment steps completed by the enrollee to
   an administrator approval step. The default content typically prompts the
   enrollee to wait for further communication.

**duplicate-landing**
   Displayed when a Petition is identified as a duplicate of an existing
   enrollment — when the system determines the person may already be in Registry.

**error-landing**
   A generic error page shown when Registry encounters an error but has no
   other place to send the user.

**mfa-required**
   Displayed when Multi-Factor Authentication is required for access to Registry
   but was not signaled by the authentication provider.

**petition-complete**
   Displayed when a Petition has completed — either via successful finalization
   or when an invitation has been declined.

The content (title and body) of all five default pages can be edited to match
your organization's language and instructions. However, they cannot be renamed
or deleted — they are expected by Registry's workflow logic.

**Customizing default pages**

Consider updating the default pages early in your Registry setup. In particular:

- Edit **default-handoff** to include instructions appropriate for your
  enrollment workflows (e.g., "Thank you for completing your enrollment. An
  administrator will review your application and contact you at the email
  address you provided.")
- Edit **error-landing** to include a contact address or help link so members
  know how to get assistance.
- Edit **petition-complete** to confirm next steps or set expectations for
  follow-up.

Mostly Static Resources
------------------------

Mostly Static Resources (v5.3.0) provide a media library for your CO. You can
upload images and other files that are then served at stable, public URLs within
your CO — useful for images referenced in Mostly Static Pages or in CSS themes.

**Adding resources**

Resources are managed via **CO Settings > Mostly Static Resources > Add a New
Mostly Static Resource**.

Each resource requires:

- **Title** — an administrative label (not currently displayed to end users)
- **Slug** — a URL-safe identifier unique within the CO (lowercase alphanumeric
  characters and dashes only)
- **File** — the file to upload

File uploads must be enabled by your Registry platform administrator before
Mostly Static Resources can be added. See
`Enabling File Uploads <https://spaces.at.internet2.edu/spaces/COmanage/pages/409764013/Enabling+File+Uploads>`_
in the Technical Manual.

**Accessing resources**

After uploading, the resource is available via a **View** link in the
configuration interface. The URL format is ``$REGISTRY/<coid>/media/<slug>``.
Resources are public — no authentication is required to access them.

To use an image resource in a Mostly Static Page body, reference the resource
URL in a standard HTML ``<img>`` tag. To use it in a CSS theme, reference the
URL in the appropriate stylesheet rule.

Changes from v4
----------------

- **Mostly Static Pages are now a standard data model element** as of v5.1.0.
  In earlier versions of v5 (v5.0.x), Mostly Static Pages required filesystem
  access and were not available through the standard configuration interface.
  They were not available at all in v5.0.x. If you are upgrading from v5.0.x,
  you will need to recreate any static pages through the new configuration
  interface.

- **Mostly Static Resources are new in v5.3.0** and have no direct v4
  equivalent.
