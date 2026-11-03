.. DRAFT (Oct 2026): Lesson 5a. Unpublished (listed in UNVERIFIED in conf.py).
   Procedure follows the workshop deck's Section 4 (h4a, h4b, h4b2, h4c),
   tested on 5.2.0 through a full invitation, approval and login.

.. _gs-enroll-invite-member:

Invite a New Member
===================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 5, Enrollment · **Learning paths:** Enterprise (Redcurrant
University) · **Features section:** :ref:`using-lifecycle` ·
**Registry:** v5.2.0

The scenario
------------

Redcurrant University wants its administrators to bring in people who
aren't in the HR file yet, such as a new colleague who starts next month.
Ruth Spence, now one of Redcurrant's administrators, will invite **Casey
Invitee**. Casey accepts by email and adds their pronouns, Ruth approves,
and Casey ends up as a member of Faculty/Staff with a username they can log
in with.

What you'll learn
-----------------

- How a v5 **Enrollment Flow** is built from **steps**, each done by one
  **actor**: the petitioner, the enrollee or the approver. See
  :ref:`lifecycle-enrollment-flows`.
- How a **petition** records an enrollment as it moves from person to person.
- How message templates and identifier assignment fit into an enrollment.

Ingredients
-----------

- Completed: :ref:`gs-module-3` (Redcurrant has a Faculty/Staff COU, and
  Ruth Spence is a Person in the CO) and :ref:`gs-module-4` (new people get a
  username)
- The templates from :ref:`recipe-communicating`: Redcurrant Invitation,
  Redcurrant Approval Request and Redcurrant Welcome
- A way to read test email (see :ref:`gs-before-you-begin`)
- **Two browsers**, or one browser plus a private window: one for Ruth, one
  for Casey. In Chrome, all private windows share one login, so close any
  open private windows before you start, or use a second browser.

Steps at a glance
-----------------

Select a card to jump to that step.

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: 1. Prepare
      :link: gs-invite-step-flow
      :link-type: ref

      See the flow you'll build: four steps, three actors.

   .. grid-item-card:: 2. Get Ruth ready
      :link: gs-invite-step-ruth
      :link-type: ref

      Make Ruth an administrator, with a verified email.

   .. grid-item-card:: 3. Create the flow
      :link: gs-invite-step-create
      :link-type: ref

      Set up the enrollment flow's properties.

   .. grid-item-card:: 4. Add the steps
      :link: gs-invite-step-steps
      :link-type: ref

      Add the four steps, one for each hand-off.

   .. grid-item-card:: 5. Run it
      :link: gs-invite-step-run
      :link-type: ref

      Ruth invites Casey, Casey accepts, Ruth approves.

Then :ref:`check your work <getting-started/lifecycle/enroll-invite-member:Check your work>`.

Step details
------------

Each step shows what to do. Select a heading marked ▸ to see why, or what to
do if something looks different.

.. _gs-invite-step-flow:

1. The flow you'll build
~~~~~~~~~~~~~~~~~~~~~~~~

:bdg-success:`Redesigned in v5`

.. list-table::
   :header-rows: 1
   :widths: 10 30 15 45

   * - Step
     - What happens
     - Actor
     - Plugin (``CoreEnroller.…``)
   * - 1
     - Ruth enters Casey's name and email
     - Petitioner
     - ``BasicAttributeCollectors``
   * - 2
     - Casey accepts the emailed invitation
     - Enrollee
     - ``InvitationAccepters``
   * - 3
     - Casey adds their pronouns
     - Enrollee
     - ``AttributeCollectors``
   * - 4
     - Ruth approves
     - Approver
     - ``ApprovalCollectors``

In v5, a flow is a list of steps you assemble, not a fixed sequence. Each
step is a plugin that does one job, and each has its own settings, such as
the message sent when it hands off to the next person. Information can be
collected over several steps, from different people: here Ruth enters the
name and email, and Casey adds their pronouns.

Everything that happens is recorded in a **petition**, which you can follow
under **People > Petitions**.

.. dropdown:: Why Ruth, and not the platform administrator?
   :icon: info

   In 5.2.0, starting an invitation that's limited to CO Administrators
   needs someone who is a Person in the CO. The platform administrator
   isn't, so Ruth does it.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`lifecycle-enrollment-flows`

.. _gs-invite-step-ruth:

2. Make Ruth an administrator, with a verified email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As the platform administrator, in Redcurrant University:

**Add Ruth to the CO's administrators**

