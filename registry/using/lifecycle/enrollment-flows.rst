.. _lifecycle-enrollment-flows:

Enrollment Flows
=================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


:bdg-warning:`Redesigned in v5` :bdg-secondary:`Available: v5.1.0` Every organization has one or more ways of bringing new people into that
organization — applications, invitations, intakes, signups. These processes
vary significantly: some require approval, some require email verification, some
involve collecting a specific set of attributes, some are immediate and others
multi-step. **Enrollment Flows** are Registry's mechanism for modeling these
processes precisely.

An Enrollment Flow defines a sequence of Steps that participants move through.
When someone begins a Flow, they create a **Petition** — the artifact that tracks
their progress and interim data through the process. At the end of a successful
Flow, the Petition is finalized and an operational Person record is created
(or updated, in the case of additional-role enrollments).

Enrollment Flows are designed for interactive, human-driven processes. For
automated system-to-system population of Registry, see
:ref:`ec-external-identity-sources` instead.

For the full technical reference, see
`Registry PE Enrollment Flows <https://spaces.at.internet2.edu/spaces/COmanage/pages/289113561/Registry+PE+Enrollment+Flows>`_
in the Technical Manual.

.. note::

   Enrollment Flows are **not available in Registry v5.0.x**.

Enrollment Flow Actors
-----------------------

Each participant in an Enrollment Flow plays a role, or **Actor type**:

- **Petitioner** — the person who starts the Flow
- **Enrollee** — the person being enrolled (the subject of the Flow)
- **Approver** — the person who reviews and approves the enrollment

In a self-signup flow, the Petitioner and Enrollee are the same person. An
invitation flow might have no Approver at all. A Flow can involve as many Actor
type changes as needed — the sequence of who does what is fully configurable.

When a Step is assigned to a different Actor type than the preceding Step, a
**handoff** occurs: the current Actor is redirected to a holding page (typically
the ``default-handoff`` Mostly Static Page) and the next Actor receives a
Notification with a link to continue the Flow.

Configuring Enrollment Flows
------------------------------

New Enrollment Flows are created via **Configuration > Enrollment Flows > Add a
New Enrollment Flow**. The following settings are configured at the Flow level:

**Petitioner Authorization** — who is allowed to start this Flow:

- *Any Authenticated User* — the Petitioner must successfully authenticate to
  the web server, but does not need an existing Person record in Registry. Use
  this for Flows where the Petitioner brings an External Identity from a
  federated or social login provider.
- *None* — anyone can start the Flow without authentication. Use this for Flows
  that create local identities as part of the enrollment process. Note that Flows
  with no authorization may attract spam submissions and should include approval
  or verification steps.

**Collect Enrollee Email** — if set, the Petitioner must provide an email address
for the Enrollee before the Flow begins. This supports invitation-style Flows,
where the collected address is used to hand off the Flow to the Enrollee. The
address does not automatically become part of the Person record.

**Enable People Picker for Self Service** :bdg-secondary:`Available: v5.2.0` — enables the People Picker
API for unauthenticated Petitioners associated with this Flow.

**Redirect on Duplicate** — when a Petition is flagged as a duplicate, the Actor
who ran the step that detected the duplicate is redirected to the configured URL,
or to the ``duplicate-landing`` Mostly Static Page if none is configured.

**Redirect on Finalize** — when the Petition finalizes, the Actor who ran the
last step is redirected to the configured URL. Useful for a "What's next?"
landing page with follow-up instructions.

**Finalization Message Template** :bdg-secondary:`Available: v5.2.0` — if an Enrollee email address was
collected, Registry sends a message using this template (of context Enrollment
Finalization) when the Petition is finalized. If no address was collected, a
Notification is sent to the Enrollee Person instead (delivery via email depends
on a configured email address on the Person record).

**Notification Group** :bdg-secondary:`Available: v5.2.0` — all members of the specified Group receive a
Notification whenever any Step in this Flow is completed.

