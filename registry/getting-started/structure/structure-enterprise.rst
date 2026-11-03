.. DRAFT (Oct 2026): Lesson 3. Unpublished (listed in UNVERIFIED in conf.py).
   Procedure follows the workshop deck's Section 3 and the kit's instructor
   guide ("Organisational structure"), both tested on 5.2.0. Uses "special
   groups" (decided Oct 24); the Features pages still say "System Groups".

.. _gs-structure-enterprise:

Model Redcurrant University's Structure
=======================================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

**Module:** 3, Model Your Structure · **Learning paths:** Enterprise (Redcurrant
University; any CO with people in it works) ·
**Features section:** :ref:`using-structure` · **Registry:** v5.2.0
**Features section:** :ref:`using-structure` · **Registry:** v5.2.0

The scenario
------------

Redcurrant University's people don't all have the same relationship with the
university. There are faculty and staff, students, alumni, and retirees, and
each group gets access to different things. People also move between them:
when Ruth Spence retires, her access should change without anyone rebuilding
it by hand.

In this lesson you give Redcurrant its basic structure, then watch what
happens to Ruth's group memberships as her role changes.

What you'll learn
-----------------

- How **COUs** (Collaborative Organizational Units) divide a CO, and what
  Registry creates for each one. See :ref:`struct-cous`.
- How a **Person Role** ties someone to a COU, and how a role's status drives
  their group memberships. See :ref:`using-people`.
- The difference between **special groups**, which Registry creates and
  maintains, and **standard groups**, which you create, and how **nesting**
  connects them. See :ref:`org-groups`.

Ingredients
-----------

- Completed: :ref:`gs-module-2`, so that Ruth Spence (or another person) is in
  your CO. If you skipped Module 2, add a person by hand under
  **People > My Population > Add a New Person**.
- No plugins to activate

.. note::

   **Coming from v4?** The v4 version of this exercise also used CO
   Departments and CO Organizations. They're planned for v5 but aren't
   available in 5.2.0 yet, so this lesson uses COUs and groups. It can be
   extended when they arrive.

Steps at a glance
-----------------

#. Prepare: the four building blocks
#. Configure: add four COUs, and see the special groups Registry creates
#. Configure: create a standard group, and nest the active retirees into it
#. Enable: give Ruth a Faculty/Staff role
#. Use: Ruth retires
#. Check your work

Step details
------------

1. The four building blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Building block
     - What it does
   * - **COU**
     - A unit inside the CO, such as Faculty/Staff or Students. Each COU gets
       its own set of special groups, including admins, approvers and
       members groups.
   * - **Person Role**
     - Ties a Person to a COU, with an affiliation, a title and a status. One
       Person can hold several roles.
   * - **Special groups**
     - Groups Registry creates and keeps up to date, such as
       ``CO:COU:Retirees:members:active``. Their names start with ``CO:``.
   * - **Standard groups**
     - Groups you create, for example for access to a service. Their members
       can come from other groups through **nesting**.

The idea that ties them together: **roles drive membership.** Change a
role's status and the special groups follow, and through nesting, so do the
standard groups you've built on them. That's what downstream services see.

2. Add four COUs
~~~~~~~~~~~~~~~~

In Redcurrant University, open **Structure > COUs** and select **Add a New
COU**. Fill in the Name and Description and save. Repeat for each COU.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Name
     - Description
   * - ``Alumni``
     - Alumni of the student body
   * - ``Faculty/Staff``
     - Active faculty and administration
   * - ``Retirees``
     - Former faculty/staff
   * - ``Students``
     - Active students

Leave **Parent** empty: all four sit directly under the CO. Descriptions are
optional, but they appear in the COUs list and help others tell the units
apart.

.. figure:: /comanage-files/registry_v5.2/orgStructure/COUs_Saved.png
   :alt: The COUs list in Redcurrant University: Alumni, Faculty/Staff, Retirees and Students, each with its description
   :width: 100%

   The four COUs.

