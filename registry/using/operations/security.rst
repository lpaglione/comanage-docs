.. _ops-security:

Security Configuration
======================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1

1. Requiring MFA for Registry Access
--------------------------------------

:bdg-success:`New in v5` :bdg-secondary:`Available: v5.2.0`

Registry can be configured to require Multi-Factor Authentication (MFA) for
access to most Registry functions. When MFA is required and a user has not
asserted MFA at login, they are redirected to a designated page rather than
being allowed into the application.

.. note::

   This page covers requiring MFA for access to the Registry application
   itself. Requiring MFA for downstream applications that Registry provisions
   to is outside the scope of this documentation.

The specifics of how MFA is enforced (the IdP, authenticator app, or other
mechanism) are outside the scope of Registry configuration. Registry relies
on the web server or operating system to signal whether MFA was asserted via
an **environment variable**, which Registry checks at request time. This
variable is called the **MFA Assertion Indicator**.

For the full technical reference, see
`Requiring MFA for Access to Registry PE <https://spaces.at.internet2.edu/spaces/COmanage/pages/350158988/Requiring+MFA+for+Access+to+Registry+PE>`_
in the Technical Manual.

2. Configuration
-----------------

MFA enforcement is a **platform-level** configuration, set in the COmanage CO:

**COmanage CO > ALL > CO Settings**

The relevant settings are:

- **MFA Assertion Indicator** — the name of the environment variable that
  signals whether MFA was asserted at login.
- **MFA Assertion Indicator Value** — the expected value of that environment
  variable when MFA has been asserted.
- **Enable MFA Exemption Groups** — whether individual COs are allowed to
  exempt specific people from the MFA requirement. See Section 3 below.

If MFA is required but not signaled at login, the user is redirected to the
``mfa-required`` Mostly Static Page. The content of this page can be
customized per CO. See :ref:`personalization-mostly-static-pages`.

3. MFA Exemption Groups
------------------------

When **Enable MFA Exemption Groups** is turned on at the platform level, each
CO gains an **MFA Exemption Group** (named ``CO:mfaexempt``). CO Administrators
can add individuals to this group to exempt them from the MFA requirement when
accessing Registry functions within that CO.

A person's exemption status is CO-specific: the same individual could be
required to assert MFA when working in one CO, but be exempt when accessing
another.

MFA Exemption Groups are created automatically when a new CO is created,
regardless of whether Enable MFA Exemption Groups is turned on — the setting
only controls whether these groups are checked as part of the MFA enforcement
process.

.. seealso::

   :ref:`org-groups` for more on System Groups, including MFA Exemption Groups.

4. Exceptions
--------------

MFA is not enforced in all circumstances:

**Enrollment Flows for unenrolled users**
   When an Enrollment Flow is started or an Enrollment Flow Step is dispatched
   by a user who is not yet a registered Person within the CO, MFA is not
   required. This allows prospective enrollees whose Identity Provider may not
   support MFA — or who may not have an IdP at all — to complete the enrollment
   process. CO members acting in an enrollment role (such as Approvers) are
   still subject to MFA when viewing or acting on Petitions.

**Mostly Static Pages**
   Mostly Static Pages are publicly accessible. MFA is not enforced when
   viewing their content.

5. Troubleshooting
-------------------

Registry logs its MFA-related decisions to the **trace log**, which can help
diagnose why a particular user is or is not being required to assert MFA.

If the MFA configuration becomes incorrect and prevents login, the MFA
settings can be reset from the command line:

.. code-block:: bash

   cd $APP
   ./bin/cake ResetMfa

6. Changes from v4
-------------------

- **MFA enforcement is new in v5.2.0.** Registry v4 did not support requiring
  MFA for access to the Registry application.
- **MFA Exemption Groups** are also new in v5.2.0, providing per-CO exemption
  capability without requiring platform-level exceptions.
