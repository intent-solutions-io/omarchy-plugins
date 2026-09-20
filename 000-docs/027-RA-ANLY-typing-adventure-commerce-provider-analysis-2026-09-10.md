---
blueprint:
  documentId: KTA-COMMERCE-001
  documentType: research-analysis
  schemaVersion: 1.0.0
  templateVersion: 3.0.0
  status: proposed
  owner: Jeremy Longshore
  authors: ["Intent Solutions / Codex"]
  reviewers: []
  approvers: []
  generatedAt: 2026-09-10
  updatedAt: 2026-09-10
  classification: public-draft
  sourceRefs: [SR-COM-101, SR-COM-102, SR-COM-103, SR-COM-104, SR-COM-105]
  assumptions: [A-COM-101, A-COM-102]
  unknowns: [U-COM-101, U-COM-102, U-COM-103, U-COM-104]
  relatedArtifacts: [KTA-BRIEF-001, KTA-ADR-001, KTA-ARCH-001, KTA-PRIV-001, KTA-AC-001, KTA-TEST-001, KTA-PROGRAM-001]
  reviewDate: TBD
  supersedes: []
  humanReview:
    required: true
    status: not-started
---

# Kids typing adventure commerce provider analysis

> Decision status: free v1.0 has no commerce dependency. Lemon Squeezy is the leading candidate for a later one-time Family purchase, not an approved vendor or production integration. Final selection requires owner, legal, security, operational, onboarding, and sandbox evidence.

## Decision to make

Choose the smallest parent-only commerce system that can sell a one-time digital software license globally, carry merchant-of-record responsibilities, support refunds and recovery, and drive a signed offline entitlement without placing accounts, checkout, payment data, or network dependence in child play.

## Recommended sequence

1. Ship and measure the permanent free product without a live checkout, payment SDK, license server, or paid feature flag.
2. Keep only a provider-neutral `CommercePort`, versioned webhook-event fixtures, and an entitlement verifier in the architecture.
3. After the paid decision gate passes, validate seller onboarding and sandbox behavior for Lemon Squeezy and Paddle against the same contract.
4. Select one provider by a recorded ADR. Do not integrate two production providers for launch.
5. Receive provider webhooks in the parent service, verify signatures and event identity, store the minimal append-only commerce event, and issue an Intent Solutions signed entitlement.
6. Deliver recovery to the verified parent email through an external parent flow. The app imports and verifies the entitlement offline.

## Lean direct-sale path examined on 2026-09-10

A separate product domain, storefront site, production game server, and custom customer database are not prerequisites for selling the downloadable app. The smallest credible path is:

```text
free Omarchy teaser
  -> oma.intentsolutions.io/<approved-product-slug>
  -> provider-hosted parent checkout
  -> provider-hosted AppImage download and receipt
  -> license activation or signed entitlement import
  -> local desktop play
```

The existing Oma GitHub Pages site can host the landing page. Lemon Squeezy documents shareable hosted checkout URLs and checkout overlays, digital files of any type up to 5 GB total per product, receipt emails, file updates for existing buyers, and generated license keys. Its current headline ecommerce price is no monthly fee and 5 percent plus $0.50 per sale, with additional fees possible in documented cases. The current 125,236,660-byte AppImage therefore fits the documented file allowance without a second file host.

This removes a custom order database from the first-sale path, but it does not remove application work. The current AppImage verifies an Intent Solutions signed offline license file and is not integrated with Lemon Squeezy. The paid lane must select one of these approaches:

1. Direct provider license activation: the parent enters the provider key, the app activates and validates it, and the app caches a bounded local status. This is the shortest integration, but subscription cancellation and expiry create an online validation policy.
2. Intent Solutions signed offline entitlement: a verified provider webhook drives a small signer that issues the existing license format. This preserves stronger offline behavior, but it requires a protected signing service, replay-safe event handling, recovery, and refund policy.
3. Bounded manual pilot issuance: an operator verifies an early order and sends a signed entitlement manually. This may prove the fulfillment path for a very small pilot, but it is not an acceptable scaled operating model.

### Seven-day trial decision

The phrase "try free for one week, then charge" has two materially different implementations:

| Model | Parent experience | System consequence |
|---|---|---|
| No card before trial | Download and play locally for seven days, then choose whether to buy | Highest trial access and simplest child boundary, but no automatic charge; the local trial must resist trivial clock and reinstall abuse without invasive device tracking |
| Payment details before trial | Parent completes a subscription checkout, receives seven trial days, and is charged automatically unless canceled | Supports automatic conversion, but requires subscription webhooks, clear cancellation and reminder language, parent-only checkout, and license lifecycle checks |