**See what Registry created.** Open **Structure > Groups**. For each COU,
Registry has added a set of special groups, for example:

- ``CO:COU:Retirees:admins`` and ``CO:COU:Retirees:approvers``: the people who
  administer this COU, and who approve its enrollments
- ``CO:COU:Retirees:members:active``: everyone with an **active** role in the
  COU
- ``CO:COU:Retirees:members:all``: everyone with **any** role in the COU,
  active or not (except archived)

Registry also creates owners groups. You don't add anyone to the members
groups yourself; Registry fills them from people's roles.

.. SCREENSHOT: the Groups list in Redcurrant University after adding the COUs
   (Groups.png in comanage-files shows the Discovery TNG CO).

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`struct-cous` · :ref:`org-groups`

3. Create a standard group, and nest the active retirees into it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Redcurrant lets every active retiree use the university wiki. Rather than
adding retirees to the wiki group one by one, you'll make the Retirees
members group a member of it.

**Create the group**

Open **Structure > Groups** and select **Add a New Group**.

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Field
     - Value
     - Why
   * - Name
     - ``Access-wiki``
     - Names the group. Standard group names can't start with ``CO:``, which
       is kept for special groups.
   * - Description
     - The individuals that can access the wiki tool.
     - Shows in lists and on people's records.
   * - Status
     - Active
     - The group is in use.

**Nest the retirees into it**

You set up nesting from the group whose members should flow **in**, not from
the group they flow into.

#. In the Groups list, open ``CO:COU:Retirees:members:active``.
#. Open its **Group Nestings** tab and select **Add**.
#. For **Target Group** (where the current group will be nested), choose
   **Access-wiki**. The **Nested Group** is filled in for you: it's the
   current group.
#. Leave **Negate Nesting** and **Queue Job to Add Group Nesting** unticked,
   and save.
#. Close the dialog with the **X**.

.. figure:: /comanage-files/registry_v5.2/orgStructure/Add_New_Group_Nesting.png
   :alt: The Add a New Group Nesting dialog on CO:COU:Retirees:members:active, with Target Group Access-wiki and Negate Nesting and Queue Job unticked
   :width: 100%

   Nesting the active retirees into Access-wiki.

.. note::

   In 5.2.0 the dialog stays open after you save, still showing a Save
   button, and the green "Saved" bar doesn't always appear. One save is
   enough. The new nesting appears in the **Group Nestings** list once you
   close the dialog.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`org-groups` (Group Nestings)

4. Give Ruth a Faculty/Staff role
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ruth came in from the HR file without a role: the file has no role columns.
Give her one by hand.

#. Find Ruth: type ``Spence`` in the search box at the top, or open
   **People > My Population**.
#. On her record, open the **Person Roles** tab and select **Add a New Person
   Role**.
#. Fill in the role and save. Leave the other fields empty.

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Field
     - Value
     - Why
   * - COU
     - Faculty/Staff
     - The unit this role belongs to.
   * - Affiliation
     - Member
     - The kind of relationship. The list comes from your CO's affiliation
       types.
   * - Status
     - Active
     - An active role puts her in the COU's ``members:active`` group.
   * - Title
     - ``Associate Professor``
     - Her job title in this role.
   * - Department
     - ``Biology``
     - Free text, for information.

.. figure:: /comanage-files/registry_v5.2/orgStructure/Add_New_Person_Role.png
   :alt: The Add a New Person Role form for Ruth Spence
   :width: 100%

   Adding Ruth's Faculty/Staff role.

Open her **Groups** tab. She's now in ``CO:COU:Faculty/Staff:members:active``
and ``CO:COU:Faculty/Staff:members:all``, with no one adding her to either.

.. admonition:: Learn more
   :class: seealso

   User guide: :ref:`using-people` (Person Roles)

5. Ruth retires
~~~~~~~~~~~~~~~

