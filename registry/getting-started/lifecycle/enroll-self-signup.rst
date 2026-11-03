.. DRAFT (Oct 2026): Lesson 5b. Unpublished (listed in UNVERIFIED in conf.py).
   Procedure adapted from the kit's instructor guide ("Enrollment:
   self-signup"), verified on 5.2.0 in the Discovery TNG demo CO; adapted
   here to the Guests CO. Walk through it in Guests before publishing.

.. _gs-enroll-self-signup:

Let Guests Sign Themselves Up
=============================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 5, Enrollment · **Learning paths:** Guest (Guests) ·
**Features section:** :ref:`using-lifecycle` · **Registry:** v5.2.0

The scenario
------------

Visitors to campus need guest Wi-Fi. Nobody on staff should have to set
each one up: a visitor should be able to sign in with an account they
already have, confirm their email address, and be enrolled as a guest
straight away.

In this lesson you build a **self sign-up** flow in the Guests CO, then sign
up as a visitor.

What you'll learn
-----------------

- How a self sign-up flow differs from an invitation: the petitioner and the
  enrollee are the same person. See :ref:`lifecycle-enrollment-flows`.
- How the **Email Verifier** step confirms someone controls an email address.
- How the **Identifier Collector** step records the login someone used, so
  they can sign in again later.

Ingredients
-----------

- The **Guests** CO from :ref:`gs-first-co` (create it now if you skipped it)
- Two message templates in the Guests CO, made as in
  :ref:`recipe-communicating` but named for Guests:

  - **Guests Email Verification**, Context Verification, with
    ``(@VERIFICATION_CODE)`` in the body
  - **Guests Welcome**, Context Enrollment Finalization

- A way to read test email (see :ref:`gs-before-you-begin`)
- A browser window that isn't logged in yet, for the visitor

Steps at a glance
-----------------

#. Prepare: add a COU for visitors
#. Configure: create the flow
#. Configure: add the steps
#. Use: sign up as a visitor
#. Check your work

Step details
------------

1. Add a COU for visitors
~~~~~~~~~~~~~~~~~~~~~~~~~

Guests who sign up need a unit to belong to. In the Guests CO, open
**Structure > COUs**, select **Add a New COU**, and save one with the Name
``Visitors`` and the Description ``Short-term campus visitors``.

.. admonition:: Learn more
   :class: seealso

   Lesson: :ref:`gs-structure-enterprise` (COUs and the special groups
   Registry creates for them)

2. Create the flow
~~~~~~~~~~~~~~~~~~

Open **People > Enrollment Flows** and select **Add**.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Field
     - Value
     - Why
   * - Name
     - ``Join Guest Wi-Fi``
     - Shown to the visitor when they start.
   * - Status
     - Active
     - The flow can be used.
   * - Petitioner Authorization
     - Any Authenticated User
     - Anyone who can sign in may start it: this is what makes it self
       sign-up.
   * - Collect Enrollee Email
     - Ticked
     - Without it, the welcome message is never sent.
   * - Finalization Message Template
     - Guests Welcome
     - The email the visitor gets when they're enrolled.

.. figure:: /comanage-files/registry_v5.2/enrollment/Enrollment-New.png
   :alt: The Add a New Enrollment Flow form: Name, Description, Status, Petitioner Authorization, Collect Enrollee Email, Redirect on Duplicate, Redirect on Finalize, Finalization Message Template and Notification Group
   :width: 100%

   The Add a New Enrollment Flow form.

.. SCREENSHOT: Enrollment-New.png shows the Discovery TNG CO; retake in
   Guests.

3. Add the steps
~~~~~~~~~~~~~~~~

On the flow's **Enrollment Flow Steps** tab, add these three steps, each
with Actor Type **Enrollee**. Each step is saved in two parts: the step's
own form, then the plugin's form. Close the dialog with the **X** after the
second save.

**Step 1: About you**

- Step form: Order ``1``, Plugin ``CoreEnroller.BasicAttributeCollectors``
- Plugin form: Name type **Official**, Email Address type **Personal**,
  Affiliation type **Affiliate**, COU **Visitors**

**Step 2: Verify your email address**

- Step form: Order ``2``, Plugin ``CoreEnroller.EmailVerifiers``
- Plugin form:

  .. list-table::
     :header-rows: 1
     :widths: 30 25 45

     * - Field
       - Value
       - Why
     * - Mode
       - One
       - The visitor verifies one address.
     * - Message Template
       - Guests Email Verification
       - The email carrying the code.
     * - Request Validity
       - ``60``
       - How long the code stays valid. Required: the field shows a
         placeholder, but you have to type a value.
     * - Enable Attempt Blocker
       - Unticked
       - Leave it off while testing, so a few wrong codes don't lock you
         out.

**Step 3: Link your login**

- Step form: Order ``3``, Plugin ``CoreEnroller.IdentifierCollectors``
- Plugin form: Identifier Type **Network**

This step has no page of its own. It records the username the visitor signed
in with as their login identifier, so they can sign in again later.

.. REVIEW: confirm the Request Validity unit, and whether the Identifier
   Collector needs "Login" set anywhere.

4. Sign up as a visitor
~~~~~~~~~~~~~~~~~~~~~~~

#. On the flow, copy the link from the **START** button (right-click and
   copy the link address).
#. In a browser window that isn't logged in, open that link and sign in as
   a new person, for example ``pat.newcomer``.
#. Enter an email address, then fill in **About you** with your name and the
   same email.
#. Select **Verify**. Open the verification email, copy the code, enter it,
   and select **Verify Email**.
#. Select **Finish**. The page says **Enrollment Complete**, and the welcome
   email follows.
#. Sign in again as ``pat.newcomer``: you land in the Guests CO.

.. warning::

   Don't click **START** while you're logged in as the administrator. In a
   self sign-up flow, whoever starts it becomes the enrollee.

.. note::

   How a visitor signs in depends on your environment. In a test environment
   that accepts any username, typing a new one is enough. In production,
   visitors would sign in through your identity provider or a social login.

Check your work
---------------

- **People > My Population** in Guests lists Pat Newcomer, Active, with a
  Visitors role and a verified email.
- Pat's record has a Network identifier ``pat.newcomer``.
- **People > Petitions** shows the petition as Finalized, with the collected
  information and its history.

Troubleshoot
------------

**The visitor never gets a verification code.** Check that the Email
Verifier's Message Template is set and Active, and that the environment can
send mail.

**Saving the Email Verifier fails.** Request Validity is required; type a
value.

**No welcome email.** Check that the flow has **Collect Enrollee Email**
ticked and a Finalization Message Template set.

**The administrator ended up as the enrollee.** Someone selected START while
logged in as the administrator. Terminate that petition under **People >
Petitions**, and start the flow from a window that isn't logged in.

**Signing up again with the same username fails.** Each login can enroll
only once. Use a different username to test again.

What you learned
----------------

- In a self sign-up flow, the person joining starts the flow themselves
  (Petitioner Authorization: Any Authenticated User).
- An Email Verifier step confirms the address before enrollment finishes.
- An Identifier Collector step keeps the login someone used, so they can
  return.

Where to go next
----------------

- Next: :ref:`gs-module-6`, to send people's information to the services
  they use
- Try on your own: add an approval step, so a staff member approves each
  visitor. The approver needs to be a Person in Guests with a login and a
  verified email (see :ref:`gs-enroll-invite-member`).
