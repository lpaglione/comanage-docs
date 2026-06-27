.. DRAFT — April 2026

.. _about-match:

About COmanage Match
====================

.. sidebar:: On this page

   .. contents::
      :local:
      :depth: 1


COmanage Match is a companion tool to Registry that addresses a specific and
surprisingly difficult problem in identity management: when a new record arrives
from an authoritative system, is that person already in your registry?

This page introduces Match, explains why identity matching is harder than it
sounds, and describes how Match and Registry work together. For full Match
documentation, see the
`COmanage Match User Guide <https://spaces.at.internet2.edu/display/COmanage/COmanage+Match+User+Guide>`_.

1. The Identity Matching Problem
----------------------------------

Every organization that aggregates identity data from multiple systems eventually
runs into the same problem: the same person appears in more than one system, and
those systems describe them differently.

An employee might be in your HR system as "Jonathan R. Smith" with a university
ID of 12345. The same person appears in your student information system as "Jon
Smith" with a different internal ID from years ago. A collaboration they joined
last year knows them only by their ORCID iD. When these records arrive in Registry,
how do you know they all belong to the same person?

Simple matching on name or email address fails quickly in practice. Names change,
email addresses change, and data entry is inconsistent across systems — all of
which can cause a simple matching approach to miss a match that should have been
found. Common names and shared email formats create the opposite problem:
incorrectly matching records that belong to different people. Getting matching
wrong in either direction has real consequences: duplicate records lead to split
identities and missed provisioning, while incorrect merges expose one person's
data to another person's access.

**Identity matching** is the systematic process of determining whether a
person's record presented by one system is already known to your identity
management system — and doing so reliably across imperfect, inconsistent data.

2. What COmanage Match Does
-----------------------------

COmanage Match provides a heuristic-based (rules-based) matching engine that compares incoming
identity records against existing records across multiple authoritative systems of
record. Rather than requiring an exact field match, Match evaluates a
configurable set of attributes and applies weighted rules to determine the
likelihood that two records represent the same person.

When Match evaluates an incoming record, one of three things happens:

**No match found.** The person is not known to the system. A new reference
identifier is assigned and the requesting system is notified.

**Rules-based match found.** The configured matching rules determine that the
incoming record belongs to a person already in the system — for example, that
"Jon Smith" and "Jonathan R. Smith" are the same person, because a rule was
defined to treat those name forms as equivalent. The existing reference
identifier is returned.

**Ambiguous result.** The incoming record partially resembles one or more
existing records, but the rules could not reach a definitive determination.
This case is routed for human review — either interactively by the system
presenting the data, or asynchronously by a staff member designated to review
and resolve ambiguous records. The reviewer examines the potential match and
makes the call: confirmed match or confirmed non-match.

The ambiguous case is where Match's value is most apparent. A simple matching
approach either forces a merge (risking incorrect links) or creates a duplicate
(splitting the identity). Match surfaces the ambiguity and routes it to a human
decision, with the context needed to resolve it correctly.

3. How Match and Registry Work Together
-----------------------------------------

Match and Registry are designed to complement each other, but they are
independent tools — Match does not require Registry, and Registry does not
require Match.

**Within Registry,** enrollment flows include a built-in identity matching step
that checks whether the person being enrolled already has a Person record. For
many deployments, this is sufficient: matching happens at enrollment time, and
the population is well-enough defined that ambiguous cases are rare or easily
handled.

**COmanage Match** is most valuable when matching needs to happen at a broader
scope — across multiple authoritative systems before data even reaches Registry.
Match can be integrated with Registry in two ways:

*Match before Registry:* Incoming records from systems of record are evaluated
by COmanage Match before being passed to Registry. Registry receives data with
a matching determination already made, simplifying the enrollment and linking
process for complex or large-scale identity populations.

*Match at Registry:* Registry calls COmanage Match as part of its Pipeline
processing, using the External Match Strategy to send incoming identity data to
Match for evaluation and receive a matching determination in return.

4. Do You Need Match?
-----------------------

Not every Registry deployment needs COmanage Match. Whether you do depends on
the complexity of your identity landscape.

Match is likely worth considering if:

- You are aggregating data from several authoritative systems with overlapping
  populations and no shared authoritative identifier.
- Duplicate records are a known problem in your current environment, or you
  anticipate they will be at scale.
- You want to share a matching service across multiple applications, not just
  Registry.
- Your enrollment volume or the diversity of your population makes manual
  duplicate review impractical.

Match may not be necessary if:

- Your population comes from a single authoritative source with reliable,
  consistent identifiers.
- Registry's built-in matching at enrollment time is sufficient for your
  ambiguity rate and volume.
- Your population is small enough that edge cases can be handled manually.

If you are unsure, it is reasonable to start with Registry's built-in matching
and add Match later if duplicate management becomes a recurring operational
problem.

.. seealso::

   `COmanage Match User Guide <https://spaces.at.internet2.edu/display/COmanage/COmanage+Match+User+Guide>`_
      Full documentation for Match, including installation, configuration, and
      the Match API.

   :doc:`Registry Concepts Overview </understanding/concepts-overview>`
      How Registry handles external identities and the matching step within
      enrollment.

   :doc:`Planning Your Implementation </understanding/planning>`
      Considerations for whether and how to incorporate Match into your
      deployment.

   :doc:`What is COmanage Registry? </about/what-is-registry>`
      Overview of Registry and the COmanage Project.