**First, end her Faculty/Staff role.** On Ruth's **Person Roles** tab, open
the Faculty/Staff role, set **Status** to **Expired**, and save. Then look at
her **Groups** tab.

She has left ``CO:COU:Faculty/Staff:members:active`` but is still in
``CO:COU:Faculty/Staff:members:all``: she still *has* a Faculty/Staff role,
just not an active one. With no active role left, Ruth herself now shows as
**Expired**.

.. figure:: /comanage-files/registry_v5.2/orgStructure/Ruth_Spence_Group_Memberships_Expired.png
   :alt: Ruth Spence's Groups tab with her status shown as Expired: she is in CO:members:all and CO:COU:Faculty/Staff:members:all only
   :width: 100%

   After her Faculty/Staff role expires.

.. SCREENSHOT: this capture shows External Identities (0); in the lesson Ruth
   came from the HR file, so it would show 1. Retake if it matters.

**Then, give her a Retirees role.** Select **Add a New Person Role** again:
COU **Retirees**, Affiliation **Member**, Status **Active**. Save, and look at
her **Groups** tab once more.

Ruth is Active again. She's in both Retirees members groups, and in
**Access-wiki** too, through the nesting you set up in step 3. The icon
beside Access-wiki means the membership can't be edited here: it comes from
the nesting, not from someone adding her.

.. figure:: /comanage-files/registry_v5.2/orgStructure/Ruth_Spence_Group_Memberships_Retirees.png
   :alt: Ruth Spence's Groups tab after the Retirees role: CO members groups, Faculty/Staff members:all, both Retirees members groups, and Access-wiki with a not-editable icon
   :width: 100%

   After her Retirees role is added. Access-wiki comes from the nesting.

.. note::

   This is how someone leaving or changing jobs looks in 5.2.0: you change
   their roles. Expiration policies, which automate this in v4, aren't
   available in v5 yet.

Check your work
---------------

- **Structure > COUs** lists Alumni, Faculty/Staff, Retirees and Students.
- **Structure > Groups** shows the special groups for each COU, and your
  standard group, Access-wiki.
- ``CO:COU:Retirees:members:active`` has a nesting into Access-wiki (its
  **Group Nestings** tab).
- Ruth has two roles: Faculty/Staff (Expired) and Retirees (Active).
- Ruth's **Groups** tab lists Access-wiki, marked as not editable.

Troubleshoot
------------

**You can't add someone to a members group.** The ``members:active`` and
``members:all`` groups are filled automatically from roles. Give the person a
role in that COU instead.

**The nesting doesn't appear in the Group Nestings list.** Close the dialog
with the X; the list updates only after it closes. If it's still missing,
open the dialog again and check that the Target Group was chosen before you
saved.

**The nesting goes the wrong way.** Check which group you started from: the
group you open is the one whose members flow *into* the Target Group. To
undo a nesting, click its row in the Group Nestings list (anywhere except the
group name) and delete it.

**Ruth isn't in Access-wiki after getting the Retirees role.** Check that the
Retirees role's Status is Active (only active roles count for
``members:active``) and that the nesting is on
``CO:COU:Retirees:members:active``, not on ``members:all``.

**Ruth is still in a Faculty/Staff group after her role expired.** That's
expected for ``members:all``, which includes every role in the COU whatever
its status. Only ``members:active`` drops her.

What you learned
----------------

- COUs divide a CO into units, and Registry creates special groups for each
  one.
- Person Roles connect people to COUs, and a role's status decides which
  special groups they're in.
- Nesting a special group into a standard group lets access follow people's
  roles, with no one curating membership by hand.

Where to go next
----------------

- Next: :ref:`gs-module-4`, to give everyone in Redcurrant a username
  automatically
- Try on your own: make someone an administrator of the Retirees COU by
  adding them to ``CO:COU:Retirees:admins`` (the group's **Group Members**
  tab).
