# Call Management

## Overview

Call management in Waldur enables organizations to manage resource allocation through a structured application proposals and review process. This feature is particularly useful for research institutions, funding agencies, and organizations that need to allocate computational or infrastructure resources through a competitive process.

## Introduction

Call management in Waldur is built around structured components: calls, rounds, proposals, and reviews. A call is a defined period during which resources can be allocated. Each call is divided into rounds, where stakeholders can submit and review proposals for resource allocation. Proposals are evaluated through a structured review process. Successful proposals lead to approved allocations, seamlessly integrating into the rest of the Waldur ecosystem. When a proposal is approved, Waldur automatically creates a project under the proposing organization that initiated the call. Allocations are granted to this project, and team members who submitted the proposal are added to the project, ensuring the resources are immediately ready for use.

## Prerequisites

- Organization must be registered as a Call Managing Organization
- Marketplace offerings must be available to be requested in calls

## Stakeholder Roles

### Organization Owner

- Assign call managers
- Grant final resource allocations, if defined in round configuration
- View statistics across all calls in the organization
- Archive calls when they are no longer active

### Call Manager

- Create and configure calls
- Manage call rounds
- Set review strategies
- Assign reviewers
- Make decisions (if configured as deciding entity)
- Add documentation and descriptions
- Monitor call progress
- Close rounds early if needed
- Manage requested offerings from service providers

### Call Member (Applicant)

- Submit proposals to active rounds
- Upload required documentation
- Select offerings and allocations
- Add team members to proposals
- Track proposal status
- Provide additional information during revision process
- View review feedback when available

### Reviewer

- Evaluate assigned proposals
- Provide scores and feedback
- Complete reviews within specified duration
- Accept or reject review assignments
- Provide both public comments (visible to applicants) and private comments (visible only to call managers)

### Service Provider

- Accept or reject requests to include their offerings in calls
- View requested resources related to their offerings
- Configure parameters for offerings available in calls

## Call Structure and Workflow

### 1. Call Setup

1. Organization owner assigns call managers
2. Call manager or Organization owner creates a call
3. Call manager configures call rounds
4. Call manager requests offerings from service providers
5. Service providers accept or reject offering requests
6. Call manager activates the call when configuration is complete

### 2. Round Configuration

Call manager must configure:
- Start and end dates
- Review strategy options:
  - After round closure
  - After proposal submission
- Review parameters:
  - Review duration (in days)
  - Minimum number of reviewers
  - Minimal average scoring threshold for automatic approval (if applicable)
- Decision making:
  - Deciding entity (call manager or automatic)
  - Allocation timing (on decision or fixed date)
  - Allocation date (if fixed date is selected)
- Round description and documentation
- Reviewers and managers assignment
- Default project role for proposal team members

### 3. Proposal Submission

Call members should:
- Submit proposals to active rounds
- Upload required documents
- Select offerings and allocations
- Add team members (optional)
- Provide required details:
  - Project name
  - Project summary
  - Description
  - OECD FOS 2007 code (Fields of Science classification)
  - Civilian purpose declaration
  - Confidentiality requirements
  - Duration in days

### 4. Review Process

1. Reviewers are assigned to rounds
2. Reviewers are assigned to specific proposals
3. Reviews are conducted according to strategy
4. Feedback and scores are provided on multiple aspects:
   - Project title
   - Project summary
   - Project description
   - Project duration
   - Supporting documentation
   - Resource requests
   - Team composition
5. Summary score and comments are provided
6. Reviews are submitted for consideration

### 5. Decision and Allocation

1. Decision maker (as configured) evaluates reviews
2. Final decisions are made (allocation or rejection)
3. For allocated proposals:
   - A project is automatically created
   - Requested resources are provisioned in the marketplace
   - Team members are assigned the configured project role
   - Resource limits are applied as specified in the proposal

### 6. Tracking and Reporting

1. Call managers can monitor statistics on:
   - Open calls
   - Active rounds
   - Accepted proposals
   - Pending proposals
   - Pending reviews
   - Rounds closing soon
   - Pending offering requests
2. Organization owners can track resource allocation across all calls

## States and Transitions

### Call States
- **Draft**: Initial state, call is being configured
- **Active**: Call is open for submissions
- **Archived**: Call is completed and no longer active

### Round Statuses
- **Scheduled**: Round start date is in the future
- **Open**: Round is currently accepting submissions
- **Ended**: Round cutoff date has passed

### Proposal States
- **Draft**: Initial creation, editable by applicant
- **Submitted**: Sent for review, awaiting reviewer assignment
- **In Review**: Assigned to reviewers, under evaluation
- **In Revision**: Sent back to applicant for changes
- **Accepted**: Approved for resource allocation
- **Rejected**: Declined for resource allocation
- **Canceled**: Withdrawn or automatically canceled

### Review States
- **Created**: Review has been assigned
- **In Review**: Reviewer has accepted and is working on evaluation
- **Submitted**: Review is complete
- **Rejected**: Reviewer has declined the assignment

### Requested Offering States
- **Requested**: Initial state, awaiting service provider decision
- **Accepted**: Service provider has approved use in call
- **Canceled**: Service provider has declined use in call

## API Endpoints

The system provides RESTful API endpoints for:
- Managing Call Organizations
- Creating and configuring Calls
- Managing Rounds
- Submitting and updating Proposals
- Assigning and completing Reviews
- Requesting and approving Offerings
- Allocating resources

## Best Practices

- Set clear evaluation criteria and communicate them to applicants
- Provide comprehensive round documentation including resource availability
- Allow adequate time for review process (recommended: 2+ weeks for reviews)
- Configure appropriate minimum number of reviewers (recommended: 2-3)
- Maintain consistent communication with applicants throughout the process
- Close rounds promptly when cutoff dates are reached
- Monitor reviewer workload to ensure balanced distribution
- Configure automatic allocation only when clear scoring criteria are established
- Provide templates for proposal documentation where applicable
- Schedule multiple rounds in advance for recurring allocation cycles

## Troubleshooting

### Round Configuration
- **Issue**: Round dates overlap with existing rounds
  **Solution**: Adjust dates to ensure no overlap within the same call

- **Issue**: Unable to create a round
  **Solution**: Ensure call is in Draft or Active state

### Proposal Submission
- **Issue**: Unable to submit proposal
  **Solution**: Verify round is in Open status and required fields are completed

- **Issue**: Resource requests unavailable
  **Solution**: Check that service providers have accepted offering requests

### Review Assignment
- **Issue**: Not enough reviewers available
  **Solution**: Assign additional reviewers to the call or adjust minimum number requirement

- **Issue**: Reviews not being created
  **Solution**: Verify review strategy configuration and check reviewer availability

### Allocation Process
- **Issue**: Resources not provisioned after approval
  **Solution**: Check marketplace availability and quotas

- **Issue**: Team members not added to project
  **Solution**: Verify default project role configuration

- **Issue**: Unable to allocate proposal
  **Solution**: Ensure proposal is in correct state (In Review, Submitted) and review requirements are met