Lemon Squeezy documents free trials for subscription products and automatic charging after a payment-required trial. Its own guidance says a no-payment trial is tracked by the application and later sends the user to checkout. A one-time permanent family license therefore does not natively auto-charge after a local trial. Pricing model, trial model, offline promise, and refund policy must be approved together.

### Alternative distribution surfaces

- itch.io can host files, provide a game page, sell downloads, issue download keys, and act as merchant of record in its collected-payout mode. It is a credible secondary discovery and delivery channel, but it does not replace the current offline entitlement decision.
- GitHub Releases can host a public free-trial or demo artifact and documents no total release-size or bandwidth limit. It is not a paid storefront or private fulfillment system.
- A new product domain is optional brand insurance after clearance. It is not a launch dependency.

## Proposed transaction path

```text
parent browser
  -> provider-hosted checkout
  -> merchant-of-record payment and tax handling
  -> signed webhook to parent service
  -> signature, replay, order-state, refund, and product checks
  -> append-only commerce event plus idempotency receipt
  -> Intent Solutions entitlement signer
  -> signed, versioned offline entitlement
  -> parent-controlled recovery or import
  -> desktop app verifies locally
  -> local Family feature state
```

Child profiles, ages, nicknames, lessons, prompts, keystrokes, mastery, session history, and research data are prohibited from checkout, webhooks, CRM, entitlement payloads, and support tooling.

## Provider comparison

| Provider | Current public position | Strength | Concern | Disposition |
|---|---|---|---|---|
| Lemon Squeezy | Merchant of record for digital products; headline fee 5% plus $0.50; one-time and recurring products; license keys, signed downloads, API, and webhooks | Best documented small-software fit and least custom commerce surface | Extra fees can apply; seller approval, payout, refund, webhook, ownership, and support behavior need validation | Leading v1.1 sandbox candidate |
| Paddle | Merchant of record; headline fee 5% plus $0.50; payments, billing, tax, fraud and chargeback protection, and support | Mature digital-software commerce and clear webhook model | Under-$10 pricing and exact license/recovery implementation need validation | Required comparison candidate |
| Stripe Managed Payments | Merchant of record option for digital products with transaction-level enablement | Familiar developer ecosystem and selective coverage | Public preview at review time and a 3.5% MoR fee in addition to processing and possible billing fees | Fallback, not first implementation |
| Direct Stripe Payments plus Tax | Processor with separate tax tooling | Maximum checkout control | Intent Solutions remains MoR and carries more tax, refund, dispute, support, and jurisdictional operations | Reject for first paid release |

## Why the provider does not own app authorization

The authoritative app artifact is a signed entitlement with a versioned canonical encoding, product and edition, order-derived opaque license ID, issue time, optional update window, key ID, and signature. It contains no child or learning data. The app must not call a vendor on every launch.

The verifier must support key rotation, old-key retention, offline grace, refund and chargeback state, recovery after device loss, backup restore, tamper failure, clock rollback or jump, and an explicit device-transfer policy. A provider outage must not revoke already verified permanent access.

There is an unavoidable policy choice: genuinely permanent offline access cannot be revoked immediately after a refund while the device remains offline. Before sale, the owner must choose and disclose either permanent offline capability with delayed or manual refund enforcement, or a bounded online renewal mechanism. The initial recommendation is no wall-clock expiry for purchased capabilities; a signed `updates_through` claim may limit future update eligibility without removing already purchased play.

## Webhook and data contract

- Strict body-size and content-type limits
- Signature verification before business-field parsing
- Replay prevention and durable idempotency keyed by provider plus event ID
- Immutable verified-envelope inbox keyed by provider plus event ID, followed by an explicit legal transition table for paid, refunded, disputed, dispute-reversed, recovered, and manual-review states
- Product and price allowlist, amount checks, and test/live separation
- No secret or raw payload in application logs
- Bounded retry and dead-letter handling with operator alerts
- Provider sequence or version when available, deterministic replayable projection, transactional entitlement outbox, issuance generation, and periodic provider reconciliation
- Tests for refund, duplicate, delay, reordering, forgery, and provider outage
- Signer isolation, key IDs, rotation, revocation, audit events, and recovery drill

Twenty may receive a minimal adult customer relationship reference after verified purchase, but it is not the order ledger, entitlement authority, or child-data store. The commerce ledger remains separate from newsletter consent and local learner SQLite.

## Selection scorecard

| Criterion | Weight |
|---|---:|
| Merchant-of-record coverage and legal review | 25 |
| Parent checkout, refund, support, and recovery experience | 20 |
| Webhook correctness and operational control | 15 |
| Permanent offline entitlement fit | 15 |
| Seller eligibility, payout reliability, and continuity | 10 |
| Total effective cost at tested prices and regions | 10 |
| Migration and provider-exit path | 5 |