**Group Notification Message Template** :bdg-secondary:`Available: v5.2.0` — the Message Template (of
context Enrollment Step Completed) used for Notifications to the Notification
Group.

Enrollment Flow Steps
----------------------

Once the Enrollment Flow is saved, a link to add **Steps** becomes available.
Each Step represents one stage of the process, implemented by a plugin. Steps
are executed from the lowest order value to the highest.

For each Step, you configure:

- **Plugin** — the plugin that implements this Step. Once selected, it cannot
  be changed for that Step. A given plugin can appear in multiple Steps within
  the same Flow; for example, the Attribute Collector can collect attributes
  from the Petitioner in one Step and from the Enrollee in a later Step.
- **Order** — a unique numeric value determining execution order. If omitted,
  the next sequential order for this Flow is automatically assigned.
- **Actor Type** — whether this Step is completed by the Petitioner, Enrollee,
  or Approver. Consecutive Steps with different Actor Types trigger a handoff.
- **Message Template** — the template (of context Enrollment Handoff) used for
  the Notification sent to the next Actor when a handoff occurs.
- **Redirect on Handoff** — the URL the current Actor is redirected to when a
  handoff occurs. Defaults to the ``default-handoff`` Mostly Static Page if not
  specified.
- **Notification Group** and **Group Notification Message Template** — as on the
  Flow itself, but scoped to this specific Step.

Additional plugin-specific settings may become available after the Step is saved.

**Approver Steps**

When an Actor Type of Approver is used, a Group must be identified to determine
who may act as Approvers for that Step. Approvers do not need to be
administrators. The Approver Group is resolved in this order:

1. :bdg-secondary:`Available: v5.2.0` The Approver Group configured on the Step itself, if set.
2. If a COU has been set for the Petition, the COU-specific Approvers Group.
3. If no COU is set, the CO-wide Approvers Group.

If two consecutive Steps both have an Actor Type of Approver, and the current
Actor is eligible to approve the second Step, no handoff occurs — the Approver
moves directly to the next Step without a notification cycle.

Working with Message Templates
---------------------------------

Enrollment Flows use :ref:`personalization-message-templates` for handoffs and
advisory notifications. When writing templates for Enrollment Flows, two
substitution tokens are particularly important:

- ``(@ENTRY_URL)`` — use in handoff templates to send the next Actor back into
  the Enrollment Flow. An Approver or Enrollee receiving a handoff should click
  this link to complete their Step.
- ``(@PETITION_URL)`` — use in notification templates for administrators, to
  provide a direct link to view the Petition. Do not use this link in handoff
  templates sent to participants who need to take action — use ``(@ENTRY_URL)``
  instead.

Available Enroller Plugins
---------------------------

The following plugins are available for use as Enrollment Flow Steps:

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Plugin
     - Description
     - Available Since
   * - Agreement Collector
     - Require agreement to Terms and Conditions
     - v5.2.0
   * - Approval Collector
     - Request approval for the Petition
     - v5.2.0
   * - Attribute Collector
     - Request attributes related to the Enrollee
     - v5.1.0
   * - Basic Attribute Collector
     - Request a limited set of attributes for the Enrollee
     - v5.1.0
   * - Email Verifier
     - Verify email addresses associated with the Petition
     - v5.1.0
   * - Env Source Collector
     - Create an External Identity via the Env Source Plugin
     - v5.1.0
   * - Identifier Collector
     - Collect the value of ``$REMOTE_USER``
     - v5.1.0
   * - Invitation Accepter
     - Ask the Enrollee to accept an invitation to join the CO
     - v5.1.0

For full documentation on each plugin, see
`Enrollment Flow Plugins (PE) <https://spaces.at.internet2.edu/spaces/COmanage/pages/289113581/Enrollment+Flow+Plugins+PE>`_
in the Technical Manual.

Running Enrollment Flows
-------------------------

