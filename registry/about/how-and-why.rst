.. DRAFT — April 2026
.. Terminology: uses confirmed v5 terms throughout.
.. Open question: confirm v5 term for "CO" / collaboration object container.

.. _how-and-why:

How and Why to Use Registry
============================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


Every organization that manages people has the same underlying challenge:
your people don't fit neatly into one system, one role, or one moment in time.
Registry exists for exactly this situation — to give you a single, reliable place
to know who your people are, manage their relationships with your organization,
and keep your connected systems in sync, without requiring your team to build
something from scratch or maintain a tangle of custom scripts.

If any of the situations below sound familiar, Registry is worth a closer look.

"We have people in multiple systems, and they don't match up."
--------------------------------------------------------------

Your HR system knows about employees. Your student information system knows about
students. Your collaboration platform has its own user records. The same person
can appear in all three — under slightly different names, with different
identifiers, and with no automated way to know they're the same individual.

Registry solves this by pulling data from all your authoritative sources into a
single **person record** per individual. You connect Registry to your existing
systems using plugins — LDAP directories, REST APIs, CSV feeds, and more — and
Registry aggregates the incoming data into one coherent view. When someone's
name changes, their role shifts, or they appear in a new system, their person
record stays current and consistent across everything that connects to Registry.

This is the foundation of Registry: **one person, one record**, no matter how
many systems they appear in.

"We need to manage people who aren't in our enterprise systems."
----------------------------------------------------------------

Visiting researchers, guest lecturers, library users, project collaborators from
partner institutions, student families, contractors, conference attendees —
there's almost always a population of people your organization needs to track and
manage access for, but who don't belong in your HR or student systems.

Registry is well-suited to this. You can enroll external people through
invitation or self-service workflows, manage what they can access, and remove
that access cleanly when their relationship with your organization ends — all
without requiring accounts in your enterprise systems. Registry manages the
guest lifecycle on its own terms, freeing your team to focus on the populations
and systems that most need their attention.

"Our enrollment process can't keep up with the variety of our populations."
---------------------------------------------------------------------------

Registry puts enrollment configuration in the hands of tool administrators —
no developer involvement required. Each enrollment workflow is built through
Registry's interface: you define the steps, the approval stages, and the
end-user experience. A research collaboration can configure an invitation-based
workflow for new collaborators. A department can configure a self-enrollment
process with its own approval chain. These workflows can be designed and
maintained independently by the people closest to each population, without
waiting on a central queue or writing any code.

Self-service enrollment lets new members initiate their own onboarding.
Invitation workflows let you reach out to people who need to be added.
Conscription workflows automatically enroll people based on data arriving from
an authoritative system. These approaches can be combined — a single enrollment
flow can pull from multiple sources and require multiple approval stages.

This delegation model — where department administrators, project leads, or
collaboration coordinators can manage their own enrollment workflows while
central IT retains overall platform control — is one of the most commonly cited
benefits of Registry among organizations that use it.

"We manage a multi-institution research collaboration."
-------------------------------------------------------

Research collaborations often span institutions, funding agencies, and national
boundaries. Managing membership, access, and offboarding for a group like this
is genuinely difficult when you're trying to do it through any single
institution's systems — or worse, through a shared spreadsheet.

Registry gives research collaborations a lightweight home of their own. A virtual
organization in Registry can enroll members from any institution, organize them
into groups, provision access to shared resources, and manage the full lifecycle
of the collaboration — including offboarding when grants end or members move on.
This works within a lightweight structure that each participating institution's
team can configure and maintain, with minimal coordination overhead across
institutions.

"We need to keep multiple systems in sync with our Registry data."
-----------------------------------------------------------------

Once people are in Registry, their data can be pushed to the systems that need
it through Registry's provisioning layer. Registry connects to LDAP directories,
collaboration platforms, mailing lists, Grouper, and more through a flexible
plugin architecture. You configure when provisioning happens — in real time as
changes occur, or in batches — and Registry handles the rest.

When a person's role changes, their access updates. When they leave, offboarding
policies trigger automatically. The goal is that the right people have access to
the right systems at the right time, with as little manual intervention as
possible.

Registry is not a purpose-built enterprise provisioning engine — for deployments
with complex, fine-grained provisioning requirements, a dedicated provisioning
tool may be a better fit. But for many deployments, Registry's provisioning
capabilities are exactly what's needed: a straightforward way to grant and
revoke access based on Registry membership, and to push data from Registry's
aggregated records to downstream systems. Provisioning in Registry isn't limited
to access control — it can also mean pushing updated name, affiliation, or
attribute data to other systems to keep them current as people's information
changes.

"We're not sure if Registry is the right tool for us."
------------------------------------------------------

That's a fair question, and the community is a good place to work it out. The
COmanage Project's monthly **Open Office Hours** is an open call where you can
bring your specific situation, ask questions, and hear how other organizations
are solving similar problems. No registration required — just show up.

The :doc:`case studies </case-studies/index>` section of this guide also
documents real deployments, with enough detail to help you recognize whether a
given pattern applies to your context.

And if Registry turns out not to be the right fit on its own, it's worth knowing
that **COmanage Match** — Registry's companion tool — can be used standalone for
organizations whose primary need is identity de-duplication rather than a full
lifecycle registry. See :doc:`About COmanage Match </about/about-match>` for a
brief overview.

.. seealso::

   :doc:`What is COmanage Registry? </about/what-is-registry>`
      A concise overview of Registry and what it does.

   :doc:`Registry Concepts Overview </understanding/concepts-overview>`
      The core mental model before you start configuring.

   :doc:`Case Studies </case-studies/index>`
      Real deployments with enough detail to recognize your own situation.

   :doc:`The COmanage Community </community/index>`
      Open Office Hours, Slack, and the newsletter.

   `COmanage Registry Technical Manual <https://spaces.at.internet2.edu/display/COmanage/Technical+Manual>`_
      Detailed reference for administrators and developers.
