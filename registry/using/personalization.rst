.. _using-personalization:

Personalization
================

Registry is built around a generic model that works for many organizations. But
your organization isn't generic — you have your own visual identity, your own
communication style, your own terminology for the relationships you manage, and
your own policies about what people can do for themselves. Personalization is
how you make Registry feel like it belongs to your organization rather than
just a piece of software you happen to be operating.

The features in this section fall into four broad purposes:

**Visual identity and content** — control how Registry looks and what people
see when they arrive. You can apply CSS themes to align the interface with your
organization's brand, create custom content pages (policies, help text, error
messages) that display within Registry's own look and feel, and maintain a media
library of images for use in those pages and themes.

**Communication** — control how Registry speaks to your members. Message
Templates let you define reusable email content for notifications, enrollment
events, and authentication updates, with substitutions that personalize each
message for its recipient and context.

**Data model customization** — control how Registry labels the building blocks
of your identity data. Types let you define the categories that apply to
multi-valued attributes across your CO: what kinds of names, identifiers, email
addresses, affiliations, and addresses your organization recognizes.

**User self-service and navigation** — control what members can do on their
own behalf and how they navigate Registry. Dashboards serve as information
portals and the primary surface for user self-service in v5.

----

.. contents:: On this page
   :local:
   :depth: 1

----

Visual Identity and Content
-----------------------------

**Themes**

Registry supports CSS-based theming that allows you to modify the look and feel
of the interface — colors, fonts, layout elements — to match your organization's
brand or website. Themes apply at the platform or CO level.

For configuration, see
`Theming COmanage Registry <https://spaces.at.internet2.edu/spaces/COmanage/pages/26582108/Theming+COmanage+Registry>`_
in the Technical Manual.

**Mostly Static Pages**

Mostly Static Pages let you create simple content pages — policy documents,
help text, custom error messages, enrollment landing pages — that are served
within Registry's interface. Each page has its own URL within your CO and
displays in the same visual style as the rest of Registry, including any CSS
theme you have applied.

Several Mostly Static Pages are created automatically with each CO for default
error and enrollment handoff behavior. You can edit their content to match your
organization's language and policies.

**Mostly Static Resources** *(new in v5.3.0)*

Mostly Static Resources provide a media library for uploading images and other
files that can be referenced from Mostly Static Pages and Themes. Resources are
served at a stable URL within your CO.

.. card:: Mostly Static Pages and Resources
   :link: personalization-mostly-static-pages
   :link-type: ref

   Creating and editing content pages, working with auto-created defaults, and
   managing the Mostly Static Resources media library.

Communication
--------------

**Message Templates**

Message Templates are reusable email content structures that Registry uses for
notifications, enrollment events, email address verification, and (as of v5.2.0)
Authenticator updates. Each template belongs to a Context that determines where
it will be used, supports both plain text and HTML bodies, and can include
substitution tokens that are replaced with relevant values when the email is
sent.

A well-configured set of Message Templates means every automated email from
Registry sounds like it came from your organization, not from a generic
identity management platform.

.. card:: Message Templates
   :link: personalization-message-templates
   :link-type: ref

   Configuring templates by context, using substitution tokens, and managing
   plain text and HTML bodies.

Data Model Customization
--------------------------

**Types**

Types are the category labels used across Registry's multi-valued attributes.
When a Person record can have multiple email addresses, the Type is what
distinguishes them — "official," "personal," "preferred," or whatever categories
make sense for your organization. The same pattern applies to Names, Identifiers,
Addresses, Telephone Numbers, URLs, Organizations, Departments, and Person Role
Affiliations.

Types are defined per-CO. When a new CO is created, Registry populates a default
set of Types for each supported attribute. You can add, modify, or (if not yet
used) delete Types to match your organization's terminology and workflows.

Affiliations (a type of Person Role attribute) have an additional option: they
can be mapped to standard eduPersonAffiliation values, which certain Provisioner
Plugins use when exporting data to downstream systems.

.. card:: Types
   :link: personalization-types
   :link-type: ref

   Configuring the category labels used across names, identifiers, email
   addresses, affiliations, and other multi-valued attributes.

.. note::

   **Relationship to v4 Attribute Enumerations and Dictionaries**

   In v4, Registry supported Attribute Enumerations (constraining free-form
   field values to a defined list) and Dictionaries (reusable value lists).
   These features were redesigned in v5. Registry Types in v5 govern attribute
   *categorization* (the type of a multi-valued attribute), not value
   *constraint* in the v4 sense. The status of value-constraint functionality
   in v5 is under active development — check the Technical Manual or community
   channels for current status.

Navigation and Self-Service
-----------------------------

**Dashboards**

Dashboards are simple information portals within a CO. Multiple Dashboards can
be defined, each composed of Dashboard Widgets that display relevant content
or provide self-service capabilities for members. Dashboard Widgets are
implemented as plugins, so the set of available dashboards can be extended.

In v5, Dashboards are the primary surface for user self-service. Capabilities
such as viewing enrollment petition status, managing Authenticators, and group
self-management are provided through Dashboard Widgets rather than embedded
directly in the main navigation.

For configuration, see
`Registry Dashboards <https://spaces.at.internet2.edu/spaces/COmanage/pages/126619230/Registry+Dashboards>`_
in the Technical Manual.

.. note::

   The self-service capabilities available through Dashboards in v5 are actively
   being developed and expanded. The v4 Self-service Permissions feature has been
   redesigned around Dashboard-based access in v5. For current status, see the
   Registry community channels and the issue tracker.

**CO Navigation Links**

Registry supports the creation of custom navigation links that persist across
the platform or within a specific CO. These can be used to link back to your
organization's website or to create a custom menu within Registry.

.. note::

   The status of CO Navigation Links as a distinct feature in Registry v5 is
   not fully reflected in the Technical Reference available to this guide. For
   current information, see
   `Configuring Navigation Links <https://spaces.at.internet2.edu/spaces/COmanage/pages/219918764/Configuring+Navigation+Links>`_
   in the Technical Manual.

Localization
-------------

Registry can be localized to translate the interface into another language or
to customize specific labels within a CO — for example, to change terminology
that doesn't match how your organization talks about its members.

.. note::

   Localization documentation is not fully reflected in the Technical Reference
   available to this guide. For current information, see
   `Registry Interface Localization <https://spaces.at.internet2.edu/spaces/COmanage/pages/43614734/Registry+Interface+Localization>`_
   in the Technical Manual.

----

If You Are Migrating from v4
------------------------------

Several v4 Personalization features have changed significantly in v5:

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

.. toctree::
   :hidden:

   personalization/message-templates
   personalization/types
   personalization/mostly-static-pages
