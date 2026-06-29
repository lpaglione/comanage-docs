.. _ops-notifications:

Notifications
=============

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

Registry **Notifications** are short internal messages with a timestamp that
Registry uses to alert participants to events requiring attention — a petition
awaiting approval, an action taken on a record, or something that needs to be
acknowledged or resolved.

For the full technical reference, see
`Registry PE Notifications <https://spaces.at.internet2.edu/spaces/COmanage/pages/297862255/Registry+PE+Notifications>`_
in the Technical Manual.

1. Notification Roles
----------------------

Each Notification involves up to four participants:

- **Actor** — the person who generated the Notification (possibly indirectly,
  such as through a system action they triggered).
- **Recipient** — the person or Group the Notification is sent to.
- **Subject** — the person the Notification is about.
- **Resolver** — the person who takes action to address the Notification, or
  acknowledges it.

2. Acknowledgment and Resolution
---------------------------------

A Notification either requires **acknowledgment** or **resolution**:

- **Acknowledgment-only** notifications require the Recipient (or any member
  of the Recipient Group) to view the notification and click **Acknowledge**
  to dismiss it. No further action is required.
- **Resolution-required** notifications require the Recipient to take a
  specific action, typically by following the URL included in the Notification.
  Acknowledging alone is not sufficient.

Notifications generate History Records, providing an audit trail of what was
sent, to whom, and when it was addressed.

3. Notification Delivery
-------------------------

**Web Interface**

Notifications appear in the notification (bell) menu in the Registry
administrative interface. Administrators will see Notifications relevant to
their role and CO when they log in.

**Email**

When a Notification is registered, Registry will attempt to send an email
with the Notification's content. Email delivery requires:

- The CO to have an Outgoing SMTP Server configured. See
  `Configuring Registry Outgoing Email <https://spaces.at.internet2.edu/spaces/COmanage/pages/297862066/Configuring+Registry+Outgoing+Email>`_
  in the Technical Manual.
- The Recipient to have a suitable email delivery address in their Person
  record.

If either condition is not met, email delivery will not occur, but the
Notification will still appear in the web interface.

**Message Templates**

The content of Notification emails is controlled by Message Templates. See
:ref:`personalization-message-templates` for information on configuring
email templates.

4. Coming to v5
----------------

A **Notifications Dashboard Widget** for non-administrator users is planned
but not yet implemented. Once available, it will allow enrolled members to
receive and respond to Notifications through the self-service Dashboard,
without requiring administrative access to the Registry interface.