#. Open **Structure > Groups** and select ``CO:admins``.
#. Open its **Group Members** tab and select **Add member**.
#. Type ``Spence``, choose Ruth Spence, and save.
#. Close the dialog with the **X**. (It stays open after you save.)

**Give Ruth a verified email address**

#. Open Ruth's record (search for ``Spence``).
#. Under **Attributes**, add an **Email Address**:
   ``ruth.spence@redcurrant.example``, type Official.
#. Select **Force Verify** on the new address, once.

.. warning::

   Ruth approves in this lesson, so she needs a **verified** email. Press
   **Force Verify** only once: pressing it again on an address that's
   already verified gives an error.

.. dropdown:: What happens without a verified email?
   :icon: info

   In 5.2.0, if a member of the approver group has no verified email, the
   invitee sees "An Internal Error Has Occurred" after adding their
   pronouns, and no approval request is sent.

.. _gs-invite-step-create:

3. Create the flow
~~~~~~~~~~~~~~~~~~

Open **People > Enrollment Flows** and select **Add**. Fill in the
properties and save.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Field
     - Value
   * - Name
     - ``Invite a Member``
   * - Status
     - Active
   * - Petitioner Authorization
     - CO Administrator
   * - Collect Enrollee Email
     - Ticked
   * - Finalization Message Template
     - Redcurrant Welcome

.. important::

   **Tick Collect Enrollee Email.** It's off by default, and without it the
   welcome message is never sent.

.. dropdown:: Why these settings?
   :icon: info

   - **Name** is shown to people who can start the flow.
   - **Status: Active** means the flow can be used.
   - **Petitioner Authorization** is who may start it: here, Redcurrant's
     administrators, such as Ruth.
   - **Finalization Message Template** is the email Casey gets when the
     enrollment is complete.

.. figure:: /comanage-files/registry_v5.2/enrollment/Configure_Enrollment_Flow.png
   :alt: The Properties tab of the Invite a Member enrollment flow: Name, Description, Status Active, Petitioner Authorization CO Administrator, Collect Enrollee Email ticked, with the START button at the upper right
   :width: 100%

   The flow's Properties tab. Once it's saved, the **Enrollment Flow Steps**
   and **Petitions** tabs appear.

.. _gs-invite-step-steps:

4. Add the steps
~~~~~~~~~~~~~~~~

On the flow's **Enrollment Flow Steps** tab, select **Add a New Enrollment
Flow Step** for each step below. Each step is saved in two parts: the
step's own form (description, order, actor, plugin, handoff message), then
the plugin's form. The dialog stays open after the second save; close it
with the **X**.

**Step 1: Enter invitee details**

- Step form: Order ``1``, Actor Type **Petitioner**, Plugin
  ``CoreEnroller.BasicAttributeCollectors``
- Plugin form: Name type and Email Address type **Official**, Affiliation
  type **Member**, COU **Faculty/Staff**

**Step 2: Accept invitation**

- Step form: Order ``2``, Actor Type **Enrollee**, Plugin
  ``CoreEnroller.InvitationAccepters``, Handoff Message Template **Redcurrant
  Invitation**
- Plugin form: Invitation Validity ``0`` (no expiry)

.. warning::

   In 5.2.0, Invitation Validity is applied in **seconds**, although its label
   says minutes. The default, 1440, makes an invitation expire after 24
   minutes. Use ``0`` for no expiry.

**Step 3: Tell us about yourself**

- Step form: Order ``3``, Actor Type **Enrollee**, Plugin
  ``CoreEnroller.AttributeCollectors``
- Plugin page: select the small **Enrollment Attributes** link at the upper
  right, then **Add**, and choose **Pronouns**.

**Step 4: Approve new member**

- Step form: Order ``4``, Actor Type **Approver**, Plugin
  ``CoreEnroller.ApprovalCollectors``, Handoff Message Template **Redcurrant
  Approval Request**
- After saving, select the step again and **Edit** it: set **Approver Group**
  to ``CO:admins``. In 5.2.0 this field only appears when you edit a saved
  step.

.. figure:: /comanage-files/registry_v5.2/enrollment/Enrollment_Flow_Steps.png
   :alt: The Enrollment Flow Steps tab of Invite a Member: Enter invitee details (Petitioner), Accept invitation (Enrollee), Tell us about yourself (Enrollee) and Approve new member (Approver), with their plugins
   :width: 100%

   The finished flow: four steps, three actors.

