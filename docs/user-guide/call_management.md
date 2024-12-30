# Call Management

## Overview

Call management in Waldur enables organizations to manage resource allocation through a structured application proposals and review process.

## Table of Contents

- [Overview](#overview)
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Stakeholder Roles](#stakeholder-roles)
   - [Organization Owner](#organization-owner)
   - [Call Manager](#call-manager)
   - [Call Member (Applicant)](#call-member-applicant)
   - [Reviewer](#reviewer)
- [Call Structure and Workflow](#call-structure-and-workflow)
   - [Call Setup](#1-call-setup)
   - [Round Configuration](#2-round-configuration)
   - [Proposal Submission](#3-proposal-submission)
   - [Review Process](#4-review-process)
   - [Decision and Allocation](#5-decision-and-allocation)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Introduction

Call management in Waldur is built around structured components: calls, rounds, proposals, and reviews. A call is a defined period during which resources can be allocated. Each call is divided into rounds, where stakeholders can submit and review proposals for resource allocation. Proposals are evaluated through a structured review process. Successful proposals lead to approved allocations, seamlessly integrating into the rest of the Waldur ecosystem. When a proposal is approved, Waldur automatically creates a project under the proposing organization that initiated the call. Allocations are granted to this project, and team members who submitted the proposal are added to the project, ensuring the resources are immediately ready for use.

## Prerequisites

- Organization must have call management enabled

## Stakeholder Roles

### Organization Owner

- Assign call managers
- Grant final resource allocations, if defined in round configuration

### Call Manager

- Create and configure calls
- Manage call rounds
- Set review strategies
- Assign reviewers
- Make decisions (if configured as deciding entity)
- Add documentation and descriptions
- Monitor call progress

### Call Member (Applicant)

- Submit proposals to active rounds
- Upload required documentation
- Select offerings and allocations
- Add team members to proposals
- Track proposal status

### Reviewer

- Evaluate assigned proposals
- Provide scores and feedback
- Complete reviews within specified duration

## Call Structure and Workflow

### 1. Call Setup

1. Organization owner assigns call managers
2. Call manager or Organization owner creates a call
3. Call manager configures call rounds

### 2. Round Configuration

Call manager must configure:
- Start and end dates
- Review strategy options:
  - After round closure
  - After proposal submission
- Review parameters:
  - Review duration (in days)
  - Minimum number of reviewers
- Decision making:
  - Deciding entity (call manager or automatic)
  - Allocation timing (on decision or fixed date)
- Round description and documentation
- Reviewers and managers assignment

### 3. Proposal Submission

Call members should:
- Submit proposals to active rounds
- Upload required documents
- Select offerings and allocations
- Add team members (optional)

### 4. Review Process

1. Reviewers are assigned to rounds
2. Reviewers are assigned to specific proposals
3. Reviews are conducted according to strategy
4. Feedback and scores are provided

### 5. Decision and Allocation

1. Decision maker (as configured) evaluates reviews
2. Final decisions are made
3. Organization owner grants approved allocations

## Best Practices

- Set clear evaluation criteria
- Provide comprehensive round documentation
- Allow adequate time for review process
- Maintain consistent communication

## Troubleshooting

Common issues and solutions for:
- Round configuration
- Proposal submission
- Review assignment
- Allocation process