**Starting a Flow**

The URL to start an Enrollment Flow is available via the **Start** link in the
Flow configuration. Share this URL directly (for administrator-initiated flows)
or distribute it through email, your website, or any other channel for
self-service. Starting a Flow is subject to the configured Petitioner
Authorization.

**Resuming a stuck Petition**

Sometimes Petitions get stuck — an Actor didn't receive a Notification, or
forgot to act on it. Any in-progress Petition can be resumed via the Petition
list: select **Resume** to see all Steps in the Flow with their current status.
A Step that has already run shows a **Rerun** action; the next Step that has
not yet run shows a **Continue** action.

When assisting a stuck Petition, keep Actor Types in mind. If an Enrollee is
stuck and contacts the Helpdesk, the correct resolution is often for the
Helpdesk agent to copy the Continue link and send it to the Enrollee — not to
click it themselves, as that would complete the Step as the wrong Actor type.

**Finalizing a Petition**

After the last configured Step runs, finalization occurs automatically:

1. The Petition status is set to Finalizing.
2. A new, empty Person record is created if none is already attached to the
   Petition.
3. Each Step's plugin is called in order, converting interim Petition data into
   operational records on the Person.
4. Identifier Assignment runs, if configured.
5. Provisioning runs for any Provisioning Targets in Enrollment Mode.

**Canceling a Petition**

An unfinalized Petition can be canceled in several ways:

- An administrator can Terminate any Petition by viewing it and selecting
  Terminate.
- During an Invitation Accepter Step, the Enrollee can decline the invitation.
- During an Approval Step, an Approver can deny the Petition.

Once canceled, a Petition cannot be restarted.

Primary Names and Enrollment
------------------------------

Registry requires every Person to have a Primary Name at all times. For Flows
that create a new Person, there is no Primary Name until one is collected and
the Person is created at Finalization. Different plugins handle Primary Name
differently: the Basic Attribute Collector always sets the Name it collects as
Primary, while the Env Source Collector only sets a Primary Name if none already
exists. When used together in the same Flow, the Basic Attribute Collector's Name
will always become the Primary — regardless of which plugin runs first.

For additional role enrollments (Flows that attach a new Role to an existing
Person), the Primary Name starts as the existing Person's Primary Name.

Changes from v4
----------------

The Enrollment Flow feature in v5 is a substantial redesign, not an incremental
update. If you are migrating from v4, expect to rebuild your Enrollment Flows
from scratch.

- **Enrollment Flows were completely redesigned in v5.1.0.** The v4 flow model
  using Enrollment Sources, Enrollment Wedges, and a mix of structured and
  plugin-based steps no longer exists. In v5, every Step is plugin-based.

- **Enrollment Flows are not available in Registry v5.0.x.**

- **Operational records are only created at finalization** (v5.1.0). In v4,
  records could be created or updated during the Flow even if the Petition was
  later rejected. In v5, all Step plugins work with interim Petition data, and
  operational records are only committed when the Petition successfully finalizes.

- **Default Enrollment is no longer supported** (v5.1.0). In v4, if no
  Enrollment Flows were configured, Registry fell back to an invitation-based
  Default Enrollment process. This fallback no longer exists in v5.

- **Enrollment Sources and Enrollment Wedges are no longer distinct concepts**
  (v5.1.0). All Enrollment Flow Steps are plugin-based, and any plugin can
  function in any Step position.

- **Sync on Login is no longer a Flow-level option** (v5.1.0). The equivalent
  functionality is available in other contexts, such as the Env Source Plugin.

- **Custom Approver Groups are supported as of v5.2.0**, allowing a specific
  Group to be designated as Approvers for a Step rather than relying solely on
  COU-based or CO-wide Approver Groups.

- **Finalization Message Template is available as of v5.2.0**, replacing the
  v4 combination of Notify on Approval and Approval Message Template.

- **Notification Groups are supported as of v5.2.0.**
