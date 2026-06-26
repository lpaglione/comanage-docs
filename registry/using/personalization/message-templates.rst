.. _personalization-message-templates:

Message Templates
==================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


Every automated email that Registry sends — an enrollment notification, a
petition approval, an email address verification, an Authenticator update — has
to come from somewhere. By default, Registry uses built-in message text. But
in most deployments you will want something that matches your organization's
voice, includes your own branding or instructions, and gives recipients the
context they need to take action.

**Message Templates** are reusable email content structures that replace
Registry's default message text. You define a template once — subject line, body
text, reply-to address — and Registry uses it every time an event of that type
occurs within your CO. Substitution tokens let each individual email be
personalized with the recipient's name, the CO name, relevant URLs, or other
context-specific values.

For the full technical reference, see
`Registry Message Templates <https://spaces.at.internet2.edu/spaces/COmanage/pages/297862258/Registry+Message+Templates>`_
in the Technical Manual.

How Message Templates Work
---------------------------

Message Templates are defined per-CO, at **ALL > Configuration > Message
Templates**. When an event occurs that would send a notification, Registry looks
for a Message Template matching that event's Context. If one is found, it uses
the template; if not, Registry uses its default built-in text.

This means you do not need to create templates for every possible event — you
can start with the ones that matter most for your enrollment workflows and add
others over time.

Templates and the SMTP relay they send through are configured separately. The
SMTP relay is configured as a Server in the External Connections area; see
:ref:`ec-servers` for details. A Template's Reply-To address can override the
default reply-to set on the SMTP Server, allowing different templates to route
replies to different inboxes.

Contexts
---------

Each Message Template belongs to a **Context** — a label that groups templates
by the situations in which they are used. Registry uses Contexts to match the
right template to the right event. The available Contexts are:

**Authenticator** :bdg-secondary:`Available: v5.2.0`
   Used when an Authenticator (password, SSH key, etc.) has been updated for a
   Person. Allows you to notify members when their credentials change.

**Enrollment Denial**
   Used when a Petition has been denied. Sent to the enrollee when an
   administrator or approver rejects an enrollment request.

**Enrollment Finalization**
   Used when a Petition has been successfully completed. Sent to the enrollee
   when enrollment is approved and finished.

**Enrollment Handoff**
   Used when a Notification is sent as part of an Enrollment Flow step handoff
   — when the enrollment process moves from one Actor type to another (for
   example, from the enrollee completing their self-enrollment steps to an
   administrator's approval step).

**Enrollment Step Completed**
   Used when a single Enrollment Flow step has been completed.

**Plugin**
   A generic Context intended for Message Templates used by specific Plugins.
   Review individual Plugin documentation for which Context value to use.

**Verification**
   Used for Email Address verifications — when Registry sends a verification
   link to confirm that a Person controls an email address.

Defining a Template
---------------------

To create a Message Template, navigate to **ALL > Configuration > Message
Templates > Add a New Message Template** and provide:

- **Context** — select from the available Contexts above
- **Description** — a label for this template (used only within Registry's
  configuration interface)
- **Subject** — the email subject line (substitutions supported)
- **Body (Plain Text)** — the plain text version of the message body
  (substitutions supported)
- **Body (HTML)** — the HTML version of the message body (substitutions
  supported); optional, but recommended for better presentation
- **Reply-To Address** — overrides the default reply-to from the SMTP Server
  configuration for this template (optional)
- **CC Addresses** — comma-separated list of addresses to CC (optional; ignored
  when a delivery override is set in the SMTP Server configuration)
- **BCC Addresses** — comma-separated list of addresses to BCC (optional; same
  caveat as CC)

You can provide both Plain Text and HTML bodies, either alone or together.

Substitution Tokens
--------------------

Message Templates support **substitutions** — tokens in the message subject and
body that Registry replaces with values specific to the notification being sent.
A substitution token is written as ``(@TOKEN_NAME)``.

For example, to address the recipient by name and include the CO name:

.. code-block:: text

   Hello (@ENROLLEE_NAME),

   Your enrollment in (@CO_NAME) has been approved.

The substitutions available depend on the template's Context. The following
tokens are available in templates:

.. list-table::
   :header-rows: 1
   :widths: 30 45 25

   * - Substitution
     - Description
     - Available In
   * - ``(@CO_NAME)``
     - The name of the CO
     - Any template
   * - ``(@COU_NAME)``
     - The name of the COU (if applicable)
     - Enrollment Flow templates
   * - ``(@EF_LAST_STEP_DESC)``
     - Description of the Enrollment Flow step just completed
     - Enrollment Handoff
   * - ``(@EF_NEXT_STEP_DESC)``
     - Description of the next Enrollment Flow step to run
     - Enrollment Handoff
   * - ``(@ENROLLEE_EMAIL)``
     - The collected Enrollee email address for the Petition
     - Enrollment Flow templates
   * - ``(@ENROLLEE_NAME)``
     - The collected Enrollee name for the Petition
     - Enrollment Flow templates
   * - ``(@ENTRY_URL)``
     - The entry URL for returning to the application
     - Any template
   * - ``(@NOTIFICATION_COMMENT)``
     - The notification comment
     - Any template
   * - ``(@NOTIFICATION_SOURCE)``
     - The notification source
     - Any template
   * - ``(@PETITION_URL)``
     - The URL to view the Petition
     - Enrollment Flow templates
   * - ``(@SUBJECT_NAME)``
     - The formatted primary name of the notification's subject Person
     - Any template with a Person as subject
   * - ``(@VERIFICATION_CODE)``
     - The email verification code
     - Verification templates

Plugins may support their own additional substitutions — check the relevant
Plugin documentation.

Changes from v4
----------------

Message Templates have been part of Registry since v2.0.0. The concept,
structure, and substitution mechanism are unchanged. If you are migrating from
v4, the main things to be aware of are how Context names have evolved:

- **Enrollment context names have been restructured** to align with the
  redesigned v5 Enrollment Flow model. The v4 contexts "Enrollment Flow Approval
  Notification" and "Enrollment Flow Finalization" map roughly to v5's
  "Enrollment Denial" and "Enrollment Finalization." The v4 "Enrollment Flow
  Approver Notification" context maps to aspects of the v5 "Enrollment Handoff"
  and "Enrollment Step Completed" contexts, which reflect v5's plugin-based step
  and Actor handoff model. Existing v4 Message Templates will need to be reviewed
  and remapped to the appropriate v5 Contexts.

- **"Enrollment Flow Verification" is now simply "Verification"** in v5.

- **The Authenticator Context** has existed since Registry v4.0.0 and continues
  in v5, available as of v5.2.0 when Authenticators became available in v5.

- **The Expiration Notification context** from v4 is not yet listed among v5
  Message Template Contexts. This context is expected to return alongside full
  v5 Expiration Policy support.
