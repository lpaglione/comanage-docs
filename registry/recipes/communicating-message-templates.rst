.. DRAFT (Oct 2026): Recipe CM-01. Unpublished (listed in UNVERIFIED in
   conf.py). Template values come from the workshop deck (Section 4) and the
   kit's instructor guide (self sign-up), both tested on 5.2.0.

.. _recipe-communicating:

Communicating from Registry: Set Up Message Templates
=====================================================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Recipe:** CM-01 · **Registry:** v5.2.0 ·
**Features section:** :ref:`personalization-message-templates`

Registry sends email at many points: inviting someone, asking them to
confirm their address, asking an approver to review a request, and welcoming
a new member. Each of those messages comes from a **Message Template** that
you write once and attach where it's used. This recipe sets up the four
templates the Getting Started enrollment lessons need, so the messages come
from your organization, in your words.

Ingredients
-----------

- A CO where you can change configuration
- An outgoing mail (SMTP) server configured for your environment. A Platform
  Administrator adds it in the COmanage CO under **Configuration > Servers**
  and selects it in **CO Settings**.
- A way to read test email (see :ref:`gs-before-you-begin`)

Steps at a glance
-----------------

Select a card to jump to that step.

.. grid:: 1 2 4 4
   :gutter: 3

   .. grid-item-card:: 1. Prepare
      :link: gs-cm-step-contexts
      :link-type: ref

      Understand contexts and substitutions.

   .. grid-item-card:: 2. Add the templates
      :link: gs-cm-step-add
      :link-type: ref

      Write the four templates.

   .. grid-item-card:: 3. Attach them
      :link: gs-cm-step-attach
      :link-type: ref

      Attach each template where it's used.

   .. grid-item-card:: 4. Test
      :link: gs-cm-step-test
      :link-type: ref

      Send a test, and read it.

If something goes wrong, see :ref:`Troubleshoot <recipes/communicating-message-templates:Troubleshoot>`.

Step details
------------

Each step shows what to do. Select a heading marked ▸ to see why, or what to
do if something looks different.

.. _gs-cm-step-contexts:

1. Contexts and substitutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every template has a **Context**: the kind of message it is. The context
decides where the template can be attached and which substitutions it can
use.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Context
     - Used for
   * - Enrollment Handoff
     - The message sent when an enrollment passes to the next person: an
       invitation to the enrollee, or a request to an approver.
   * - Enrollment Finalization
     - The message sent to the new member when their enrollment is complete.
   * - Verification
     - The message carrying a code that confirms someone controls an email
       address.

**Substitutions** are placeholders that Registry fills in when it sends the
message. They're written ``(@NAME)``. The ones these templates use:

- ``(@CO_NAME)``: the CO's name
- ``(@ENROLLEE_NAME)``: the person enrolling
- ``(@ENTRY_URL)``: the link the recipient follows to act on the enrollment
- ``(@VERIFICATION_CODE)``: the code for email verification

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`personalization-message-templates` · Technical Manual:
   `Registry Message Templates (full list of substitutions)
   <https://spaces.at.internet2.edu/spaces/COmanage/pages/297862258/Registry+Message+Templates>`_

.. _gs-cm-step-add:

2. Add the templates
~~~~~~~~~~~~~~~~~~~~

Open **Configuration > Message Templates** (under Personalization) and
select **Add**. For each template below, set **Status** to Active and
**Format** to Plain Text, then fill in the rest and save.

.. list-table::
   :header-rows: 1
   :widths: 22 18 25 35

   * - Description
     - Context
     - Subject
     - Body
   * - Redcurrant Invitation
     - Enrollment Handoff
     - ``You are invited to join (@CO_NAME)``
     - ``Hello (@ENROLLEE_NAME), you have been invited to join (@CO_NAME).
       Open this link to accept: (@ENTRY_URL)``
   * - Redcurrant Approval Request
     - Enrollment Handoff
     - ``Please review a new member for (@CO_NAME)``
     - ``A new member, (@ENROLLEE_NAME), is waiting for your approval in
       (@CO_NAME). Review it here: (@ENTRY_URL)``
   * - Redcurrant Welcome
     - Enrollment Finalization
     - ``Welcome to (@CO_NAME)``
     - ``Hello (@ENROLLEE_NAME), your enrollment in (@CO_NAME) is
       complete.``
   * - Redcurrant Email Verification
     - Verification
     - ``(@CO_NAME) email verification code``
     - ``Your verification code is (@VERIFICATION_CODE).``

.. note::

   Plain-text templates can't contain ``<`` or ``>``. Write links as the
   bare ``(@ENTRY_URL)`` substitution.

.. SCREENSHOT: the Add a New Message Template form (not yet in
   comanage-files).

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`personalization-message-templates` (Defining a Template)

.. _gs-cm-step-attach:

3. Attach each template where it's used
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A template does nothing until it's attached. Where each one goes:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Template
     - Attach it to
   * - Redcurrant Invitation
     - The invitation step's **Handoff Message Template**, on the step's own
       form (not the plugin's)
   * - Redcurrant Approval Request
     - The approval step's **Handoff Message Template**
   * - Redcurrant Welcome
     - The enrollment flow's **Finalization Message Template**, on the flow's
       Properties tab. The flow must have **Collect Enrollee Email** ticked,
       or the welcome is never sent.
   * - Redcurrant Email Verification
     - The Email Verifier step's **Message Template**, on the plugin's form

The Getting Started lesson :ref:`gs-enroll-invite-member` attaches the first
three as it builds its flow; :ref:`gs-enroll-self-signup` uses the
verification template.

.. _gs-cm-step-test:

4. Send a test, and read it
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run a flow that uses the templates (for example the invitation lesson) and
open the messages in your test inbox. Check that:

- every substitution was filled in (no ``(@…)`` left in the text)
- the link in the invitation and approval request opens the right page

Troubleshoot
------------

.. dropdown:: No email arrives

   Check that an outgoing mail server is configured and selected in CO
   Settings, and that the template is Active and attached. For the welcome
   message, check that the flow has **Collect Enrollee Email** ticked.

.. dropdown:: A substitution arrives unreplaced

   Not every substitution is available in every context. In 5.2.0,
   ``(@EF_LAST_STEP_DESC)`` and ``(@EF_NEXT_STEP_DESC)`` aren't filled in for
   handoff messages, although the Technical Manual lists them. Leave them
   out of handoff templates for now.

.. dropdown:: The template doesn't appear where you expect it

   Check its Context and Status. A template is offered where its Context
   fits, for example an Enrollment Handoff template for a step's Handoff
   Message Template, and only when it's Active.

.. VERIFY: that template lists are filtered by Context and Status.

.. dropdown:: An enrollee sees "An Internal Error Has Occurred" before approval

   In 5.2.0, if a member of the approver group has no verified email
   address, the approval request fails. Make sure every approver has a
   verified email.
