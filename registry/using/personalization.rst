.. _using-personalization:

Personalization
================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry is built around a generic model that works for many organizations. But
your organization isn't generic — you have your own visual identity, your own
communication style, your own terminology for the relationships you manage, and
your own policies about what people can do for themselves. Personalization is
how you make Registry feel like it belongs to your organization rather than
just a piece of software you happen to be operating.

The features currently available in this section fall into two broad purposes:

**Visual identity and content** — create custom content pages (policies, help
text, error messages, enrollment landing pages) that display within Registry's
own look and feel, and maintain a media library of images for use in those pages.

**Communication** — control how Registry speaks to your members. Message
Templates let you define reusable email content for notifications, enrollment
events, and authentication updates, with substitutions that personalize each
message for its recipient and context.

Additional Personalization features — including CSS theming, dashboards,
navigation links, and localization — are being completed for v5. See
`Coming to v5`_ below.

1. Visual Identity and Content
------------------------------

**Mostly Static Pages**

Mostly Static Pages let you create simple content pages — policy documents,
help text, custom error messages, enrollment landing pages — that are served
within Registry's interface. Each page has its own URL within your CO and
displays in the same visual style as the rest of Registry, including any CSS
theme you have applied.

Several Mostly Static Pages are created automatically with each CO for default
error and enrollment handoff behavior. You can edit their content to match your
organization's language and policies.

**Mostly Static Resources** :bdg-success:`New in v5` :bdg-secondary:`Available: v5.3.0`

Mostly Static Resources provide a media library for uploading images and other
files that can be referenced from Mostly Static Pages and Themes. Resources are
served at a stable URL within your CO.

.. button-ref:: personalization-mostly-static-pages
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Mostly Static Pages and Resources →

2. Communication
----------------

**Message Templates**

Message Templates are reusable email content structures that Registry uses for
notifications, enrollment events, email address verification, and Authenticator updates. Each template belongs to a Context that determines where
it will be used, supports both plain text and HTML bodies, and can include
substitution tokens that are replaced with relevant values when the email is
sent.

A well-configured set of Message Templates means every automated email from
Registry sounds like it came from your organization, not from a generic
identity management platform.

.. button-ref:: personalization-message-templates
   :ref-type: ref
   :color: primary
   :outline:
   :align: right

   Learn more about Message Templates →

----

.. _personalization-coming-to-v5:

3. Coming to v5
---------------

The following Personalization features are available in Registry v4 and are
being completed for v5 in the coming releases. See :doc:`../transitioning/index`
for current feature completion status.

**Visual Identity and Content**

*Themes* — CSS-based theming lets you modify the look and feel of the Registry
interface — colors, fonts, layout elements — to match your organization's brand
or website. Themes apply at the platform or CO level. For reference while v5
theming is in progress, see
`Theming COmanage Registry <https://spaces.at.internet2.edu/spaces/COmanage/pages/26582108/Theming+COmanage+Registry>`_
in the v4 Technical Manual.

**Navigation and Self-Service**

*Dashboards* — Dashboards will be the primary surface for user self-service in
v5, composed of Dashboard Widgets that provide capabilities such as managing
Authenticators, viewing enrollment petition status, and group self-management.
The planned design is described in the Registry PE Delegated Administration and
User Self Service specification in the Technical Manual.

*CO Navigation Links* — custom links that persist across the platform or within
a specific CO, used to link back to your organization's website or create a
custom menu within Registry.

**Localization**

*Localization* — the ability to translate the Registry interface into another
language, or to customize specific labels within a CO to match how your
organization talks about its members. For reference while v5 localization is in
progress, see
`Registry Interface Localization <https://spaces.at.internet2.edu/spaces/COmanage/pages/43614734/Registry+Interface+Localization>`_
in the v4 Technical Manual.

----

4. If You Are Migrating from v4
-------------------------------

Several v4 Personalization features have changed significantly in v5:

- **Extended Types** — In v4, Extended Types were part of Personalization. In
  v5, they have been renamed to **Types** and moved to the Extending Registry
  section, reflecting their role in extending the data model. See
  :ref:`extend-types`.

- **Attribute Enumerations** — The v4 mechanism for constraining free-form
  field values to a defined list has been redesigned. In v5, Types govern
  attribute categorization, which is a related but distinct concept. Value
  constraint functionality is under active development in v5.

- **Dictionaries** — v4 Dictionaries (reusable value lists for Attribute
  Enumerations and Identifier Validation) have not carried over directly to
  v5. Check the current Technical Manual and community channels for status.

- **Self-service Permissions** — The v4 Self-service Permissions feature has
  been replaced by a Dashboard-based approach in v5. Self-service capabilities
  are now provided through Dashboard Widgets and permission configurations.

- **Mostly Static Pages** — Now a standard data model element (as of v5.1.0),
  no longer requiring filesystem access.

----

Pages in This Section
----------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   personalization/mostly-static-pages
   personalization/message-templates