A provider fails regardless of score if it cannot approve the product, support the seller jurisdiction, deliver auditable webhooks, permit the one-time license model, or pass legal and security review.

## Go-live evidence gate

- Approved seller account and verified business identity
- Current contract, prohibited-product, refund, chargeback, tax, privacy, DPA, subprocessor, payout, reserve, and termination review
- Sandbox evidence for purchase, duplicate, delay, reordering, refund, dispute, recovery, and outage
- Exact fee model at candidate prices, including fixed, international, currency, payout, refund, dispute, and tax-on-fee effects
- Webhook signature and replay evidence
- Entitlement signing, rotation, recovery, transfer, and offline evidence
- Reconciliation runbook, alert, backup, restore, rollback, and provider-exit export
- Owner approval tied to an exact revision and production configuration

## Source register

| ID | State | Source | Use and limitation |
|---|---|---|---|
| SR-COM-101 | verified current vendor source | [Lemon Squeezy pricing](https://www.lemonsqueezy.com/pricing) | Fee, MoR position, keys, downloads, and one-time products; contract still requires review |
| SR-COM-102 | verified current vendor source | [Lemon Squeezy license-key guide](https://docs.lemonsqueezy.com/guides/tutorials/license-keys) and [webhook guide](https://docs.lemonsqueezy.com/guides/developer-guide/webhooks) | Candidate primitives, not proof of our entitlement safety |
| SR-COM-103 | verified current vendor source | [Paddle pricing](https://www.paddle.com/pricing) and [digital-product model](https://developer.paddle.com/get-started/how-paddle-works/digital-products/) | Fee and software fit; seller terms remain unknown |
| SR-COM-104 | verified current vendor source | [Stripe Managed Payments](https://docs.stripe.com/payments/managed-payments) | MoR capabilities and preview status |
| SR-COM-105 | verified current vendor source | [Stripe Managed Payments pricing](https://support.stripe.com/questions/managed-payments-pricing) | 3.5 percent MoR fee in addition to processing |
| SR-COM-106 | verified current vendor source | [Lemon Squeezy product setup and file delivery](https://docs.lemonsqueezy.com/help/products/adding-products) | Hosted files, receipts, variants, license keys, and current 5 GB product-file allowance |
| SR-COM-107 | verified current vendor source | [Lemon Squeezy hosted product links](https://docs.lemonsqueezy.com/help/products/sharing-products) | Shareable checkout URLs without a second custom storefront |
| SR-COM-108 | verified current vendor source | [Lemon Squeezy free trials](https://docs.lemonsqueezy.com/help/products/free-trials) and [trial implementation guide](https://docs.lemonsqueezy.com/guides/tutorials/saas-free-trials) | Distinguishes local no-card trials from payment-required auto-charging subscription trials |
| SR-COM-109 | verified current vendor source | [Lemon Squeezy license generation](https://docs.lemonsqueezy.com/help/licensing/generating-license-keys) and [License API](https://docs.lemonsqueezy.com/api/license-api) | Provider-key option; does not prove permanent offline semantics |
| SR-COM-110 | verified current vendor source | [itch.io creator FAQ](https://itch.io/docs/creators/faq) and [payment modes](https://itch.io/docs/creators/payments) | Secondary hosted game sales and merchant-of-record alternative |
| SR-COM-111 | verified current vendor source | [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) | Public demo delivery alternative, not paid fulfillment |

## Assumptions and unknowns

| ID | State | Item | Closure method |
|---|---|---|---|
| A-COM-101 | assumed | A one-time Family license is preferable to a subscription. | Parent research and unit economics |
| A-COM-102 | assumed | A merchant of record is preferable for the first global sale. | Legal, tax, and operating-cost review |
| U-COM-101 | unknown | Lemon Squeezy seller eligibility and agreement for this product | Onboarding and counsel review |
| U-COM-102 | unknown | Final price, refund, device count, transfer, and update policy | Owner decision after research |
| U-COM-103 | unknown | Value of provider-native keys without weakening offline behavior | Comparative sandbox spike |
| U-COM-104 | unknown | Signer placement and key-custody owner | Security review and recovery drill |
| U-COM-105 | owner-held | No-card local trial or payment-required auto-charging trial | Product, parent-experience, refund, and unit-economics decision |
| U-COM-106 | unknown | Whether a paid pilot should precede the currently planned permanent free v1.0 | Owner decision and reconciliation with ADR-117 |

## Human review

- Required: yes
- Status: not started
- Minimum reviewers: product owner, finance, legal/privacy, security, operations, and support
- Final authority: Jeremy Longshore or an explicitly delegated decision owner