.. dropdown:: Why these settings?
   :icon: info

   - **Step 1's COU** gives Casey a Faculty/Staff role when the enrollment
     finishes.
   - **A step's Handoff Message Template** is the email sent to whoever acts
     on that step, so step 2's is Casey's invitation, and step 4's is Ruth's
     approval request.
   - **Approver Group** ``CO:admins``: without it, the CO's approvers group
     is used, which has no one in it.

.. dropdown:: Can't find the pronouns or the Approver Group?
   :icon: question

   Two settings hide in corners: the pronouns are behind the **Enrollment
   Attributes** link on the Attribute Collector's page, and the Approver
   Group only shows when you **Edit** a saved step.

.. _gs-invite-step-run:

5. Ruth invites Casey, Casey accepts, Ruth approves
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use two browsers: one for Ruth, one for Casey. Open each email link in the
right person's browser.

#. **Ruth's browser.** Log out as the administrator and log in as
   ``ruth.spence``. Open **People > Enrollment Flows** and start **Invite a
   Member**. Enter Casey's email, ``casey@redcurrant.example``, then their
   name, **Casey Invitee**. The petition now waits for Casey.
#. **Casey's browser.** Open the invitation email and follow its link.
   Accept the invitation, add pronouns, and continue. The petition now waits
   for approval, and Ruth gets the approval request.
#. **Ruth's browser.** Open the approval request email, follow its link, and
   **Approve**.
#. **Casey's browser.** When the welcome email arrives, log in as
   ``casey.invitee``.

.. dropdown:: A red bar says "Petition N is not in Finalizing status"?
   :icon: question

   After Ruth approves, the page says **Enrollment Complete**, with a red bar
   reading "Petition N is not in Finalizing status". In 5.2.0 this appears on
   every successful enrollment, and the petition is finalized. The page has
   no menus; use the browser's Back button to return to Registry.

.. dropdown:: Why doesn't Casey log in until the end?
   :icon: info

   Casey doesn't log in during the enrollment: the links in the emails carry
   everything needed. Casey's username comes from the Identifier Assignment
   you set up in :ref:`gs-module-4`.

Check your work
---------------

- **People > My Population** lists Casey Invitee, Active, with a
  Faculty/Staff role, their pronouns, and a Network identifier
  ``casey.invitee`` flagged for login.
- **People > Petitions** shows the petition as Finalized, with its history.
- Casey can log in as ``casey.invitee`` and lands in Redcurrant University.

Troubleshoot
------------

.. dropdown:: Starting the flow as the platform administrator ends in "too many redirects"

   In 5.2.0 the administrator isn't a Person in the CO, so it can't start a
   CO Administrator flow. Start it as Ruth.

.. dropdown:: Casey sees "An Internal Error Has Occurred" after adding pronouns

   A member of the approver group (Ruth) has no verified email. Force-verify
   Ruth's email, then have Ruth open the petition under **People >
   Petitions** and resume it to approve.

.. dropdown:: An email link ends on "The requested address … was not found"

   The link was opened in a browser logged in as someone else; it's really a
   permission error. The invitation may now be tied to the wrong login: as
   the administrator, open the petition under **People > Petitions**,
   terminate it, and have Ruth invite again. Open each link in the right
   person's browser.

.. dropdown:: The invitation has expired

   Invitation Validity is in seconds in 5.2.0. Set it to ``0`` on the Accept
   invitation step's plugin form.

.. dropdown:: No approval request arrives

   Check that the approval step has a Handoff Message Template, that its
   Approver Group is ``CO:admins``, and that Ruth is in ``CO:admins`` with a
   verified email.

.. dropdown:: Casey can log in but sees no COs

   Casey has no username flagged for login. Check the Identifier Assignment
   from :ref:`gs-module-4` is Active and its Identifier Type has **Login**
   ticked.

.. dropdown:: Reopening a used invitation link gives an error

   That's expected: the petition is complete.

What you learned
----------------

- A v5 enrollment flow is assembled from steps, each done by the petitioner,
  the enrollee or an approver.
- A petition records each enrollment, and you can follow it under People >
  Petitions.
- Message templates carry the enrollment from person to person by email, and
  an identifier assignment gives the new person a username.

Where to go next
----------------

- Next: :ref:`gs-enroll-self-signup`, where people enroll themselves
- Try on your own: start an invitation and stop before Casey accepts. Then
  open **People > Petitions** and look at which step the petition is waiting
  on.
